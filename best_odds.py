"""Best Spanish price per outcome for a team's upcoming matches, and the combined book % (< 100% = surebet)."""

import argparse
from itertools import groupby

from common import run_actor

ap = argparse.ArgumentParser()
ap.add_argument("team", help="e.g. Betis")
args = ap.parse_args()

rows = run_actor({"mode": "best_odds", "teamFilter": args.team, "maxResults": 100})
rows.sort(key=lambda r: (r["start"], r["event_key"], r["market"], r["selection"]))
for (start, _, market), grp in groupby(rows, key=lambda r: (r["start"], r["event_key"], r["market"])):
    grp = list(grp)
    r0 = grp[0]
    tag = "  ← SUREBET" if r0["is_surebet"] else ""
    print(f"{start[:16]} {r0['home']} v {r0['away']} [{market}] book {r0['combined_book']:.1%}{tag}")
    for r in grp:
        stake = f", stake {r['surebet_stake_share']:.1%}" if r.get("surebet_stake_share") else ""
        print(f"   {r['selection']:>5} @ {r['odds']:<6} {r['bookmaker']} ({r['n_books']} books){stake}")
