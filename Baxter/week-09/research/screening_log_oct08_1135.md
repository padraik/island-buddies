# Screening log, Thu Oct 8, 2026, MIDDAY (11:35am ET, VM)

Reserve $741.32 settled. Rule 5 lines: 3.5/5 $0.741, 4/5 $1.00 (transitional lock), screen $1.00.

First run under the clarified Rule 2 (binder Tab 1, ratified on the Oct 8 ~11:15am call): pass when the expiry is at least 21 days after the latest of (1) the tool date, (2) last year's same-quarter date, (3) the 10-Q deadline (Sep 30 quarter: Nov 9 for accelerated filers, Nov 14 for others). 6-K filers: (1) and (2) only.

## 1. Rule 2 under the new text, every doc name

| Name | Tool date (verified?) | Last year | 10-Q deadline | Latest + 21 | Contract expiry | Rule 2 |
|---|---|---|---|---|---|---|
| COUR | Oct 22 PM (false) | Oct 23, 2025 PM | Nov 9 / Nov 14 | Nov 30 / Dec 5 | Nov 20 | **FAIL on leg (3)**: Nov20 is 11 days past Nov 9. Next listed expiry Jan15 (no Dec). |
| ONDS | Nov 12 AM (false) | Nov 13, 2025 AM | Nov 9 / Nov 14 | Dec 4 / Dec 5 | Nov20 / Dec18 | Nov20 FAIL, Dec18 PASS |
| QUBT | Nov 13 PM (false) | Nov 14, 2025 PM | Nov 9 / Nov 14 | Dec 5 | Nov20 / Dec18 | Nov20 FAIL, Dec18 PASS |
| WRD (6-K) | Nov 23 AM (false) | Nov 24, 2025 AM | n/a | Dec 15 | Jan15 | PASS |
| TDUP | **Nov 4 PM (TRUE, changed: was Nov 2 PM unverified)** | Nov 3, 2025 PM | Nov 9 / Nov 14 | Dec 5 | Nov20 | Company-announced date 16 days before expiry: passes the original reading (a confirmed date before expiry). Fails leg (3) of the new test if that test is read as the only path. Question to Michael. |
| UTI | Nov 18 PM (false) | Nov 19, 2025 PM | Sep 30 FY end: 10-K, n/a here | Dec 10 | Nov20 / Dec18 | Nov20 FAIL, Dec18 PASS |

**The COUR finding.** On the call the expectation was "COUR is buyable from 11:35 on." The ratified text includes the 10-Q deadline, and for any US filer with a Sep 30 quarter that pushes the minimum expiry to Nov 30 or later. COUR's Nov20 doesn't make it. I'm reading the rule as written (the stricter reading) and asking Michael whether leg (3) was meant to bind when the tool and last-year dates are both a month early. A company announcement still clears it: a confirmed date before expiry was always a pass, and the call didn't take that away (it removed `verified: true` as a *requirement*).

## 2. Requotes, ~11:36am

| Name | Stock | Contract | Bid / Ask | Max price | Verdict |
|---|---|---|---|---|---|
| COUR | $5.10 (-0.2%) | $5C Nov20 | 0.55 / 0.75 | $0.741 (R5) | R2 fail (above). Ask still a cent over the line. |
| COUR | $5.10 | $5C Jan15 | 0.65 / 0.95, OI 1,249 | $0.741 (R5) | **R5 FAIL** at the ask (mid 0.80 also over). |
| COUR | $5.10 | $6C Jan15 | 0.30 / 0.60, OI 825 | n/a | **R4 FAIL** (BE $6.45-6.60 vs $6.00 low) and **R6 FAIL** (+26-29% vs cap 19.9%). |
| ONDS | $6.90 (-4.0%) | $8C Dec18 | 0.54 / 0.56 | 6.90 x 1.2089 - 8 = $0.341 | **R6 FAIL**. |
| QUBT | $7.355 (-3.5%) | $8C Dec18 | 0.60 / 0.68 | 7.355 x 1.1388 - 8 = $0.376 | **R6 FAIL**. |
| WRD | $4.55 (-8.3%) | $5C Jan15 | (not requoted) | 4.55 x 1.1397 - 5 = $0.186 | R6 fail, still sliding. |
| BRSL | $9.795 | $11C Nov20 | (not requoted) | 9.795 x 1.1101 - 11 = -$0.13 | Fails. |
| UTI | $20.11 | $22.5C Nov20 | 0.85 / 1.00 | | R5 fail, R2 fail. |
| UTI | $20.11 | $22.5C Dec18 | 1.25 / 1.45, OI 70 | | **R5 FAIL**. |
| UTI | $20.11 | $25C Dec18 | 0.65 / 0.85, OI 71 | | **R5 FAIL** at the ask; BE $25.85 needs +28.5% vs cap 28.2%, R6 fail too. UTI watch closed. |
| TDUP | $2.225 | $2.5C Nov20 | 0.15 / 0.25, OI 17 | 2.225 x 1.285 - 2.5 = $0.359 | Passes R5/R6 at the ask. Floor-blocked (below). |

## 3. TDUP floor (one search)

`get_equity_analyst_ratings`: 6/1/0, low $5.70. One WebSearch ("ThredUp TDUP price target analyst October 2026"): nothing newer than Telsey Outperform $7 -> $6 (Aug 2026). Prior MarketBeat read: Roth Buy $6.50 and Telsey $6 on Aug 6, TD Cowen $5.70 May 5. Aug 6 is now 63 days old, past Tab 6's 60-day line. **Still floor-blocked.** Watch for Q3 previews in the last two weeks of October; a fresh Buy target before Nov 4 unblocks it.

## 4. Ratings (all 9 checked names, ~11:36am)

Unchanged: COUR 8/4/0 low $6, ONDS 11/0/0 low $13, QUBT 5/2/0 low $10, WRD 13/0/0 low $10.51, BRSL 7/3/0 low $11.90, TME 22/14/0 low $9.05 (updated Aug 12), UTI 6/1/0 low $25, TDUP 6/1/0 low $5.70, SERV 6/2/0 low $7.

## 5. Tally

10 names moved: COUR, ONDS, QUBT, WRD, TDUP, UTI through the new Rule 2 test; COUR Jan15 x2, ONDS Dec18, QUBT Dec18, UTI Dec18 x2 chain-checked; TDUP floor search. Kills this run: UTI (watch closed: R5 at every reachable strike, R2 at Nov20). No new name passes everything. Every "loaded doc" now needs either a company date announcement (COUR, TDUP's floor) or a stock move back up (ONDS, QUBT Dec18 on R6).

## GLOSSARY

- **R1 / Rule 1:** stock in the bottom 20-25% of its 52-week range.
- **R2 / Rule 2 (Oct 8 text):** expiry at least 21 days after the latest of the tool's date, last year's same-quarter date, and the SEC 10-Q filing deadline. `verified: true` = the company announced the date itself.
- **10-Q deadline:** the latest a US company can file its quarterly report: 40 days after quarter end for larger filers, 45 for smaller ones.
- **6-K filer:** a foreign company (often an ADR) that files 6-Ks instead of 10-Qs, so it has no 10-Q deadline.
- **R3 / Rule 3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds (Buy/Hold/Sell counts like 8/4/0).
- **R4:** lowest Buy target above breakeven, dated within 60 days and set after the decline (Tab 6).
- **R5 / Rule 5:** one contract's ask must fit the conviction tier's budget; $0.741 per share for 3.5/5 at this reserve.
- **R6 / Rule 6:** the move to breakeven must be no more than 1.5x the stock's median earnings-day move.
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike.
- **Max price (doc formula):** the highest ask at which a doc's contract still passes R6 at the current stock price.
