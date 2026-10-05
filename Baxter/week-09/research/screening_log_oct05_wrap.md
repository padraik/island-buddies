# Screening Log: Mon Oct 5, 2026, 4:15pm ET run (VM, WRAP slot)

**Source:** the research queue as the 3:35 LASTCALL run left it. WRAP is a PREPARE slot: free checks only, no chain checks and no web searches. The next three Tier A names (COLL, AORT, TREE) got their earnings date and Rule 6 history, and the seven names ahead of them got closing prices and a ratings refresh.

**Rule 5 line (Tuesday preview, if the $290.54 settles):** reserve ~$741.32. The 3.5/5 line is **$0.741** and the 4/5 line is $1.00 (transitional lock).

**Prices are the 4:00pm ET closing trades.**

## Funnel

| Stage | Names | Tool |
|---|---|---|
| Queue in | 3 new (COLL, AORT, TREE) + 7 refreshed | research_queue.md |
| Rule 2 date check | COLL **Nov 5 AM** (scanner 11/06), AORT **Nov 5 PM** (11/06), TREE **Oct 29 AM** (10/30). All unverified. The scanner date was a day late again on all three, which makes 13 of 13 Tier A names today. COUR still **Oct 22 PM, unverified**. | get_earnings_results |
| Rule 3 / Rule 4 proxy refresh | 8 (COLL, AORT, TREE, COUR, PCT, CWH, ADTN, REZI). None changed from the queue. | get_equity_analyst_ratings |
| Rule 6 history (free) | 3 | get_equity_historicals, daily, 6 prints each |
| Killed without a chain | 0 | |
| Alive, chain next | 3 (TREE, AORT, COLL) | |

## Rule 6 history

Each move runs from the prior close to the reaction-day close. For an AM print that's the day before to the print day; for a PM print it's the print day to the next day. Max BE uses the Oct 5 close.

| Ticker | Close | Print moves (oldest -> newest) | Median | Cap | Max BE at cap |
|---|---|---|---|---|---|
| COLL | $21.88 | +5.9 (PM), +10.7, +13.4, -3.3, +7.7, -18.6 (AM) | 9.20% | 13.80% | $24.90 |
| AORT | $22.615 | +15.4, +25.2, -5.5, -10.0, -28.3, +2.1 (all PM) | 12.70% | 19.05% | $26.92 |
| TREE | $24.55 | -20.1 (PM), +6.0 (PM), +6.3 (AM), +23.9, -21.7, -19.6 (PM) | 19.85% | 29.78% | $31.86 |

## Verdicts

| Ticker | Earnings (tool) | Ratings B/H/S | Low tgt | Range | Verdict |
|---|---|---|---|---|---|
| TREE | Oct 29 AM (unverified) | 6/0/0 | $45 | 0.025 | **ALIVE, chain next (best of the three).** Max BE $31.86, R4 floor $45. A $27.5C or $30C asking $0.74 or less passes R4, R5 and R6. Ramp-sell deadline would be **Oct 28 3:35pm ET** (AM print). **Bearxter:** 3 of the last 6 prints fell ~20%, including the last two, and the last two quarters missed EPS (Q1 1.22 vs 1.34, Q2 0.68 vs 1.33). That's a fundamental slide, and the doc has to answer it. |
| AORT | Nov 5 PM (unverified) | 8/0/0 | $38 | 0.11 | **ALIVE, chain next.** Max BE $26.92, R4 floor $38. A $25C passes R6 up to a $1.92 ask, so R5 ($0.74) is the binding rule. A $22.5C would have to be under $0.74 with the stock at the strike, which is unlikely. **Bearxter:** the May 2026 print fell 28.3% on an EPS miss. |
| COLL | Nov 5 AM (unverified) | 7/1/0 | $43 | 0.02 | **ALIVE, low odds.** Max BE $24.90. A $25C fails R6 at any price. A $22.5C needs an ask of $0.74 or less with the stock $0.62 under the strike, which is unlikely for 46 days. Only a listed $24C at $0.74 or less (BE $24.74) would fit. If strikes are 2.5-wide, kill it on the chain. |

## Refreshed (no change in status)

| Ticker | Close | Ratings B/H/S | Low tgt | Note |
|---|---|---|---|---|
| COUR | $5.185 | 8/4/0 | $6.50 | Oct 22 PM still unverified. $5C was last 0.60/0.70 (2:35pm). |
| PCT | $4.09 | 3/3/0 | $6.00 | Nov 5 PM unverified. |
| CWH | $4.545 | 11/2/0 | $6.00 | Analysts still haven't reacted to the guidance cut. |
| ADTN | $7.15 | 7/2/0 | $11.00 | $7C was 0.75/0.85 at 2:35pm, $0.01-0.11 over the line. |
| REZI | $18.575 | 6/1/0 | $27.00 | Max BE at 24.23% cap from today's close: $23.08. |
| FWRG | $10.51 | (not re-pulled) | $15 | Max BE from close: $11.66. |
| QBTS | $15.64 | (not re-pulled) | $22 | Max BE from close: $17.46. |

## GLOSSARY

- **R1 / Rule 1:** the stock has to sit in the bottom quarter of its 52-week range (calls).
- **R2 / Rule 2:** the earnings date has to be real, in the window, and not already past.
- **R3 / Rule 3:** analyst mix: 3+ Buys, Buys at least equal to Holds, at most 1 Sell.
- **R4 / Rule 4:** the lowest analyst Buy target has to sit above our breakeven.
- **R5 / Rule 5:** the premium cap per share, set by conviction tier and the reserve.
- **R6 / Rule 6:** the move needed to reach breakeven can't exceed 1.5x the stock's median earnings-day move.
- **BE (breakeven):** strike plus premium paid. The stock has to close above this at exit for the call to make money.
- **Max BE at cap:** current price x (1 + R6 cap). The highest breakeven Rule 6 allows.
- **Range:** where the price sits in the 52-week range, 0 = at the low, 1 = at the high.
- **AM / PM print:** earnings released before the open / after the close.
- **Ramp sell:** selling the option into the run-up before earnings instead of holding through the report.
- **Unverified:** the date is estimated from the company's cadence, not announced.
- **Free math:** a check done from price history alone, without spending a chain check.
