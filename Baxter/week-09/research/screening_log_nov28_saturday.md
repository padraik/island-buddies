# Screening log: Sat Nov 28, SATURDAY (9:00am ET)

**Job (from Friday EVENING 3's queue):** (1) the old tabled names, median-first: VC, CRH, INVX, AXSM, MWH, ERO, AUPH; (2) ELE / INFQ / SKHY (2 prints each); (3) re-run the Apr 1-30 A/B scan for never-worked names. Plus CHRW's R1 line.

**Source:** Robinhood tools only, run ~14:00-14:30 UTC Nov 28 on Friday's half-day close (stock and option quotes stamped ~18:00 UTC Nov 27). 0 web searches. Daily bars through Fri Nov 27. R5 line: 10% x $715.96 / 100 = **$0.716/share** (3.5/5). Every name below is paper-size at that line.

## (1) R1 refresh (trailing 252 daily closes, through Fri Nov 27)

| Ticker | Fri close | 52w close low / high | Pctile | R1 line | Verdict |
|---|---|---|---|---|---|
| VC | 82.91 | 72.42 / 123.90 | 0.204 | 85.29 | passes |
| CRH | 98.11 | 79.20 / 131.38 | **0.362** | 92.25 | **KILLED R1** (was 0.22 at $90.54 on Nov 20) |
| INVX | 24.32 | 21.22 / 31.63 | **0.298** | 23.82 | **KILLED R1** (was 0.22 at $23.48) |
| AXSM | 147.91 | 129.36 / 255.17 | 0.147 | 160.81 | passes |
| MWH | 27.21 | 21.375 / 46.77 | 0.230 | 27.72 | passes (thin) |
| ERO | 21.60 | 21.47 / 40.40 | 0.007 | 26.20 | passes |
| AUPH | 14.75 | 13.95 / 18.62 | 0.171 | 15.12 | passes |
| ELE | 13.06 | 11.33 / 24.25 | 0.134 | 14.56 | passes |
| INFQ | 7.05 | 6.32 / 19.87 | 0.054 | 9.71 | passes |
| SKHY | 119.50 | 103.57 / 198.63 | 0.168 | 127.33 | passes |
| CHRW | 146.98 | 124.61 / 209.42 | 0.264 | 145.81 | out, unchanged (needs a close under $145.81) |

## (2) Ratings (`get_equity_analyst_ratings`)

VC 10/3/0 low $90 (no stamp); AXSM 23/1/0 low $220 (no stamp); MWH 12/0/0 low $34 (no stamp); ERO 10/9/0 low $30 (no stamp); AUPH 4/2/0 low $16 (no stamp). All pass R3 and the R4 proxy. ELE 6/0/0 low $25.98; INFQ 6/1/0 low $12; SKHY 14/1/0 low $190, stamp Nov 18.

## (3) Chains: near-ATM books, Friday close (medians from the Nov 20 logs; no prints since)

R2 expiry: VC Feb 18 AM and AXSM Feb 22 AM -> Mar19; MWH Feb 13 PM (no Mar listed), ERO Mar 4 PM, AUPH Feb 25 AM (no Mar listed) -> Apr16.

| Contract | Bid / Ask | OI | BE at ask | Needs | Cap (1.5 x median) | Verdict |
|---|---|---|---|---|---|---|
| VC $80C Mar19 | 7.90 / 9.60 | 18 | 89.60 | +8.1% | 6.8% | R6, R7 |
| VC $85C Mar19 | 4.30 / 7.20 | 4 | 92.20 | +11.3% | 6.8% | R6, R7 |
| VC $90C Mar19 | 2.10 / 6.00 | 5 | 96.00 | +15.9% | 6.8% | R6, R7 |
| AXSM $140C Mar19 | 20.50 / 23.50 | 18 | 163.50 | +10.6% | 5.7% | R6, R7 |
| AXSM $150C Mar19 | 15.60 / 18.70 | 122 | 168.70 | +14.1% | 5.7% | R6, R7 |
| AXSM $160C Mar19 | 11.70 / 14.30 | 160 | 174.30 | +17.9% | 5.7% | R6, R7 |
| MWH $25C Apr16 | 5.60 / 6.10 | 421 | 31.10 | +14.1% | 6.5% | R6 (passes R7) |
| MWH $30C Apr16 | 3.40 / 4.00 | 64 | 34.00 | +24.7% | 6.5% | R6, R7 |
| ERO $21C Apr16 | 3.40 / 4.10 | 7 | 25.10 | +15.9% | 6.0% | R6, R7 |
| ERO $22.5C Apr16 | 2.75 / 3.60 | 4 | 26.10 | +20.5% | 6.0% | R6, R7 |
| ERO $24C Apr16 | 2.20 / 2.90 | 1 | 26.90 | +24.5% | 6.0% | R6, R7 |
| AUPH $14C Apr16 | 1.05 / 2.80 | 36 | 16.80 | +13.8% | 4.9% | R6, R7 |
| AUPH $15C Apr16 | 1.25 / 2.35 | 51 | 17.35 | +17.6% | 4.9% | R6, R7 |
| AUPH $16C Apr16 | 0.60 / 3.10 | 384 | 19.10 | +29.5% | 4.9% | R6, R7 (spread) |

Every contract needs at least 1.2x its cap; most need 2-3x. That's the structural problem the Nov 20 table predicted: 3-4.5% medians can't pay for 2-5 months of time value.

## (4) April print window re-sweep

- **A/B ($1-25) `42772e1a-5c4a-439e-b539-b615b3fd611c`:** 14 rows (16 on Nov 24). 12 already worked (SFD, FRPH, NPFD, MUJ, MUC, JKS, JFR, INFQ, JPC, JQC, PSNY, EVO). Never-worked this week: **MUA** (BlackRock closed-end fund, out of universe) and **LAES** (SEALSQ, +24.1% Fri; no analyst coverage, **KILLED R3**, same as Nov 3).
- **C/D ($25+), new scan `f6919fee-23b3-4729-a565-6c35dc37b2cf`:** **0 rows.** Same reason as Nov 24: the scanner carries each company's next print only, and for calendar-year companies that's the Q4 report in Feb/Mar. The April window fills in after those prints land.

## Verdicts

- **Killed (8):** R1 CRH, INVX; R6 at the ask VC, AXSM, MWH, ERO, AUPH; R3 LAES.
- **Out of universe (1):** MUA (closed-end fund).
- **Parked, unchanged (3):** ELE, INFQ, SKHY. Still only 2 prints each, so no median; R1 and R3 still pass. They become workable after their Feb prints (third data point).
- **Watching (1):** CHRW, R1 0.264, line $145.81. No trading since Friday's EVENING checks.
- **Tally:** 13 names moved, 0 advanced, 0 docs, 0 buyable (real or paper), 0 searches.

## The finding

The tabled bucket is empty now, and every name in it died the way the Nov 20 ratio said it would. MWH's $25C was the only book with real open interest (421), and it needs +14.1% against a 6.5% cap. The April window is still closed to the scanner until the Q4 prints land. So the honest state of the pipeline on Saturday: nothing real-money-sized is alive, and the only fresh supply before mid-February is names that drop under R1 0.25 on new trading, which Monday EVENING 1 checks with the eight saved scans.

## GLOSSARY

- **R1 (range percentile):** (price - 52-week low) / (52-week high - 52-week low). Under 0.25 = calls candidate.
- **R2:** the print is proven to land before expiry: expiry 21+ days after the later of the tool date and last year's date, with the filing deadline 5+ trading days before expiry.
- **R3 (calls):** at most 1 Sell, at least 3 Buys, and Buys at least equal to Holds.
- **R4 (bear floor):** lowest Buy target above breakeven (strike + premium). The R4 proxy at screening: lowest target above the stock price.
- **R5:** one contract's ask x 100 must fit the conviction tier on reserve (3.5/5 = 10% = $0.716/share).
- **R6:** the move to breakeven (strike + ask) can be no more than 1.5x the median earnings-day move over the last 4-8 prints.
- **R7:** the exact contract needs open interest >= 250 and a spread <= 25% of mid.
- **Median print move:** the middle value of the absolute earnings-day moves; sign ignored.
- **R6 cap:** 1.5 x median.
- **BE (breakeven):** strike + premium paid, the price the stock must reach by expiry to not lose money.
- **OI (open interest):** contracts currently open on that exact strike and expiry.
- **Tabled:** median and R6 cap computed, book not quoted yet.
- **Closed-end fund:** a fund that trades like a stock; outside the single-company universe the screen covers.
