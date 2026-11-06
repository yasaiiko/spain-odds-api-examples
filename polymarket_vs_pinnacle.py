"""How far Polymarket sports prices are from Pinnacle's no-vig line, after taker fees, by league."""

import os
import statistics as st
import sys
from collections import defaultdict

from apify_client import ApifyClient

ACTOR = "Yakk000/polymarket-sports-odds-pinnacle"

token = os.environ.get("APIFY_TOKEN")
if not token:
    sys.exit("Set APIFY_TOKEN (https://console.apify.com/settings/integrations)")
client = ApifyClient(token)
run = client.actor(ACTOR).call(run_input={"mode": "all", "maxResults": 500})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id

leagues = defaultdict(list)
for r in client.dataset(dataset_id).iterate_items():
    if r.get("ev") is not None and r.get("mid_vs_fair_pp") is not None and 0.05 <= r["best_ask"] <= 0.95:
        leagues[r["league"]].append(r)

print(f"{'League':<20}{'Prices':>7}{'Gap (pts)':>11}{'Median EV':>11}")
for name, rows in sorted(leagues.items(), key=lambda kv: -len(kv[1])):
    gap = st.median(abs(r["mid_vs_fair_pp"]) for r in rows)
    ev = st.median(r["ev"] for r in rows)
    print(f"{name:<20}{len(rows):>7}{gap:>11.2f}{ev:>11.1%}")
