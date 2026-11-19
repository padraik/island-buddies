# Screening log, Wed Nov 18 EVENING 3 (10:00pm ET)

*Session 3 of 3: refill the queue and leave PREMARKET Thursday's plan. Bands A-D were fully staged by EVENING 2, so this session (a) chain-checked the sub-$1 trio, the only staged names that could ever be real-money size, and (b) re-ran band A's scan `01ce0035` and band E's `7c6e42a7` for rows that weren't there on Nov 13/14. Nothing held. Spendable $715.96, so the 3.5/5 R5 line is $0.716/share. Prices: Wednesday Nov 18 regular close; option books are the 20:59 UTC closing quotes. 0 web searches.*

## (a) Sub-$1 trio: chain stage, all three KILLED on R7

Lowest strikes on the listed expiry each name was staged to. Closing book, Nov 18.

| Ticker | Close | Expiry | Strike | Bid / Ask | Mid | Spread % of mid | OI | BE at ask (move) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| OCGN | 0.7392 | Apr16 | $0.5C | 0.20 / 0.45 | 0.325 | 77% | 455 | 0.95 (+29%) | R7 fail (spread) |
| OCGN | | Apr16 | $1C | 0.10 / 0.20 | 0.15 | 67% | 737 | 1.20 (+62%) | R7 fail (spread) |
| ALLO | 0.6959 | May21 | $0.5C | 0.25 / 0.65 | 0.45 | 89% | 71 | 1.15 (+65%) | R7 fail (spread + OI) |
| ALLO | | May21 | $1C | 0.10 / 0.55 | 0.325 | 138% | 230 | 1.55 (+123%) | R7 fail (spread + OI) |
| ZURA | 0.9651 | Jun17 | $0.5C | 0.00 / 4.90 | n/a | no bid | 0 | n/a | R7 fail (no market) |
| ZURA | | Jun17 | $1C | 0.30 / 0.90 | 0.60 | 100% | 306 | 1.90 (+97%) | R7 fail (spread) |

**OCGN, ALLO, ZURA: KILLED, Rule 7** (no strike within reach shows a spread at or under 25% of mid). R6 was not run to a print table: every BE above is +29% to +123% on a stock whose prints are EPS-noise biotech quarters, and R7 kills first. Dates re-pulled for the record: OCGN Q4 Wed Mar 3 AM (f), LY Mar 4; ALLO Thu Mar 11 PM (f), LY Mar 12; ZURA Thu Mar 18 AM (f), LY Mar 19.

The lesson worth keeping: "cheap enough for the real fund" and "liquid enough for Rule 7" don't overlap anywhere in the sub-$1 pool. A $0.70 stock's calls trade in nickels, so a one-tick spread is already 30%+ of a $0.15 contract.

## (b) Band A / band E re-run

| Band | Scan ID | Rows Nov 13/14 | Rows tonight |
|---|---|---|---|
| A ($1-8.19) | `01ce0035-28a6-49c0-aed8-0ee1b83da395` | 124 | **158** |
| E ($0-1) | `7c6e42a7-d92a-422c-b529-276466c1e14b` | 2 | **3** (GERN, SID, IQ) |

Diffed every row against all week-08 / week-09 logs and passes.md. **11 never-worked names in band A.** Band E's three are all known R3 kills; re-confirmed: GERN (no coverage), SID 0/7/3, IQ 7/9/2 (Buys < Holds).

| Ticker | Last | R1 | B/H/S | Low vs Last | Q4 (tool) | LY | Later | Listed expiries (2027) | Pick | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| OIS | 7.825 | 0.230 | none | | | | | | | **KILLED R3** (no coverage) |
| BCRX | 7.43 | 0.240 | 8/2/0 | $11 (48%) | Thu Feb 25 AM (f) | Feb 26 | Feb 26 | Jan15, Mar19, Apr16, Jun17 | **Mar19** (0d), Apr16 fallback | STAGED. Mar19 $9C 0.40 / 0.90, OI 181; $7C 0.20 / 2.00, OI 14. Spring books not formed yet |
| ABX | 7.14 | 0.229 | 7/1/0 | $10 (40%) | Thu Mar 11 PM (f) | Mar 12 | Mar 12 | Feb19, May21 | **May21** | STAGED |
| EPRX | 6.21 | 0.157 | 13/0/0 | $12.13 (95%) | Thu Mar 11 PM (f) | Mar 12 | | none | | **KILLED** (no listed options) |
| TGB | 5.555 | 0.250 | 8/1/0 | $8.21 (48%) | Wed Feb 17 PM (f) | Feb 18 | Feb 18 | Feb19, May21 | **May21** (no Mar listed) | STAGED. Foreign filer (40-F): both dates required, both present. R1 exactly on the edge |
| CADL | 5.318 | 0.100 | 10/0/0 | $11 (107%) | Thu Mar 11 AM (f) | Mar 12 | Mar 12 | Apr16 | **Apr16** | STAGED |
| ALOY | 4.54 | -0.042 | none | | | | | | | **KILLED R3** (no coverage) |
| AVAL | 3.65 | 0.105 | none | | | | | | | **KILLED R3** (no coverage) |
| CCCC | 2.460 | 0.221 | 9/0/0 | $6 (144%) | Thu Feb 25 AM (f) | Feb 26 | Feb 26 | Apr16 (no Mar) | **Apr16** | STAGED. Apr16 $3C 0.10 / 0.95 (OI 35); $4C no bid / 0.75 (OI 4,971). Cheapest real-size candidate in the staged pool once the book forms |
| CERS | 1.94 | 0.235 | none | | | | | | | **KILLED R3** (no coverage) |
| IAUX | 1.139 | 0.146 | 7/0/0 | $2.80 (146%) | Thu Mar 11 PM (f) | Feb 19 | Mar 11 | none | | **KILLED** (no listed options) |

None of the five stagers carries a ratings `updated_at` stamp, so the Tab 6 dated-floor gate is unverified for all of them; that's the doc-stage check.

## Totals

17 names moved: 3 chain-checked and killed (R7), 11 never-worked (5 staged, 4 killed R3, 2 killed no options), 3 known band E kills re-confirmed. 0 advanced past the chain, 0 buyable, 0 searches.

## Watch (closing / after-hours, Nov 18)

- NIO $2.77 (AH $2.82), 16/7/1, low $3.7026, `updated_at` still 2026-11-18 00:55Z: gate shut.
- AVGO $354.05 (AH $356.00), above the $338.85-341.08 window; stamp Oct 27.
- Paper GOOGL $282.44 (AH $284.73), under $300; 63/8/0, low $300 (stamp Nov 7) vs BE $285.95.
- BABA (paper, closed at LASTCALL) $84.37, AH $82.38 (-2.4%); FQ2 prints Thu AM.

## GLOSSARY

- **R1 (range percentile):** where the price sits in its 52-week range, 0 = at the low, 1 = at the high. Calls need under 0.25.
- **R3 (ratings):** 3+ Buys, Buys at least equal to Holds, 0-1 Sells. No coverage = killed.
- **R4 proxy:** the lowest analyst target must sit above the price (and, at entry, above breakeven).
- **R5 line:** the most one contract may cost: tier % x spendable cash / 100. At 3.5/5 on $715.96 that's $0.716/share.
- **R6 (reachability):** the move to breakeven must be no more than 1.5x the stock's median earnings-day move.
- **R7 (liquidity floor):** the exact contract needs open interest of 250+ and a bid/ask spread no wider than 25% of the mid.
- **Later of tool / LY:** the earnings date used for the 21-day cushion is the later of the tool's estimate and last year's same-quarter date.
- **(f):** the tool's date is `verified: false`, an estimate from cadence.
- **Staged / parked:** passed the free screens; waits for the December chain pass when spring books have real open interest.
- **Band:** a price slice of the December re-sweep scan (A $1-8.19, B $8.19-25, C $25-100, D $100+, E under $1).
- **Floor gate (Tab 6):** the lowest Buy target needs a dated source before a doc can lean on it.
