# SCREENING LOG — Wed Oct 7, 2026, 3:35pm ET (VM LASTCALL run, PREPARE)

**Source:** research_queue.md plan written by the 2:35 run: date checks on COUR / QUBT / ONDS / TDUP, ratings on the queue, then tee up EVENING 1 with a **$10-15 scan** (prints Oct 20 - Nov 20). LASTCALL is a PREPARE slot: free tools only (scanner, ratings, dates, quotes). No chains, no web searches.

Scan (preview, not saved): market cap $300M+, earnings Oct 20 - Nov 20, stock, price $10-15, 52-week range percentile < 0.25 (same expression filter as the Oct 5 sweep). **113 matches, all returned.** Deduped against every ticker in this week's research files, research_queue.md and passes.md: **6 new names** (RDY, NEWT, KRSP, MTRX, MARA, RDW), plus F (Ford), re-checked because a one-letter ticker can't be deduped by text search.

| Step | Names | Tool |
|---|---|---|
| Dates | COUR, QUBT, ONDS, TDUP | get_earnings_results |
| Ratings | 18 queue names + 7 new | get_equity_analyst_ratings (2 calls) |
| Requotes | COUR, QUBT, ONDS, TDUP | get_option_quotes, get_equity_quotes |
| Scanner | 1 preview, 113 rows | preview_scan |
| Killed | **7** (all free, R3 / R4 proxy) | |
| Advanced | none | |

## Dates (queue)

| Ticker | Date (tool) | Verified | Note |
|---|---|---|---|
| COUR | Oct 22 PM | false | Unchanged. |
| QUBT | Nov 13 PM | false | Unchanged. |
| ONDS | Nov 12 AM | false | Unchanged. |
| TDUP | Nov 2 PM | false | Unchanged. |

## Requotes (3:35pm ET)

| Ticker | Stock | Contract | Bid / Ask | R5 / R6 at the ask |
|---|---|---|---|---|
| COUR | $5.135 | $5C Nov20 | 0.55 / 0.70, OI 3,137 | Passes R5 ($0.70 <= $0.741). Date gate only. Bid jumped from 0.40 to 0.55. |
| QUBT | $7.595 | $8C Nov20 | 0.54 / 0.60, OI 769 | Max price = 7.595 x 1.1388 - 8.00 = $0.649. Passes at the ask (BE $8.60). Date gate only. |
| ONDS | $7.155 | $8C Nov20 | 0.45 / 0.48, OI 10,604 | Max price = 7.155 x 1.2089 - 8.00 = $0.650. Passes. Date gate only. |
| TDUP | $2.235 | $2.5C Nov20 | 0.15 / 0.25, OI 17 | Max price = 2.235 x 1.285 - 2.50 = $0.372. Passes R5/R6. Floor-blocked. |

## Ratings (queue, unchanged)

COUR 8/4/0 low $6.00; QUBT 5/2/0 low $10; ONDS 11/0/0 low $13; FUBO 8/2/0 low $12; FINV 6/1/0 low $4.11; TDUP 6/1/0 low $5.70; BRSL 7/3/0 low $11.90; TME 22/14/0 low $9.04; OBDC 11/2/0 low $11; GAU 5/1/0 low $2.99; SERV 6/2/0 low $7; FRMI 6/2/0 low $6; ADTN 7/2/0 low $11; MLCO 11/4/0 low $5.30; PCT 3/3/0 low $6; ENVX 7/3/1 low $5; BXMT 5/4/0 low $16; CWH 11/2/0 low $6. No counts or lows moved.

## Free screen: 7 names

| Ticker | Stock | Ratings B/H/S, low | Verdict |
|---|---|---|---|
| RDY | $12.255 | 17/10/13, $10.85 | **KILL, R3** (13 Sells). |
| NEWT | $10.945 | 2/5/0, $13 | **KILL, R3** (2 Buys, Holds > Buys). |
| KRSP | $10.57 | no coverage | **KILL, R3** (SPAC). |
| MTRX | $10.38 | no coverage | **KILL, R3.** |
| MARA | $10.305 | 10/4/2, $10 | **KILL, R3** (2 Sells; low = price anyway). |
| RDW | $10.215 | 6/3/1, $8 | **KILL, R4 proxy** (lowest target $8 under the stock). |
| F | $12.10 | 8/13/1 | **KILL, R3** (Holds > Buys). |

## What this means

Prints Oct 20 - Nov 20, bottom quartile, $300M+: the **$2-10 band (248 names) and the $10-15 band (113 names) have both been through the funnel this week.** Of the 113, 106 were already in the logs. The well under $15 is dry for this earnings window. EVENING 1 needs a different source (see research_queue.md).

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R1 (52w):** (price - 52-week low) / (52-week high - 52-week low); calls need <= 0.25.
- **R2:** a confirmed earnings date before expiry. `verified: false` means the date is estimated from the company's cadence, not announced.
- **R3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4:** lowest Buy target, dated within 60 days, above breakeven. **R4 proxy** (free screen): the tool's lowest target sits under the stock price. "Floor-blocked" = the target clears, but no Buy target dated inside 60 days has been found yet.
- **R5:** one contract's ask <= 10% of reserve / 100 at 3.5/5 (today $0.741).
- **R6:** move to breakeven <= 1.5x the median earnings-day move (the "cap"). Max price = stock x (1 + cap) - strike.
- **OI (open interest):** contracts outstanding. Low OI means a thin market and wide spreads.
- **DOC COMPLETE:** research doc with Iron Rules, Five-Baxter meeting, EXIT PLAN, sizing and GLOSSARY committed; entry waits only on the named gates.
- **PREPARE slot:** a run that tees up the next one instead of doing chain checks or web searches.
