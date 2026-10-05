# Screening Log: Mon Oct 5, 2026, 2:35pm ET run (VM, MIDDAY slot)

**Source:** the research queue as left by the 1:35 run (COUR, PCT, CWH on top, then Tier A cheapest-first: GRAB, PHAT, ADTN, ALHC, AMPX). No fresh scanner pass. Run was under HALT (no order tools); research only.

**Rule 5 line this run:** reserve = spendable cash $450.78 ($290.54 still unsettled until Tue Oct 6). Screen line $0.90/share, 3.5/5 tier top $0.45, 4/5 tier top $0.72. **Tuesday preview** (reserve ~$741.32 if it settles): 3.5/5 line **$0.741**, 4/5 line $1.00 (transitional lock). Verdicts below are against the Tuesday line, since nothing can be bought today anyway.

**Prices pulled 2:35-2:37pm ET.**

## Funnel

| Stage | Names | Tool |
|---|---|---|
| Queue in | 8 touched (COUR, PCT, CWH, GRAB, PHAT, ADTN, ALHC, AMPX) | research_queue.md |
| Rule 2 date check | GRAB **Nov 2 PM** (scanner 11/03), PHAT **Oct 29 AM** (scanner 10/30), ADTN **Nov 2 PM** (scanner 11/03), ALHC **Oct 29 PM** (scanner 10/30), AMPX **Nov 5 PM** (scanner 11/06). All unverified. The scanner runs one day late on every one of them. | get_earnings_results |
| Rule 3 / Rule 4 proxy refresh | 8. CWH unchanged after the guidance cut (11 B / 2 H / 0 S, low $6). Others unchanged from the sweep. | get_equity_analyst_ratings |
| Rule 6 history (free) | GRAB, PHAT, ADTN, ALHC, AMPX | get_equity_historicals, daily, 6 prints each |
| Killed without a chain | GRAB (R6) | free math |
| Chain check (cap 5) | 4 (PHAT, ADTN, ALHC, AMPX) | get_option_instruments / get_option_quotes, Nov 20 calls |
| Requote | COUR $5C, CWH $4C | get_option_quotes |
| Killed | 4 (GRAB, PHAT, ALHC, AMPX) | |
| Alive | COUR, PCT, ADTN, CWH | |

## Rule 6 history

Prior close -> reaction-day close (AM print: day before -> print day; PM print: print day -> next day).

| Ticker | Price | Print moves (oldest -> newest) | Median | Cap | Max BE at cap |
|---|---|---|---|---|---|
| GRAB | $3.17 | +1.9, -7.6, -4.7 (AM), +0.9, +1.7, +1.4 (PM) | 1.80% | 2.70% | $3.26 |
| PHAT | $6.74 | -21.7, +8.3, -1.6, +10.1, -4.9, -22.4 (all AM) | 9.20% | 13.80% | $7.67 |
| ADTN | $7.095 | -3.0, -14.6, -24.2, -7.3, -16.6, -1.1 (all PM) | 10.95% | 16.42% | $8.26 |
| ALHC | $8.425 | -7.4, +6.0, -1.5, -5.9, -10.1, -20.2 (all PM) | 6.70% | 10.05% | $9.27 |
| AMPX | $9.35 | -0.8, +4.4, +13.1, +18.6, -27.4, +8.4 (all PM) | 10.75% | 16.12% | $10.86 |

## Chain-checked / requoted

| Ticker | Earnings (tool) | Ratings B/H/S | Low tgt | Contract | Bid/Ask | BE (ask) | Needs | R6 cap | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| GRAB | Nov 2 PM (unverified) | 24/0/0 | $4.50 | none checked | | | | 2.70% | **KILL, R6 (free).** Max BE $3.26. The $3C carries $0.17 intrinsic, so it would need under $0.09 of time value for 46 days; $3.5C BE is above max. No chain spent. |
| PHAT | Oct 29 AM (unverified) | 9/2/0 | $10 | $7.5C Nov20 | 0.50 / 4.50 | $12.00 | +78% | 13.80% | **KILL, R6 + R5 + liquidity.** Only 2.5-wide strikes. $4.00 wide spread, OI 16. Even at a $0 premium the $7.5C BE is barely under max. |
| ADTN | Nov 2 PM (unverified) | 7/2/0 | $11 | $7C / $8C Nov20 | 0.75/0.85, 0.40/0.50 | $7.85 / $8.50 | +10.6% / +19.8% | 16.42% | **ALIVE, $7C fails R5 by $0.11 at the ask (Tuesday line $0.74).** R6 passes on the $7C (10.6% vs 16.42%), R4 passes ($11 vs $7.85). OI 1,598, volume 1,087 today. $8C fails R6. **Bearxter:** 5 of the last 6 prints fell, and four fell more than 7%. |
| ALHC | Oct 29 PM (unverified) | 12/2/0 | $13 | $7.5C Nov20 | 1.40 / 2.40 | $9.90 | +17.5% | 10.05% | **KILL, R5 + R6.** Only 2.5-wide strikes: $7.5C carries $0.93 intrinsic (over any R5 line), $10C BE above $9.27 max. |
| AMPX | Nov 5 PM (unverified) | 11/0/0 | $18 | $9C / $10C Nov20 | 1.20/1.40, 0.85/0.95 | $10.40 / $10.95 | +11.2% / +17.1% | 16.12% | **KILL, R5 (+ R6 on the $10C).** $9C passes R6 but asks $1.40. $10C asks $0.95 and BE $10.95 is over the $10.86 max. |
| CWH | Oct 27 (from earlier runs) | 11/2/0 | $6 | $4C Nov20 | 0.65 / 0.90 | $4.90 | +9.3% | 23.90% | **ALIVE, fails R5 ($0.90 vs $0.74).** Spread widened from 0.60/0.80. Ratings not yet moved by the guidance cut. Decline category leans fundamental (guidance cut + refinancing search), not a sentiment dip. |
| COUR | Oct 22 PM (unverified) | 8/4/0 | $6.50 | $5C Nov20 | 0.60 / **0.70** | $5.70 | +9.6% | 19.89% | **ALIVE, ask back to $0.70: fits Tuesday's $0.741 line.** OI 3,135. Stock $5.20. |

## Notes

- **Scanner earnings dates run one day late.** All five Tier A names this run came back a trading day earlier from `get_earnings_results` than the sweep listed. KGC was off by four days at 1:35. Every Tier A date should be treated as a placeholder until the tool confirms it.
- ADTN is the only new name past the chain stage. It's behind COUR and PCT.

## GLOSSARY

- **R1 / Rule 1:** the stock has to sit in the bottom quarter of its 52-week range (calls).
- **R2 / Rule 2:** the earnings date has to be real, in the window, and not already past.
- **R3 / Rule 3:** analyst mix: 3+ Buys, Buys at least equal to Holds, at most 1 Sell.
- **R4 / Rule 4:** the lowest analyst Buy target has to sit above our breakeven.
- **R5 / Rule 5:** the premium cap per share, set by conviction tier and the reserve.
- **R6 / Rule 6:** the move needed to reach breakeven can't exceed 1.5x the stock's median earnings-day move.
- **BE (breakeven):** strike plus premium paid. The stock has to close above this at exit for the call to make money.
- **Max BE at cap:** current price x (1 + R6 cap). Highest breakeven Rule 6 allows.
- **Intrinsic value:** how far in the money a call already is (stock minus strike).
- **OI (open interest):** contracts currently open on that strike. Low OI = hard to get out at a fair price.
- **AM / PM print:** earnings released before the open / after the close.
- **Unverified:** the date is estimated from the company's cadence, not announced.
