# Screening log, Tue Oct 20, OPEN (9:35am ET): DONE

*Market open (quotes 9:35-9:36am ET, first minutes, so option spreads are opening-wide). 3 searches (CLS $375, ALGM $40 x2 counted as 2, RIOT $19), live quotes on 6 queue contracts. No chain pulls beyond the saved instruments.*

## Held: COUR $5C Nov20

| Check | Result |
|---|---|
| Quote (9:35) | 0.20 / 0.70 (opening spread; bid size 2,833, ask size 1,523, vol 0), mark 0.45, OI 3,235, IV 71.0% |
| Stock | $5.05 (+1.0%), 5.04 / 5.05 |
| Q3 | Thu Oct 29 PM, `verified: true`, `actual: null` (LY Oct 23 PM) |
| Rule 4 | 8/4/0, low **$6.00** vs BE $5.65: holds |
| Tab 4 | nothing fires; 0.20 bid is a first-minute quote with the stock up (same shape as Oct 12 / Oct 13 opens) |

## Queue: names moved

| # | Name | Contract | Stock (9:35) | Live quote | Ratings (B/H/S, low) | Result |
|---|---|---|---|---|---|---|
| 1 | CLS | Nov20 $310C | $289.18 (-3.7%) | 18.30 / 23.70, OI 1,884 | 25/0/0, $375 | **KILL R4 (Tab 6 stale floor).** One search traces the $375 low to Citi's upgrade to Buy, $375, right after the Oct 27, **2025** Q3 print: a year old and from before the slide. Working rule (Oct 19): one search tracing the low to a pre-decline target = kill. Also R7 at the open: spread 5.40 / mid 21.00 = 25.7% (> 25%). R6 would have passed (BE $333.70 = +15.4% vs 17.36%). |
| 2 | ALGM | Nov20 $32.5C | $32.49 (-2.1%) | 2.80 / 3.40, OI 3,518 | 14/1/0, $40 | **Still open (paper).** R6 at the ask: BE $35.90 = +10.50% vs 10.5% cap, passes by zero. R7: 0.60 / 3.10 = 19.4%, pass. Floor: one search found the UBS 38 -> 40 note undated again; a second search shows an aggregator snapshot "verified Oct 1, 2026" with stock $36.35 and range **low $48**, high $62. So the tool's $40 is either a fresh cut since Oct 1 or a stale 2025 UBS line re-surfacing (UBS was at $25 in May 2025, so 38 -> 40 is from 2025 or later). Either way every Buy target >= $40 > BE $35.90; the gate is still the date. **Kill Mon Oct 26.** |
| 3 | FLUT | Jan15 $75C | $77.76 (+0.5%) | 9.30 / 11.70, OI 772 | 27/9/1, $84 | **KILL R4.** BE at the ask $86.70 > $84 low; at the mid $85.50 > $84; at Monday's close ask 10.50, $85.50 > $84. Fails at every price the contract has shown since the low moved $85 -> $84. |
| 4 | NRG | Dec18 $105C | $98.01 (-1.4%) | 5.50 / 7.00, OI 510 | 16/4/0, $131 | Floor gate. R6 at the ask: BE $112.00 = +14.3%. R7 1.50 / 6.25 = 24.0%, pass (opening). $131 cutter still unknown. Kill Mon Nov 2. |
| 5 | NXT | Nov20 $80C | $78.91 (-1.0%) | 6.40 / 7.80, OI 283 | 27/4/0, $101 | Floor gate. BE $87.80 = +11.3%; R7 1.40 / 7.10 = 19.7%, OI 283 pass. Kill Mon Oct 26. |
| 6 | RIOT | Nov20 | $13.32 (-4.7%) | (not pulled) | 24/1/0, $19 | Cutter search: results are all 2025 cuts *from* $19 (JPMorgan 19 -> 17 Nov 2025, Needham 19 -> 18, ATB 19 -> 17). Nobody found cutting *to* $19 recently. Undated; stays floor-gated. Kill Tue Oct 27. |

**Unchanged, not worked this run:** TTWO $205.75 (low $270 stamped Aug 7), PAAS $43.96 (R1), AA (Rule 425 read at MIDDAY), BAC, PLD (Mar19 chains at MIDDAY).
**Paper:** LVS $38.05 (ramp sell today 3:35pm, ITM by $0.55 now). MSTR $134.20 (paper $120C, BE $142.05).

## Moved this run

6 names moved: 2 killed (CLS R4 stale floor + R7, FLUT R4), 4 re-checked at live asks with floor searches (ALGM, NRG, NXT, RIOT). 0 advanced. Queue 9 live + 3 watch.

## GLOSSARY

- **R1-R7:** the Iron Rules in binder Tab 1. R1 range position, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest Buy target above breakeven), R5 price cap, R6 reachability (needed move vs 1.5x median print move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid.
- **Floor-dating gate (Tab 6):** a bear floor only counts if it was published within 60 days and after the decline.
- **Opening spread:** in the first minutes of trading, market makers quote options wide; bids are often far under fair value until the book fills in.
- **Mid:** halfway between bid and ask.
- **Kill date:** the last day a name can still get a doc and an entry with room for its own ramp sell.
- **Paper:** tracked in `paper_book.md`, no money moves.
