# Screening log, Thu Oct 8, 2026, MIDDAY (10:35am ET, VM)

Reserve $741.32 settled. Rule 5 lines: 3.5/5 $0.741, 4/5 $1.00 (transitional lock), screen $1.00.

## 1. Doc names (R2 dates + requotes, ~10:35am)

`get_earnings_results`: all six still `verified: false`, dates unchanged (COUR Oct 22 PM, ONDS Nov 12 AM, QUBT Nov 13 PM, BRSL Nov 3 AM, WRD Nov 23 AM, TME Nov 11 AM). No entry possible under the current Rule 2 reading (`call_me.md` still OPEN).

| Name | Stock | Contract | Bid / Ask | Max price (doc formula) | Verdict |
|---|---|---|---|---|---|
| COUR | $5.18 (+1.4%) | $5C Nov20 | 0.55 / 0.75 | $0.741 (R5 line) | Ask fails by $0.009 again; mid 0.65 passes. |
| ONDS | $7.035 (-2.2%) | $8C Nov20 | 0.40 / 0.41 | 7.035 x 1.2089 - 8 = $0.505 | Passes at the ask. OI 11,257. |
| ONDS | $7.035 | $8C Dec18 | 0.62 / 0.63 | $0.505 | Fails R6 at the bid. |
| QUBT | $7.50 (-1.6%) | $8C Nov20 | 0.50 / 0.53 | 7.50 x 1.1388 - 8 = $0.541 | Passes at the ask (98% of cap). |
| WRD | $4.625 (-6.8%) | $5C Jan15 | 0.45 / 0.55 | 4.625 x 1.1397 - 5 = $0.271 | **R6 FAIL**, worse than at the open. Needs the stock back near $4.83 even at the bid. |
| BRSL | $9.965 | $11C Nov20 | 0.00 / 0.30 | 9.965 x 1.1101 - 11 = $0.062 | Fails. |
| FUBO | $9.405 (+1.7%) | $10C Nov20 | 0.81 / 1.01 | n/a | **R5 FAIL**: bid alone is over the line. |
| TDUP | $2.265 | $2.5C Nov20 | 0.15 / 0.25 | 2.265 x 1.285 - 2.5 = $0.411 | Passes at the ask. Floor-blocked (OI 17). |
| SERV | $4.59 | $5C Nov20 | 0.28 / 0.33 | ~$0.28 | Fails at mid and ask. Floor dies after Fri Oct 9. |
| TME | $7.89 | $8C Nov20 | 0.40 / 0.50 | n/a | Floor dies Sun Oct 11. |

Queue ratings (`get_equity_analyst_ratings`, ~10:37am): unchanged on all 19 (COUR 8/4/0 low $6, ONDS 11/0/0 low $13, QUBT 5/2/0 low $10, WRD 13/0/0 low $10.51, BRSL 7/3/0 low $11.90, TME 22/14/0 low $9.05). MLCO now shows a $5.30 low (updated Sep 17).

## 2. The Oct 7 slice, $19.5-25 names (9 names, queue item 15)

Free screen first (ratings + `get_earnings_results`), then the nearest-OTM strike at the first expiry after the print, then R6 from daily closes over the last 5 prints (PM print: print-day close to next close; AM print: prior close to print-day close).

| Name | Stock | B/H/S, low target | Print (tool) | Contract checked, bid / ask | Median print move, R6 cap | Verdict |
|---|---|---|---|---|---|---|
| BXSL | $23.74 | 5/5/1, low $22 | Nov 9 AM | (none) | | **KILLED R4 proxy**: low target $22 is under the stock. |
| SARO | $20.07 | 12/4/0, low $25 | Nov 9 PM | $22.5C Nov20 0.40 / 0.60, OI 1,339 | 3.42% (-4.0, -1.0, +3.5, -3.4, -2.7), cap 5.13% | **KILLED R6**: mid BE $23.00 needs +14.6%. |
| CAE | $23.20 | 10/5/1, low $25.10 | Nov 10 PM | $25C Nov20 0.20 / 0.95, OI 3 | 4.88% (-5.6, 0.0, -3.7, -14.0, -4.9), cap 7.32% | **KILLED R6 + liquidity**: mid BE $25.575 needs +10.2%. |
| ZTO | $19.81 | 11/4/0, low $21.62 | Nov 18 PM | Dec18 $21C 0.35 / 1.10 OI 1, $22C no bid / 0.90 | 1.40% (-1.1, -0.1, +7.5, -1.4, -7.0), cap 2.10% | **KILLED R6 + liquidity**. |
| LINC | $22.86 | 6/0/0, low $40 | Nov 9 AM | $25C Nov20 1.10 / 1.35; $30C 0.20 / 0.40 (no $27.5) | 12.81% (-15.1, +12.8, +10.2, +10.6, -24.9), cap 19.21% | **KILLED R5 + R6 (strike grid)**: $25C bid over the line; $30C BE $30.30 needs +32.5%. |
| FLY | $21.00 | 7/3/0, low $25 | Nov 11 PM | $22C 2.20/2.40, $24C 1.55/1.75, $28C 0.70/0.95, $30C 0.60/0.85 | not pulled | **KILLED R5**: nothing asks under $0.741 below $30, where BE is +46.9%. Only 4 real prints since the 2025 IPO. |
| MLYS | $21.72 | 8/1/0, low $30 | Nov 9 PM | $22.5C 1.45/2.20, $25C 0.60/1.40, $30C 0.20/0.75 | not pulled | **KILLED R5 + R6**: $30C ask $0.75 over the line; mid BE $30.48 needs +40%. |
| QURE | $22.60 | 11/2/0, low $28 | Nov 9 AM | $23C 2.60/3.30, $25C 2.00/2.55, $30C 0.90/1.40, $35C 0.25/0.75 | not pulled | **KILLED R5 + R6**: first strike under the line is $35C, BE +57%. |
| UTI | $19.89 | 6/1/0, low $25 | Nov 18 PM | Nov20 $22.5C 0.75 / 0.95, OI 56; Dec18 $22.5C 1.15/1.40, $25C 0.55/0.80 | 18.82% (-18.8, -20.4, -11.2, -4.0, -34.2), cap 28.23% | **WATCH, not killed.** Nov20 $22.5C (id 92100d2d-c87f-46d6-ac3f-232498325d25): mid BE $23.35 needs +17.4%, inside R6, under the $25 low; fails R5 only because the bid is $0.75. Dec18 $25C dies on R4 (BE $25.675 > $25 low) and R6 (+29.1% vs 28.23%). Two flags for any doc: Nov20 expires 2 days after an unverified Nov 18 date, and **all five of the last prints fell**. |

**Result:** 9 worked, 8 killed, 1 parked as a watch (UTI). FUBO requote: R5 fail at $1.01.

## GLOSSARY

- **R1 / Rule 1:** stock in the bottom 20-25% of its 52-week range.
- **R2 / Rule 2:** confirmed earnings date before the option expires. `verified: false` = the date is estimated, not company-announced.
- **R3 / Rule 3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds. Written as Buy/Hold/Sell counts (e.g. 10/5/1).
- **R4 proxy:** lowest analyst price target above the current stock price (and, for a specific contract, above its breakeven). The full Rule 4 also needs the target dated within 60 days.
- **R5 / Rule 5:** one contract's ask must fit the conviction tier's budget; at this reserve that's $0.741 per share for 3.5/5.
- **R6 / Rule 6:** the move to breakeven must be no more than 1.5x the stock's median earnings-day move.
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike; near zero means no real market.
- **Max price (doc formula):** the highest ask at which a doc's contract still passes R6 at the current stock price.
- **Strike grid:** the listed strikes jump too far apart for any one of them to fit both R5 and R6.
