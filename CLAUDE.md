# Cambridge Battlecode 2026a bot

Python bot for event `cambc2026a`. Solo project.

## Where the rules live

[agents/GameRules.md](agents/GameRules.md) and [agents/BotAPIPython.md](agents/BotAPIPython.md) are
exports of the official handbook and SDK reference. **They are the authority — read them, don't guess.**
The docs site (`https://2026a.battlecode.co.uk/game/docs`) is a client-side SPA behind signed-cookie
assets and cannot be fetched; these exports are the only readable copy.

The live SDK source in `sdk/python/cambc/` is worth reading too — it documents helpers the markdown
export omits (`cambc.vision.*`, `cambc.constants.*`, `Champion.attack_tiles()`).

## Commands

Run from the project root. All of these need the working directory inside the project.

```powershell
cambc run main baseline --map packs --view     # one match, open the replay
cambc run main baseline --statistics s.json    # machine-readable result
cambc view                                     # reopen the latest replay (port 7026)
cambc build main                               # compile only; catches what submission would reject
cambc mapeditor                                # author a custom test map
cambc maps pull                                # refresh the pool, keeping custom maps
cambc login                                    # browser device-code flow, 7-day session
cambc submit main                              # UPLOADS to the ladder
python scripts/arena.py                        # main vs baseline, 9 maps x both sides
python scripts/arena.py --snapshot             # promote main's source over baseline
```

`cambc build` takes ~6 s; a full match takes 15–60 s depending on map and length.

### Reading bot output

`print()` goes nowhere visible on the console. A `.repl26a` file is a **ZIP** containing
`replay.repl26a`, `team-a.stdout`, `team-b.stdout`, `team-a.debug`, `team-b.debug`. To read what a bot
printed:

```python
import zipfile
print(zipfile.ZipFile("replays/<bundle>.repl26a").read("team-a.stdout").decode())
```

`cambc.debug.draw_dot` / `draw_line` render overlays in the visualiser.

## Fuel is the binding constraint

Compute is metered in **Wasmtime fuel**, not time — deterministic and machine-independent. Python gets
25× the C++ limit, which sounds generous and isn't: interpreting one Python bytecode costs hundreds of
fuel, while host-side SDK calls do bulk work for almost nothing.

**Measured on `rows` (50×50), rounds 1 and 3. Approximate — the probe itself was in the loop.**

| Operation | Fuel | Notes |
|---|---|---|
| Turn budget | **~2,500,000** | Observed 2,477,776 at a turn start; round 1 gets 2× (4,600,272 observed) |
| `for i in range(1000): total += i*i` | **1,446,890** | **~1,450 fuel per trivial Python statement** |
| `game_map.camp_groups()` | **270,362** | ~11% of a turn in one call — **cache it, never call per turn** |
| `DistanceField.compute()` full 50×50 map | **156,625** | A 2500-tile BFS for the price of ~108 Python statements |
| `Bitboard.positions()` | **60,551** | Materializes a Python `Vec2` list — avoid in hot paths |
| `vision.champions()` | 46,385 | Builds Python `Champion` objects |
| `me.attack_tiles()` | ~12,000 | |
| `vision.champion_tiles()` | ~9,000 | Bitboard, not objects — far cheaper than `champions()` |
| `Bitboard.shadow_cast(origin, 8)` | ~7,000 | |
| `bitboard \| bitboard \| bitboard` | ~6,000 | |
| `Bitboard.reachable_tiles(origin, 10)` | ~4,900 | |
| `vision.visible_tiles()` | ~3,000 | |
| `game_map.walls()` | 2,731 first call, **428** after | Cached host-side |
| `cambc.fuel_remaining()` | ~2,800 | Measuring costs more than most host calls |

**The architecture this forces:** roughly **1,700 trivial Python statements per turn**, total. Do all
geometry with `Bitboard` / `DistanceField` / `vision.*_tiles()` host calls and keep guest-side loops to
tens of iterations. A loop over every tile of the map in Python is a dead bot. Prefer the `*_into(out)`
variants to avoid allocating new boards, and prefer bitboard masks over object lists
(`vision.champion_tiles()` at 9k over `vision.champions()` at 46k).

**Running out mid-turn does not raise — it suspends.** Execution resumes next round from the suspension
point, so the champion silently does nothing for a round. Observed directly: `fuel_remaining()` deltas go
negative across the boundary. Budget with `cambc.fuel_remaining()` and bail out to `end_turn()` early.

Unused fuel does not carry over.

## Hard constraints

- **Never edit `sdk/` or `cmake/`.** CLI-managed and verified against the template; `cambc init` restores
  them (all four languages, regardless of `cambc.toml`). Both are gitignored.
- **Stdlib only.** No pip, no numpy, no third-party imports in the sandbox.
- **The sandbox is CPython 3.13** (`/lib/python3.13`); bot source is mounted at `/guest`. Local `.venv`
  and `pyrightconfig.json` are pinned to 3.13 to match.
- **Module-level work is free at runtime.** The bot is wizer-snapshotted, so imports and module-level
  precomputation run at build time and cost zero fuel in-match — but have a **2-minute build limit**, and
  happen *before the map is known*. Map-dependent precompute belongs in round 1 (double fuel).
  The whole stdlib is preloaded into the snapshot, so stdlib imports are free.
- **`cambc.toml` has `languages = ["python"]`.** Keeping it that way stops `cambc init` from recreating
  the other starter bots and re-downloading a 1.77 GB wasi-sdk/cmake toolchain that Python never uses.
- **WASI randomness always returns zero in matches.** Seed a PRNG from spawn position and champion start
  position instead — see `bots/starter-python/src/randomness.py`.
- Shared memory is **8 bytes** for the whole match; draft memory is **1024 bytes**, written in the draft
  and read-only afterwards. Every allied bot must agree on the byte layout.
- Each champion is a **separate bot instance** with its own state, and vision is **not** shared between
  allies. Coordination has to go through those 8 bytes.
- The bot is a **persistent process**: `main.py` loops forever and calls `cambc.end_turn()` to yield, so
  instance state survives between turns.

## Gotchas worth not rediscovering

- **Ranged champions cannot move and basic-attack in the same turn** — the two share one allowance.
  Melee can do both. Attack-reset abilities restore the attack allowance.
- **A blocked move returns `False`; it does not raise** — that's a hidden enemy in a bush. The attempt
  costs no movement allowance, cooldown or consumable, and reveals the tile for the rest of the round, so
  pick another tile and retry. A destination *known* to be occupied raises `cambc.Error` instead.
- **Channel timing:** timers tick at the owner's *turn end* (including the turn you start one) and
  complete at the owner's *next turn start*. A 1-tick tribute finishes at your next turn start, not at the
  end of the turn you began it.
- **Tribute duration is `max(1, ceil(gems / 10))`** turn ends, computed from your bag *when you start*,
  but completion banks your whole bag including gems gained since. Captures resolve before channels.
- **Carried gems are not score.** They are stolen by whoever kills you, destroyed if a camp kills you, and
  only count once tributed.
- Damage does **not** interrupt a tribute; stun, death or a new altar lock does. Damage *does* interrupt
  a recall.
- Monsters are friendly until hit, then attack the nearest champion until they die or go 2 rounds
  untouched. All of them have attack range 3 and vision 8, see through bushes, and never chase.
- **Capture requires standing on a cleared group's spawn tile, uncontested, for 5 rounds.** Extra allies
  don't speed it up; an empty or contested region resets it.
- Teams alternate who acts first each round, and `set_priority` only takes effect from the next round.

## The arena

`scripts/arena.py` plays both bots on every map **twice, with sides swapped** — side assignment is not
neutral (Team B wins all-tie tiebreaks, and the starting team alternates). On the current pool, Team A
wins on `collision`, `corners`, `elkring`, `interlock`, `lanes`, `packs`; Team B wins on `expanse`,
`monolith`, `rows`.

**The engine is fully deterministic.** Identical bots produce byte-identical results every time, so two
scaffold copies score exactly 9-9 and *any* change in the table is a real behavioural change, not
variance. No need to repeat matches for significance.

A nonzero exit means a bot crashed (`botFaults`) or a match failed. Crashes are bugs, not losses — the
starter catches exceptions per turn and keeps going, so a fault count above zero means something escaped
that handler.

**Known flake:** roughly 1 match in 18 can fail to produce statistics under `-j 4`, and passes on retry.
Full transcripts land in `replays/arena-failures/`. If it reproduces at `-j 1`, it's real.

## Layout

| Path | |
|---|---|
| `bots/main/src/` | the bot — all development here |
| `bots/baseline/src/` | frozen comparison fixture; advance with `arena.py --snapshot` |
| `bots/starter-python/` | pristine CLI template; restore a file from here |
| `scripts/arena.py` | head-to-head harness |
| `agents/*.md` | rules and API reference — read, never edit |
| `maps/` | 9-map competition pool, committed |
| `sdk/`, `cmake/`, `.cambc/`, `replays/`, `.venv/` | generated, gitignored |

## Notes

- The CLI nags that "a newer version is available" — it's comparing against the platform's published
  build, which is **2.1.5**, older than the **2.1.6** we have from PyPI. Ignore it, or set
  `CAMBC_NO_UPDATE_CHECK=1`. Re-check before the deadline in case the platform moves ahead.
- `cambc submit` uploads **source**, which the platform compiles with its own SDK. If the platform is
  still on 2.1.5 at submission time, verify a submission actually builds server-side.
