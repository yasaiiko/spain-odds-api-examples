"""Send new value bets to Telegram. Run it every 10–30 minutes (cron, Task Scheduler or an Apify Schedule).

Env: APIFY_TOKEN, TELEGRAM_BOT_TOKEN (from @BotFather), TELEGRAM_CHAT_ID.
Bets already sent are remembered in sent.json, so nothing is sent twice (unless the odds change).
"""

import json
import os
from pathlib import Path

import httpx

from common import fmt, run_actor

SEEN = Path(__file__).with_name("sent.json")
MIN_EV = float(os.environ.get("MIN_EV", "0.03"))

seen = set(json.loads(SEEN.read_text())) if SEEN.exists() else set()
rows = run_actor({"mode": "value_bets", "minEv": str(MIN_EV), "maxResults": 200})
new = [r for r in rows if f"{r['event_key']}|{r['bookmaker']}|{r['market']}|{r['selection']}|{r['odds']}" not in seen]

for r in sorted(new, key=lambda r: -r["ev"]):
    httpx.post(f"https://api.telegram.org/bot{os.environ['TELEGRAM_BOT_TOKEN']}/sendMessage",
               json={"chat_id": os.environ["TELEGRAM_CHAT_ID"], "text": "💰 " + fmt(r)}, timeout=30)
    seen.add(f"{r['event_key']}|{r['bookmaker']}|{r['market']}|{r['selection']}|{r['odds']}")

SEEN.write_text(json.dumps(sorted(seen)))
print(f"{len(new)} new alerts sent")
