# Screening log: Tue Oct 20, EVENING 1 (6:00pm ET)

**Session job:** move up to 25 names through the funnel. Market closed; every quote below is the 4:00pm close (option quotes stamped 19:59-20:00 UTC). Reserve (spendable) $676.28: Rule 5 3.5/5 line **$0.676**, so anything over that is paper only. 2 web searches.

**What ran:** (1) the three parked names from WRAP (BX, INSM, FLUT); (2) a fresh scan, market cap >= $300M, `FILTER_TYPE_EARNINGS_DATE` 20261022-20261223, total call volume > 200, 52w range pct < 0.25: **398 rows** (split at $25: 200 + ~163 unique). Diffed against every ticker in week-08/week-09 logs, passes.md and paper_book.md: only **3 never screened** (BANC, EBS, FPI). (3) Free Rule 3 + R4-proxy pass on the 200 under-$25 names (3 ratings calls). (4) Chain checks on 17 cheap names whose earlier kills were price-sensitive (R5/R6/R7), at the first expiry that passes R2.

## Part 1: the three parked names

| Ticker | Contract | Check | Result | Verdict |
|---|---|---|---|---|
| BX | Nov20 $110C (`08ff8a64`) | Search: who owns the tool's $116 low (15/11/1, stamp Oct 13) | **Barclays raised to $116 from $110, Equal Weight** (Hold, not a Buy). Morgan Stanley Overweight also shows a raise to $116, undated in the results. So the lowest *Buy* is MS $116 or higher, and neither $116 has a date | **KILL R4 (Tab 6 dating)** + R6 already failing by 0.02pt at the close (+4.67% vs 4.65%). Print Thu Oct 22 AM leaves one session. Off the queue |
| INSM | Nov20 $100C (`a002982d`) | Search: "Insmed price target 165" | $165 is **Mizuho, Aug 13 2025** (raised from $130), and Mizuho has since gone to **$196**. The $165 low is a 2025 line on a stock now at $95.69 | **KILL R4 (Tab 6: stale, pre-decline floor)**. Closing spread 50.5% also fails R7 |
| FLUT | Dec18 calls | Chain (Q3 Nov 11 PM f, LY Nov 12) | $70C 12.10 / 14.30 BE **$84.30** (OI 9); $75C 8.30 / 10.70 BE $85.70 (OI 25); $80C 6.30 / 9.10 BE $89.10 (OI 361); $85C BE $92.10 (OI 193). Low $84 (stamp Oct 16) | **KILL R4**: every strike's BE is over $84; the only R7-sized OI ($80C) is $5 over |

## Part 2: new names from the scan

| Ticker | Last | R1 | R3 | Verdict |
|---|---|---|---|---|
| BANC | $17.36 | 0.215 | 9/3/0, low $19 | Q3 Oct 27. Nov20 $17.5C 0.55 / 0.95, **OI 39**: **KILL R7** |
| EBS | $6.29 | 0.199 | no coverage | **KILL R3** |
| FPI | $9.98 | 0.191 | no coverage | **KILL R3** |

## Part 3: R3 / R4-proxy pass on the under-$25 band (free)

200 names, 3 ratings calls. **~95 pass Rule 3** (<= 1 Sell, >= 3 Buys, Buys >= Holds). Of those, ~70 have a tool low at least 15% over the price. Nearly all were already worked in week-09; the ones whose earlier deaths were price-dependent (R5/R6/R7 move with the stock) went to Part 4. Left alone tonight: CIFR, UEC, PL, NRG-type stale-floor kills (dating doesn't change with price), ARDX (dead by standing order), ONDS/BTBT/CLSK (watch line, levels known).

## Part 4: chain checks (closing quotes)

R2 for every November print (Nov 3-13): Dec18 passes (expiry >21 days after the later of tool and LY dates; 10-Q deadline Nov 9 / 16 well before). Oct 23-28 prints use Nov20.

| Ticker | Stock | Print (tool) | Contract | Bid / Ask | OI | Spread | BE / needs | Verdict |
|---|---|---|---|---|---|---|---|---|
| **QUBT** | $6.57 | Nov 13 PM (f), LY Nov 14 PM | **Dec18 $7C** `d92fe604-2aca-4cb3-a0b8-4779b06b511d` | **0.47 / 0.52** | **1,091** | 10.1% | $7.52 / **+14.46%** | R1 0.038, R3 5/2/0, R5 pass (0.52 <= 0.676), R7 pass. **R6: six-print median 9.25%, cap 13.875%: fails by 0.58pt.** Passes when ask <= stock x 1.13875 - 7.00 (at $6.57: <= **$0.48**). R4: low $10 vs BE $7.52, room $2.48, but the doc's dated floor (Ascendiant) ages out Oct 25. **PARKED, real-money near-miss** |
| ACHR | $4.03 | Nov 5 PM (f) | Dec18 $5C | 0.19 / 0.25 | 377 | 27.3% | $5.25 / +30.3% | **KILL R6**: six prints +22.9 / +7.4 / -7.9 / -10.6 / -2.3 / +8.5, median 8.2%, cap 12.3% |
| UUUU | $8.21 | Nov 4 | Dec18 $9C | 0.66 / 0.78 | 1,208 | 16.7% | $9.78 / +19.1% | R5 fails real money (0.78). R6 stays dead per the Oct 8 E2 kill (reaction history small for the vol). **KILL R5/R6** |
| USAS | $3.65 | Nov 10 | Dec18 $4C | 0.20 / 0.40 | 483 | 66.7% | $4.40 / +20.5% | **KILL R7** (closing spread) |
| VNET | $4.10 | Nov 20 | Dec18 $5C | 0.10 / 0.40 | 9,151 | 120% | $5.40 / +31.7% | **KILL R6**: median 6.65% / cap 9.98% (Oct 8 log) |
| RITM | $8.65 | Oct 23 | Nov20 $9C | 0.10 / 0.20 | 2,216 | 66.7% | $9.20 / +6.4% | **KILL R6** (prints move 1-4%, Oct 8 log) + R7 spread |
| RCAT | $4.51 | Nov 13 | Dec18 $5C | 0.25 / 0.52 | 107 | 70% | $5.52 / +22.4% | **KILL R7** |
| AMPX | $7.70 | Nov 6 | Dec18 $8C | 0.80 / 0.90 | **0** | 11.8% | $8.90 / +15.6% | **KILL R7** (OI 0) |
| CRMD | $7.65 | Nov 12 | Dec18 $8C | 0.20 / 1.10 | 36 | 138% | | **KILL R7** |
| FUBO | $8.28 | Nov 13 | Dec18 $9C | 0.59 / 1.08 | **0** | 58.7% | | **KILL R7** |
| NUVB | $4.86 | Nov 3 | Dec18 $5C | 0.30 / 0.70 | 124 | 80% | | **KILL R7** |
| SOUN | $4.71 | Nov 6 | Dec18 $5C | 0.42 / 0.51 | 162 | 19.4% | $5.51 / +17.0% | **KILL R7** (OI 162) |
| ZURA | $3.98 | Nov 13 | Dec18 $5C | 0.90 / 2.00 | 1,206 | 75.9% | | **KILL R7** (IV 277%, no real market) |
| SOC | $3.16 | Nov 13 | Dec18 $4C | 0.17 / 0.26 | 91 | 41.9% | | **KILL R7** |
| WVE | $3.39 | Nov 10 | Dec18 $4C | 0.20 / 0.85 | 149 | 124% | | **KILL R7** |
| OCUL | $6.61 | Nov 4 | Dec18 $7C | 0.40 / 0.80 | 207 | 66.7% | | **KILL R7** |
| BANC | (Part 2) | | | | | | | |

No Dec18 contract at the strike tried (strike grid is different; next run pulls the full Dec18 list): **PONY** ($6), **IE** ($9), **FUN** ($8), **STUB** ($6), **ALMS** ($7.5).

## QUBT R6 base (six prints, close on print day -> next close, all PM)

| Print | Close | Next close | Move |
|---|---|---|---|
| May 15 2025 | $9.24 | $12.87 | +39.3% |
| Aug 14 2025 | $15.38 | $15.32 | -0.4% |
| Nov 14 2025 | $10.60 | $11.50 | +8.5% |
| Mar 2 2026 | $8.59 | $7.73 | -10.0% |
| May 11 2026 | $10.18 | $11.78 | +15.7% |
| Aug 10 2026 | $8.93 | $8.95 | +0.2% |

Median absolute **9.25%** (same as the four-print base in `research_QUBT.md`), cap **13.875%**.

## Moved this run

**22 names moved at least one stage** (plus the 200-name free ratings pass). **20 killed:** BX (R4 dating), INSM (R4 stale), FLUT (R4), BANC (R7), EBS, FPI (R3), ACHR, VNET, RITM (R6), UUUU (R5/R6), USAS, RCAT, AMPX, CRMD, FUBO, NUVB, SOUN, ZURA, SOC, WVE, OCUL (R7). **Parked:** QUBT Dec18 $7C (R6 by 0.58pt, R4 dating). Unchanged: APH (closing ask $4.30 vs $4.18 line, no new quote after hours), TTWO (low $270 still stamped Aug 7).

## GLOSSARY

- **R1-R7:** the Iron Rules in binder Tab 1. R1 range position, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest Buy target above breakeven), R5 price cap, R6 reachability (needed move vs 1.5x median print move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Range pct / percentile:** where the price sits between the 52-week low (0) and high (1). Calls need under 0.25.
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts currently open on that strike. Under 250 fails R7.
- **Spread % of mid:** (ask - bid) / ((ask + bid) / 2).
- **Tab 6 dating:** a Rule 4 floor counts only if it's dated within 60 days and was set after the stock's decline.
- **(f) / (v):** earnings date from the tool, `verified: false` (estimated) or `true` (company-announced).
- **LY:** last year's same-quarter report date.
- **Equal Weight / Overweight:** a broker's Hold / Buy rating.
- **Paper:** the paper book, which applies every rule except R5 and moves no money.
