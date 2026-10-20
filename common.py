import os
import sys

from apify_client import ApifyClient

ACTOR = "Yakk000/spain-odds-pinnacle-value"


def run_actor(run_input: dict) -> list[dict]:
    """Run the Actor and return its rows."""
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set APIFY_TOKEN (https://console.apify.com/settings/integrations)")
    client = ApifyClient(token)
    run = client.actor(ACTOR).call(run_input=run_input)
    dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
    return list(client.dataset(dataset_id).iterate_items())


def fmt(row: dict) -> str:
    ev = f"{row['ev']:+.1%}" if row.get("ev") is not None else "n/a"
    return (f"{row['start'][:16].replace('T', ' ')} UTC | {row['home']} v {row['away']} | {row['market']} "
            f"{row['selection']} @ {row['odds']} ({row['bookmaker']}) | EV {ev}")
