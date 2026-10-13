# Screening log, Tue Oct 13, 6:00pm ET (EVENING 1, DO)

*Live data pulled 22:00-22:03 UTC, market closed: option quotes are the 4:00pm closing quotes (closing spreads run wide, so an R7 spread fail at the close gets one mid-session re-quote before it's final). Reserve $676.28 (3.5/5 line $0.676). Two jobs: (1) queue items 4-9 (LRN, ADC, VC, ITRI, BMRN, ALGT) through the chain stage; (2) the >$100 band of the Oct 20 - Nov 20 print window. Two web searches (NBIX, TTWO decline cause).*

## Part 1: queue items 4-9 at the chain stage

| Name | Stock | Contract(s) checked | Bid / ask | OI | Spread % of mid | BE at ask | Low target | Result |
|---|---|---|---|---|---|---|---|---|
| LRN | 82.98 | Nov20 $80C / $85C / $90C | 8.20/9.80, 5.80/6.50, 3.80/5.30 | 206 / 188 / 271 | 18% / 11% / 33% | 89.80 / 91.50 / 95.30 | $90 | **KILL, R7** ($80C and $85C under 250 OI; $90C spread 33%, and $85C/$90C BE over the $90 floor, R4) |
| ADC | 65.42 | Nov20 $65C / $70C | 1.70/3.60, 0.25/0.45 | 10 / 45 | 72% / 57% | 68.60 / 70.45 | $72 | **KILL, R7** |
| VC | 86.58 | Nov20 $85C / $90C / $95C | 3.50/7.00, 2.10/4.70, 0.05/3.20 | 1 / 0 / 0 | 67%+ | | $104 | **KILL, R7** (no open interest) |
| ITRI | 86.62 | Nov20 $85C / $90C / $95C | 6.00/7.70, 4.10/5.10, 2.05/4.00 | 21 / 81 / 52 | 25% / 22% / 64% | 92.70 / 95.10 / 99.00 | $115 | **KILL, R7** (OI) |
| BMRN | 54.39 | Nov20 $55C / $57.5C / $60C | 2.40/4.80, 1.25/3.10, 0.15/1.15 | 96 / 75 / 324 | 67% / 85% / 154% | 59.80 / 60.60 / 61.15 | $60 | **KILL, R7** (only $60C has OI, and its BE is over the $60 floor, R4) |
| ALGT | 72.38 | no Dec18 listed (expiries Oct16, Nov20, Jan15, Apr16); Nov20 fails R2 (16 days past LY Nov 4); **Jan15** $70C / $75C / $80C | 9.30/11.90, 7.20/9.00, 5.00/7.00 | 14 / 12 / 22 | 25% / 22% / 33% | 81.90 / 84.00 / 87.00 | $85 | **KILL, R7** (OI) |

## Part 2: scanner, prints Oct 20 - Nov 20, range pct < 0.25, cap >= $300M, Last > $100 (preview, not saved)

116 matches, all returned. Whole-word diff against every week-09 file plus passes.md and paper_book.md: **16 new**.

| Name | Last | Range pct | Print (scanner) | Buy / Hold / Sell | Low target | Result |
|---|---|---|---|---|---|---|
| GD | 329.66 | 0.25 | Oct 23 | 16 / 11 / 1 | $309 | **KILL, R4 proxy** (floor under the stock) |
| LAD | 286.78 | 0.24 | Oct 21 | 13 / 5 / 0 | $310 | advance |
| ASR | 234.39 | 0.05 | Oct 22 | 9 / 5 / 2 | $240 (stamped 2020) | **KILL, R3** (2 Sells) |
| HWM | 216.84 | 0.25 | Oct 29 | 22 / 4 / 0 | $255 (stamped 2021) | advance (floor stamp stale) |
| WDFC | 204.41 | 0.23 | Oct 21 | 4 / 2 / 0 | $245 | advance |
| TTWO | 199.95 | 0.16 | Nov 6 | 29 / 1 / 1 | $270 | advance |
| SAM | 177.23 | 0.18 | Oct 23 | 1 / 12 / 1 | $153 | **KILL, R3** |
| POOL | 160.60 | 0.05 | Oct 22 | 6 / 10 / 1 | $167 | **KILL, R3** (Buys < Holds) |
| NBIX | 135.13 | 0.20 | Oct 28 | 27 / 4 / 0 | $150 | advance |
| EXR | 133.74 | 0.24 | Oct 27 | 11 / 10 / 1 | $140 | advance (R4 tight) |
| BMI | 131.25 | 0.21 | Oct 22 | 10 / 2 / 1 | $111 | **KILL, R4 proxy** |
| FSV | 130.81 | 0.16 | Oct 22 | 9 / 2 / 0 | $140 | advance |
| VRTS | 128.46 | 0.09 | Oct 23 | none | | **KILL, no coverage** |
| MHO | 125.99 | 0.20 | Oct 21 | none | | **KILL, no coverage** |
| ARES | 115.62 | 0.23 | Oct 29 | 16 / 7 / 0 | $119 | **KILL, R4 proxy** (floor 2.9% over the stock) |
| CAR | 107.60 | 0.03 | Oct 27 | 0 / 7 / 3 | $94 | **KILL, R3** |

### R2 (`get_earnings_results`) and chain for the 7 advancers

| Name | Tool date | LY same quarter | R2 expiry | Contract | Bid / ask | OI | Spread | BE at ask | Result |
|---|---|---|---|---|---|---|---|---|---|
| LAD | Oct 21 AM (**verified**) | Oct 22, 2025 AM | Nov20 | $290C | 13.70/16.80 | 78 | 20% | 306.80 | **KILL, R7** (OI) |
| HWM | Oct 29 AM (**verified**) | Oct 30, 2025 AM | Nov20 (exactly 21 days) | $220C | 9.20/11.80 | 51 | 25% | 231.80 | **KILL, R7** (OI) |
| WDFC | Oct 21 PM (**verified**, FQ4) | Oct 22, 2025 PM | Nov20 | $210C | 6.60/7.60 | 31 | 14% | 217.60 | **KILL, R7** (OI) |
| EXR | Oct 27 PM (**verified**) | Oct 29, 2025 PM | Nov20 (22 days) | $135C | 3.40/5.30 | 11 | 44% | 140.30 | **KILL, R7** (and BE over the $140 floor, R4) |
| FSV | Oct 22 AM (**verified**) | Oct 23, 2025 AM | Nov20 | $135C | 0.90/5.50 | 0 | 144% | 140.50 | **KILL, R7** (and R4) |
| **TTWO** | Nov 9 PM (**verified**, FQ2) | Nov 6, 2025 PM | **Dec18** (Nov20 is 11 days past the print) | $200C / **$190C** / $180C | 17.90/19.70, **22.80/25.00**, 28.70/31.20 | 1,432 / **835** / 78 | 10% / **9%** / 8% | 219.70 / **215.00** / 211.20 | **PARK, R6** on the $190C (below) |
| **NBIX** | Nov 2 PM (**verified**) | Oct 28, 2025 PM | **Dec18** (Nov20 is 18 days past the print) | $140C / **$135C** | 5.40/9.50, **8.30/11.90** | 302 / **307** | 55% / **36%** | 149.50 / **146.90** | **PARK, R7** on the $135C closing spread (below) |

**TTWO R6.** Print-day close moves, last six (tool dates): May 15 2025 PM -2.41%, Aug 7 2025 PM -4.03%, Nov 6 2025 PM -8.08%, Feb 3 2026 PM -5.38%, May 21 2026 PM -4.42%, Aug 7 2026 AM +6.04%. Median 4.90%, cap 1.5x = **7.35%**. $190C BE $215.00 at the ask needs **+7.53%** from $199.95: misses by 0.18 points. Passes at stock >= ~$200.28 with a $25.00 ask. $180C needs +5.6% but OI 78 (R7). $200C needs +9.9%. R1 0.16, R3 29/1/1 (one Sell, allowed), R4 $270 floor vs $215 BE (wide). Paper only: $2,500 a contract against a $67.63 line. Today -4.2% (Mon close $208.82); one search found no named cause for today (August GTA VI leak worries and the earlier GTA VI delay are the background). Four of six prints went down on the day, which Bearxter will want answered before a paper entry.

**NBIX R6.** Print-day close moves: May 5 2025 PM +8.36%, Jul 30 2025 -6.24%, Oct 28 2025 -6.35%, Feb 11 2026 -10.43%, May 5 2026 +8.86%, Jul 30 2026 -10.08%. Median 8.61%, cap **12.91%**. $135C BE $146.90 needs **+8.7%** (pass); R4 $150 floor vs $146.90 BE (pass, 2.1% margin, floor undated in the tool). R1 0.20, R3 27/4/0. R7 fails only on the closing spread (3.60 wide on a 10.10 mid, 36%); OI 307 passes. Decline cause (one search): stock fell ~10% after Q2 (Jul 30) on growth spending despite ~$959M revenue, plus two Phase 2 misses (NBI-921352 focal seizures, NBI-1065846 anhedonia); it's -27% since. Today -4.4% (Mon $141.37), cause not found. Estimate revisions unverified: caps it at 3.5/5. Paper only: ~$1,190 a contract.

**Moved:** 22 (6 queue names, 16 new). **Killed:** 20 (LRN, ADC, VC, ITRI, BMRN, ALGT, LAD, HWM, WDFC, EXR, FSV on R7; GD, BMI, ARES on R4 proxy; ASR, SAM, POOL, CAR on R3; VRTS, MHO no coverage). **Parked:** TTWO Dec18 $190C (R6, 0.18 points), NBIX Dec18 $135C (R7 spread at the close).

**Pattern:** the >$100 band has the floors and the coverage, and its contracts have no open interest. 11 of 13 chain checks tonight died on R7 OI, not on any thesis rule. The only contracts with real OI were on the two names with big option followings (TTWO, NBIX). This window is now screened through every price band.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile (bottom quartile for calls), R2 earnings before expiry (21-day cushion on the later of tool date and last year's date; 10-Q deadline at least 5 trading days before expiry; 6-K filers need both dates), R3 analyst consensus (max 1 Sell, 3+ Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability (ask x 100 <= 10% of reserve at 3.5/5), R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **R4 proxy:** the free screen's version of Rule 4, before any chain: if the lowest Buy target isn't comfortably above the stock price, no call's breakeven can sit under it.
- **BE:** breakeven, strike plus premium paid (here at the ask).
- **OI:** open interest, contracts outstanding on that exact strike and expiry.
- **LY:** last year's same-quarter report date.
- **PARK:** the contract is alive but fails one rule today; re-checked every run.
- **Closing spread:** the 4:00pm quote. Market makers widen at the close, so a spread fail there gets one mid-session re-quote.
- **Paper only:** one contract costs more than Rule 5 allows the real fund; it can only go in the paper book.
- **Print-day move:** close-to-close change across the earnings report (PM print: report day close to next close; AM print: prior close to report-day close).
