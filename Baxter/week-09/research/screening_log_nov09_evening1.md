# Screening log, Mon Nov 9, 2026, EVENING 1 (6:00pm ET), VM

*Session 1 of 3. Order of jobs: SWEEP #4 (`take_profit_sweep_nov09.md`, done first, no threshold changes, counter reset to 1 of 5), holdings fact check, POWL paper gate, the slide-in scan on Monday's closes, Monday's passes.md review. Reserve $539.11 (spendable; $166.90 of ACHR/QUBT proceeds settle Tue). 3.5/5 R5 line $0.539, screen line $1.078. Stock prices are the scan's live values at ~6pm (after hours). Option quotes are Monday's 3:59pm closes.*

**Scan (preview, not saved):** cap >= $0.3B, stock, last >= $1, prints **Nov 16 - Dec 22**, range pct (52W) **< 0.30**, call volume >= 100. Same filters as Fri EVENING 3. **75 rows** (Friday: 75). I diffed every row against the week-09 screening logs: **all 75 have been worked since Oct 7, and 0 are new.** The window is fished out for the third night running. So the 25 moves tonight are free re-rates of the stalest rows (last logged Oct 7 - Oct 30) and of the big Monday movers (+10% or more), looking for a verdict that flipped.

## Ratings re-rate (25)

| # | Ticker | Last ~6pm | R1 (scan) | Print (scan) | B/H/S, low | Result |
|---|---|---|---|---|---|---|
| 1 | YMM | 8.94 | 0.264 | Nov 19 | 15/2/0, $9.11 | KILLED R4 proxy (low only 1.9% over the stock; no Dec18 strike's BE fits under it). Was R6 + strike grid Oct 7 |
| 2 | QFIN | 5.59 | 0.026 | Nov 18 | 7/3/2 | KILLED R3 (2 Sells) |
| 3 | MNSO | 10.92 | 0.172 | Nov 17 | 12/4/0, $10.87 | KILLED R4 proxy (low under the stock) |
| 4 | XXI | 5.59 | 0.172 | Nov 30 | no coverage | KILLED R3 |
| 5 | CRML | 6.04 | 0.056 | Nov 16 | no coverage | KILLED R3 |
| 6 | POET | 5.25 | 0.081 | Nov 16 | no coverage | KILLED R3 |
| 7 | VZLA | 3.50 | 0.144 | Dec 11 | no coverage | KILLED R3 |
| 8 | BULL | 4.99 | 0.083 | Nov 20 | no coverage | KILLED R3 |
| 9 | IMSR | 3.01 | 0.048 | Nov 30 (scan, stale) | **5/1/0, $4 (new coverage)** | **KILLED R2:** `get_earnings_results` has Q3 **Tue Nov 10 AM `verified: true`**, tomorrow before the open. The scanner's Nov 30 is stale. Catalyst is a day away and nothing can ramp |
| 10 | ASPI | 2.15 | 0.064 | Nov 20 | no coverage | KILLED R3 |
| 11 | AGX | 305.90 (+10.2%) | 0.096 | Dec 4 | 4/2/1, $273 | stays KILLED R4 proxy (low under the stock) |
| 12 | AVAV | 126.50 (+12.2%) | 0.085 | Dec 9 | 21/4/0, $165 | stays KILLED R7 (Nov 5: Jan15 OI under 250 at every near strike). Not re-quoted, paper-size only |
| 13 | CIEN | 273.35 (+12.3%) | 0.224 | Dec 11 | 19/5/0, $347 | stays as logged Nov 5 (paper-size, R6). Not re-quoted |
| 14 | IESC | 174.86 (+10.4%) | 0.121 | Nov 20 | no coverage | KILLED R3 |
| 15 | **ROAD** | 85.30 (+10.5%) | 0.141 | **Thu Nov 19 AM `verified: true`**; LY Nov 20 | **5/1/0, $90 (new coverage; was R3 Nov 5)** | to chain (below) -> **KILLED R7** |
| 16 | CRDO | 134.50 (+11.6%) | 0.216 | Dec 1 | 21/1/0, $235 | paper doc, floor gate unchanged (no Buy target dated after the slide) |
| 17 | PL | 14.35 (+14.3%) | 0.093 | Dec 10 | 8/5/0, $17 | paper doc, floor gate unchanged (no dated floor since DB $28 aged out Nov 7) |
| 18 | UEC | 7.65 (+10.5%) | 0.108 | Dec 10 | 8/3/0, $10 | stays KILLED R6 (Oct 31: Jan15 $7C needs +9.9% vs 8.12%; stock 7.65 vs 7.715 then) |
| 19 | CLSK | 6.91 (+12.2%) | 0.101 | Nov 25 | 15/1/0, $9.50 | stays KILLED R5 + R6 (Nov 4; stock 6.91 vs 6.805 then, same math) |
| 20 | NNE | 12.49 (+12.4%) | 0.099 | Dec 18 | 8/1/0, $18 | stays KILLED R7 (Jan15 OI under 250, three straight closes). Dec18 fails R2 (prints expiry day) |
| 21 | RCAT | 4.49 (+11.1%) | 0.080 | Mon Nov 16 PM (v) | 7/1/0, $6 | stays KILLED R6 (Nov 3 at 4.46: $5C +14.3% vs 10.29% cap; four of six prints fell) |
| 22 | AMBA | 62.00 | 0.283 | Nov 25 | 7/5/0, $65 | stays KILLED R4 + R7 (Nov 4) |
| 23 | GENB | 14.18 (+8.6%) | 0.273 | Nov 30 | 6/0/0, $22 | stays KILLED R7 (Nov 5: Dec18 OI 3-36; two prints of history) |
| 24 | BLSH | 23.49 (+10.2%) | 0.119 | Nov 18 | 7/8/0 | KILLED R3 (Holds > Buys) |
| 25 | UTI | 21.95 (+10.1%) | 0.118 | Nov 18 | 6/1/0, $25 | stays KILLED R7 (Fri Nov 6) |

## Chain (1)

| Ticker | Contract | Bid / ask (3:59pm close) | OI | BE at ask | vs $90 low | Result |
|---|---|---|---|---|---|---|
| ROAD | Dec18 $80C `cc85b696` | 9.20 / 9.70 | 3 | $89.70 | under by $0.30 | R7 (OI 3), R5 (ask 18x the line) |
| ROAD | Dec18 $85C `0921527c` | 6.30 / 6.70 | 13 | $91.70 | **over** | R4 + R7 |
| ROAD | Dec18 $90C `590667bb` | 4.00 / 4.50 | 14 | $94.50 | over | R4 + R7 |

**ROAD: KILLED R7** (OI 3-14 on every near strike) and R4 above $80. R2 would have passed (Nov 19 AM verified, LY Nov 20, Dec18 is 28 days later; the FY Sep 30 10-K deadline of Nov 29 lands 14 trading days before expiry). Don't bring back this quarter.

## POWL paper entry gate (Mon Nov 9 evening, window Mon Nov 9 - Fri Nov 13)

Close **$141.65** (+6.4%; AH $139.66). Dec18 $130C `5625538d`: closing book **19.70 / 26.00** (mid 22.85), OI 2,291, vol 1. Q4 (FY) **Mon Nov 16 PM `verified: true`**.
1. Buy target dated after Oct 12 and above $150.20: **SHUT.** Tool low $235 (3/3/0), still the undated May-era number. One search turned up a Roth MKM Buy $350 and a raise to $381, both undated. Nothing provably after Oct 12.
2. Close <= ~$151.44 (R1): pass.
3. R3 >= 3 Buys, Buys >= Holds: pass (3/3/0).
4. Ask at least $0.25 under 1.129 x close - 130 = **$29.92**: pass (ask 26.00).
5. Spread <= 22% of mid: **FAIL** (6.30 / 22.85 = **27.6%**; also over Rule 7's 25%). This is a closing-quote width, so re-check on Tuesday evening's close.

**No paper entry tonight** (gates 1 and 5). Window runs through Fri Nov 13's evening session. Paper ramp sell would be Mon Nov 16 3:35pm.

## Holdings fact check

FRMI $2.5C Dec18: stock $1.655 close, AH $1.66. Closing book 0.05 / 0.10 (OI 1,042). Q3 **Thu Nov 12 AM `verified: true`**, `actual: null`. 6/2/0, low $6 vs BE $3.15: Rule 4 holds. SEC index since Nov 5: only the Nov 5 Form 4. EDGAR submissions (CIK 2071778, direct JSON): newest is still the Nov 5 Form 4 / 144. **Facts unchanged.** Ramp sell Wed Nov 11 3:35pm.

## passes.md (Monday review)

ONDS **$5.97** (+11.9% on the day). Neither trigger hit ($4-5, or above $15), so Keep Watching. No other live entries. No new pitches.

## Tally

26 names moved (25 re-rated + the POWL gate). **0 advanced, 0 buyable.** New kills: YMM, MNSO (R4 proxy); QFIN, BLSH, XXI, CRML, POET, VZLA, BULL, ASPI, IESC (R3); IMSR (R2); ROAD (R7). Kept dead on their logged verdicts: AGX, AVAV, CIEN, UEC, CLSK, NNE, RCAT, AMBA, GENB, UTI. Gates unchanged: CRDO, PL, POWL.

**Finding:** the Nov 16 - Dec 22 window has nothing left at real-money size, and Mar19 chains don't have OI until ~Dec 15 (Saturday's finding). Rows that moved +10% today flipped no verdicts. The only flip was ROAD gaining coverage, and its chain is empty. The queue stays at 6, all gated. EVENING 3 should look at a different source: names that just reported and sold off (post-print bottom-quartile names with Jan/Feb prints that pass R2's 10-K test on Mar19 only once OI lists), or a puts-free Tier B re-pull from the Nov 7 sweep for Jan15 names that were R7-parked and may have built OI.

---

## GLOSSARY

- **R1 (range percentile):** where the stock sits in its 52-week range, 0 = at the low. Calls want under 0.25.
- **R2 (calendar):** the print has to land at least 21 days before expiry (later of the tool date and last year's date), with the 10-Q/10-K deadline at least 5 trading days before expiry.
- **R3 (ratings):** 3+ Buys, Buys at least equal to Holds, 0-1 Sells.
- **R4 (floor):** breakeven has to sit under the lowest Buy-side price target. "Proxy" means using the tool's low target before checking who set it and when.
- **R5 (affordability):** one contract's ask under the tier cap (10% of reserve at 3.5/5).
- **R6 (reachability):** the move needed to breakeven has to fit inside the stock's typical earnings-day move.
- **R7 (liquidity floor):** open interest of at least 250 and a spread of at most 25% of mid on the exact contract.
- **OI:** open interest, the contracts currently outstanding.
- **BE:** breakeven, strike plus premium paid.
- **Slide-in scan:** the earnings-window scan re-run on the latest closes to catch names that just fell into the bottom of their range.
- **Floor gate:** the doc is otherwise done but waits for a Buy target dated after the stock's slide.
- **Paper book:** simulated trades on larger names, same rules except Rule 5, no money moves.
- **(v) / (f):** verified (company-announced) or forecast earnings date.
