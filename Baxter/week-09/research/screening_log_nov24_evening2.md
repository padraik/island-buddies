# Screening log: Tue Nov 24, EVENING 2 (8:00pm ET)

**Job:** EVENING 2 writes docs for names past the chain stage. None exist (TAL went to Stopped Watching at EVENING 1), so per the queue this session started EVENING 3's job: the April re-sweep, then queue item 2 (bands C/D parks, median-first). Nothing held. R5 line: 10% x $715.96 / 100 = **$0.716/share** (3.5/5).

**Source:** Robinhood tools, run ~01:00-01:30 UTC Nov 25 on Tuesday's close. 0 web searches.

## 1. Re-sweep, prints Apr 1 - Apr 30 2027, bands A + B ($1-25)

| Scan | ID | Filters | Rows |
|---|---|---|---|
| Bands A+B, Apr prints | `42772e1a-5c4a-439e-b539-b615b3fd611c` | cap $300M+, stock, Last $1-25, R1 < 0.25, earnings Apr 1-30 2027 | 16 |

**Why only 16:** the scanner's earnings field is each company's *next* print. For almost every company that's the Q4 report (Jan-Mar), so an April window only catches odd fiscal years and closed-end funds. Calendar Q1 prints (late April) won't show in the scanner until the Q4 prints have happened in Feb/Mar. **The April window can't be swept from here yet.** Bands A/B for Jan 15 - Mar 31 were already fished out (Nov 20, Nov 23).

Dropped as closed-end funds (9): NPFD, ECAT, MUJ, MHD, MUC, MYN, JFR, JPC, JQC.

| Ticker | Last | Pct | B/H/S | Low target | Verdict |
|---|---|---|---|---|---|
| SFD | 18.93 | 0.09 | 5/3/0 | 20.00 | park -> median (below) |
| FRPH | 18.23 | 0.11 | none | -- | **KILLED R3** (no coverage) |
| ADSE | 9.70 | 0.24 | none | -- | **KILLED R3** (no coverage) |
| JKS | 7.195 | 0.01 | 3/2/2 | 5.27 | **KILLED R3 + R4** (2 Sells; low under Last) |
| INFQ | 6.37 | 0.01 | 6/1/0 | 12.00 | **PARKED: only 2 prints on record** (Aug 12 PM -1.5%, Nov 16 PM -4.6%) |
| PSNY | 2.70 | 0.01 | none | -- | **KILLED R3** (no coverage) |
| EVO | 1.38 | 0.02 | 3/6/0 | 1.68 | **KILLED R3** (Holds > Buys; stamp Oct 2025) |

**SFD:** the scanner says Apr 27, but `get_earnings_results` has Q4 on **Mar 23 2027 AM (f)** (LY Mar 24), so the scanner date is wrong. Last 7 prints (AM, prior close to print day): +8.8 / -2.6 / +4.8 / +4.3 / -6.4 / -2.3 / +0.1. Median **4.3%**. **KILLED R6 structural.**

## 2. Queue item 2: band C parks, median-first (paper size)

Picked the 9 band C parks most likely to have big prints (semis, biotech, telecom equipment). Moves from daily closes, last 6 prints (PM = print day to next day; AM = prior close to print day).

| Ticker | Next print (f) | Moves | Median | Verdict |
|---|---|---|---|---|
| VKTX | Feb 10 PM | +8.0 / +6.8 / -0.5 / -1.0 / +5.9 / +0.3 | 3.45% | **KILLED R6 structural** |
| ALGM | Jan 28 AM | -7.3 / -1.5 / +9.9 / -6.7 / -1.8 / -6.6 | 6.65% | **KILLED R6 structural** |
| ICHR | Feb 8 PM | -30.2 / -31.4 / +32.7 / -2.8 / -11.2 / -0.8 | **20.7%** | to the chain |
| PDFS | Feb 11 PM | -11.0 / -3.8 / +4.9 / +8.2 / +7.7 / +9.0 | 7.95% | **KILLED R6 structural** (closest) |
| CALX | Jan 27 PM | +3.1 / +9.3 / -11.9 / -14.0 / -2.3 / -8.0 | **8.65%** | to the chain |
| AMKR | Feb 8 PM | +18.1 / -3.1 / +1.8 / -5.6 / -24.7 / +8.5 | 7.05% | **KILLED R6 structural** |
| CRSP | Feb 11 PM | -6.7 / -1.0 / +8.5 / -2.2 / +7.1 / -2.8 | 4.75% | **KILLED R6 structural** |
| ARWR | Feb 4 PM | +2.2 / +23.3 / -0.2 / -6.7 / -3.0 / +1.3 | 2.6% | **KILLED R6 structural** |
| POWI | Feb 4 PM | -9.2 / +1.6 / +0.3 / +2.0 / -4.8 / -17.0 | 3.4% | **KILLED R6 structural** |

### CALX chain (Apr16; the chain lists no Mar19)

Stock $34.66. Cap 1.5 x 8.65% = 13.0%.
| Strike | Bid / Ask | OI | IV | BE at ask | Needs | Verdict |
|---|---|---|---|---|---|---|
| $35C | 3.50 / 5.70 | 0 | 49% | 40.70 | +17.4% (+14.3% at mid) | R6, R7 |
| $37.5C | 2.65 / 4.70 | 1 | 51% | 42.20 | +21.8% | R6, R7 |
| $40C | 1.35 / 3.80 | 11 | 48% | 43.80 | +26.4% | R6, R7 |

**CALX KILLED R6 + R7.**

### ICHR chain (May21; Feb19 fails R2: LY Feb 9 + 21 = Mar 2. Chain lists Dec18 / Jan15 / Feb19 / May21 only)

Stock $31.60. Cap 1.5 x 20.7% = 31.1%. Ratings 7/1/0, **low $37**, no `updated_at` stamp.
| Strike | Bid / Ask | OI | IV | BE at ask | Needs | R4 (BE < $37) | Verdict |
|---|---|---|---|---|---|---|---|
| $30C | 4.60 / 7.10 | 93 | 95% | 37.10 | +17.4% | fails by 10c (passes at mid, $35.85) | R4 at ask; R7 (spread 43%, OI 93) |
| $32.5C | 4.00 / 6.10 | 10 | 94% | 38.60 | +22.2% | fails | R4, R7 |
| $35C | 4.00 / 4.50 | 36 | 91% | 39.50 | +25.0% | fails | R4, R7 (OI) |
| $40C | 1.75 / 5.40 | 29 | 96% | 45.40 | +43.7% | fails | R4, R6, R7 |

**ICHR KILLED R4 + R7.** It's the first R6 pass at the ask since TAL, and the fund's own lesson cuts the other way: a 20.7% median with three 30% prints in six quarters means the floor ($37, unstamped, only +17% over the stock) is closer than the move. Nothing here works even on paper.

## Tally

25 names moved: 16 April re-sweep (9 funds dropped, 4 R3, SFD R6, INFQ parked on print count), 9 band C parks (7 R6 structural, CALX R6 + R7, ICHR R4 + R7). 0 advanced, 0 docs, 0 buyable, 0 searches.

**The finding:** real-money candidates for bands A/B have no new print window left to sweep until the Q4 dates pass in Feb/Mar and the scanner rolls forward. Until then the remaining supply is (a) band C/D parks for the paper book, (b) names whose R1 percentile changes (new lows), and (c) re-quotes on Keep Watching (COUR, NIO). A re-run of the Jan 15 - Mar 31 A/B scans every week or so catches new bottom-quartile entrants.

## GLOSSARY

- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 ratings mix, R4 bear floor, R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Park:** passed R3 and the R4 proxy; waits for the next check.
- **R6 structural:** the median print move is too small (under ~8%) for any spring contract's time value to fit inside 1.5x of it.
- **(f):** earnings date estimated from cadence (`verified: false`).
- **LY:** last year's same-quarter report date.
- **Closed-end fund:** an exchange-traded fund with a fixed share count; no earnings catalyst in our sense, dropped from the screen.
- **BE:** breakeven, strike + premium.
- **IV:** implied volatility.
- **Stamp:** the ratings record's `updated_at`; used to date the floor (binder Tab 6, 60-day rule).
