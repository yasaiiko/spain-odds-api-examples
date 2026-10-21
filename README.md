# Spanish Bookmakers Odds API: examples

Python examples for the [Spanish Bookmakers Odds API](https://apify.com/Yakk000/spain-odds-pinnacle-value) on Apify. It provides pre-match football odds from **14 Spanish-licensed bookmakers** (William Hill.es, Betway.es, Bwin.es, Tonybet.es, LeoVegas.es, Paf.es, Admiralbet.es, Paston, Bet777.es, Yaass and Betfair Exchange.es), de-vigged against **Pinnacle**, and refreshed every 10 minutes.

| Example | What it does |
|---|---|
| [`value_bets.py`](value_bets.py) | Prints the current +EV value bets against Pinnacle's no-vig fair odds |
| [`telegram_alerts.py`](telegram_alerts.py) | Sends each new value bet to a Telegram chat, without repeats (run it on a schedule) |
| [`best_odds.py`](best_odds.py) | Best Spanish price per outcome for a team's next match, and whether it's a surebet |
| [`clv_report.py`](clv_report.py) | Closing line value of the opening odds for the matches played on a given day |

📣 **Free daily value bets on Telegram:** [t.me/valuebets_es](https://t.me/valuebets_es) · 🌐 **Daily web preview:** [yasaiiko.github.io/spain-odds-api-examples](https://yasaiiko.github.io/spain-odds-api-examples/)

## Setup

```bash
pip install -r requirements.txt
export APIFY_TOKEN=your_apify_token   # https://console.apify.com/settings/integrations
python value_bets.py --min-ev 0.03 --league la_liga
```

On Windows PowerShell, use `$env:APIFY_TOKEN="..."` instead of `export`.

The Actor is pay per result (about $1.50 per 1,000 rows). Each example caps its rows with `maxResults`, so a run costs cents.

## Output fields

`league, start, home, away, bookmaker, market (1x2 | ou2.5), selection (1/X/2 | over/under), odds, opening, moves, pinnacle_fair_prob, ev, data_updated_at`

`ev = odds × pinnacle_fair_prob − 1`, where the fair probability comes from Pinnacle's latest prices with the margin removed by multiplicative normalisation. For Betfair Exchange, EV is net of the 5% commission.

## Disclaimer

This is market data, not betting advice. 18+, gamble responsibly.

## License

MIT

## Real-time HTTP API (no SDK)

```bash
curl "https://yakk000--spain-odds-pinnacle-value.apify.actor/?mode=value_bets&leagues=la_liga&minEv=0.03&maxResults=20" \
  -H "Authorization: Bearer $APIFY_TOKEN"
```
