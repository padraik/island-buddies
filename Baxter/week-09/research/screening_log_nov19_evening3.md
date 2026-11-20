# Screening log: Thu Nov 19, EVENING 3 (10:00pm ET)

**Job (from EVENING 2's plan):** rank the staged pool by median print move instead of by price. R6 tables for SOUN, WVE, DNN (Nov 17 stage), then the staged band A/B names most likely to have big prints, and quote the spring book only where 1.5x median looks like it could beat the time value. Then leave Friday PREMARKET its plan.

**Source:** Robinhood tools only, run ~03:00-03:20 UTC on Thursday's closing books (option quotes stamped 20:59 UTC Nov 19). 0 web searches. R5 line tonight: 10% x $715.96 reserve / 100 = **$0.716/share** (3.5/5).

**Data note:** the daily-bar call returned a Nov 19 bar that copies Nov 18's close (SOUN 3.01, WVE 2.77, DNN 1.83), so it's interpolated. Every max-BE below uses the official Nov 19 close from `get_equity_quotes`.

## (1) R6 print tables

Earnings-day close-to-close (AM prints: prior close to print-day close; PM prints: print-day close to next close). Dates from `get_earnings_results`, all `verified: true`.

| Ticker | Close | R1 | Prints (oldest first) | Median | R6 cap | Max BE | Next print (tool, f) |
|---|---|---|---|---|---|---|---|
| SOUN | 2.91 | ~0.00 (new low) | -7.8, +26.4, -0.6, -4.2, -7.8, +10.1, -3.5 | 7.8% | 11.7% | 3.25 | Feb 25 PM |
| WVE | 2.72 | ~0.00 (new low) | +0.8, -1.9, -10.3, +5.6, +8.4, -0.9, +7.5 | 5.6% | 8.4% | 2.95 | Feb 25 AM |
| DNN | 1.81 | ~0.00 (new low) | -1.3, -5.4, -0.4, -1.0, -3.0, -0.9, -2.4 | 1.3% | 1.9% | 1.84 | Mar 9 PM |
| **AEVA** | 9.57 | 0.057 | +17.9, -15.0, -6.1, -2.8, -17.6, +28.8, -3.2 | **15.0%** | 22.5% | 11.72 | Feb 25 PM |
| RSI | 11.47 | 0.009 | -5.6, +25.5, -6.7, +7.3, +16.6, -13.0, -10.0 | 10.0% | 15.0% | 13.19 | Feb 16 PM |
| BBNX | 13.32 | 0.189 | +26.6, +14.3, +10.3, -2.6, -0.6, -5.9, -16.5 | 10.3% | 15.5% | 15.38 | Feb 16 PM |
| CAPR | 7.53 | 0.122 | +5.1, +2.9, +11.5, -8.7, -3.8, +58.0, +26.5 | 8.7% | 13.0% | 8.51 | Mar 11 PM |
| OMDA | 12.50 | 0.146 | -2.3, -7.1, +3.3, -9.6, +21.1, -20.4 (6) | 8.3% | 12.5% | 14.07 | Mar 4 PM |
| BRSL | 8.83 | ~0.00 | -9.5, +7.6, +0.4, +5.1, -9.6, +11.8, -4.2 | 7.6% | 11.4% | 9.84 | Feb 23 AM |
| EQX | 8.88 | 0.038 | -8.3, +15.2, +7.6, +8.5, 0.0, +4.1, -7.1 | 7.6% | 11.4% | 9.89 | Mar 11 PM |
| NUVB | 3.81 | 0.017 | +2.9, -0.4, -6.6, -25.3, +9.5, -4.1, -11.4 | 6.6% | 9.9% | 4.19 | Mar 1 PM |
| JANX | 10.29 | 0.004 | -3.1, +1.1, -7.6, -1.4, -2.5, -1.6, +9.8 | 2.5% | 3.8% | 10.68 | Feb 25 PM |
| CBIO | 12.91 | 0.224 | -1.4, +5.4, -1.2, +6.8, +1.7, -1.5 (6) | 1.6% | 2.4% | 13.22 | Feb 25 AM |

R1 here is on the last year of daily bars (high/low), a check only; the scanner value governs.

## (2) Apr16 books (closing quotes, 20:59 UTC)

| Contract | Bid / Ask | Spread % mid | OI | BE at ask | Needs | Max BE | Verdict |
|---|---|---|---|---|---|---|---|
| SOUN $2C | 1.00 / 1.16 | 15% | 176 | 3.16 | +8.6% | 3.25 | R6 pass, **R5 fail** (1.16 > 0.716), R7 fail (OI) |
| **SOUN $3C** | **0.53 / 0.59** | **11%** | **828** | **3.59** | **+23.4%** | 3.25 | R5 + R7 pass, **R6 fail** (needs 23.4% vs 11.7%) |
| SOUN $4C | 0.29 / 0.34 | 16% | 4,543 | 4.34 | +49.1% | 3.25 | R6 fail |
| WVE $2C | 0.05 / 1.80 | - | 0 | - | - | 2.95 | R7 (no market) |
| WVE $2.5C | 0.00 / 4.90 | - | 37 | - | - | 2.95 | R7 (no bid) |
| WVE $3C | 0.00 / 2.25 | - | 2 | - | - | 2.95 | R7 (no bid) |
| WVE $3.5C | 0.05 / 1.15 | - | 26 | - | - | 2.95 | R7 |
| AEVA $10C | 1.85 / 2.65 | 36% | 14 | 12.65 | +32.2% | 11.72 | R5, R6, R7 |
| AEVA $11C | 1.60 / 2.95 | 59% | 2 | 13.95 | +45.8% | 11.72 | R5, R6, R7 |
| AEVA $12.5C | 1.20 / 2.00 | 50% | 220 | 14.50 | +51.5% | 11.72 | R5, R6, R7 |
| RSI $11C | 1.90 / 2.25 | 17% | 38 | 13.25 | +15.5% | 13.19 | R5, R6 (by 6 cents), R7 (OI) |
| RSI $12.5C | 1.35 / 1.55 | 14% | 203 | 14.05 | +22.5% | 13.19 | R5, R6, R7 (OI) |
| RSI $14C | 0.75 / 1.15 | 42% | 45 | 15.15 | +32.1% | 13.19 | R5, R6, R7 |
| BBNX $12.5C | 2.85 / 5.50 | 63% | 4 | 18.00 | +35.1% | 15.38 | R5, R6, R7 |
| BBNX $15C | 1.80 / 4.70 | 89% | 1 | 19.70 | +47.9% | 15.38 | R5, R6, R7 |
| BBNX $17.5C | 0.25 / 4.40 | - | 8 | 21.90 | - | 15.38 | R5, R6, R7 |
| OMDA $12.5C | 1.70 / 3.90 | 79% | 0 | 16.40 | +31.2% | 14.07 | R5, R6, R7 |
| OMDA $15C | 0.65 / 2.70 | 122% | 2 | 17.70 | +41.6% | 14.07 | R5, R6, R7 |

IVs on these books: SOUN 76-84%, AEVA 98-113%, RSI 59-62%, BBNX 105-115%, OMDA 78-87%.

## Verdicts

- **Killed (13 moved, 10 killed):** SOUN (R6: the only R5/R7-clean strike, $3C at 0.59, needs +23.4% vs 11.7%), WVE (R7: no two-sided market at any strike near the money), DNN (R6: 1.3% median, 1.9% cap, structural), AEVA (R5 + R6 + R7), RSI (R5 + R6; the $11C misses R6 by 6 cents but costs 3x the R5 line), BBNX (R5 + R6 + R7), OMDA (R5 + R6 + R7), JANX (R6: 2.5% median, $0.39 of room on a $10 stock, no Apr16 strike carries that little time value), CBIO (R6: 1.6% median, $0.31 of room).
- **R6 table done, book not quoted, staged for Saturday:** CAPR (Jun17; room $0.98 on $7.53), BRSL (Apr16; room $1.01 on $8.83), EQX (Apr16; room $1.01 on $8.88), NUVB (Jun17; room $0.38 on $3.81). Honest expectation: all four die on the same math. NUVB almost certainly (its Apr/Jun time value has run $0.50+ at every check since October).

## The finding (adds to EVENING 2's, still not a rule change)

EVENING 2 said real money needs names with 15%+ median prints. Tonight tested that: AEVA has exactly a 15.0% median, and its cheapest-to-reach Apr16 strike still needs +32% against a 22.5% cap. The market prices big movers with big IV (AEVA ~100%), so the time value scales with the move. Big medians don't rescue spring contracts; they just raise both sides of the comparison. The contracts that come closest are the ones with **lower IV than the stock's print history justifies**: RSI's $11C (IV 62%, 10% median) missed R6 by six cents. That's the screen worth building: the ratio of median print move to the contract's time value as a fraction of price, best ratio first. For a $716 fund, the honest answer is still the one the queue already had: the real-money window reopens around Dec 15, when January prints come inside a Feb/Mar expiry and the contract carries 6-9 weeks of time value instead of 4-5 months.

## GLOSSARY

- **R1 (range percentile):** (price - 52-week low) / (52-week high - 52-week low). Under 0.25 = calls candidate.
- **R2:** the print is proven to land before expiry: expiry 21+ days after the later of the tool date and last year's date, and the filing deadline 5+ trading days before expiry.
- **R5:** one contract's ask x 100 must fit the conviction tier on reserve (3.5/5 = 10% = $0.716/share tonight).
- **R6:** the move to breakeven (strike + ask) must be no more than 1.5x the median earnings-day move over the last 4-8 prints.
- **R7:** the exact contract needs open interest >= 250 and a spread <= 25% of mid.
- **Median print move:** the middle value of the absolute earnings-day moves; sign ignored.
- **Max BE:** close x (1 + R6 cap). Any contract whose strike + ask sits above it fails R6.
- **Room:** max BE minus the stock price; the most time value (plus out-of-the-money distance) a contract can carry and still pass R6.
- **IV (implied volatility):** the yearly move the option price assumes. High IV = expensive time value.
- **Time value:** the part of an option's price above what it's worth if exercised now. Breakeven can never sit closer to the stock than this.
- **Staged:** dated R2 verdict and a listed expiry, waiting for its chain to be checked.
- **Interpolated bar:** a filler bar the data feed made up for a day it didn't have yet; it carries no real price.
