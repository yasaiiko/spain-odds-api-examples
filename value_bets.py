"""Print the current value bets: Spanish bookmaker prices above Pinnacle's no-vig fair odds."""

import argparse

from common import fmt, run_actor

ap = argparse.ArgumentParser()
ap.add_argument("--min-ev", type=float, default=0.02)
ap.add_argument("--league", action="append", default=[], help="la_liga, premier_league, serie_a, ...")
ap.add_argument("--bookmaker", action="append", default=[], help="e.g. 'Tonybet.es'")
args = ap.parse_args()

rows = run_actor({"mode": "value_bets", "minEv": str(args.min_ev), "leagues": args.league,
                  "bookmakers": args.bookmaker, "maxResults": 200})
for r in sorted(rows, key=lambda r: -r["ev"]):
    print(fmt(r))
print(f"\n{len(rows)} value bets (EV ≥ {args.min_ev:.0%})")
