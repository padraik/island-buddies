# Screening log, Thu Oct 8, 2026, MIDDAY (12:35pm ET, VM)

Reserve $741.32 settled. Rule 5 lines: 3.5/5 $0.741, 4/5 $1.00 (transitional lock), screen $1.00.

First run under the **corrected** Rule 2 text (Michael, 11:45am Oct 8): (a) expiry at least 21 days after the later of the tool date and last year's same-quarter date; (b) the 10-Q deadline at least 5 trading days before expiry. 6-K filers: (a) only, both dates required.

## 1. COUR, the entry candidate

| Check | Live number (12:35-12:37pm) | Result |
|---|---|---|
| R1 | $5.115; 52w $4.5305 (Sep 29, 2026) to $10.77 (Oct 22, 2025, the old $11.11 rolled off) -> 0.094 | PASS |
| R2 (a) | tool Oct 22 PM (`verified: false`), last year Oct 23, 2025 PM; Oct 23 + 21 = Nov 13 <= Nov 20 | PASS |
| R2 (b) | Sep 30 quarter, 40-day filer: deadline Mon Nov 9, 9 trading days before Nov 20. COUR's last 10-Qs went in at 37 days (Aug 5, 2026) and 30 days (Oct 30, 2025); market cap $1.35B, float 231M shares. XBRL filer-category tag came back empty, so the 40-day status is inferred, not read off the cover page. | PASS |
| Already reported? | Q3 2026 `actual: null`; last print Jul 29 | Not reported |
| R3 | 8 Buy / 4 Hold / 0 Sell | PASS |
| R4 | low $6.00 (BMO Outperform, Oct 5, 3 days old) vs BE <= $5.74 | PASS ($0.26+) |
| **R5** | **$5C Nov20 0.55 / 0.75** (ask size 762-764, bid size 5), three pulls 12:35, 12:36, 12:37, and a fourth at the end of the run (journal). Line $0.7413. | **FAIL by $0.009 at the ask** |
| R6 | at a $0.74 fill BE $5.74 needs +12.2% vs cap 19.89% | PASS |

**Verdict: no order.** Rule 5 reads the ask ("the option ask, times 100, must not exceed..."), and the doc's own gate is "ask <= $0.74." The ask has sat at $0.75 since 9:37 this morning. A limit at mid (0.65) might well fill, but the rule doesn't measure what we'd pay, it measures the ask, and I'm not going to reinterpret a second rule on the same day as the first.

## 2. Rule 2 (corrected) re-test of every queue name holding a Nov20 contract

| Name | Tool date (verified?) | Last year | Later + 21 | Nov20 | Next-out | Status after this run |
|---|---|---|---|---|---|---|
| BRSL | Nov 3 AM (f) | Nov 4, 2025 AM | Nov 25 | **FAIL** | Jan15 (no Dec); failed R6 Oct 7 E3, stock lower since ($9.815) | **KILLED**: R2 on Nov20, R6 on Jan15 |
| SERV | Nov 11 PM (f) | Nov 12, 2025 PM | Dec 3 | **FAIL** | not checked | **KILLED**: R2 on Nov20, and its only dated floor (Oppenheimer/Guggenheim Aug 7/10) goes stale after Fri Oct 9, before any Dec doc could be written. Stock $4.455 (-4.4%). |
| FUBO | Nov 2 AM (f) | Nov 3, 2025 AM | Nov 24 | **FAIL** | Nov27 weekly: $10C 0.00 / 3.05, $11C 0.00 / 2.75, **OI 0, no bid**. Jan15 costs more than the Nov20 that already failed R5 (0.81 / 1.01). | **KILLED**: R2 on Nov20, no market on Nov27, R5 on Jan15. Tool's quarter labels for FUBO are scrambled (two quarters on May 6), noted. |
| TDUP | **Nov 4 PM (TRUE)** | Nov 3, 2025 PM | Nov 25 | **FAIL** under the text (16 days) | **Jan15 $2.5C** (`ba0a44c6-08ed-46c8-99e2-0de82c90039d`) **0.25 / 0.45, OI 420**; stock $2.265, max = 2.265 x 1.285 - 2.50 = $0.411 | R2 PASS at Jan15 (72 days). R5 PASS. **R6 at mid only** (0.35). Still floor-blocked (Telsey Aug 6, 63 days). Jan15 replaces Nov20 as the contract: far better liquidity (OI 420 vs 17). |
| TME (6-K) | Nov 11 AM (f) | Nov 12, 2025 AM | Dec 3 | **FAIL** | not checked (floor dies Sun) | Floor-blocked; Nov20 out. Next-out only matters if a fresh Buy target appears. Tool low now $9.0494 (FX drift from $9.04). |
| OBDC | Nov 4 PM (TRUE) | Nov 5, 2025 PM | Nov 26 | **FAIL** | not checked | Floor-blocked; Nov20 out. |
| GAU | Nov 5 PM (f) | Nov 6, 2025 PM | Nov 27 | **FAIL** | not checked | Floor-blocked; Nov20 out. Stock $2.075 (+6.4%). |
| FRMI | Nov 10 AM (f) | Nov 10, 2025 PM | Dec 1 | **FAIL** | not checked | Floor-blocked; Nov20 out. Stock $3.64 (-8.3%). |
| ADTN | Nov 2 PM (f) | Nov 3, 2025 PM | Nov 24 | **FAIL** | not checked | Floor-blocked; Nov20 out. |
| PCT | Nov 5 PM (f) | Nov 6, 2025 PM | Nov 27 | **FAIL** | not checked | Floor-blocked; Nov20 out. Ratings 3/3/0 (still passes R3 at the minimum). |

**The finding:** under the corrected text, **COUR is the only name in the queue whose Nov20 contract passes Rule 2.** Everything printing in November needs a December or January contract, and most small names have no December listing (BRSL, TDUP: Nov20 then Jan15). Longer contracts cost more, so at a $741 reserve the hunting ground is now "prints before ~Oct 30 on Nov20" or "cheap Jan15 strikes."

**Open question (not urgent, TDUP has a Jan15):** TDUP's date is company-confirmed (Nov 4) and falls 16 days before Nov20. The 11:35 run read a confirmed date before expiry as an automatic pass; the corrected binder text has no such path ("Pass when BOTH hold"). I'm reading the text. For any held position, the confirmed date only sets the ramp sell.

## 3. Ratings (12 names, ~12:36pm)

Unchanged except TME's low ($9.04 -> $9.0494, FX): BRSL 7/3/0 low $11.90, FUBO 8/2/0 low $12, SERV 6/2/0 low $7, OBDC 11/2/0 low $11, GAU 5/1/0 low $2.99, FRMI 6/2/0 low $6, ADTN 7/2/0 low $11, PCT 3/3/0 low $6, MLCO 11/4/0 low $5.30, ENVX 7/3/1 low $5, FINV 6/1/0 low $4.11. COUR/ONDS/QUBT/TDUP/WRD as in the journal.

## 4. Tally

10 names moved one stage (Rule 2 re-test under the corrected text): BRSL, SERV, FUBO, TDUP, TME, OBDC, GAU, FRMI, ADTN, PCT. Chain checks: FUBO Nov27 x2, TDUP Jan15. **Killed 3:** BRSL (R2 Nov20 / R6 Jan15), SERV (R2 Nov20 / floor stale Fri), FUBO (R2 Nov20 / no Nov27 market / R5 Jan15). TDUP moved to Jan15. Six floor-blocked names lose their Nov20 contracts.

## GLOSSARY

- **R1 / Rule 1:** stock in the bottom 20-25% of its 52-week range.
- **R2 / Rule 2 (corrected Oct 8, 11:45am):** expiry at least 21 days after the later of the tool's date and last year's same-quarter date, and the 10-Q deadline at least 5 trading days before expiry. `verified: true` = the company announced the date itself.
- **10-Q deadline:** the latest a US company can file its quarterly report: 40 days after quarter end for larger filers, 45 for smaller ones.
- **6-K filer:** a foreign company (often an ADR) that files 6-Ks instead of 10-Qs, so it has no 10-Q deadline.
- **R3 / Rule 3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds (Buy/Hold/Sell counts like 8/4/0).
- **R4:** lowest Buy target above breakeven, dated within 60 days and set after the decline (Tab 6).
- **R5 / Rule 5:** one contract's ask must fit the conviction tier's budget; $0.741 per share for 3.5/5 at this reserve.
- **R6 / Rule 6:** the move to breakeven must be no more than 1.5x the stock's median earnings-day move.
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike.
- **Weekly:** a contract expiring on a Friday that isn't the monthly third Friday; often thin.
- **Max price (doc formula):** the highest ask at which a doc's contract still passes R6 at the current stock price.
