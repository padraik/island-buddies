# Screening log: Wed Oct 14, EVENING 3 (10:00pm ET)

*EVENING session 3 of 3. Job: refill the queue and leave PREMARKET a plan. Market closed; quotes are the 4:00pm close. Reserve $676.28 (3.5/5 line $0.676). Free tools only, no web searches.*

## Sourcing

Saved scan `4bc59b84-cc60-4619-870c-359c2daae902`, re-pointed and renamed `Baxter Oct14 E3 refill` (new configuration versions; the EVENING 2 version is preserved). Same filters as EVENING 2 (market cap $300M+, 52-week range pct < 0.25) with two new windows, the two bands nobody had touched:

| Band | Print window | Rows | Already screened | New |
|---|---|---|---|---|
| Last >= $110 | Nov 21 - Dec 18 | 9 | BURL (paper book), AVAV (killed R6 tonight) | AZO, AGX, FERG*, DKS*, TOL, ORCL, RH |
| Last >= $25 | Dec 19 - Jan 31 | 7 | RPM, CALM, FUL, MKC, SHAZ (all screened Oct 13) | FBK |

*FERG and DKS were screened earlier this month (FERG killed R7, DKS killed R3); tonight's ratings call re-confirmed both.

With these two bands, every price band and every print window from Oct 20 to Jan 31 has been scanned this week. The bottom-quartile pool is fished out until prices move.

## Ratings screen (one call, 13 symbols)

| Ticker | Last | Range | Print (scanner) | B/H/S | Low target | Result |
|---|---|---|---|---|---|---|
| AZO | 2,911.62 | 0.127 | Dec 8 AM (f), LY Dec 9 AM | 27/5/0 | $3,000 | pass, to chain |
| AGX | 362.00 | 0.190 | Dec 4 | 4/2/1 | $273 | **KILLED, R4 proxy** (low under the stock; same as Oct 13) |
| FERG | 222.94 | 0.179 | Nov 30 | 14/9/0 | $235 (stamp Aug 12) | already **KILLED R7** (Dec18 OI 7-23), not re-pulled |
| DKS | 135.60 | 0.124 | Nov 25 | 16/13/2 | $99 | **KILLED, R3** (2 Sells) |
| TOL | 131.63 | 0.188 | Dec 8 | 17/5/1 | $118 | **KILLED, R4 proxy** (low $118 under the $131.63 stock) |
| ORCL | 128.56 | 0.068 | Dec 10 | 36/8/1 | $110 | **KILLED, R4 proxy** (low $110 under the stock) |
| RH | 110.85 | 0.034 | Dec 11 | 7/12/2 | $81 | **KILLED, R3** (2 Sells, Holds > Buys) |
| RPM | 97.90 | 0.173 | Jan 8 | 18/2/0 | $107 | already **KILLED R7** Oct 13 (Feb19 OI 71-110) |
| CALM | 63.19 | 0.039 | Jan 7 | none | | already **KILLED R3** (no coverage) |
| FBK | 50.38 | 0.070 | Jan 20 PM (f), LY Jan 21 PM | 8/0/0 | $61 | pass, to chain |
| FUL | 50.09 | 0.155 | Jan 14 | 8/0/0 | $62 | already **KILLED R7** Oct 13 (Feb19 OI 0-6) |
| MKC | 45.16 | 0.066 | Jan 22 | 8/8/1 | $47 | Oct 13: Mar19 $40C passed R4 by 1.1%, failed R7 on OI 231. **Back on the queue** (OI is daily) |
| SHAZ | 30.00 | 0.166 | Dec 31 | 8/0/0 | $80 | already **KILLED R6** (2 reported prints ever) |

## Chain stage (AZO, FBK)

**AZO** (`get_earnings_results`: Q1 FY27 Dec 8 AM `verified: false`, LY Dec 9 AM; Q4 already reported Sep 22). Rule 2: Dec 9 + 21 = Dec 30, so Jan15 (no expiry between Dec 18 and Jan 15). 10-Q for the ~Nov 22 quarter due ~Jan 1, more than 5 trading days before Jan 15: pass.
- Print reactions (last 6, AM prints, close vs prior close): -3.42, -0.02, -7.17, -6.32, -8.99, +3.26. Median 4.87%, **R6 cap 7.30%**.
- Jan15 $2900C 200.20 / 232.90, OI 7, BE $3,132.90 = **+7.60%** off $2,911.62. $2950C 175.50 / 208.00, OI 2, BE $3,158 (+8.5%). $3000C 152.90 / 185.80, OI 13, BE $3,185.80 (+9.4%).
- **KILLED, R6 + R7.** The best strike misses R6 by 0.3 points, and no strike has OI over 13. Spreads are 14-19% of mid, so R7 dies on OI alone.

**FBK** (Q3 reported Oct 13, `actual` 1.21; Q4 Jan 20 PM `verified: false`, LY Jan 21 PM). Rule 2: Jan 21 + 21 = Feb 11; the chain lists Jan15 then Apr16, so Apr16.
- Print reactions (last 6): -4.57, +4.07, -1.41, -2.30, +3.23, -4.21. Median 3.65%, **R6 cap 5.48%**.
- Apr16 $50C 2.90 / 5.90, OI 0, BE $55.90 = **+11.0%**. $55C 0.75 / 3.80, OI 1, BE $58.80 (+16.7%).
- **KILLED, R6 + R7.** A bank that moves 3.65% on earnings can't carry an 11% breakeven, and nobody holds the contracts.

## Result

**Moved: 13** (2 to the chain, 11 settled at the ratings screen or by prior kills). **Killed: 13** (AZO, FBK on R6 + R7; AGX, TOL, ORCL R4 proxy; DKS, RH R3; FERG, RPM, FUL R7, CALM R3, SHAZ R6 re-confirmed). **Advanced: 0.** MKC re-queued on its daily OI.

**Pattern:** the far bands are large, slow companies (AZO, ORCL, TOL, banks). They're well covered and liquid in the stock, but their earnings moves are small (3-5%) and their option chains are thin far out. Rule 6 and Rule 7 together are a wall for anything reporting more than ~6 weeks out.

## GLOSSARY

- **R1-R7:** the Iron Rules in binder Tab 1 (range, earnings before expiry, rating consensus, bear floor, chain affordability, reachability, liquidity).
- **Range pct:** where the price sits in the 52-week range; 0 = at the low, 1 = at the high. Calls need <= 0.25.
- **R4 proxy:** at the screen, the lowest analyst target must at least clear the stock price; if it doesn't, no call breakeven can pass Rule 4.
- **R6 cap:** 1.5x the median absolute one-day move on the last 4-8 earnings prints. Breakeven has to be within that distance of the stock.
- **OI (open interest):** number of contracts outstanding. Rule 7 needs >= 250.
- **(f) / verified: false:** the earnings date is estimated from the company's pattern, not announced.
- **LY:** last year's same-quarter report date.
- **BE (breakeven):** strike + premium paid.
