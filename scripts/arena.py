#!/usr/bin/env python3
"""Rank two bots head-to-head across the map pool.

Every map is played twice with the sides swapped, because side assignment is not
neutral: Team B wins every all-tie tiebreak and the starting team alternates each
round. Single-side results are biased.

    python scripts/arena.py                      # main vs baseline, all maps
    python scripts/arena.py main baseline -j 4   # four matches at a time
    python scripts/arena.py --maps packs,lanes   # a quick subset
    python scripts/arena.py --snapshot           # promote main over baseline

Drives `cambc run --statistics`, which emits a JSON file per match containing the
outcome and per-champion stats. `cambc run-batch` is faster to launch but has no
--statistics flag, so its results would have to be scraped from human-readable
stdout; the JSON is worth the extra process.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
MAPS_DIR = PROJECT / "maps"
BOTS_DIR = PROJECT / "bots"


@dataclass
class Match:
    """One played match. `bot_a`/`bot_b` are the actual side assignments."""

    map_name: str
    bot_a: str
    bot_b: str
    winner: str | None = None
    rounds: int = 0
    gems: tuple[int, int] = (0, 0)
    faults: tuple[int, int] = (0, 0)
    error: str | None = None
    error_log: Path | None = None

    def gems_for(self, bot: str) -> int:
        return self.gems[0] if bot == self.bot_a else self.gems[1]

    def faults_for(self, bot: str) -> int:
        return self.faults[0] if bot == self.bot_a else self.faults[1]


def cambc_env() -> dict[str, str]:
    env = dict(os.environ)
    env["CAMBC_NO_UPDATE_CHECK"] = "1"
    return env


def run_cambc(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["cambc", *args],
        cwd=PROJECT,
        env=cambc_env(),
        capture_output=True,
        text=True,
    )


def prebuild(bots: list[str]) -> None:
    """Build each bot once, serially.

    Parallel `cambc run` invocations of the same bot would otherwise race on the
    shared build directory at bots/<name>/.cambc/build.
    """
    for bot in bots:
        print(f"building {bot}...", flush=True)
        result = run_cambc(["build", bot])
        if result.returncode != 0:
            sys.exit(f"build failed for {bot}:\n{result.stdout}\n{result.stderr}")


def play(match: Match, replay_dir: Path, rounds: int | None) -> Match:
    with tempfile.TemporaryDirectory() as scratch:
        stats_path = Path(scratch) / "stats.json"
        args = [
            "run",
            match.bot_a,
            match.bot_b,
            "--map",
            match.map_name,
            "-o",
            str(replay_dir),
            "--statistics",
            str(stats_path),
        ]
        if rounds is not None:
            args += ["--rounds", str(rounds)]

        result = run_cambc(args)
        if not stats_path.exists():
            match.error = f"exit {result.returncode}"
            # Keep the whole transcript: a one-line tail of a traceback is useless.
            # Lives outside replay_dir, which is discarded on a clean run.
            failures = PROJECT / "replays" / "arena-failures"
            failures.mkdir(parents=True, exist_ok=True)
            log = failures / f"{match.map_name}-{match.bot_a}-as-A.log"
            log.write_text(
                f"$ cambc {' '.join(args)}\nexit {result.returncode}\n"
                f"--- stdout ---\n{result.stdout}\n--- stderr ---\n{result.stderr}\n",
                encoding="utf-8",
            )
            match.error_log = log
            return match

        stats = json.loads(stats_path.read_text(encoding="utf-8"))

    outcome = stats.get("outcome")
    match.winner = {"teamA": match.bot_a, "teamB": match.bot_b}.get(outcome)
    match.rounds = stats.get("round", 0)
    teams = stats.get("teams", [])
    match.gems = tuple(team.get("submittedGems", 0) for team in teams[:2]) or (0, 0)
    faults = stats.get("botFaults") or [0, 0]
    match.faults = (faults[0], faults[1])
    return match


def resolve_maps(requested: str | None) -> list[str]:
    available = sorted(path.stem for path in MAPS_DIR.glob("*.map26a"))
    if not available:
        sys.exit("no maps in maps/; run `cambc maps pull`")
    if not requested:
        return available
    chosen = [name.strip() for name in requested.split(",") if name.strip()]
    unknown = [name for name in chosen if name not in available]
    if unknown:
        sys.exit(f"unknown map(s): {', '.join(unknown)}\navailable: {', '.join(available)}")
    return chosen


def snapshot(source: str, target: str) -> None:
    src, dst = BOTS_DIR / source / "src", BOTS_DIR / target / "src"
    if not src.is_dir():
        sys.exit(f"no such bot source: {src}")
    shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(src, dst)
    print(f"snapshot: {source}/src -> {target}/src")


def report(matches: list[Match], bot_a: str, bot_b: str) -> int:
    ordered = sorted(matches, key=lambda m: (m.map_name, m.bot_a))
    map_width = max([len(m.map_name) for m in ordered] + [len("map")])
    verdict_width = max(
        [len(f"{m.winner or 'no result'} ({m.bot_a} as A)") for m in ordered if not m.error]
        + [len("result")]
    )
    header = f"{'map':<{map_width}}  {'result':<{verdict_width}}  rounds  gems ({bot_a}-{bot_b})"
    print()
    print(header)
    print("-" * len(header))

    wins = {bot_a: 0, bot_b: 0}
    faults = {bot_a: 0, bot_b: 0}
    errors = 0

    for match in ordered:
        if match.error:
            errors += 1
            where = f"  see {match.error_log}" if match.error_log else ""
            print(f"{match.map_name:<{map_width}}  ERROR ({match.bot_a} as A): {match.error}{where}")
            continue
        if match.winner:
            wins[match.winner] += 1
        for bot in (bot_a, bot_b):
            faults[bot] += match.faults_for(bot)
        verdict = f"{match.winner or 'no result'} ({match.bot_a} as A)"
        print(
            f"{match.map_name:<{map_width}}  {verdict:<{verdict_width}}  {match.rounds:>6}  "
            f"{match.gems_for(bot_a)}-{match.gems_for(bot_b)}"
        )

    played = wins[bot_a] + wins[bot_b]
    print()
    if played:
        rate = 100.0 * wins[bot_a] / played
        print(f"{bot_a} {wins[bot_a]} - {wins[bot_b]} {bot_b}   ({rate:.1f}% for {bot_a}, {played} matches)")
    if errors:
        print(f"{errors} match(es) failed to produce statistics")
    if faults[bot_a] or faults[bot_b]:
        print(f"BOT FAULTS: {bot_a}={faults[bot_a]} {bot_b}={faults[bot_b]} -- a crashing bot is a bug, not a loss")

    return 1 if errors or faults[bot_a] or faults[bot_b] else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("bot_a", nargs="?", default="main")
    parser.add_argument("bot_b", nargs="?", default="baseline")
    parser.add_argument("--maps", help="comma-separated map names (default: the whole pool)")
    parser.add_argument("-j", "--jobs", type=int, default=4, help="matches in flight (default: 4)")
    parser.add_argument("--rounds", type=int, help="stop early; no winner is recorded if a match is cut short")
    parser.add_argument("--keep-replays", action="store_true", help="keep replay bundles instead of discarding them")
    parser.add_argument("--snapshot", action="store_true", help="copy bot_a's source over bot_b, then exit")
    args = parser.parse_args()

    if args.snapshot:
        snapshot(args.bot_a, args.bot_b)
        return 0

    for bot in (args.bot_a, args.bot_b):
        if not (BOTS_DIR / bot).is_dir():
            sys.exit(f"no such bot: bots/{bot}")

    maps = resolve_maps(args.maps)
    prebuild([args.bot_a, args.bot_b])

    # Each map twice, sides swapped.
    schedule = [
        Match(map_name=name, bot_a=a, bot_b=b)
        for name in maps
        for a, b in ((args.bot_a, args.bot_b), (args.bot_b, args.bot_a))
    ]
    print(f"{len(schedule)} matches on {len(maps)} map(s), {args.jobs} at a time")

    replay_root = PROJECT / "replays" / "arena"
    replay_root.mkdir(parents=True, exist_ok=True)

    done: list[Match] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = [pool.submit(play, match, replay_root, args.rounds) for match in schedule]
        for future in concurrent.futures.as_completed(futures):
            match = future.result()
            done.append(match)
            tag = match.error or match.winner or "no result"
            print(f"  [{len(done)}/{len(schedule)}] {match.map_name} ({match.bot_a} as A): {tag}", flush=True)

    if not args.keep_replays:
        shutil.rmtree(replay_root, ignore_errors=True)

    return report(done, args.bot_a, args.bot_b)


if __name__ == "__main__":
    sys.exit(main())
