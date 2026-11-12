# SCREENING LOG: Wed Nov 11, EVENING 3 (10:00pm ET), VM

*Session 3 of 3. Job (from EVENING 2): the Nov 16 - Dec 22 window is fished out from five sides; the queue is 4 live, all gated, so under 10 is the honest state until the ~Dec 12-15 re-sweep. Re-rate the queue and watch names on tonight's after-hours prices, re-check dates, leave PREMARKET the Thursday plan.*

**No new scan tonight, on purpose.** Every scan the queue draws on reads Wednesday's close, and EVENING 1 (slide-in `696cbe51`) and EVENING 2 (losers `2a4b3aa6`, 67 rows, 0 never-worked) already ran on that close. A third pass on the same close returns the same rows. The next scan with new information is Thursday's close (EVENING 1 Thu) or the ~Dec 12-15 Mar19/Apr16 re-sweep (definitions in `screening_log_nov11_evening2.md`).

## Queue and watch names, re-rated (free: one ratings call, one quote call, `get_earnings_results` each)

| Ticker | Direction | Close / AH (03:00 UTC) | B/H/S, low (stamp) | Next print | Gate status | Verdict |
|---|---|---|---|---|---|---|
| NIO | CALLS (real) | $3.24 / $3.23 | 16/7/1, $3.70 (stamp Sep 1, unchanged) | Q3 Tue Nov 24 AM (f); LY Nov 25 | Floor gate: no Buy dated after Sep 29. SEC index: newest 6-K Nov 2, three Form 4s Nov 6, **no date notice yet** (LY's came Nov 12) | Stays #2, gated |
| CRDO | CALLS (paper) | $141.41 / $139.13 | 21/1/0, $235 | FQ2 Tue Dec 1 PM, verified | R1 at AH $139.13 is under the $142.03 line; floor gate (no Buy dated after Oct 12) unchanged | Stays #3, gated |
| PL | CALLS (paper) | $14.34 / $14.25 | 8/5/0, $17 | FQ3 Thu Dec 10 PM, verified | Floor gate unchanged (no dated floor since DB $28 aged out Nov 7) | Stays #4, gated |
| POWL | CALLS (paper) | $145.90 / $143.50 | 3/3/0, $235 | FQ4 Mon Nov 16 PM, verified | R1 passes (line ~$151.44). Gate (1) floor still shut. Window ends Fri Nov 13 evening | Stays #1, gated |
| MRVL | watch | $168.80 / $164.77 (-2.4%) | 40/5/0, $175 (Nov 7) | (not re-pulled, R1 out) | R1 out (watch line ~$135.5) | Watch |
| GNRC | watch | $194.00 / $190.15 | 19/5/0, $232 (Nov 5) | (Feb print) | R1 out (watch line ~$175) | Watch |
| ONDS | watch | $5.73 / $5.78 | 11/0/0, $13 | (Feb cycle) | Not in the Nov/Dec window | Watch |
| NVDA | watch | $173.73 / **$161.42** (-7.1%; was $159.49 at 8pm) | 67/5/1, $180 (Nov 11 18:09 UTC) | FQ3 Tue Nov 17 PM, verified | R6 structural (median 3.2%, cap 4.8%) | Dead this quarter (EVENING 2) |

## Paper book date re-check (the finding of the night)

| Contract | Recorded print / ramp | Tool tonight | Change |
|---|---|---|---|
| **BABA $110C Dec18** | Tue Nov 24 AM (f) / **Mon Nov 23 3:35pm** | **Thu Nov 19 AM, `verified: true`** | **Ramp sell moves to Wed Nov 18, 3:35pm.** R2 still passes (Nov 19 + 21 = Dec 10 <= Dec 18). Rule 4 holds (45/1/0, $140.92 vs BE $118.55). AH $97.93 (-3.5%). Fixed in `paper_book.md` and `research_BABA_paper.md` this run. |
| AVGO $280C Jan15 | Wed Dec 9 PM / Wed Dec 9 3:35pm | Dec 9 PM verified | None. AH $352.50, over the $350 target (close $345.45): first daytime run that sees a print over $350 writes the exit evaluation |
| GOOGL $200C Mar19 | Feb 3 2027 PM (f) / Tue Feb 2 3:35pm | Feb 3 PM (f) | None |

FRMI (closed real position, ramp-sold Wed 9:39am @ $0.10): Q3 Thu Nov 12 AM verified, `actual: null`. AH $1.97 (+8.8% on the $1.81 official close). Thursday PREMARKET logs the print reaction.

**Moved tonight:** 8 queue/watch names re-rated + 3 paper positions date-checked + FRMI = 12. **Killed:** 0. **Advanced:** 0. **Buyable real-money docs:** 0. Searches spent: 0.

## GLOSSARY

- **R1 (range percentile):** (price - 52-week low) / (52-week high - 52-week low). Under 0.25 = calls candidate.
- **R2:** earnings print proven to land before expiry: expiry 21+ days after the later of the tool date and last year's date, and the 10-Q / 10-K deadline 5+ trading days before expiry (6-K filers: both dates required, no deadline test).
- **R3:** at most 1 Sell, at least 3 Buys, Buys >= Holds.
- **R4 / floor gate:** the lowest Buy target must sit above the call's breakeven, and be dated within 60 days and after the stock's fall.
- **R6:** breakeven move no larger than 1.5x the median absolute earnings reaction over the last 4-8 prints.
- **R7:** open interest >= 250 and spread <= 25% of mid on the exact contract.
- **Ramp sell:** selling before the print into the pre-earnings premium (binder Tab 4).
- **(f) / verified:** `get_earnings_results` date is an estimate (false) or company-announced (true).
- **AH:** after-hours trading, after the 4pm close.
- **6-K:** the current-report form foreign issuers (NIO, BABA) file instead of an 8-K.
- **BE (breakeven):** strike + premium paid.
