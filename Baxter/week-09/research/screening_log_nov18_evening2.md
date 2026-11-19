# Screening log, Wed Nov 18 EVENING 2 (8:00pm ET)

*Session 2 of 3. Session 2's own job is writing research docs for names past the chain stage. None exist (EVENING 1 staged 25 and advanced 0), so per the handoff this session started EVENING 3's job: band C's last three (TFII, NICE, NRG), all 16 band D parks (cheapest first), then OCGN / ALLO / AQST / ZURA. 23 names moved. Nothing held. Spendable $715.96, so the 3.5/5 R5 line is $0.716/share. Prices: Wednesday Nov 18 regular close. 0 web searches.*

## 1. R3, R4 proxy, dates, listed expiries

R3 = at least 3 Buys, Buys >= Holds, at most 1 Sell. R4 proxy = low target above Wednesday's close. Contract = the earliest *listed* expiry at least 21 days after the later of (tool date, LY date). Mar19 also needs a large-accelerated filer (10-K due Mar 1) for US filers. Foreign filers (20-F / 40-F / 6-K) need both dates and no deadline test. R1 for band D comes from the live scan's 52w range column (run 01:0xZ); band C names and the four parks from `get_equity_fundamentals` (section 2). All tool dates are `verified: false` (f).

| Ticker | Close | R1 | B/H/S | Low (margin) | Q4 tool date | LY | Later | Listed (2027) | Contract | Ramp line* | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TFII | 93.99 | 0.153 | 15/4/1 | 101 (7.5%) | Tue Feb 16 PM (f) | Feb 17 | Feb 17 | Jan15, Apr16 | **Apr16** | Tue Feb 16 | STAGED. Foreign (40-F), both dates. No Mar19 listed. **52w low ($80.63) is dated Nov 20 2025 and rolls off this week: R1 will rise** |
| NICE | 89.85 | 0.129 | 10/6/0 | 100 (11.3%) | Thu Feb 18 AM (f) | Feb 19 | Feb 19 | Jan15, Feb19, May21 | **May21** | Wed Feb 17 | STAGED. Foreign (20-F). No Mar19/Apr16 listed. Stamp Nov 7 |
| NRG | 93.66 | 0.127 | 14/3/0 | 116 (23.9%) | Tue Feb 23 AM (f) | Feb 24 | Feb 24 | Jan15, Mar19, Jun17 + weeklies | **Mar19** (2d, LA) | Mon Feb 22 | STAGED. Stamp Nov 9. Q3 beat big (4.68 vs 3.11) |
| CAMT | 98.42 | 0.073 | 8/4/1 | 115 (16.8%) | Wed Feb 17 AM (f) | Feb 18 | Feb 18 | Jan15, Feb19, May21 | **May21** | Tue Feb 16 | STAGED. Foreign (20-F). Under $100 now, so it left band D's scan (price band, not R1) |
| ACLS | 100.98 | 0.246 | 3/3/1 | 116 (14.9%) | Tue Feb 16 PM (f) | Feb 17 | Feb 17 | Mar19, Jun17 | **Mar19 if LA (9d), else Jun17** | Tue Feb 16 | STAGED. **R3 at the edge on all three counts** (3 Buys, Buys = Holds, 1 Sell). **R1 0.246, on the edge.** $3.0B cap: filer status at doc stage |
| DTM | 118.26 | 0.146 | 11/6/0 | 127 (7.4%) | Thu Feb 18 AM (f) | Feb 19 | Feb 19 | Mar19, Jun17 | **Mar19** (7d, LA) | Wed Feb 17 | STAGED. Thin margin |
| BWXT | 117.93 | 0.042 | 16/5/0 | 140 (18.7%) | Mon Feb 22 PM (f) | Feb 23 | Feb 23 | Jan15, Feb19, May21 | **May21** | Mon Feb 22 | STAGED. No Mar19/Apr16 listed |
| VST | 125.58 | 0.215 | 23/1/1 | 164 (30.6%) | Thu Feb 25 AM (f) | Feb 26 | Feb 26 | Jan15, Feb19, Mar19, Apr16 + weeklies | **Mar19** (0d, LA), Apr16 fallback | Wed Feb 24 | STAGED. Zero spare on Mar19: any later date moves it to Apr16. AH $127.72 (+1.7%) |
| AXSM | 134.00 | 0.087 | 22/1/0 | 220 (64%) | Mon Feb 22 AM (f) | Feb 23 | Feb 23 | Jan15, Mar19, May21 | **Mar19** (3d, LA) | Fri Feb 19 | STAGED. Widest band D margin |
| PODD | 139.98 | 0.060 | 15/13/0 | 160 (14.3%) | Wed Feb 17 AM (f) | Feb 18 | Feb 18 | Mar19, Jun17 | **Mar19** (8d, LA) | Tue Feb 16 | STAGED. R3 close (15 vs 13). Stamp Nov 4 |
| SPXC | 144.43 | 0.033 | 15/1/0 | 190 (31.6%) | Tue Feb 23 PM (f) | Feb 24 | Feb 24 | Mar19, Jun17 | **Mar19** (2d, LA) | Tue Feb 23 | STAGED. AH $141.61 (-2.0%) |
| GPOR | 160.44 | 0.147 | 10/6/1 | 180 (12.2%) | Tue Feb 23 PM (f) | Feb 24 | Feb 24 | Jan15, Apr16, May21 | **Apr16** | Tue Feb 23 | STAGED |
| FTAI | 172.25 | 0.147 | 12/0/0 | 265 (53.8%) | Wed Feb 24 PM (f) | Feb 25 | Feb 25 | Jan15, Feb19, Mar19 + weeklies | **Mar19** (1d, LA) | Wed Feb 24 | STAGED |
| MTZ | 174.89 | 0.091 | 23/2/0 | 220 (25.8%) | Thu Feb 25 PM (f) | Feb 26 | Feb 26 | Jan15, Feb19, Apr16 | **Apr16** | Thu Feb 25 | STAGED. Low target fell $232 -> $220 since Sat. Stamp Nov 7 |
| MYRG | 272.21 | 0.240 | 7/2/0 | 331 (21.6%) | Wed Feb 24 PM (f) | Feb 25 | Feb 25 | Jan15, Apr16 | **Apr16** | Wed Feb 24 | STAGED. R1 near the edge |
| STRL | 276.36 | 0.053 | 12/0/0 | 565 (104%) | Wed Feb 24 PM (f) | Feb 25 | Feb 25 | Jan15, Mar19, Jun17 | **Mar19** (1d, LA) | Wed Feb 24 | STAGED. AH $280.00 |
| AXON | 300.69 | 0.025 | 19/3/0 | 380 (26.4%) | Tue Feb 23 PM (f) | Feb 24 | Feb 24 | Jan15, Mar19, Jun17 + weeklies | **Mar19** (2d, LA) | Tue Feb 23 | STAGED. Stamp Nov 6 |
| EME | 646.23 | 0.210 | 9/5/0 | 700 (8.3%) | Thu Feb 25 AM (f) | Feb 26 | Feb 26 | Jan15, Apr16, May21 | **Apr16** | Wed Feb 24 | STAGED. Thin margin |
| FIX | 1140.59 | 0.246 | 11/2/0 | 1410 (23.6%) | Thu Feb 18 PM (f) | Feb 19 | Feb 19 | Jan15, Feb19, Apr16 | **Apr16** | Thu Feb 18 | STAGED. **Low target fell $1,700 -> $1,410 since Sat.** R1 0.246, on the edge |
| OCGN | 0.7392 | 0.024 | 6/0/0 | 8 (982%) | Wed Mar 3 AM (f) | Mar 4 | Mar 4 | Jan15, Apr16, Jun17 | **Apr16** (22d) | Tue Mar 2 | STAGED. No ratings stamp: floor gate likely dead at doc stage (targets pre-date the collapse) |
| ALLO | 0.6959 | 0.003 | 10/1/0 | 4 (475%) | Thu Mar 11 PM (f) | Mar 12 | Mar 12 | Feb19, May21 | **May21** | Thu Mar 11 | STAGED. **New 52w low today ($0.6859).** No stamp: same floor caveat |
| AQST | 3.78 | 0.223 | 9/0/0 | 6 (58.7%) | Wed Mar 3 PM (f) | Mar 4 | Mar 4 | Feb19, Mar19, May21 | **May21** | Wed Mar 3 | STAGED. Mar19 misses (needs Mar 25). **52w high ($6.735) is dated Dec 8 2025 and rolls off in ~3 weeks: R1 rises** |
| ZURA | 0.9651 | 0.005 | 8/0/0 | 5 (418%) | Thu Mar 18 AM (f) | Mar 19 | Mar 19 | Jan15, Mar19, Jun17 | **Jun17** | Wed Mar 17 | STAGED. Tool rows are mislabeled (FY25 Q4 filed as "2026 Q4", next as "2027 Q4"), but both dates read cleanly. No stamp: same floor caveat |

*Ramp line = the last trading run before the earliest of (tool date, LY date): same day for a PM print, the trading day before for an AM print, 3:35pm ET. Mon Feb 15 2027 is Presidents' Day. It moves when the company announces.

## 2. R1 from fundamentals (non-band-D names)

| Ticker | Close | 52w low (date) | 52w high (date) | R1 |
|---|---|---|---|---|
| TFII | 93.99 | 80.625 (2025-11-20) | 167.69 (2026-06-09) | 0.153 |
| NICE | 89.85 | 83.10 (2026-06-17) | 135.55 (2026-03-05) | 0.129 |
| NRG | 93.66 | 79.65 (2026-11-05) | 189.96 (2026-02-25) | 0.127 |
| CAMT | 98.42 | 89.13 (2026-11-05) | 215.99 (2026-05-11) | 0.073 |
| OCGN | 0.7392 | 0.6909 (2026-10-30) | 2.725 (2026-03-17) | 0.024 |
| ALLO | 0.6959 | 0.6859 (2026-11-18) | 4.46 (2026-04-13) | 0.003 |
| AQST | 3.78 | 2.93 (2026-01-30) | 6.735 (2025-12-08) | 0.223 |
| ZURA | 0.9651 | 0.9342 (2026-11-09) | 7.44 (2026-03-10) | 0.005 |

## 3. Why the sub-$1 parks matter

OCGN, ALLO and ZURA are the only names in the whole staged queue that could ever be real-money size at the $0.716 line, because a call on a sub-$1 stock costs cents. Two things stand in front of them, and both get checked at the next stage, not tonight:
- **R6:** the lowest listed strike is probably $1 (or $0.50 if listed). On a $0.70 stock, a $1 strike needs +45% or more to break even, against a cap of 1.5x the median print move. Biotech prints rarely move that much. Next check: `get_option_instruments` on the listed expiry for the lowest strikes, then the R6 print table.
- **Tab 6 floor gate:** none of the three ratings records carries an `updated_at`, and $4-8 low targets on sub-$1 stocks are almost certainly stale. Tab 6 needs a dated Buy target after the slide.

## 4. Watch names (not counted)

- **NIO:** close $2.77. 16/7/1, low $3.7026, `updated_at` still **2026-11-18 00:55Z**: no new target. Gate shut. Keep Watching until Mon Nov 30 3:35pm.
- **AVGO (paper):** close $354.05, AH $359.77, above the $338.85-341.08 window. Stamp Oct 27.
- **Paper GOOGL (held):** close $282.44, **AH $287.08** (+1.6%), under $300. 63/8/0, low $300 (stamp Nov 7) vs BE $285.95.
- **BABA (paper, closed at LASTCALL):** close $84.37, AH $85.24. FQ2 prints Thu AM.

## Tally

23 names moved, **23 staged**, 0 killed, 0 dates unusable. 0 advanced to a doc, 0 buyable. Web searches 0. **Band C and band D are now fully staged.**
- **Mar19 firm (LA):** DTM (7d), PODD (8d), AXSM (3d), NRG (2d), SPXC (2d), AXON (2d), FTAI (1d), STRL (1d), VST (0d, Apr16 fallback).
- **Mar19-if-LA:** ACLS (9d; else Jun17).
- **Apr16:** TFII (40-F), GPOR, MTZ, MYRG, EME, FIX, OCGN.
- **May21:** NICE (20-F), CAMT (20-F), BWXT, ALLO, AQST. **Jun17:** ZURA.
- **Edges:** ACLS (R3 on all three counts, R1 0.246), FIX (R1 0.246, low cut to $1,410), MYRG (R1 0.240). Thin R4 margins: DTM 7.4%, TFII 7.5%, EME 8.3%.

## Handed on

1. EVENING 3 (10pm): the staging backlog is done. Per Step 6, refill: re-run the sweep scans if the Nov 14 sweep is a week old by then (it's 4 days old tonight), otherwise Tier B / the sub-$1 chain checks (OCGN, ALLO, ZURA lowest strikes + R6 print table), then leave PREMARKET Thursday's plan.

## GLOSSARY

- **R1 (range percentile):** where the stock sits in its 52-week range, (price - low) / (high - low). Calls need 0.25 or lower.
- **R2 (confirmed earnings before expiry):** the later of the tool's date and last year's same-quarter date, plus 21 days, has to land on or before expiry.
- **R3 (ratings):** at least 3 Buys, at least as many Buys as Holds, at most 1 Sell.
- **R4 proxy:** the lowest analyst target sits above today's price. The real Rule 4 compares it to the breakeven at doc stage.
- **R5:** the price cap per share from the conviction tier, as a percent of reserve (3.5/5 = 10% of $715.96 = $0.716/share).
- **R6:** breakeven at the ask has to be within 1.5x the stock's median earnings-day move.
- **R7 (liquidity floor):** open interest of 250 or more and a spread of 25% of mid or less, on the exact contract.
- **LA (large accelerated filer):** a US company whose 10-K is due 60 days after year-end (Mar 1), early enough for a Mar19 contract.
- **(f):** the tool's date is `verified: false`, estimated from the company's cadence.
- **Ramp line:** the last 3:35pm run before the print, when an OTM call gets sold.
- **Tab 6 floor gate:** the low target has to be a dated Buy, recent and after the slide, before it counts as a floor.
- **Stamp:** the ratings record's `updated_at`.
- **AH:** after-hours price.
