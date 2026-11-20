# Screening log: Thu Nov 19, EVENING 2 (8:00pm ET)

**Job (from EVENING 1's plan):** no name cleared the chain at 6pm, so there's no doc to write. (1) Find band B's two missing cheap rows. (2) Date + chain the 7 band C parks left (GLNG, KGS, VIST, DOCN, AAON, CRH, KBR). (3) Live books on the sub-$10 Apr16 stagers (CTNM, DSGN, CTGO; ECVT) against the $0.716 R5 line. Finished early, so started EVENING 3's job: R6 print tables for the cheap band A stagers (CCCC, CADL, BCRX, TGB, ABX).

**Source:** Robinhood tools only, run ~01:00-01:20 UTC on Thursday's closing books (option quotes stamped 20:58-21:00 UTC). 0 web searches. R5 line tonight: 10% x $715.96 reserve / 100 = **$0.716/share** (3.5/5).

## (1) Band B's cheap end

Previewed band B's exact filters (`fccfd39a`: market cap $300M+, earnings Feb 13 - Mar 20 2027, stocks, R1 < 0.25) with the price band cut to **$8.19-9.30**: **26 rows.** Diffed every ticker against the week-09 logs, the full sweep, passes.md and paper_book.md: **all 26 are already worked** (LXU VITL OTF FPI BSRT WBTN TME CGEM SNDX HLN ZVRA HUN BRSL GLUE CTNM REAX EQX BWAY BKD NPKI VINP PRTA NN XRAY HE SDHC). The two rows the 200 cap cut at 6pm were old names. Nothing new. (Preview only; no scan saved.)

## (2) Band C parks: date + chain stage

Same test as the 6pm log: L = later of the tool date and last year's same-quarter date; expiry 21+ days past L; 10-K filers need LA status for Mar19.

| Ticker | Close | Tool date (verified false) | LY | L | Listed spring expiries | Verdict |
|---|---|---|---|---|---|---|
| KGS | 42.69 | Feb 24 PM | Feb 25 2026 PM | Feb 25 | Apr16, Jul16 | **Apr16** (50d; no Mar19 listed) |
| VIST | 50.18 | Feb 24 PM | Feb 25 2026 PM | Feb 25 | Mar19, May21, Jun17 | **Mar19** (20-F/6-K, both dates present, 1d) |
| DOCN | 77.09 | Feb 23 AM | Feb 24 2026 AM | Feb 24 | Feb19, Mar19, May21 | **Mar19-if-LA** (2d); else **May21** |
| AAON | 77.08 | Mar 1 AM | Mar 2 2026 AM | Mar 2 | Mar19, Apr16, Jul16 | **Apr16** (Mar19 misses: 17d) |
| CRH | 90.54 | Feb 17 PM | Feb 18 2026 PM | Feb 18 | Mar19, Jun17 | **Mar19 firm** (LA, 8d) |
| KBR | 31.99 | Feb 25 AM | Feb 26 2026 AM | Feb 26 | Mar19, Jun17 | **Mar19 firm** (LA, 0d); fallback Jun17 |
| GLNG | 40.40 | **none** | Feb 25 2026 AM | - | Mar19, Jun17 | **Dates unusable**: the tool's rows are mislabeled (a "2024 Q3" row dated 2026-11-18) and carry no upcoming Q4 date. 6-K filer, so both dates are required. Held, not killed; re-pull Saturday. |

All six staged names are paper-book size (KBR $32 is the cheapest); none can be real money at $0.716.

## (3) Sub-$10 Apr16 stagers: live books (closing quotes)

| Contract | Bid / Ask | Spread % mid | OI | BE at ask | Needs | Verdict |
|---|---|---|---|---|---|---|
| CTNM $10C Apr16 | 2.75 / 5.50 | 67% | 4,635 | 15.50 | +71% | R5, R7 |
| CTNM $12.5C Apr16 | 1.75 / 3.10 | 56% | 3,211 | 15.60 | +73% | R5, R7 |
| CTNM $15C Apr16 | 0.00 / 4.90 | - | 11 | - | - | no bid, R7 |
| DSGN $10C-$13C Apr16 | 0.00 / 3.90-4.60 | - | 0-1 | - | - | no bid on any strike, R7 |
| CTGO $10C Apr16 | 1.25 / 2.05 | 48% | 673 | 12.05 | +21.2% | R5, R6, R7 |
| CTGO $12.5C Apr16 | 0.65 / 1.55 | 82% | 183 | 14.05 | +41.3% | R5, R6, R7 |
| **CTGO $15C Apr16** | **0.30 / 0.55** | **59%** | **539** | **15.55** | **+56.4%** | **R5 pass ($0.55 <= $0.716); R6 and R7 fail** |
| ECVT $10C Mar19 | 0.65 / 0.90 | 32% | 55 | 10.90 | +12.9% | R5, R6, R7 |
| ECVT $12.5C Mar19 | 0.15 / 0.30 | 67% | 164 | 12.80 | +32.6% | R6, R7 |
| ECVT $10C Jun17 | 0.75 / 1.70 | 78% | 2 | 11.70 | +21.2% | R5, R6, R7 |

**R6 print tables** (earnings-day close-to-close; AM prints = prior close to print-day close, PM prints = print-day close to next close):

- **CTGO:** May 14 '25 +16.7, Aug 13 '25 +1.8, Nov 13 '25 -5.5, Mar 16 '26 -2.6, May 14 '26 -6.3, Aug 13 '26 +3.7, Nov 13 '26 -9.5. **Median 5.5%, cap 8.3%.**
- **ECVT:** May 1 '25 -36.3, Aug 7 '25 -2.3, Nov 4 '25 -5.2, Feb 26 '26 +1.1, May 5 '26 +4.3, Aug 5 '26 -5.5, Nov 5 '26 +2.1. **Median 4.3%, cap 6.5%.**

**Killed: CTNM (R5 + R7), DSGN (R7, no market), CTGO (R6: $15C needs +56.4% vs 8.3% cap; R7 59% spread), ECVT (R6: cheapest R5-fit strike needs +32.6% vs 6.5%).**

## (4) Started EVENING 3's job: band A cheap stagers, R6 tables + books

| Ticker | Close | Prints (7) | Median | R6 cap | Max BE | Best contract quoted | BE at ask | Verdict |
|---|---|---|---|---|---|---|---|---|
| CCCC | 2.475 | +6.4, +31.6, +0.4, +0.4, 0.0, +6.9, -5.4 | 5.5% | 8.2% | 2.68 | $2C Apr16 0.40 / 1.40, OI 4 | 3.40 | **R6, R7, R5** |
| CADL | 5.13 | +7.7, -5.6, -6.3, -2.4, -1.6, +10.5, -26.1 | 6.3% | 9.5% | 5.61 | $5C Apr16 1.05 / 4.80, OI 215 | 9.80 | **R6, R7, R5** |
| BCRX | 7.30 | +23.5, +9.8, -6.3, +4.6, -2.2, +0.6, -3.9 | 4.6% | 7.0% | 7.81 | $7C Mar19 0.30 / 2.15, OI 14 ($8C no bid) | 9.15 | **R6, R7, R5** |
| TGB | 5.56 | -11.3, +2.0, -11.9, -4.4, -3.6, +0.7, -7.7 | 4.4% | 6.5% | 5.92 | $5C May21 1.30 / 1.50, OI 200; $6C 0.75 / 1.20, OI 106 | 6.50 / 7.20 | **R6, R5, R7 (OI)** |
| ABX | 6.53 | +5.4, +8.0, +22.2, -0.5, -3.2, -8.5, +0.3 | 5.4% | 8.1% | 7.06 | $5C May21 1.85 / 2.90; $7.5C 0.80 / 1.00, OI 111 | 7.90 / 8.50 | **R6, R5, R7 (OI)** |

**Killed: CCCC, CADL, BCRX, TGB, ABX, all on R6.**

**The pattern (a finding, not a rule change):** on every cheap name checked tonight, the time value in a spring contract is bigger than the whole room R6 allows. Breakeven is at least price + time value, so a contract can only pass R6 if its time value fits inside 1.5x the median print move, which is $0.20 to $0.70 on a $2.50-$10 stock. Spring books on these names carry $0.40 to $3.00 of time value, and those spreads are wide too. As long as R2 forces expiries 3-5 months out, sub-$10 names with ~5% median moves can't pass R6 at any strike. The real-money path runs through names with big median moves (15%+), not through cheap prices.

## Tally

Moved 16 names: 9 killed (CTNM, DSGN, CTGO, ECVT, CCCC, CADL, BCRX, TGB, ABX), 6 staged (KGS, VIST, DOCN, AAON, CRH, KBR), 1 held on unusable dates (GLNG). 26 band B cheap rows diffed: 0 new. 0 advanced past the chain, 0 buyable, 0 docs, 0 web searches.

## GLOSSARY

- **R1 (range percentile):** (price - 52-week low) / (52-week high - 52-week low). Under 0.25 = calls candidate.
- **R2:** the print is proven to land before expiry: expiry 21+ days after the later of the tool date and last year's date, and the 10-K deadline 5+ trading days before expiry (20-F / 40-F filers: both dates required, no deadline test).
- **R5:** one contract's ask x 100 must fit the conviction tier on reserve (3.5/5 = 10% = $0.716/share tonight).
- **R6:** the move to breakeven (strike + ask) must be no more than 1.5x the median earnings-day move over the last 4-8 prints.
- **R7:** the exact contract needs open interest >= 250 and a spread <= 25% of mid.
- **Time value:** the part of an option's price above what it's worth if exercised now. Breakeven can never sit closer to the stock price than this.
- **LA / large accelerated filer:** $700M+ public float; 10-K due Mar 1, the only deadline early enough for a Mar19 expiry.
- **Staged:** has a dated R2 verdict and a listed expiry, waiting for its spring chain to be checked.
- **Preview scan:** a scanner run that saves nothing.
