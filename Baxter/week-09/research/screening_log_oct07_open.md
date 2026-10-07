# SCREENING LOG: Wed Oct 7, 2026, 9:35am ET (VM OPEN)

**Source:** research_queue.md (COUR date gate, requotes of the 14 queue names), then a fresh scanner slice no run had touched yet: **prints Nov 10-20**, price $2-25, market cap $300M+, common stock, 52-week range percentile < 0.25 (same expression filter as the Oct 5 sweep). Prints that late mostly need Dec18 expiries. 133 matches, 77 already in this week's logs, **56 new**.

**Rule 5 line this run:** reserve = spendable $741.32 (unsettled $0.00). 3.5/5 line **$0.741**, 4/5 $1.00 (lock), screen $1.00.

**Quotes were pulled 9:35-9:37am, in the first two minutes of the session.** Option spreads were wider than last night's close on several names (COUR 0.30/0.75, TME 0.35/0.65). Next run requotes before anything is decided on them.

## Summary

| Step | Count | Tool |
|---|---|---|
| Queue gate (COUR date) | Oct 22 PM, still `verified: false` | get_earnings_results |
| Requotes + ratings (queue) | 14 names, no count or low-target changes | get_option_quotes, get_equity_quotes, get_equity_analyst_ratings |
| Scanner | 1 preview scan, 56 new names | preview_scan |
| R3 / R4 proxy | 56 names: 14 no coverage, 7 fail R3, 1 fails R4 proxy, 34 survive | get_equity_analyst_ratings |
| Dates + R1 + R6 history | 10 cheapest survivors (where R5 is reachable) | get_earnings_results, get_equity_historicals |
| Chains | 9 names (one had no listed options) | get_option_chains, get_option_instruments, get_option_quotes |
| Web | none | |
| Moved this run | **10** (OPEN batch line) | |
| Killed | **7: IMTX, MNSO, YMM, KC, BRBR, VNET, RERE** | |
| Advanced to chain-passed | **3: ONDS (at the ask), FUBO, FINV (at mid only)** | |

## Queue requotes (9:35am)

| Ticker | Stock | Contract | Bid / Ask | Live R6 math | Status |
|---|---|---|---|---|---|
| COUR | $5.135 | $5C Nov20 | 0.30 / 0.75 | (doc) | Oct 22 PM `verified: false`. Ask $0.75 > $0.741. **Both gates shut.** |
| QUBT | $7.61 | $8C Nov20 | 0.47 / 0.70 | cap 13.88%, max BE $8.67, **max price $0.67** | Ask now passes R5 ($0.70 <= $0.741) but fails R6 by $0.03; passes at mid ($0.585). Nov 13 PM unverified. |
| SERV | $4.625 | $5C Nov20 | 0.29 / 0.40 | cap 15.1%, max BE $5.32, max price $0.32 | **Fails R6 at mid and ask** with the stock down 3%. Floor goes stale Fri Oct 9. |
| GAU | $1.96 | $2C Nov20 | 0.10 / 0.25 | cap 12.19%, max BE $2.20, max price $0.20 | Fails R6 at the ask, passes at mid. Still blocked on R4 dating. |
| FRMI | $4.09 | $4C Nov20 | 0.55 / 0.70 | cap ~20.1%, max BE $4.91 | Now passes R5 and R6 at the ask. Still blocked on R4 dating. |
| OBDC | $9.84 (new 52w low) | $10C Nov20 | 0.35 / 0.50 | cap 4.28%, max BE $10.26, max price $0.26 | Fails R6 at mid and ask now. Still blocked on R4 dating. |
| TME | $7.86 | $8C Nov20 | 0.35 / 0.65 | | Spread wide at the open. Blocked (date, floor turns 60 days Oct 11). |
| BRSL | $10.105 | $11C Nov20 | 0.00 / 0.30 | | No bid. Blocked. |
| ADTN | $7.59 | $8C Nov20 | 0.25 / 0.95 | | Blocked, stale floor; R5 fails at the ask. |
| MLCO | $4.25 | $4C Nov20 | 0.10 / 0.70 | | Blocked, stale floor. |
| PCT | $3.8675 | $4C Nov20 | 0.45 / 0.60 | | Blocked, stale floor. |
| ENVX | $2.625 | $3C Nov20 | 0.20 / 0.27 | | Blocked, stale floor. |
| BXMT | $11.145 | $11C Nov20 | 0.55 / 0.90 | | Fails R5 at the ask. |
| CWH | $4.46 | $4C Nov20 | 0.60 / 1.00 | | Fails R5. |

Ratings on all 14: counts and low targets unchanged from PREMARKET.

## Fresh slice: free screen (56 new names)

- **No coverage (14):** BMNR, ASMB, MATW, SPH, SHOE, SOHU, TVA, MOVE, RTAC, CRML, BULL, CSHR, ASPI, ZKH.
- **R3 fail (7):** ODD (0/8/4), KLAR (10 Buy / 15 Hold), OCSL (0/6/0), XPEV (2 Sells), JKS (1/4/2), QFIN (2 Sells), WB (ratings block dated Aug 2022, 9/9/1; stale data, not a usable screen).
- **R4 proxy fail (1):** BV (low $10 under the $10.49 stock).
- **Survive (34):** CAE, BXSL, QURE, LINC, MLYS, FLY, SARO, ZTO, UTI, PPTA, LEGN, PHI, WYFI, BCAX, CTGO, HSAI, BZ, RGTI, JBIO, VIPS, GBDC, GRRR, CNL, MSIF, KC, MNSO, FUBO, YMM, BRBR, IMTX, ONDS, VNET, RERE, FINV. This run took the 10 cheapest (R5 is only reachable under ~$10); GBDC, GRRR, CNL, MSIF and the $12-25 names go to the queue.

## Fresh slice: dates, R6, chains (10 names)

R6 uses daily closes since Nov 2025; AM print = print-day close vs prior close, PM print = next-day close vs print-day close.

| Ticker | Stock | R1 | Print (tool) | Ratings / low | Last 4 prints | Median / cap / max BE | Contract | Bid / Ask | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **ONDS** | $7.14 | 0.21 | Nov 12 AM `verified: false` | 11/0/0, $13 | +19.1 / +8.4 / +26.5 / -8.8 | 13.93% / 20.89% / $8.63 | $8C Nov20 (9d6ece20-12bf-487e-a664-04b851d1665a) | 0.44 / 0.48, OI 10,604 | **CHAIN PASSED AT THE ASK.** BE $8.48, needs +18.8% (90% of cap). Max price $0.63. Floor needs dating. |
| **FUBO** | $8.795 | 0.02 | Nov 2 AM `verified: false` | 8/2/0, $12 | (+370.2) / -22.0 / -15.9 / +11.6 | 15.89% / 23.84% / $10.89 (3 clean prints) | $10C Nov20 (8f88e958-9d46-4d4d-9b0a-3145461ee638) | 0.55 / 0.79, OI 1,128 | **CHAIN PASSED AT MID ONLY** ($0.67, BE $10.67, 89% of cap). Ask $0.79 fails R5. The Nov 3 2025 +370% bar is almost certainly a data artifact (Hulu Live deal era); excluded, with it the median is 18.96%. |
| **FINV** | $2.95 | 0.03 | Nov 18 PM `verified: false` | 6/1/0, $4.11 | -13.9 / +12.6 / +11.1 / -15.4 | 13.23% / 19.85% / $3.54 | $2.5C Dec18 (550a4ddc-3740-4120-94ad-6e19b8923b2e) | 0.25 / 0.95, OI 380 | **CHAIN PASSED AT MID ONLY** ($0.60, BE $3.10, +5.1%). Ask fails R5. Spread is 70 cents wide on a 60-cent mid: liquidity flag. Only 2.5/5 strikes. |
| KC | $9.155 | 0.10 | Nov 18 AM `verified: false` | 17/0/0, $15.34 | -0.6 / +6.7 / +0.7 / +14.1 | 3.70% / 5.55% / $9.66 | Nov20 only, 2.5-wide strikes | | **KILLED, R6 + R5 strike grid:** $10C BE > $9.66; $7.5C intrinsic $1.66 > $0.741. No Dec chain. |
| MNSO | $8.86 | 0.02 | Nov 20 AM `verified: false` | 12/4/0, $10.80 | -0.1 / +5.5 / -4.2 / -4.4 | 4.33% / 6.49% / $9.49 | Dec18, 2.5-wide | | **KILLED, R6 + R5 strike grid:** $10C BE > $9.49; $7.5C intrinsic $1.36. |
| YMM | $8.325 | 0.13 | Nov 16 AM `verified: false` | 15/2/0, $9.04 | -11.9 / -1.6 / +4.3 / -1.1 | 2.95% / 4.42% / $8.81 | Dec18, 2.5-wide | | **KILLED, R6 + R5 strike grid:** $10C BE > $8.81; $7.5C intrinsic $0.83. |
| BRBR | $7.60 | 0.01 | Nov 17 AM `verified: false` | 10/5/1, $10 | +2.5 / -14.4 / -38.8 / -1.5 | 8.45% / 12.67% / $8.66 | $7.5C Dec18 | 1.00 / 1.55, OI 29 | **KILLED, R5:** bid alone over the line; $10C BE > $8.66. |
| VNET | $5.26 | 0.03 | Nov 19 AM `verified: false` | 14/1/0, $11.06 | -1.2 / -9.3 / +4.0 / -16.9 | 6.65% / 9.98% / $5.78 | $5C Dec18 | 0.55 / 1.30, OI 9,050 | **KILLED, R5 + R6:** mid $0.925 over the line and BE $5.93 > $5.78; $6C BE over max. |
| IMTX | $7.35 | 0.02 | Nov 16 AM `verified: false` | 10/0/0, $11.55 | -7.2 / -0.3 / -1.3 / -1.7 | 1.52% / 2.27% / $7.52 | | | **KILLED, R6** (free, no chain): a 2.3% cap leaves no strike. |
| RERE | $3.745 | 0.08 | Nov 19 AM `verified: false` | 6/0/0, $5.54 | +1.0 / -10.1 / +11.6 / -11.1 | 10.62% / 15.94% / $4.34 | none | | **KILLED: no listed options.** |

**ONDS and passes.md:** ONDS has sat on the passes.md Keep Watching list since Jun 1 with an Era 1 trigger ("pulls back to $4-5 AND Q3 setup AND the income-statement anomaly explained"). Live $7.14 doesn't hit it. It came back today on its own through the scanner under the current rules, which is the stronger signal. The anomaly question (TTM net income above revenue, likely non-cash warrant/acquisition accounting) is the first thing the doc has to answer.

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R1 (52w):** (price - 52-week low) / (52-week high - 52-week low); calls need <= 0.25.
- **R3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4 proxy:** the lowest analyst target must sit above the stock price before a chain is worth pulling; the real Rule 4 test is lowest Buy target vs breakeven, with a dated floor.
- **R5 line:** max ask per share for one contract at the conviction tier (10% of reserve / 100 at 3.5/5).
- **R6 cap:** 1.5x the median earnings-day move over the last 4 prints; the needed move to breakeven must fit under it.
- **Max BE:** stock price x (1 + R6 cap). **Max price:** max BE minus the strike.
- **Strike grid:** the spacing of listed strikes; a 2.5-wide grid often leaves no strike that fits.
- **Intrinsic:** how far a call is already in the money (stock minus strike).
- **Passes at mid:** fits R5/R6 only if it fills at the bid/ask midpoint, not at the ask.
- **Stale floor:** a price target set before the decline or more than 60 days ago; it doesn't count for Rule 4 (binder Tab 6).
- **verified: false:** the earnings date is estimated from the company's cadence, not announced.
- **Data artifact:** a price bar that can't be real (FUBO +370% in a day); excluded from the median and named, not silently dropped.
- **BE:** breakeven, strike + premium. **OI:** open interest. **AM / PM print:** earnings before the open / after the close.
