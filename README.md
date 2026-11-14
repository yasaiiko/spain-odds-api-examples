<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img src="assets/hero-light.svg" width="900" alt="Spain Odds API: odds from Spanish-licensed bookmakers, de-vigged against Pinnacle">
</picture>

<br>

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-97d700?style=flat-square&logo=apify&logoColor=white)](https://apify.com/Yakk000/spain-odds-pinnacle-value)
[![Python](https://img.shields.io/badge/Python-examples-3776ab?style=flat-square&logo=python&logoColor=white)](requirements.txt)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-valuebets__es-26a5e4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/valuebets_es)
[![Daily preview](https://img.shields.io/badge/Web-daily%20preview-222?style=flat-square&logo=githubpages&logoColor=white)](https://yasaiiko.github.io/spain-odds-api-examples/)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stats-dark.svg">
  <img src="assets/stats-light.svg" width="900" alt="11 Spanish bookmakers plus Betfair Exchange, 18 competitions, Pinnacle no-vig fair odds, refreshed at least every 30 minutes">
</picture>

</div>

Python examples for the **[Spanish Bookmakers Odds API](https://apify.com/Yakk000/spain-odds-pinnacle-value)** on Apify: pre-match odds from William Hill, Betway, bwin, Tonybet, LeoVegas, Paf, Bet777, Yaass, Sportium, Marca Apuestas and Versus, plus Betfair Exchange Spain, de-vigged against **Pinnacle** and refreshed at least every 30 minutes.

## ⚡ Quick start

```bash
pip install -r requirements.txt
export APIFY_TOKEN=your_apify_token   # https://console.apify.com/settings/integrations
python value_bets.py --min-ev 0.03 --league la_liga
```

> [!TIP]
> On Windows PowerShell, use `$env:APIFY_TOKEN="..."` instead of `export`.

The Actor is pay per result (about $1.50 per 1,000 rows). Each example caps its rows with `maxResults`, so a run costs cents.

## 🧰 Examples

| | Script | What it does |
|:-:|---|---|
| 💎 | [`value_bets.py`](value_bets.py) | Current +EV value bets against Pinnacle's no-vig fair odds |
| 🔔 | [`telegram_alerts.py`](telegram_alerts.py) | Sends each new value bet to a Telegram chat, without repeats (run it on a schedule) |
| 🏆 | [`best_odds.py`](best_odds.py) | Best Spanish price per outcome for a team's next match, and whether it's a surebet |
| ⚖️ | [`betfair_back_lay.py`](betfair_back_lay.py) | Betfair Exchange Spain back and lay prices with liquidity, tightest spread first ([Actor](https://apify.com/Yakk000/betfair-exchange-spain-odds)) |
| 🔮 | [`polymarket_vs_pinnacle.py`](polymarket_vs_pinnacle.py) | How far Polymarket sports prices are from Pinnacle's no-vig line after fees, by league ([Actor](https://apify.com/Yakk000/polymarket-sports-odds-pinnacle)) |
| 📈 | [`clv_report.py`](clv_report.py) | Closing line value of the opening odds for the matches played on a given day |

## 🌐 Real-time HTTP API (no SDK)

```bash
curl "https://yakk000--spain-odds-pinnacle-value.apify.actor/?mode=value_bets&leagues=la_liga&minEv=0.03&maxResults=20" \
  -H "Authorization: Bearer $APIFY_TOKEN"
```

## 📦 Output fields

```text
league, start, home, away, bookmaker, market (1x2 | ou2.5), selection (1/X/2 | over/under),
odds, opening, moves, pinnacle_fair_prob, ev, data_updated_at
```

`ev = odds × pinnacle_fair_prob − 1`, where the fair probability comes from Pinnacle's latest prices with the margin removed by multiplicative normalisation. For Betfair Exchange, EV is net of the 5% commission.

<details>
<summary><b>Coverage</b></summary>

- **Football:** LaLiga, Segunda, Copa del Rey, Premier League, Championship, Bundesliga, Serie A, Ligue 1, Eredivisie, Primeira Liga, Champions League, Europa League, Conference League. Markets: 1X2 and over/under 2.5 goals.
- **Basketball:** NBA, EuroLeague, Liga ACB. Market: moneyline.
- **Tennis:** ATP and WTA singles. Market: moneyline.

</details>

---

<sub>Market data, not betting advice. 18+, gamble responsibly. · MIT License</sub>
