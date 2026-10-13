# SCREENING LOG: Tue Oct 13, 2026, MIDDAY (11:35am ET, VM)

**Session job:** queue re-tests (BTBT, ONDS, ALGM), IPX through R2 / R7, then the **Dec 12 - Jan 31 print window, $25+ band** (the last unscanned band of that window). Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676, so every $25+ name is a paper candidate only. 0 web searches.

## Queue re-tests (live, ~11:35)

| Name | Contract | Quote | Stock | R6 | Result |
|---|---|---|---|---|---|
| BTBT | Jan15 $1C `25ebc8de` | 0.34 / 0.37, OI 2,252 | $1.23 (-0.8%) | BE $1.37 vs max $1.331 (x1.0823): needs +11.4% vs 8.23% | **PARK, R6** |
| ONDS | Dec18 $8C `cfbc25b7` | 0.43 / 0.45, OI 37,782 | $6.634 (-0.5%) | BE $8.45 vs max $8.020 (x1.2089): needs +27.4% vs 20.89% | **PARK, R6** |
| ALGM | Nov20 $35C `832a1519` | 2.05 / 2.15, OI 6,793 | $32.41 (-4.1%) | BE $37.15 vs max $35.81 (x1.105): needs +14.6% vs 10.5% | **PARK, R6** (further away; stock down 4% today) |

## IPX (IperionX), carried from 10:35

| Check | Result |
|---|---|
| Price | $14.69 (-6.0% today), range pct < 0 |
| Ratings | 6/0/0, low $26.00 |
| `get_earnings_results` | **empty** (no dates, no history) |
| `get_sec_filing_index` since 2025-06 | **empty** |
| Chain | expiries Oct16, Nov20, Jan15, Apr16 |
| Jan15 $15C | 1.90 / 3.30, **OI 3**, spread 54% of mid |
| Jan15 $17.5C | 0.95 / 2.20, **OI 2**, spread 79% |
| Apr16 $15C | 2.05 / 4.70, **OI 0**, spread 78% |
| Apr16 $17.5C | 1.10 / 3.40, **OI 1**, spread 102% |

**KILLED, R7** (OI 0-3, spreads 54-102% of mid). R2 also unprovable from the tools (no tool date, no LY date, no filings in the index).

## Scanner: prints Dec 12 - Jan 31, market cap >= $300M, last > $25, range pct < 0.25

Preview (not saved): **13 rows**, 11 companies (LEN.B and MKC.V are share classes of LEN and MKC).

| Name | Price | Range pct | Ratings B/H/S, low | Next fact | Result |
|---|---|---|---|---|---|
| HEI.A | 218.93 | 0.244 | 15/12/0, low $320 | HEI Q4 (FY Oct 31): Dec 17 PM (f) / LY Dec 18 PM; 10-K due ~Dec 30; **Jan15** passes R2 (29 days) | **ADVANCE** (paper): chain OI on HEI.A Jan15, else HEI |
| RPM | 97.69 | 0.165 | 18/2/0, low $107 | Jan 7 AM (f) / LY Jan 8 AM; 10-Q (Nov 30 qtr) due ~Jan 9; **Feb19** passes R2 | **ADVANCE** (paper): Feb19 chain, print moves |
| LEN / LEN.B | 74.59 | 0.014 | 3/10/11 | | **KILLED, R3** |
| CALM | 62.25 | 0.011 | no coverage | | **KILLED, R3** |
| FUL | 49.97 | 0.149 | 8/0/0, low $62 | Jan 13 PM (f) / LY Jan 14 PM; **Feb19** passes R2 | **ADVANCE** (paper): Feb19 chain OI first (expect R7) |
| MKC / MKC.V | 44.58 | 0.045 | 8/8/1, low $47 (stamp Oct 5) | Jan 21 AM (f) / LY Jan 22 AM; 10-K (FY Nov 30) due ~Jan 29; **Feb19** passes R2 (28 days) | **ADVANCE** (paper): Feb19 chain; R4 tight (BE must stay under $47, +5.4%) |
| KBH | 41.76 | <0 | 3/10/6 | | **KILLED, R3** |
| NKE | 35.49 | 0.092 | 11/25/7 | | **KILLED, R3** |
| SHAZ | 34.46 | 0.221 | 8/0/0, low $80 | tool says Q3 **Nov 15 PM (f)** (scanner said Dec 31); only 2 reported prints ever (May 15, Aug 6) | **KILLED, R6** (needs 4-8 prints to verify; has 2) |
| BIRK | 34.36 | 0.213 | 20/5/0, low $33.78 (stamp Aug 20) | low is under the stock, and stale | **KILLED, R4** (proxy) |
| GIS | 31.95 | 0.042 | 4/15/4 | | **KILLED, R3** |

**Moved:** 15 (3 re-tests + IPX + 11 new companies; the ratings call was one free 11-symbol call, so the batch ran past 10). 8 kills (5 R3, 1 R4 proxy, 1 R6, IPX R7), 3 parked on R6, 4 advanced to the chain stage (HEI.A, RPM, FUL, MKC). 0 entries.

**Pattern:** the $25+ band of this window is consumer staples and housing (LEN, KBH, GIS, MKC, CALM, NKE): mostly Hold-heavy or Sell-heavy, which is why Rule 3 took five of eleven. The survivors are quality industrials (HEI, RPM, FUL) and McCormick. Expect R7 to be the next wall on FUL and HEI.A.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry (21-day cushion on the later of tool date and last year's date; 10-Q/10-K deadline at least 5 trading days before expiry; 6-K filers need both dates), R3 analyst consensus (calls: at most 1 Sell, at least 3 Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability (ask x 100 <= 10% of reserve at 3.5/5, $67.63 today), R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid (at the ask).
- **(f):** the tool's date is `verified: false`, estimated from cadence.
- **LY:** last year's same-quarter report date.
- **R4 proxy:** a screening kill when the lowest Buy target is at or below the stock, so no normal call's breakeven can sit under it.
- **PARK:** alive, waiting on one specific price; stays on the queue.
- **ADVANCE:** cleared R1-R3 and the R2 date test; next stop is the live chain (R5-R7).
- **OI:** open interest.
- **Share class:** HEI.A / LEN.B / MKC.V are second share classes of the same company; options and ratings usually sit on the main ticker.
