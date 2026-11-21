# Screening log: Fri Nov 20, EVENING 2 (8:00pm ET)

**Job (from EVENING 1's plan):** nothing cleared the chain stage, so there's no doc to write. Pulled EVENING 3's job forward: the ratio pre-screen (median print move vs near-ATM time value) on the next 21 stagers: VIST, DOCN, AAON, CRH, EMBJ, CAAP, CAI, INVX, JBIO, OUST, ARIS, then the Nov 17-18 band B/C Mar19-firm names IONQ, CENX, CDE, QXO, SGI, EXE, VC, IRTC, PODD, AXSM.

**Source:** Robinhood tools only, run ~01:00-01:30 UTC Nov 21 on Friday's closing books (option quotes stamped ~20:59 UTC Nov 20). 0 web searches. Daily bars include Fri Nov 20. R5 line: 10% x $715.96 / 100 = **$0.716/share** (3.5/5). Every name below is paper-size at that line; R5 is noted only where it matters.

## (1) Medians: last 7 reported prints (CAI has 6), all `verified: true` in `get_earnings_results`

AM print: prior close to print-day close. PM print: print-day close to next close. Percentile = Friday close in the trailing 252-day close range.

| Ticker | Fri | Pctile | Prints (oldest first) | Median | R6 cap | Next (tool, f) |
|---|---|---|---|---|---|---|
| CAI | 18.54 | 0.18 | +5.6, -15.7, +4.7, -18.6, +21.6, -21.6 (6) | **17.1%** | 25.7% | Feb 25 PM |
| DOCN | 77.09 | 0.25 | -13.8, +28.9, +18.0, +5.9, +40.4, +1.4, +0.8 | **13.8%** | 20.7% | Feb 23 AM |
| PODD | 137.23 | 0.03 | +20.9, +9.5, +2.8, +4.8, -9.7, -20.1, +6.6 | 9.5% | 14.2% | Feb 17 AM |
| IONQ | 22.71 | 0.00 | +9.3, -1.8, +3.6, +21.7, -9.3, -0.5, +23.4 | 9.3% | 14.0% | Feb 24 PM |
| OUST | 23.80 | 0.16 | +22.8, +11.7, -6.5, +7.3, +2.8, -4.8, +15.7 | 7.3% | 10.9% | Mar 1 PM |
| AAON | 77.08 | 0.24 | +5.7, -10.5, +7.0, +3.5, +31.5, -5.9, +19.3 | 7.0% | 10.5% | Mar 1 AM |
| SGI | 59.44 | 0.03 | -1.0, +0.4, +11.8, -8.6, -10.1, -6.8, +3.3 | 6.8% | 10.2% | Feb 16 AM |
| CDE | 11.54 | 0.00 | +21.6, +14.1, -3.0, +6.5, -3.4, -10.2, +0.3 | 6.5% | 9.8% | Feb 17 PM |
| IRTC | 94.24 | 0.08 | +20.7, +17.7, +1.7, -5.0, -6.5, -0.2, -30.7 | 6.5% | 9.8% | Feb 18 PM |
| VC | 81.30 | 0.17 | +4.6, +0.8, -4.5, -11.5, +9.4, -3.0, -3.7 | 4.5% | 6.8% | Feb 18 AM |
| CRH | 90.54 | 0.22 | -4.4, +9.5, -0.8, +0.6, +4.4, -3.7, +4.7 | 4.4% | 6.6% | Feb 17 PM |
| INVX | 23.48 | 0.22 | +2.7, -3.1, -4.0, +6.4, -2.7, +11.8, -6.4 | 4.0% | 6.0% | Feb 22 PM |
| AXSM | 135.68 | 0.05 | +3.8, +3.4, +0.6, -4.9, +8.3, +3.8, -5.8 | 3.8% | 5.7% | Feb 22 AM |
| EXE | 82.44 | 0.00 | -3.3, +4.9, -0.6, -3.1, +4.2, +4.5, -3.2 | 3.3% | 4.9% | Feb 16 PM |
| CENX | 30.44 | 0.10 | -2.0, +1.6, +14.0, +0.3, -2.8, +11.5, +11.3 | 2.8% | 4.2% | Feb 18 PM |
| QXO | 11.02 | 0.05 | -0.1, -0.2, +6.5, -3.7, -4.1, -2.6, -1.6 | 2.6% | 3.9% | Feb 24 AM |
| CAAP | 22.73 | 0.04 | -2.5, +6.9, +1.6, +2.6, -4.4, -4.2, -1.8 | 2.6% | 3.9% | Mar 16 AM |
| VIST | 50.18 | 0.18 | +2.7, -5.9, +11.5, -0.8, -0.1, +2.6, -1.0 | 2.6% | 3.9% | Feb 24 PM |
| ARIS | 12.74 | 0.12 | +0.7, -6.9, +8.1, -2.3, +0.4, +2.5, -2.8 | 2.5% | 3.8% | Mar 10 PM |
| JBIO | 15.31 | 0.25 | -2.0, -7.6, -3.2, +1.2, +6.6, -1.0, +1.7 | 2.0% | 3.0% | Mar 5 AM |
| EMBJ | 18.37 | **0.69** | -0.2, -1.1, -4.1, -7.2, -11.3, +1.1, +7.0 | 4.1% | 6.1% | Mar 5 AM |

## (2) Near-ATM quotes on the top nine by median (Friday close)

| Contract | Bid / Ask | Spread % mid | OI | IV | TV at mid (% stock) | Ratio at mid | BE at ask | Needs | Cap | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **DOCN $80C Mar19** | 8.80 / 11.50 | 27% | 32 | 95% | 10.15 (13.2%) | **1.05** | 91.50 | **+18.7%** | 20.7% | **R6 PASSES at the ask.** R7 (OI 32, spread 27%), R5 |
| DOCN $75C Mar19 | 10.30 / 13.00 | 23% | 1 | 95% | 9.56 (12.4%) | 1.11 | 88.00 | +14.2% | 20.7% | R6 pass; R7 (OI 1), R5 |
| DOCN $85C Mar19 | 7.50 / 10.00 | 29% | 7 | 94% | 8.75 (11.4%) | - | 95.00 | +23.2% | 20.7% | R6, R7 |
| DOCN $70C Mar19 | 13.10 / 14.80 | 12% | 3 | 99% | 6.86 (8.9%) | - | 84.80 | +10.0% | 20.7% | R6 pass; R7 (OI 3), R5 |
| DOCN $90C / $100C Mar19 | 6.10 / 8.50, 5.20 / 7.40 | 33%, 35% | 24, 79 | 92-97% | - | - | 98.50, 107.40 | +27.8%, +39.3% | 20.7% | R6, R7 |
| DOCN $80C May21 | 12.80 / 14.20 | 10% | 4 | 93% | 13.50 (17.5%) | 0.79 | 94.20 | +22.2% | 20.7% | R6, R7 |
| CAI $17.5C Apr16 | 2.15 / 5.90 | 93% | 80 | 88% | 2.99 (16.1%) | **1.06** | 23.40 | +26.2% | 25.7% | R6 by 0.5 pt at the ask; R7, R5 |
| CAI $20C Apr16 | 1.05 / 4.90 | 129% | 28 | 84% | 2.98 (16.0%) | 1.07 | 24.90 | +34.3% | 25.7% | R6, R7, R5 |
| CAI $15C / $22.5C Apr16 | 3.40 / 7.00, 0.30 / 4.30 | 69%, 174% | 0, 0 | 84-89% | - | - | - | - | - | R7 (no book) |
| PODD $140C Mar19 | 11.30 / 17.00 | 40% | 115 | 54% | 14.15 (10.3%) | 0.92 | 157.00 | +14.4% | 14.2% | R6 by 0.2 pt; R7, R5 |
| SGI $60C Mar19 | 5.20 / 6.40 | 21% | 20 | 49% | 5.80 (9.8%) | 0.69 | 66.40 | +11.7% | 10.2% | R6, R7, R5 |
| CDE $12.5C Mar19 | 1.05 / 1.20 | 13% | 808 | 71% | 1.125 (9.7%) | 0.67 | 13.70 | +18.7% | 9.8% | R6 (OTM), R5 |
| IONQ $22.5C Mar19 | 3.55 / 4.50 | 24% | 284 | 98% | 3.82 (16.8%) | 0.55 | 27.00 | +18.9% | 14.0% | R6, R5 |
| IRTC $95C Mar19 | 11.00 / 14.70 | 29% | 2 | 57% | 12.85 (13.6%) | 0.48 | 109.70 | +16.4% | 9.8% | R6, R7, R5 |
| AAON $80C Apr16 | 11.20 / 13.40 | 18% | 5 | 72% | 12.30 (16.0%) | 0.44 | 93.40 | +21.2% | 10.5% | R6, R7, R5 |
| OUST $25C May21 | 5.90 / 6.40 | 8% | 8 | 97% | 6.15 (25.8%) | 0.28 | 31.40 | +31.9% | 10.9% | R6, R7, R5 |

**Ratings on the survivors' neighborhood (`get_equity_analyst_ratings`):**
- **DOCN 16 / 2 / 0, low $100, high $220, no `updated_at` stamp.** R3 passes. $100 low vs $91.50 BE would pass R4, but the stock fell from $146 (Sep 21) to $77 and there's no date on the low target. Tab 6: a floor has to be dated and published after the decline. **Floor gate shut (unverifiable).**
- CAI 10 / 4 / 0, low $25, no stamp. Stock fell $36.14 (Oct 29) to $18.54, with -21.6% on the Nov 4 print. Same gate problem.
- PODD 14 / 15 / 0: **R3 fails** too (Buys < Holds).
- SGI 11 / 2 / 0, low $72. CDE 10 / 3 / 0, low $16. IONQ 14 / 3 / 0, low $37.90. All pass R3; all died on R6 anyway.

## Verdicts

- **Killed (16):**
  - R6 at the ask: IONQ, OUST, AAON, SGI, IRTC, CDE.
  - PODD: R6 by 0.2 points, plus R3 (14 Buy / 15 Hold) and R7.
  - CAI: R6 by 0.5 points at the ask, and R7 (dollar-wide book, OI 0-80).
  - R6 structural, caps 3.0-4.9%: VIST, CAAP, JBIO, ARIS, CENX, QXO, EXE. No spring strike carries that little time value.
  - EMBJ: R1. It's at the 69th percentile now.
- **Tabled, quote only if cheap (4):** VC (cap 6.8%), CRH (6.6%), INVX (6.0%), AXSM (5.7%). Same bucket as MWH / ERO / AUPH.
- **Keep Watching (1): DOCN $75C / $80C Mar19.** It's the first contract since the ratio work started to pass R6 at the ask. It's still blocked by R7 (OI 1-79 on every Mar19 strike; spreads 23-35% on the $75-90 strikes), by the floor gate (no stamp on a $100 low after a 47% slide), and by R5 for real money ($1,150 vs $71.60). R2: Q4 Feb 23 AM (f), last year Feb 24. Mar19 is 23 days past the later date, and the 10-K deadline (Mar 1 if large accelerated) is 13 trading days before expiry. That holds **if DOCN is a large accelerated filer**; otherwise May21, which fails R6. Re-check OI and the stamp weekly. Paper-book candidate only.
- **Tally:** 21 moved, 16 killed, 4 tabled, 1 to Keep Watching, 0 advanced, 0 buyable, 0 searches.

## The finding

The ratio worked as a sort key on its first live use. The two names with ratio > 1 at the mid (DOCN 1.05, CAI 1.06) both had medians over 13%, and both are names that just got cut in half (DOCN $146 -> $77 in two months; CAI $36 -> $18.50 in three weeks). That's the pattern Nov 19 predicted: real R6 room needs a 15%-ish median print. It also shows why those names are hard to trade. Big crashes leave thin, wide option books, with OI 0-80 and 27-129% spreads, and the analyst targets haven't caught up (no stamps). So R6 now passes in the same place R7 and the floor gate fail. The quoted pool has no name where all three line up. Not a rule change.

**Watch notes (not entries):** AVGO stamp still Oct 27 04:32Z (53/3/0, low $398.47), so the gate is shut and there's no Jan15 paper book. NIO stamp still Nov 18 00:55Z (16/7/1, low $3.7026), gate shut.

## GLOSSARY

- **R1 (range percentile):** (price - 52-week low) / (52-week high - 52-week low). Under 0.25 = calls candidate.
- **R2:** the print is proven to land before expiry: expiry 21+ days after the later of the tool date and last year's date, with the filing deadline 5+ trading days before expiry.
- **R3 (calls):** at most 1 Sell, at least 3 Buys, and Buys at least equal to Holds.
- **R4 (bear floor):** lowest Buy target above breakeven (strike + premium).
- **R5:** one contract's ask x 100 must fit the conviction tier on reserve (3.5/5 = 10% = $0.716/share tonight).
- **R6:** the move to breakeven (strike + ask) can be no more than 1.5x the median earnings-day move over the last 4-8 prints.
- **R7:** the exact contract needs open interest >= 250 and a spread <= 25% of mid.
- **Median print move:** the middle value of the absolute earnings-day moves; sign ignored.
- **R6 cap:** 1.5 x median. Max breakeven = stock x (1 + cap).
- **Time value (TV):** the part of an option's price above what it's worth if exercised now.
- **Ratio:** median print move / (near-ATM time value as % of stock). Needs >= 0.67 at the ask to pass R6.
- **IV (implied volatility):** the yearly move the option price assumes.
- **Floor gate / stamp:** Tab 6 needs the lowest Buy target to be dated and published after the decline; `updated_at` on the ratings record is the stamp. No stamp = can't verify = gate shut.
- **Large accelerated filer (LA):** big SEC filer with a 60-day 10-K deadline (Mar 1 for a Dec year-end); others get 75-90 days.
- **Tabled:** median and R6 cap computed, book not quoted yet.
