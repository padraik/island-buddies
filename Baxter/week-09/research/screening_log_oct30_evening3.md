# Screening log: Fri Oct 30, EVENING 3 (10:00pm ET)

**Source:** the queue's carried chain jobs (GLXY, DX, NLY), slide-ins B and WGS, then a refill: slide-in scan `696cbe51` (28 rows), early-sweep scan `e6411b30` on its $8.45-25 band (103 rows), and a preview of the same screen on $1-8.45 with prints Nov 2 - Mar 5 and call volume >= 500 (105 rows, nothing saved).
**Reserve / lines:** spendable $592.15 -> R5 line at 3.5/5 = **$0.592**.
**Data:** Friday closing option quotes (stamped 19:59 UTC, so closing spreads), last-trade closes, after-hours prints, analyst counts, earnings dates and daily closes pulled live this run.

## Chain stage

| Ticker | Dir | Stock | Next print | R3 / tool low | Contract | Bid / Ask | OI | Spread | BE / needs | R6 cap | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **NIO** | CALLS | 3.19 (AH 3.20), R1 under 0 | Tue Nov 24 AM (f), LY Tue Nov 25 AM | 16/7/1, $3.70 | **$3C Dec18** `6f04dc70` | 0.34 / 0.39 | 699 | 13.7% | $3.39, +6.27% at 3.19, +5.94% at 3.20 | 6.0% | **ADVANCED, REAL-MONEY CANDIDATE.** R1-R5 and R7 pass. R6 passes at the AH price and fails at the last trade, on the line. Floor date open. Doc goes Saturday. |
| NIO | CALLS | | | | $4C Dec18 `32ecfcca` | 0.06 / 0.07 | 2,385 | 15.4% | $4.07, +27.6% | 6.0% | Fails R6 and R4. Whole-dollar strikes only. |
| B | CALLS | 36.97 (AH 37.06), scanner R1 0.255 | Mon Nov 9 AM verified | 15/5/1, $42 | **$39C Dec18** `bbe37c92` | 1.33 / 1.61 | 1,293 | 19.0% | $40.61, +9.85% | 10.2% (4 prints: +5.2, -7.2, +9.0, -6.4; median 6.8%) | **Paper only (R5). R4, R6, R7 pass; R1 gate.** Paper doc Saturday if R1 <= 0.25. |
| B | CALLS | | | | $38C `0aafec01` | 1.47 / 1.98 | 274 | 29.5% | $39.98, +8.1% | 10.2% | R7 spread at the close. |
| B | CALLS | | | | $40C `7a84654e` | 1.10 / 1.23 | 2,265 | 11.2% | $41.23, +11.5% | 10.2% | R6. |
| GLXY | CALLS | 16.00 | Tue Feb 2 AM (f) | 15/1/0, $20.50 | Apr16 $15C `220e1b54` | 4.05 / 4.70 | 165 | 14.9% | $19.70, +23.1% | 14.4% (5 prints: +8.1, -16.9, +5.2, -13.9, +9.6; median 9.6%) | **KILLED, R6 and R7.** $17.5C (OI 362) BE $21.05 fails R4. $20C spread 39%. $12.5C OI 8. $10C OI 51, spread 26%. |
| NLY | CALLS | 18.25 | Wed Jan 27 PM (f) | 9/4/0, $19.50 | Apr16 $18C `2c77023a` | 1.09 / 1.14 | 132 | 4.5% | $19.14, +4.9% | 1.5% (5 prints; median 1.0%) | **KILLED, R6 structural, plus R7.** |
| DX | CALLS | 10.64 | Mon Jan 25 AM (f) | 4/2/0, $11.50 | Mar19 $10C `a6b7b83d` | 0.70 / 1.10 | 85 | 44% | $11.10, +4.3% | 1.2% (5 prints; median 0.8%) | **KILLED, R6 structural, plus R7.** $12.5C 0.00 / 0.10 fails R4. |
| WGS | CALLS | 69.19 (AH 67.00) | Mon Nov 9 PM verified | 8/0/0, $83 | Dec18 $70C / $72.5C / $75C / $80C | 10.90 / 14.50 and wider | 57-77 | 28-43% | | 8.5% (4 prints, one of them -49.2%) | **KILLED, R7** on every strike tested. |
| CLBT | CALLS | 12.16 | Thu Nov 12 AM verified | 9/0/0, $12.50 | Dec18 $10C `73318103` | 2.35 / 2.70 | 979 | 13.9% | $12.70 | | **KILLED, R4** (BE over the low). $12.5C 0.80 / 1.15 fails R4 and R7. Same grid problem as Oct 6. |
| AEVA | CALLS | 9.27 | Wed Nov 4 PM verified | 3/3/0, $15 | Dec18 $10C `5d0ed3f7` | 0.65 / 1.40 | 134 | 73% | $11.40 | | **KILLED, R7.** |
| BBD | CALLS | 2.55 | Thu Feb 4 PM (f) | 5/1/0, $4.20 | Mar19 $3C `41f5ff44` | 0.05 / 0.10 | 766 | 67% | $3.10, +21.6% | | **KILLED, R7.** Not worth an R6 pull at that spread. |

## NIO work

- **Why it's new:** on Oct 7 NIO's chain jumped from Nov 20 to Jan 15. Dec18 is listed now. The Oct 28 pass list had NIO but it didn't get a chain that night.
- **R1:** scanner reads under 0, a fresh 52-week low. **R2:** 6-K filer, so both dates are required and both exist. Later of Nov 24 / Nov 25 + 21 days = Dec 16, Dec 18 clears by two days, company hasn't announced. Ramp sell until announced: Mon Nov 23 3:35pm. **R3:** 16/7/1. **R4:** tool low $3.70 vs BE $3.39. On Oct 15 the low was $3.90, so somebody cut.
- **R5:** 0.39 vs $0.592. **R7:** OI 699, 13.7%.
- **R6:** reactions from daily closes: Sep 2 2025 +3.1, Nov 25 2025 -4.3, Mar 10 2026 +15.4, May 21 2026 +0.2, Sep 1 2026 -4.0. Median 4.0%, cap 6.0%. Five prints; Jun 3 2025 is on file and not pulled yet. Max ask = 1.06 x stock - 3.00, so 0.392 at $3.20. Today's daily bar closes $3.21 while the last trade reads $3.19; Saturday settles which one the doc uses.
- **Floor dating, unresolved:** one search. Goldman Buy $7 is Jul 13, so stale. Citi Buy $8.10, undated. Bernstein, Macquarie and BofA cuts, undated. Search range quotes a $4.03 low against the tool's $3.70. Whose $3.70 it is: unknown.
- **Q3 guide (company):** revenue RMB 33.29-34.05B, +52.7% to +56.2% year on year; Q3 deliveries 109,178, +25.4%. Search found no Q3 report date.

## Free ratings screen

68 re-rated; 13 of them are in the table above.

- **R3 fails (30):** CC, FSK, RIVN, SKYD, MARA, JOBY, LUMN, STNE, SMR, LCID, HTZ, OPEN, EOSE, PLUG, QS, LAC, STLA, CAPR, FLO, GTM, PMT, MBLY, VRRM, UWMC, DNUT, JBLU, MPT, QFIN, NVTS, AGNC.
- **R4 proxy fails (3):** TAC (low under the stock), RDW ($8 vs $8.36), INDI ($1.75 vs $1.66, too thin for any strike).
- **No coverage (17):** AEXA, CCXI, LPTH, BULL, POET, ITUB, DJT, TMC, BBAI, CRML, VZLA, EVLV, ASM, VFF, XXI, IEP, RUM.
- **R2 timing, print inside a week (7):** GRAB, DNN (Tue Nov 3), GROY, SHLS, UUUU (Wed Nov 4), KEEL, NXE (Thu Nov 5). Nothing to stand on.
- **Pass, not chained tonight:** OLMA 11/0-1, low $16 (no $7.5 strike on Dec18, needs the strike list), LAR 8/2/0, low $5 (no $4 strike on Dec18, same), ACHR 8/2/0, low $7, NB 6/1/0, low $4.70, MNSO 12/4/0.
- **SBET** stays out: R4 proxy too tight. **COUR**, for the record: 6/6/0, low $4.50, stock $3.475 after a -25.4% Friday. Nothing to do; next print is February.

## Paper gates checked

- **PL:** 8/5/0, tool low $17. One search; nothing dated after Oct 16. A search summary called $49 and $53 targets "late October" and tied them to Q1 results, so they don't hold up; not opened. Gate stays shut. $12C 2.70 / 2.90.
- **TTWO:** the tool's analyst stamp moved Aug 7 -> Oct 30, low still $270, 29/1/1. That stamp is the block's update time, not a named target's date, but it's the first movement. Q2 FY27 is Mon Nov 9 PM verified.

## Real-money read

**NIO $3C Dec18 is the first thing under the line to clear R6 at any price this week, and it clears by a rounding error.** ONDS $6.32, RCAT $4.62, BTBT $0.811, CLSK $7.655: no change.

## Tally

13 to a verdict or a chain: NIO advanced; B, TTWO carried; GLXY, NLY, DX, WGS, CLBT, AEVA, BBD killed; OLMA, LAR need strike lists; PL gate shut. 57 more cut free. Queue back to 10 live.

## GLOSSARY
- **R1-R7**: binder Tab 1 Iron Rules (calls). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest target above breakeven), R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven at expiry = strike + ask.
- **OI**: open interest, contracts outstanding.
- **AH**: after-hours trade.
- **(f)**: earnings date estimated from cadence, not announced.
- **6-K filer**: foreign private issuer, no 10-Q deadline, so R2 needs both the tool date and last year's date.
- **Tab 6 dating**: a floor only counts if it's dated inside 60 days and published after the stock's decline.
- **Closing spread**: the wider book quoted in the last minute of the session.
- **Paper**: tracked in the paper book, no money moves.
