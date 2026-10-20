# Screening log, Tue Oct 20, MIDDAY (10:35am ET): DONE

*Quotes 10:35-10:37am ET. 1 web search (ALGM $40), 1 EDGAR read (AA 8-K + two 425s; `get_sec_filing` 404'd on both, write-up `aa_425_oct20.md`), Mar19 chains on BAC / PLD / AA, daily bars Oct 2024 - Oct 19 2026 for the R6 print base.*

## Held: COUR $5C Nov20

| Check | Result |
|---|---|
| Quote (10:35) | 0.30 / 0.65 (bid size 3,377, ask size 613, vol 1), mark 0.475, OI 3,235, IV 70.2% |
| Stock | $5.11 (+2.2%), 5.11 / 5.12 |
| Q3 | Thu Oct 29 PM, `verified: true`, `actual: null` (LY Oct 23 PM) |
| Rule 4 | 8/4/0, low **$6.00** vs BE $5.65: holds |
| Filings | none since Oct 15 (index empty) |
| Tab 4 | nothing fires. Bid 0.30 with the stock up 2.2% is still a thin morning book (the mark rose 0.45 -> 0.475); not acted on |

## R6 print base (median absolute one-day reaction, computed from daily closes)

| Name | Prints (oldest -> newest) | Median abs, 7 | Median abs, last 6 | R6 cap (1.5 x last-6) |
|---|---|---|---|---|
| BAC (AM) | +3.6, -0.3, +4.4, -3.8, +1.8, +1.9, -4.8 | 3.60% | 2.83% | 4.25% |
| PLD (AM) | +1.8, +1.4, +6.3, +0.3, +1.7, +4.6, -2.7 | 1.84% | 2.21% | 3.32% |
| AA (PM) | -7.0, +2.9, +12.6, -1.5, -6.8, -6.1, +2.5 | 6.13% | 4.52% | 6.78% |

## Queue: names moved

| # | Name | Contract | Stock (10:35) | Live quote | Ratings (B/H/S, low) | Result |
|---|---|---|---|---|---|---|
| 1 | AA | Mar19 $40C / $45C / $50C | $41.11 (-1.3%) | 5.35 / 5.95 (OI 320); 3.35 / 3.80 (OI 672); 1.95 / 2.43 (OI 1,481) | 14/4/1, $48 | **KILL R6.** 425 read first: Alcoa is the **buyer** (South32's AliGroup, ~$3.1B cash + CVR up to $750M, close 1H27), so no deal cap on calls; Q3 already printed Oct 15, guidance reaffirmed; catalyst would be Q4 ~Jan 21 PM (f). R1 0.133 pass. Best BE is the $40C at $45.95 = **+11.8%** vs 6.78% cap (9.2% even on the 7-print base). |
| 2 | BAC | Mar19 $50C / $52.5C / $55C | $51.03 (+1.3%) | 4.05 / 4.15; 2.69 / 2.91 (OI 2,622); 1.76 / 1.86 | 23/5/0, $55 | **KILL R6.** Q4 Jan 15 AM `verified: true`, R1 0.224. BE at the ask: $54.15 (+6.1%), $55.41 (+8.6%), $56.86 (+11.4%) vs 4.25% cap. |
| 3 | PLD | Mar19 $125C / $130C | $126.13 (+1.6%) | 7.10 / 9.40 (OI 11); 5.30 / 6.60 (OI 188) | 13/5/0, $136 | **KILL R6 (and R7).** R1 0.091. BE $134.40 (+6.6%) / $136.60 (+8.3%) vs 3.32% cap; OI 11 and 188 < 250. |
| 4 | ALGM | Nov20 $32.5C | $33.815 (+1.9%) | 3.70 / 4.00, OI 3,518 | 14/1/0, $40 | **KILL R4 (Tab 6 stale floor).** R6 now passes with room (BE $36.50 = +7.9% vs 10.5%), R7 7.8%. The floor: one search returns only **raises to $40** (UBS 38 -> 40, Mizuho 37 -> 40) and a BofA cut 45 -> 38, all undated, and no cut *to* $40 anywhere. An aggregator had the range low at **$48 on Oct 1, 2026**, so a raise to $40 can't have happened since; the $40 is a stale pre-decline line resurfacing in the tool. Working rule (Oct 19): one search tracing the low to a pre-decline target = kill, don't park. |

**Re-rated free, unchanged (ratings pulled 10:35):** NXT $79.50 (27/4/0, $101 stamp Oct 13; kill Oct 26), RIOT $14.20 (24/1/0, $19 undated; kill Oct 27), NRG $99.44 (16/4/0, $131 stamp Oct 3; kill Nov 2), TTWO $206.74 (29/1/1, $270 stamp Aug 7), PAAS $45.52 (6/2/0, $51; over its R1 line).
**Paper:** LVS $38.31 (ramp sell today 3:35pm, ITM by $0.81). MSTR **$143.96 (+5.8%)**, over the paper $120C's $142.05 BE; WRAP marks it.

## Moved this run

4 names moved, 4 killed (AA R6, BAC R6, PLD R6 + R7, ALGM R4 Tab 6). 0 advanced. Queue 5 live + 3 watch: under 10, EVENING 3 refills (or LASTCALL/WRAP PREPARE).

## GLOSSARY

- **R1-R7:** the Iron Rules in binder Tab 1. R1 range position, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest Buy target above breakeven), R5 price cap, R6 reachability (needed move vs 1.5x median print move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid (here, at the ask).
- **Print base:** the stock's one-day move on its recent earnings reports, used to judge whether a breakeven is reachable.
- **Rule 425 filing:** an SEC filing of communications about a merger or acquisition.
- **CVR (contingent value right):** an extra payment to the seller that depends on future events (here, aluminum and alumina prices).
- **Floor-dating gate (Tab 6):** a bear floor only counts if it was published within 60 days and after the decline.
- **(f):** earnings date not yet verified by the company (`verified: false`).
- **Paper:** tracked in `paper_book.md`, no money moves.
