# SCREENING LOG — Wed Oct 7, 2026, 2:35pm ET (VM MIDDAY run)

**Source:** research_queue.md plan written by the 1:35 run: date checks on COUR / QUBT / ONDS, then a fresh $2-10 scan instead of finishing the $19.5-23 slice by hand. Scan (preview, not saved): market cap $300M+, earnings Oct 20 - Nov 20, stock, price $2-10, 52-week range percentile < 0.25 (same expression filter as the Oct 5 sweep). 248 matches: 200 returned for $3.11-$9.97, then a second pass for $2-$3.11 (49). Deduped against every ticker in this week's research files, research_queue.md and passes.md: **17 new names**. Almost all of the band was already worked by EVENING 1/3 and the slice runs.

| Step | Names | Tool |
|---|---|---|
| Dates | COUR, QUBT, ONDS + 8 new names | get_earnings_results |
| Ratings (free R3 screen) | 17 new names | get_equity_analyst_ratings (2 calls) |
| Requotes | COUR, QUBT, ONDS | get_option_quotes, get_equity_quotes |
| Chains | GTN, LXEO, BBOT, GNL, NXE, CATX, HLLY, TDUP (Nov20 calls) | get_option_chains, get_option_instruments, get_option_quotes |
| R6 history | GTN, NXE, TDUP, HLLY, GNL (6 prints each, daily closes) | get_equity_historicals |
| Web | TDUP (why it halved, floor date): 1 search | WebSearch |
| Moved this run | **8** names through the chain stage (plus 9 killed free at R3) | |
| Killed | **16** (9 free, 7 at the chain stage) | |
| Advanced | **TDUP** (floor-dating stage) | |

## Dates (queue)

| Ticker | Date (tool) | Verified | Note |
|---|---|---|---|
| COUR | Oct 22 PM | false | Unchanged. |
| QUBT | Nov 13 PM | false | Unchanged. |
| ONDS | Nov 12 AM | false | Unchanged. |

## Requotes (2:35pm ET)

| Ticker | Stock | Contract | Bid / Ask | R5 / R6 at the ask |
|---|---|---|---|---|
| COUR | $5.10 | $5C Nov20 | 0.40 / 0.70, OI 3,137 | Passes R5. Date gate only. |
| QUBT | $7.569 | $8C Nov20 | 0.53 / 0.55, OI 769 | Max price = 7.569 x 1.1388 - 8.00 = $0.620. Passes at the ask (BE $8.55, +13.0% vs 13.88%). Date gate only. |
| ONDS | $7.165 | $8C Nov20 | 0.45 / 0.47, OI 10,604 | Max price = 7.165 x 1.2089 - 8.00 = $0.662. Passes (BE $8.47, +18.2% vs 20.89%). Date gate only. |

## Free R3 screen: 17 new names

| Ticker | Direction | Stock | Ratings B/H/S, low | Verdict |
|---|---|---|---|---|
| HRZN | CALLS | $4.50 | 2/4/0, $4.50 | **KILL, R3** (2 Buys, Holds > Buys). |
| SION | CALLS | $4.84 | 1/10/0 | **KILL, R3.** |
| TDOC | CALLS | $5.62 | 5/18/0 | **KILL, R3** (Holds > Buys). |
| RCKT | CALLS | $2.565 | 7/5/2 | **KILL, R3** (2 Sells). |
| PSFE | CALLS | $5.75 | no coverage | **KILL, R3.** |
| VISN | CALLS | $6.08 | no coverage | **KILL, R3.** |
| GSBD | CALLS | $8.81 | no coverage | **KILL, R3.** |
| XFOR | CALLS | $2.815 | no coverage | **KILL, R3.** |
| GOGO | CALLS | $2.19 | no coverage | **KILL, R3.** |
| LXEO, BBOT, GTN, GNL, NXE, CATX, HLLY, TDUP | CALLS | | | Pass R3, to chains (below). |

## Chain stage: 8 names

| Ticker | Stock | Print (tool) | Ratings B/H/S, low | Chain (Nov20) | R6 (6 prints) | Verdict |
|---|---|---|---|---|---|---|
| GTN | $4.67 | **Nov 6 AM, verified true** | 4/1/1, $3 | $5C 0.20 / 0.30, OI 1,087 (BE $5.30, +13.5%); $7.5C 0 / 0.10 | +16.9, -0.2, +4.8, +23.8, -20.1, +25.5: median 18.50%, cap 27.75% | **KILL, R1.** The scan matched GTN.A (Class A, 0.010), but the options trade on GTN common: 52w $3.55-$6.44, R1 = 0.38 at $4.67. MID-OUT. The only verified date of the week, on the wrong share class. |
| NXE | $8.915 | Nov 4 PM, unverified | 20/0/0, $11.01 | $9C 0.60 / 0.70 (BE $9.70, +8.8%); $10C 0.30 / 0.35 (BE $10.35, +16.1%) | -0.2, -1.8, -7.1, +3.3, +6.3, +2.9: median 3.10%, cap 4.65% | **KILL, R6**: nearest strike needs 1.9x the cap. |
| GNL | $8.105 | Nov 4 PM, unverified | 6/2/1, $9 | $10C 0 / 0.05, OI 0 (BE $10.05, +24%); $2.50 grid | +4.2, +9.1, +5.2, -3.1, -1.3, +5.2: median 4.70%, cap 7.05% | **KILL, R6 + strike grid.** |
| HLLY | $2.315 | Nov 6 AM, unverified | 6/2/0, $3.50 | $2.5C 0.10 / 0.75, OI 86 | -14.5, +31.4, +32.6, -12.4, -13.0, +7.4: median 13.75%, cap 20.62% | **KILL, R5 + R6**: ask over $0.741; at mid (0.425) BE $2.925 needs +26.3% vs 20.62%. |
| LXEO | $3.375 | Nov 4 AM, unverified | 9/0/0, $9 | $4C no bid / 4.50, $5C no bid / 0.45 | not pulled | **KILL, liquidity**: no bid on the OTM strikes. |
| CATX | $2.46 | Nov 5 PM, unverified | 14/1/0, $5 | $2.5C 0.05 / 0.70, OI 2; $5C no bid | not pulled | **KILL, liquidity**: OI 2 and a 0.05 / 0.70 market. |
| BBOT | $3.485 | Nov 11 PM, unverified | 10/0/0, $15 | no listed options | n/a | **KILL, no options.** |
| **TDUP** | $2.215 | Nov 2 PM, unverified | 6/1/0, $5.70 | **$2.5C 0.15 / 0.25**, OI 17 (BE $2.75, +24.2% at the ask; mid 0.20, BE $2.70, +21.9%) | +47.7, +5.7, -7.5, -23.4, +14.6, -50.5: median 19.00%, cap 28.50% | **ADVANCE: passes R1 (0.02), R3, R5, R6 at the ask (85% of cap).** Floor-blocked: see below. |

## TDUP notes

- Aug 5 PM print: Q2 revenue +17% to $90.8M, active buyers +21% to 1.77M, loss of $0.05 vs estimate -$0.03, Q3 guide $87-89M and FY $344.4-348.4M both under the Street. Stock -50.5% next day (-49.1% per web). The stock had already fallen before the print (MarketBeat, Jul 22: "down 7.1%").
- Floor: Telsey Outperform, target cut $7 -> $6 on Aug 6 (web, MarketBeat). That is post-decline, but **62 days old today** and past the 60-day line (Oct 5). The tool's low is $5.70, so some Buy-side target sits under Telsey's; its date isn't known. Every target is about 2x the BE ($2.75), so the floor clears by a mile if any of them is dated after Aug 8.
- Liquidity: OI 17 on the $2.5C, ten-cent spread. One contract is fine; a fill at mid is not certain.
- R6 history is all over the place (+47.7 / -50.5). The cap is honest, but most of the size comes from two huge moves; the middle four are 5.7-23.4.
- Next: find a dated Buy target since Aug 8 (one web search or `get_equity_analyst_ratings` changes), confirm the Nov 2 date, then the doc.

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R1 (52w):** (price - 52-week low) / (52-week high - 52-week low); calls need <= 0.25. Checked on the share class the options trade on.
- **R2:** a confirmed earnings date before expiry. `verified: false` means the date is estimated from the company's cadence, not announced.
- **R3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4:** lowest Buy target, dated within 60 days, above breakeven. "Floor-blocked" = the target clears, but no Buy target with a date inside 60 days has been found yet.
- **R5:** one contract's ask <= 10% of reserve / 100 at 3.5/5 (today $0.741).
- **R6:** move to breakeven <= 1.5x the median earnings-day move (the "cap"). AM print: prior close to print-day close. PM print: print-day close to next-day close.
- **Strike grid kill:** strikes too far apart (here $2.50) for any one strike to be both affordable and reachable.
- **OI (open interest):** contracts outstanding. Low OI means a thin market and wide spreads.
- **MID-OUT:** range percentile between 0.25 and 0.75; no direction, no play.
- **DOC COMPLETE:** research doc with Iron Rules, Five-Baxter meeting, EXIT PLAN, sizing and GLOSSARY committed; entry waits only on the named gates.
