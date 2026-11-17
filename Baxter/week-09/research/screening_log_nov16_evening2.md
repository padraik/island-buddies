# Screening log, Mon Nov 16 EVENING 2 (8:00pm ET)

*Session 2 of 3. Session 2's usual job is research docs for names that cleared the chain stage. None did tonight, so there was no doc to write, and I started EVENING 3's job: December date-staging on the next 25 parks (band A's remainder first, then band B's new names). Also drafted the IV note Michael's Nov 15 question asked for (`iv_check_proposal_nov16.md`). Nothing held. Real-money reserve $715.96 spendable, so the 3.5/5 R5 line is $0.716/share. Prices: Monday Nov 16 close. 0 web searches. 25 names moved.*

## 1. What changed in the method tonight

EVENING 1 staged 21 names "to Apr16" but pulled expiration lists for only 4 of them (NAMS, GPCR, SNDX, ONDS). Tonight I pulled the list for **all 25**, and **Apr16 is not universal.** Some chains run a Feb/May cycle with no Mar19 or Apr16 (ADTN, ALHC, EXK, IQMX). Others list Mar19 and Jun17 but no Apr16 (HIVE, PUMP, INR, UMH). So the contract month is now **the earliest *listed* expiry that passes R2**, not a calendar guess.

**Correction carried forward:** EVENING 1's 17 unchecked "Apr16" names (AMPX, KURA, OCS, RGNX, ORN, OLMA, SVRA, TSHA, CGEM, GLUE, ZVRA, MUX, UMAC, CRVS, REAX, AVBP, GENB) need their expiration lists pulled before that staging can be trusted. EVENING 3 does it (one free `get_option_chains` each).

**Filer-type test for Mar19.** The 10-K deadline has to fall at least 5 trading days before expiry. For Mar19 that's Mar 12, so only a **large accelerated** filer (Mar 1) passes. I used float x price as a proxy. Today's float value is a lower bound, because the test date is Jun 30 2026 and most of these names were much higher then. The doc stage confirms it on the 10-K cover. Foreign filers (40-F / 20-F / 6-K) skip the deadline test and need both dates. HIVE's Feb print is a fiscal Q3 10-Q (FY ends Mar 31), and its deadline is mid-February, so the deadline test passes either way.

## 2. R3 + R4 proxy (re-run on Monday's close, all 25 still pass)

| Ticker | Close | B/H/S | Low tgt | Proxy margin |
|---|---|---|---|---|
| EXK | 7.15 | 6/1/0 | 10.53 | 47% |
| ATEC | 6.78 | 12/2/0 | 8.00 | 18% |
| IQMX | 6.42 | 4/1/1 | 7.30 | 14% |
| TRTX | 6.56 | 5/0/1 | 8.00 | 22% |
| PHAT | 5.88 | 9/1/0 | 7.50 | 28% |
| AESI | 5.13 | 8/6/1 | 7.00 | 36% |
| SBET | 5.30 | 7/0/0 | 8.00 | 51% |
| STUB | 4.89 | 8/5/1 | 6.50 | 33% |
| ADTN | 4.69 | 7/2/0 | 6.25 | 33% |
| CINT | 2.98 | 7/2/0 | 4.00 | 34% |
| GROY | 2.81 | 8/0/0 | 4.00 | 42% |
| EVEX | 1.64 | 7/3/0 | 2.75 | 68% |
| HIVE | 1.46 | 8/1/0 | 2.50 | 71% |
| NXE | 7.41 | 18/0/0 | 10.14 | 37% |
| BLZE | 7.10 | 6/1/0 | 15.00 | 111% |
| PUMP | 7.21 | 10/3/0 | 11.00 | 53% |
| ALHC | 7.47 | 10/6/0 | 8.00 | 7% (thin) |
| CIFR | 6.54 | 22/3/0 | 9.50 | 45% |
| UUUU | 6.04 | 8/0/0 | 14.00 | 132% |
| DAN | 23.47 | 6/2/0 | 32.00 | 36% |
| GTX | 20.54 | 6/0/0 | 30.00 | 46% |
| UMH | 14.06 | 6/2/0 | 16.00 | 14% |
| XPRO | 12.75 | 3/2/1 | 14.00 | 10% (thin) |
| MESO | 12.45 | 7/0/0 | 19.38 | 56% |
| INR | 12.79 | 11/0/0 | 17.00 | 33% |

No target stamps were returned for any of the 25, so the floor gate (the target has to be dated after the slide) waits for the doc stage, as usual.

## 3. Date-staging

R2 (Oct 8 order): expiry at least 21 days after the later of the tool date and LY's same-quarter date. Domestic filers also need the deadline at least 5 trading days before expiry. Contract = earliest listed expiry that passes.

| Ticker | Q4 tool date | LY | Later | Listed (2027) | Contract | Note |
|---|---|---|---|---|---|---|
| **HIVE** | Feb 16 AM (f) | Feb 17 AM | Feb 17 | Mar19, Jun17 | **Mar19** | 9 days spare. Fiscal Q3 10-Q, deadline mid-Feb, so it passes as either filer type. Real-money size |
| **CIFR** | Feb 23 AM (f) | Feb 24 AM | Feb 24 | Mar19, Jun17 | **Mar19** | 2 days spare. Float $2.5B today: large accelerated |
| **DAN** | Feb 17 AM (f) | Feb 18 AM | Feb 18 | Feb19, Mar19, Jun17 | **Mar19** | 8 days spare. Large accelerated ($2.3B). Paper size at $23 |
| **GTX** | Feb 18 AM (f) | Feb 19 AM | Feb 19 | Mar19, Apr16, May21 | **Mar19** | 7 days spare. Large accelerated ($3.8B). Paper size at $20 |
| PHAT | Feb 25 AM (f) | Feb 26 AM | Feb 26 | Feb19, Mar19, May21 | **Mar19 if LA, else May21** | Zero margin on Mar19. Float $303M today. Large accelerated status depends on the Jun 30 price (52w high $18.31). Confirm on the 10-K cover |
| PUMP | Feb 17 AM (f) | Feb 18 AM | Feb 18 | Mar19, Jun17 | **Mar19 (LA likely), else Jun17** | 8 days spare. Float $814M at today's $7.21, higher on Jun 30 |
| UMH | **none** | Feb 25 PM | Feb 25 (LY only) | Mar19, Jun17 | **Mar19 provisional, Jun17 fallback** | The tool returns no Q4 row (Q3 Nov 2 is the newest). LY alone gives 1 day spare. A tool date after Feb 26 means Jun17. Large accelerated (~$1.1B) |
| ATEC | Feb 23 PM (f) | Feb 24 PM | Feb 24 | Jan15, Apr16 | **Apr16** | no Mar19 listed |
| TRTX | Feb 16 PM (f) | Feb 17 PM | Feb 17 | Jan15, Apr16 | **Apr16** | no Mar19 listed. Also accelerated at most ($463M), so Mar19 would fail the deadline anyway |
| AESI | Feb 22 PM (f) | Feb 23 PM | Feb 23 | Jan15, Apr16 | **Apr16** | no Mar19 listed |
| BLZE | Feb 22 PM (f) | Feb 23 PM | Feb 23 | Jan15, Apr16 | **Apr16** | no Mar19 listed |
| UUUU | Feb 25 PM (f) | Feb 26 PM | Feb 26 | Jan15, Apr16 | **Apr16** | no Mar19 listed |
| XPRO | Feb 18 AM (f) | Feb 19 AM | Feb 19 | Jan15, Apr16 | **Apr16** | no Mar19 listed |
| SBET | Mar 8 AM (f) | Mar 9 AM | Mar 9 | Jan15, Apr16 | **Apr16** | 17 days spare |
| STUB | Mar 3 PM (f) | Mar 4 PM | Mar 4 | Jan15, Apr16 | **Apr16** | |
| CINT | Mar 10 PM (f) | Mar 11 PM | Mar 11 | Jan15, Apr16 | **Apr16** | 15 days spare |
| GROY | Mar 17 PM (f) | Mar 18 PM | Mar 18 | Mar19, Apr16, Jun17 | **Apr16** | 8 days spare. Mar19 fails on date |
| EVEX | Mar 15 PM (f) | Mar 16 PM | Mar 16 | Jan15, Apr16 | **Apr16** | 10 days spare |
| EXK | Feb 26 AM (f) | Feb 27 AM | Feb 27 | Feb19, May21 | **May21** | Feb/May cycle. Canadian filer, both dates present |
| IQMX | Feb 22 AM (f) | **none** (history starts Q2 2026) | Feb 22 | Feb19, May21 | **May21** | No LY. If it's a 6-K filer, R2 needs both dates and fails until a doc-stage source confirms the date. Flag |
| ADTN | Feb 24 PM (f) | Feb 25 PM | Feb 25 | Feb19, May21 | **May21** | Feb/May cycle |
| NXE | Mar 2 PM (f) | Mar 3 PM | Mar 3 | Feb19, Mar19, May21 | **May21** | Mar19 fails on date (Mar 24 needed) |
| ALHC | Feb 25 PM (f) | Feb 26 PM | Feb 26 | Feb19, May21 | **May21** | Feb/May cycle |
| INR | Mar 9 PM (f) | Mar 10 PM | Mar 10 | Mar19, Jun17 | **Jun17** | no Apr16 listed |
| MESO | **none usable** | ~Feb 26 (H1 FY26 row, `actual: null`) | n/a | Apr16 | **UNSTAGED** | The tool's rows are malformed (null actuals, no upcoming quarter). It's a foreign filer (Mesoblast, Australia, FY ends Jun 30), so R2 needs both dates. It stays parked, flagged like TMQ. Saturday re-pulls it, and if it's still unusable that's a kill under R2 |

**Result: 4 Mar19 (HIVE, CIFR, DAN, GTX), 3 Mar19-conditional (PHAT, PUMP, UMH), 11 Apr16, 5 May21, 1 Jun17, 1 unstaged (MESO).**

Mar19 matters because it puts these trades about a month closer to the catalyst than Apr16, and about two months closer than May21/Jun17. That's less time value paid for the same print. **HIVE is the most interesting one for real money:** $1.46 stock, 8/1/0, low $2.50, and Mar19 is listed. Its chain has weeklies too, so it trades. CIFR at $6.54 might also fit under the $0.716 line on an OTM strike. Both get chain-checked (OI and R6) as soon as spring OI exists.

**Ramp-sell lines, if ever bought** (the trading day before the earliest date; AM = the prior day at 3:35pm, PM = the same day at 3:35pm): HIVE Fri Feb 12 (Feb 15 is Presidents Day), CIFR Mon Feb 22, DAN Tue Feb 16, GTX Wed Feb 17, PHAT Wed Feb 24, PUMP Tue Feb 16, UMH Thu Feb 25 (provisional), ATEC Tue Feb 23, TRTX Tue Feb 16, AESI Mon Feb 22, BLZE Mon Feb 22, UUUU Thu Feb 25, XPRO Wed Feb 17, SBET Fri Mar 5, STUB Wed Mar 3, CINT Wed Mar 10, GROY Wed Mar 17, EVEX Mon Mar 15, EXK Thu Feb 25, IQMX Fri Feb 19, ADTN Wed Feb 24, NXE Tue Mar 2, ALHC Thu Feb 25, INR Tue Mar 9.

## 4. Watch line and NIO

- **NIO:** $2.72 close (AH $2.77). Q3 still Fri Nov 27 AM `verified: false`, LY Nov 25 AM. Ratings 16/7/1, low $3.6996, **stamp 2026-09-01: gate shut.** Unchanged since EVENING 1.
- AVGO $333.40 close (AH $332.30), still below the $338.85-341.08 window. DY $215.39, under ~$225.50. No change.

## Tally

25 names moved: 24 date-staged to a listed contract month, MESO flagged unstaged, 25 expiration lists pulled, 16 fundamentals pulled for filer type. NIO, AVGO and DY watch-checked. **0 kills, 0 advanced to a doc, 0 buyable.** Web searches 0.

## Handed to EVENING 3

1. Pull expiration lists for EVENING 1's 17 unchecked "Apr16" names (list in section 1) and fix any that don't list Apr16.
2. Stage the remaining band A parks: QUBT, ACHR, ARDX, PCT, ALT, RDW, METC, MFA, NUVB, SOUN, WVE, DNN, CTMX, SANA.
3. Leave PREMARKET Tuesday's plan.

## GLOSSARY

- **Date-staging:** working out which option expiry a name's next earnings date allows under Rule 2, before spending a chain check.
- **Listed expiry:** an expiration date that actually appears on the stock's option chain. Not every stock has every monthly. Some run Jan/Apr/Jul/Oct cycles, others Feb/May/Aug/Nov, or Mar/Jun/Sep/Dec, plus nearby months.
- **R2 / Rule 2:** the earnings date must land at least 21 days before expiry (the later of the tool date and last year's date). For US filers, the filing deadline must also fall at least 5 trading days before expiry.
- **Large accelerated filer (LA):** an SEC filer with $700M+ public float on the last day of its Q2. It files its 10-K within 60 days of year-end (Mar 1), versus 75 (accelerated) or 90 (non-accelerated).
- **Float x price proxy:** a rough filer-type guess from today's share float and price. The real test date was Jun 30, so the 10-K cover page is the authority.
- **R3:** at least 3 Buys, Buys at least equal to Holds, at most 1 Sell.
- **R4 proxy:** at screening, is the lowest analyst target above the stock price?
- **Floor gate:** the lowest Buy target has to be dated after the stock's slide to count as a floor.
- **(f):** `verified: false`, an estimated date.
- **Ramp sell:** selling before the print into the pre-earnings premium.
- **Park:** passes the free screens and waits on a later check (here, spring open interest).
- **OI:** open interest.
