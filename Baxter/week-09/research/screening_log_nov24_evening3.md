# Screening log: Tue Nov 24, EVENING 3 (10:00pm ET)

**Job:** queue item 1 (re-run the Jan 15 - Mar 31 bands A/B scans, diff for never-worked bottom-quartile names), then queue item 2 (band C parks, median-first, higher-beta first). Nothing held. R5 line: 10% x $715.96 / 100 = **$0.716/share** (3.5/5).

**Source:** Robinhood tools, run ~03:00-03:30 UTC Nov 25 on Tuesday's close. 0 web searches.

## 1. Re-run of the Jan 15 - Mar 31 A/B scans

| Scan | ID | Window | Rows then | Rows now |
|---|---|---|---|---|
| Band A $1-8.19 | `b7b61d9f-7278-4bbb-92bd-c096eddf2ee3` | Jan 15 - Feb 12 | 66 (Nov 20) | 60 |
| Band B $8.19-25 | `770b42be-6b18-4508-974c-6c2e135e1703` | Jan 15 - Feb 12 | 110 (Nov 20) | 100 |
| Band A $1-8.19 | `01ce0035-28a6-49c0-aed8-0ee1b83da395` | Feb 13 - Mar 20 | (Nov 13) | 162 |
| Band B $8.19-25 | `fccfd39a-e704-451e-8e48-72719f90258a` | Feb 13 - Mar 20 | 158 (Nov 14) | 196 |
| Bands A+B $1-25 | `a7226397-cbb5-4ff4-b12d-01f39cd0455a` | Mar 21 - Mar 31 | (Nov 23) | 42 |

560 rows diffed against every `screening_log_*` file in week-09 and passes.md (whole-word match). **10 never-worked names** (single-letter and common-word tickers can hide in the grep; none of those are new entrants worth chasing).

| Ticker | Name | Last | Next print (scanner) | B/H/S | Low target | Verdict |
|---|---|---|---|---|---|---|
| FHN | First Horizon | 22.22 | Jan 15 | 9/14/0 | 25.00 | **KILLED R3** (Holds > Buys) |
| TFSL | TFS Financial | 14.65 | Jan 29 | none | -- | **KILLED R3** (no coverage) |
| MRTN | Marten Transport | 11.44 | Jan 27 | none | -- | **KILLED R3** (no coverage) |
| EVMN | Evommune | 7.95 | Mar 5 | 9/3/0 | 8.00 | **KILLED R4 proxy** (low $8.00 is 0.6% over the stock; no call clears it) |
| DNA | Ginkgo Bioworks | 7.51 | Feb 26 | none | -- | **KILLED R3** (no coverage) |
| ENIC | Enel Chile ADR | 3.94 | Feb 26 | 2/6/0 | 4.23 | **KILLED R3** |
| AAPG | Ascentage Pharma | 12.45 | Mar 25 | 10/0/0 | 33.00 | passed R3/R4 proxy; **KILLED: no listed options** (`get_option_chains` empty). Semiannual reporter anyway. |
| NMAX | Newsmax | 6.62 | Mar 26 | none | -- | **KILLED R3** (no coverage) |
| CDLR | Cadeler | 5.76 | Mar 23 | none | -- | **KILLED R3** (no coverage) |
| ISD | PGIM High Yield Bond Fund | 11.26 | Mar 26 | none | -- | dropped (closed-end fund) |

**Side note, not a reopen:** the band B scan shows TAL at $9.90 with a scanner percentile of 0.235. The scanner uses weekly intraday highs/lows; the TAL doc's R1 line ($9.93) is on the closing range. TAL was moved to Stopped Watching at EVENING 1 under its own stop trigger, and R7 (OI 189) and R5 (ask ~0.85 vs $0.716) block it regardless.

## 2. Queue item 2: band C parks, median-first (paper size)

Moves from daily closes, last 6 prints (PM = print day to next day; AM = prior close to print day). Bars through Nov 23.

| Ticker | Next print (f) | Moves | Median | Verdict |
|---|---|---|---|---|
| FORM | Feb 3 PM | -17.5 / +24.2 / +17.2 / +0.3 / +26.3 / -11.6 | **17.35%** | to the chain |
| RMBS | Feb 1 PM | +13.9 / -8.7 / -13.4 / -21.3 / -9.0 / -1.6 | **11.2%** | to the chain |
| LEU | Feb 9 PM | +8.7 / -14.7 / -20.7 / +12.3 / -5.1 / -3.8 | **10.5%** | to the chain |
| NXT | Jan 26 PM | -9.3 / +8.7 / +13.3 / +8.8 / -7.3 / -2.7 | **8.75%** | to the chain |
| MRCY | Feb 2 PM | +27.0 / +3.3 / -22.3 / +10.5 / -3.6 / +5.7 | **8.1%** | to the chain |
| SNDK | Jan 28 PM | -4.6 / +15.3 / +6.9 / +8.3 / -6.8 / -13.5 | 7.6% | **KILLED R6 structural** |
| GFS | Feb 10 AM | -9.3 / -1.8 / +16.3 / +9.3 / -4.9 / -5.9 | 7.6% | **KILLED R6 structural** |
| HOOD | Feb 9 PM | -2.9 / -10.8 / -8.9 / -13.2 / -3.6 / -3.3 | 6.25% | **KILLED R6 structural** |
| MCHP | Feb 4 PM | -6.6 / -5.2 / -2.6 / -2.5 / +13.9 / -10.0 | 5.9% | **KILLED R6 structural** |
| B | Feb 4 AM | -2.5 / +5.2 / -7.2 / +9.0 / -6.4 / +4.2 | 5.8% | **KILLED R6 structural** |
| AA | Jan 21 PM | +2.9 / +12.6 / -1.5 / -6.8 / -6.1 / +2.5 | 4.5% | **KILLED R6 structural** |
| TTMI | Feb 3 PM | -3.0 / -2.4 / -3.8 / +15.1 / +3.9 / -27.7 | 3.85% | **KILLED R6 structural** |
| ALB | Feb 10 PM | -1.5 / -0.8 / -9.4 / +3.0 / +5.5 / +3.6 | 3.3% | **KILLED R6 structural** |
| FCX | Jan 21 AM | -2.1 / +1.1 / -2.9 / -12.6 / -2.3 / +1.2 | 2.2% | **KILLED R6 structural** |
| ON | Feb 8 PM | -15.6 / +0.8 / +3.5 / +0.6 / +0.5 / +3.6 | 2.15% | **KILLED R6 structural** |

### Ratings on the five chain names (R3 + R4 floor)

| Ticker | Close Nov 24 | B/H/S | Low target | Stamp | R3 | Floor vs stock |
|---|---|---|---|---|---|---|
| FORM | 73.30 (-10.2% on the day) | 9/3/0 | 102 | none | pass | +39% |
| RMBS | 68.76 (-9.1%) | 8/3/0 | 91 | none | pass | +32% |
| LEU | 84.04 | 15/7/0 | 100 | none | pass | +19% |
| NXT | 65.76 | 27/4/0 | 89 | Nov 19 | pass | +35% |
| MRCY | 72.17 | 12/2/1 | 83 | none | pass (1 Sell) | +15% |

Expiry picked by R2 (later of tool date / last year's date, plus 21 days): FORM Apr16 (Mar19 not listed; Jan15 fails), RMBS **May21** (Feb19 fails: LY Feb 2 + 21 = Feb 23), LEU Apr16 (Mar19 not listed), NXT Feb19 (LY Jan 27 + 21 = Feb 17), MRCY Mar19.

### Chains (live quotes from Tuesday's close; needs = BE at the ask vs the close)

| Contract | Bid / Ask | OI | IV | BE at ask | Needs | Cap (1.5 x median) | Verdict |
|---|---|---|---|---|---|---|---|
| FORM $70C Apr16 | 16.20 / 18.90 | 6 | 87% | 88.90 | +21.3% | 26.0% | R6 **passes**; R4 passes (BE < $102); **R7 fails (OI 6)** |
| FORM $75C Apr16 | 13.70 / 16.70 | 15 | 85% | 91.70 | +25.1% | 26.0% | R6 passes (thin); **R7 fails (OI 15)** |
| FORM $80C Apr16 | 11.80 / 14.90 | 22 | 85% | 94.90 | +29.5% | 26.0% | R6, R7 |
| RMBS $65C May21 | 14.90 / 18.00 | 0 | 75% | 83.00 | +20.7% | 16.8% | R6, R7 |
| RMBS $70C May21 | 12.60 / 16.20 | 9 | 76% | 86.20 | +25.4% | 16.8% | R6, R7 |
| RMBS $75C May21 | 10.60 / 14.40 | 1 | 75% | 89.40 | +30.0% | 16.8% | R6, R7 |
| LEU $80C Apr16 | 20.00 / 23.80 | 3 | 95% | 103.80 | +23.5% | 15.75% | R6, R7 |
| LEU $85C Apr16 | 17.80 / 20.00 | 2 | 90% | 105.00 | +24.9% | 15.75% | R6, R7 |
| LEU $90C Apr16 | 16.00 / 18.00 | 178 | 90% | 108.00 | +28.5% | 15.75% | R6, R7 |
| NXT $65C Feb19 | 9.70 / 11.00 | 50 | 76% | 76.00 | +15.6% (+14.6% at mid) | 13.1% | R6, R7 |
| NXT $70C Feb19 | 7.60 / 9.60 | 10 | 79% | 79.60 | +21.0% | 13.1% | R6, R7 |
| NXT $75C Feb19 | 5.80 / 7.20 | 23 | 75% | 82.20 | +25.0% | 13.1% | R6, R7 |
| MRCY $70C Mar19 | 9.00 / 13.00 | 2 | 60% | 83.00 | +15.0% | 12.15% | R6, R7 (spread 36%) |
| MRCY $75C Mar19 | 6.60 / 10.80 | 2 | 59% | 85.80 | +18.9% | 12.15% | R6, R7 |
| MRCY $80C Mar19 | 4.80 / 8.90 | 6 | 59% | 88.90 | +23.2% | 12.15% | R6, R7 |

**FORM KILLED R7** (paper book applies R7 too). It's the cleanest R6 pass on the board this week: a 17% median, a $102 floor 39% over a stock that just fell 10% in a day, and the $70C needs 21% against a 26% cap. The Apr16 strikes just don't trade (OI 6-22). Worth one re-quote after the holiday in case OI builds on the selloff; it goes on the queue as a re-check, not a park.
**RMBS, LEU, NXT, MRCY KILLED R6** at the ask (and R7 everywhere). The longer R2-forced expiries (May21 for RMBS, Apr16 for LEU) load too much time value onto 10-11% medians.

## Tally

25 names moved: 10 never-worked from the A/B re-run (8 R3/fund, EVMN R4 proxy, AAPG no options), 15 band C parks (10 R6 structural, 5 to the chain: FORM R7, RMBS / LEU / NXT / MRCY R6). 0 advanced, 0 docs, 0 buyable, 0 searches.

**The finding:** the Jan 15 - Mar 31 A/B universe gained only 10 never-worked names since Nov 20-23, and none survived. Real-money supply is dry until the Q4 prints pass. Band C has real R6 candidates (FORM) but no liquidity at the expiries R2 forces.

## GLOSSARY

- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 ratings mix, R4 bear floor, R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Park:** passed R3 and the R4 proxy; waits for the next check.
- **R4 proxy:** lowest analyst target vs the stock price, before any chain is pulled. If the low target is barely above the stock, no call's breakeven can clear it.
- **R6 structural:** the median move is so small that even a contract with almost no time value couldn't pass R6.
- **Median move:** the middle of the last 6 absolute one-day stock moves on earnings.
- **BE (breakeven):** strike + premium paid. The stock has to be above this at expiry for the call to make money.
- **OI (open interest):** contracts outstanding. Low OI means a thin market and a wide spread to get out.
- **IV (implied volatility):** the move the option market is pricing in, annualized.
- **(f):** the earnings date is the tool's estimate (`verified: false`), not company-announced.
- **Band A/B/C/D:** price bands for the scanner ($1-8.19 / $8.19-25 / $25-100 / $100+). A/B are real-money size; C/D are paper-book size.
