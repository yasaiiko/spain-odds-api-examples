"""Closing line value: did the opening odds of each bookmaker beat Pinnacle's closing fair price?"""

import argparse
from collections import defaultdict
from datetime import date, timedelta

from common import run_actor

ap = argparse.ArgumentParser()
ap.add_argument("--date", default=str(date.today() - timedelta(days=1)), help="kick-off date YYYY-MM-DD")
args = ap.parse_args()

rows = run_actor({"mode": "closing_lines", "dateFrom": args.date, "dateTo": args.date,
                  "includePinnacle": False, "maxResults": 5000})
by_book = defaultdict(list)
for r in rows:
    if r.get("clv_opening") is not None:
        by_book[r["bookmaker"]].append(r["clv_opening"])
print(f"Average CLV of opening odds vs Pinnacle's closing fair line, matches on {args.date}:")
for book, v in sorted(by_book.items(), key=lambda kv: -sum(kv[1]) / len(kv[1])):
    print(f"  {book:<22} {sum(v) / len(v):+.2%}  ({len(v)} selections)")
