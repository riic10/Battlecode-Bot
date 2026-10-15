# Battlecode-Bot

Python bot for [Cambridge Battlecode](https://2026a.battlecode.co.uk) event `cambc2026a`.

## Setup on a fresh clone

```powershell
uv tool install cambc          # the CLI (a single native binary)
cambc init --yes               # restores sdk/ and cmake/, which are not committed
uv venv --python 3.13          # matches the sandbox interpreter, for editor typechecking
```

`cambc init` is safe to re-run: it preserves `maps/`, hand-written `.gitignore` entries, and the
`languages = ["python"]` setting in `cambc.toml`.

## Daily loop

```powershell
cambc run main baseline --map packs --view   # play one match and watch it
python scripts/arena.py                      # 18 matches: 9 maps, both sides
python scripts/arena.py --snapshot            # promote main over baseline once it wins
```

Development happens in [bots/main/src/](bots/main/src/). [bots/baseline/src/](bots/baseline/src/) is a
frozen copy used only as a comparison opponent.

## Submitting

```powershell
cambc build main     # verify it compiles the way the submission service expects
cambc login          # browser device-code flow, 7-day session
cambc submit main    # uploads to your team's submissions
```

## Reference

[CLAUDE.md](CLAUDE.md) has the fuel budget, measured SDK call costs, and the rule gotchas that cost the
most time to rediscover. [agents/GameRules.md](agents/GameRules.md) and
[agents/BotAPIPython.md](agents/BotAPIPython.md) are the official rules and API reference.
