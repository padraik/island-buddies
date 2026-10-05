# Screening Log: Mon Oct 5, 2026, 3:35pm ET run (VM, LASTCALL slot)

**Source:** the research queue as the 2:35 run left it, entries 5-9 (FWRG, UUUU, QXO, QBTS, REZI). LASTCALL is a PREPARE slot, so only the free checks ran: no chain checks and no web searches. Ratings were also refreshed on the four names ahead of these (COUR, PCT, CWH, ADTN).

**Rule 5 line (Tuesday preview, if the $290.54 settles):** reserve ~$741.32. The 3.5/5 line is **$0.741** and the 4/5 line is $1.00 (transitional lock).

**Prices pulled 3:35pm ET.**

## Funnel

| Stage | Names | Tool |
|---|---|---|
| Queue in | 5 (FWRG, UUUU, QXO, QBTS, REZI) | research_queue.md |
| Rule 2 date check | FWRG **Nov 3 AM** (scanner 11/04), UUUU **Nov 2 PM** (11/04), QXO **Nov 5 PM** (11/06), QBTS **Nov 5 AM** (11/06), REZI **Nov 4 PM** (11/05). All unverified, and the scanner date is a day or more late on every one. | get_earnings_results |
| Rule 3 / Rule 4 proxy refresh | 9 (the five above plus COUR, PCT, CWH, ADTN). None changed from the queue. | get_equity_analyst_ratings |
| Rule 6 history (free) | 5 | get_equity_historicals, daily, 6 prints each |
| Killed without a chain | 2 (UUUU, QXO) | free math |
| Alive, chain next | 3 (REZI, FWRG, QBTS) | |

## Rule 6 history

Each move runs from the prior close to the reaction-day close. For an AM print that's the day before to the print day; for a PM print it's the print day to the next day.

| Ticker | Price | Print moves (oldest -> newest) | Median | Cap | Max BE at cap |
|---|---|---|---|---|---|
| FWRG | $10.47 | -17.6, +3.5, +11.0, -20.5, -0.2, +2.4 (all AM) | 7.27% | 10.90% | $11.61 |
| UUUU | $10.75 | +0.2, -0.8, -4.4, -6.7, -0.7, +3.7 (all PM) | 2.25% | 3.38% | $11.11 |
| QXO | $11.855 | -0.1 (PM), -0.2 (AM), +6.5 (PM), -3.7 (AM), -4.1 (PM), -2.6 (PM) | 3.15% | 4.73% | $12.42 |
| QBTS | $15.475 | +51.2, -2.3, -8.5, +2.5, -7.0, -9.3 (all AM) | 7.75% | 11.63% | $17.27 |
| REZI | $18.655 | +8.9, +8.8, -23.7, +14.4, -17.9, -20.4 (all PM) | 16.15% | 24.23% | $23.17 |

## Verdicts

| Ticker | Earnings (tool) | Ratings B/H/S | Low tgt | Verdict |
|---|---|---|---|---|
| UUUU | Nov 2 PM (unverified) | 9/0/0 | $16 | **KILL, R6 (free).** Max BE $11.11, only 3.4% above the price. A $10.5C carries $0.25 intrinsic and could hold at most $0.36 of time value for 46 days on a uranium miner, and a $11C would need a $0.11 ask. The reaction history is tiny for a stock this volatile. No chain spent. |
| QXO | Nov 5 PM (unverified) | 18/0/0 | $18 | **KILL, R6 + R5 (free).** Max BE $12.42. A $12C would have to ask $0.42 or less with the stock $0.145 below the strike; the ITM $11C would need $1.42 or less, which is still over the $0.741 line. No strike fits both rules. No chain spent. |
| REZI | Nov 4 PM (unverified) | 6/1/0 | $27 | **ALIVE, chain next.** This is the widest R6 cap on the board: max BE $23.17, R4 floor $27. Any $20-$22.5 strike asking $0.74 or less passes R6, R4 and R5. **Bearxter:** 3 of the last 4 prints fell 18-24%. Needs a look at why it sits at a 52w low (it was $30 a year ago). |
| FWRG | Nov 3 AM (unverified) | 10/0/0 | $15 | **ALIVE, chain next.** Max BE $11.61, so only an $11C (if listed) can work: it needs an ask of $0.61 or less. A $12.5C fails R6 at any price, and a $10C's ask is likely over $0.741. If there's no $11 strike, kill it. |
| QBTS | Nov 5 AM (unverified) | 15/2/1 | $22 | **ALIVE, but likely dies on the chain.** Max BE $17.27. A $16C passes at an ask of $0.74 or less, a $16.5C at $0.77 or less (R5 binds first), and a $17C at $0.27 or less. Quantum-name IV probably prices the $16C well over $1. Without the +51% May 2025 print, the median would be lower. Check it last. |

## GLOSSARY

- **R1 / Rule 1:** the stock has to sit in the bottom quarter of its 52-week range (calls).
- **R2 / Rule 2:** the earnings date has to be real, in the window, and not already past.
- **R3 / Rule 3:** analyst mix: 3+ Buys, Buys at least equal to Holds, at most 1 Sell.
- **R4 / Rule 4:** the lowest analyst Buy target has to sit above our breakeven.
- **R5 / Rule 5:** the premium cap per share, set by conviction tier and the reserve.
- **R6 / Rule 6:** the move needed to reach breakeven can't exceed 1.5x the stock's median earnings-day move.
- **BE (breakeven):** strike plus premium paid. The stock has to close above this at exit for the call to make money.
- **Max BE at cap:** current price x (1 + R6 cap). The highest breakeven Rule 6 allows.
- **Intrinsic value:** how far in the money a call already is (stock minus strike).
- **AM / PM print:** earnings released before the open / after the close.
- **Unverified:** the date is estimated from the company's cadence, not announced.
- **Free math:** a kill made from price history alone, without spending a chain check.
