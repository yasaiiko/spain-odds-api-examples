"""Betfair Exchange Spain: back/lay spread and liquidity for upcoming matches, tightest spread first."""

import os
import sys

from apify_client import ApifyClient

ACTOR = "Yakk000/betfair-exchange-spain-odds"

token = os.environ.get("APIFY_TOKEN")
if not token:
    sys.exit("Set APIFY_TOKEN (https://console.apify.com/settings/integrations)")
client = ApifyClient(token)
run = client.actor(ACTOR).call(run_input={"mode": "upcoming", "maxResults": 200})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id

rows = [r for r in client.dataset(dataset_id).iterate_items() if r.get("lay_odds")]
rows.sort(key=lambda r: r["lay_odds"] / r["odds"])
for r in rows[:25]:
    spread = r["lay_odds"] / r["odds"] - 1
    print(f"{r['start'][:16].replace('T', ' ')} {r['home']} v {r['away']} [{r['market']} {r['selection']}] "
          f"back {r['odds']} (€{r.get('liquidity_eur') or 0:.0f}) lay {r['lay_odds']} (€{r.get('lay_liquidity_eur') or 0:.0f}) "
          f"spread {spread:.1%}")
