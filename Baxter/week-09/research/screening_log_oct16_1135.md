# Screening log, Fri Oct 16, MIDDAY (11:35am ET)

Batch: 10 names (7 queue re-tests on live quotes + HLNE, NXT, AZN dated, R6-based and chain-checked). 2 web searches (PL investor day, NXT dated floor). Quotes ~15:35 UTC.

## New names: HLNE, NXT, AZN (free screen, then the chain)

| Ticker | Stock | 52w range pct | Print (tool) | LY same Q | Ratings / low | Median print move (4) | R6 cap | Expiry for R2 |
|---|---|---|---|---|---|---|---|---|
| HLNE | $82.20 (-1.6%) | 0.12 (71.88 - 155.66) | Nov 3 AM `verified` | Nov 4 AM | 8/1/0, low $103 | 5.24% (+6.39, -3.74, +4.09, +7.06) | 7.86% | Dec18 (Nov20 is 16 days after Nov 4) |
| NXT | $84.07 (+0.7%) | 0.085 (76.72 - 163.13) | Oct 28 PM `verified` | Oct 23 PM | 27/4/0, low $101 (record Oct 13) | 8.76% (+8.74, +13.28, +8.77, -7.25) | 13.14% | Nov20 (23 days after Oct 28; 10-Q deadline Nov 9 is 9 trading days before) |
| AZN | $166.31 (-0.2%) | 0.22 (153.41 - 212.71) | Oct 30 AM `verified` | Nov 6 AM | 10/0/1, low $198 | 1.83% (+3.23, +2.87, -0.79, +0.22) | 2.74% | Dec18 (6-K filer; Nov20 is 14 days after Nov 6) |

R1, R3 and the R4 proxy pass on all three. Then the chain:

| Ticker | Contract | Bid / Ask | BE at ask | Needs | R6 cap | R7 (OI / spread) | Result |
|---|---|---|---|---|---|---|---|
| NXT | Nov20 $80C | 9.30 / 10.90 | $90.90 | +8.1% | 13.14% | 258 / 15.8% | passes R6/R7 |
| NXT | Nov20 $85C | 7.00 / 7.90 | $92.90 | +10.5% | 13.14% | 324 / 12.1% | passes R6/R7 |
| NXT | Nov20 $90C | 5.10 / 5.90 | $95.90 | +14.1% | 13.14% | 1,237 / 14.5% | R6 |
| HLNE | Dec18 $75C | 9.70 / 12.50 | $87.50 | +6.4% | 7.86% | **0** / 25% | R7 |
| HLNE | Dec18 $80C | 6.60 / 9.50 | $89.50 | +8.9% | 7.86% | **0** / 36% | R6 + R7 |
| HLNE | Dec18 $85C | 4.00 / 7.00 | $92.00 | +11.9% | 7.86% | **0** / 55% | R6 + R7 |
| HLNE | Dec18 $90C | 2.00 / 5.50 | $95.50 | +16.2% | 7.86% | **0** / 93% | R6 + R7 |
| AZN | Dec18 $160C | 12.60 / 13.40 | $173.40 | +4.3% | 2.74% | 2,116 / 6.2% | R6 |
| AZN | Dec18 $165C | 9.80 / 10.50 | $175.50 | +5.5% | 2.74% | **53** / 6.9% | R6 + R7 |
| AZN | Dec18 $170C | 7.50 / 8.00 | $178.00 | +7.0% | 2.74% | **118** / 6.5% | R6 + R7 |

- **HLNE: KILLED, R7.** Zero open interest on every Dec18 strike near the money.
- **AZN: KILLED, R6.** The stock moves under 2% on a typical print; no December call is within 2.74%.
- **NXT: ADVANCE (paper), dated-floor gate.** Best contract: **Nov20 $85C** `80f67e0a-35b9-483a-951f-b36687f59da8` (tighter, more OI; $80C `c1c39e5f-3fee-40b0-868d-4d3574cbef0a` is the alternate). The low target $101 clears both breakevens by ~10%, and the ratings record updated Oct 13. But the stock bottomed Sep 16 ($76.72), and the only dated cuts found are Jul 31 - Aug 3 (JPM $152, Susquehanna $157, RBC $147, Citi $132), all before the bottom. The search also turned up "Susquehanna $76 -> $100, Monday Oct 13" and "Deutsche $99, Friday Oct 24", but those weekdays only fit 2025, so they're last year's items. Next (EVENING, one search): who holds the $101 low and when they set it. Paper ramp sell Wed Oct 28 3:35pm (PM print). Kill Mon Oct 26 if the floor is never dated.

## Queue re-tests (live quotes ~15:35 UTC)

| Ticker | Contract | Stock | Bid / Ask | BE at ask | Needs | R6 cap | R7 (OI / spread) | Result |
|---|---|---|---|---|---|---|---|---|
| RIOT | Nov20 $13C (paper) | $14.73 (-5.0%) | 2.56 / 3.00 | $16.00 | +8.6% | 10.69% | 568 / 15.8% | PARK, floor gate only |
| NRG | Dec18 $105C (paper) | $103.96 (+1.1%) | 8.50 / 9.00 | $114.00 | +9.7% | 13.42% | 517 / 5.7% | PARK, floor gate only |
| INSM | Nov20 $105C (paper) | $96.80 (-2.4%) | 4.20 / 4.60 | $109.60 | +13.2% | 17.1% | 5,117 / 9.1% | PARK, floor gate only (R7 passes again) |
| PL | Jan15 $10C (paper) | $13.71 (-5.7%) | 4.30 / 4.50 | $14.50 | +5.8% | 45.75% | 4,139 / 4.5% | PARK, floor gate; ratings now **8/5/0** (one more Hold) |
| TTWO | Dec18 $190C (paper) | $205.86 (-1.7%) | 26.20 / 28.20 | $218.20 | +6.0% | 7.35% | 850 / 7.4% | WRAP re-vote |
| ALGM | Nov20 $35C (paper) | $32.38 (+0.1%) | 1.75 / 2.10 | $37.10 | +14.6% | ~15% kill line | 6,822 / 18.2% | WRAP kill check |
| PAAS | Jan15 $40C (paper) | $44.32 | n/a | | | | | R1 (over $42.31) |

Ratings re-pulled (free): COUR 8/4/0 low $6; RIOT 24/1/0 low $22; NRG 16/4/0 low $159; INSM 24/1/0 low $165; PL **8/5/0** low $17 (was 8/4/0 at 10:35); TTWO 29/1/1 low $270; ALGM 14/1/0 low $48.

## PL (one web search)

Searched "Planet Labs investor day October 16 2026 stock price target". Every hit is the **2025** investor day (Citizens JMP $8 -> $11, Cantor $8.50 -> $20, Needham $8 -> $12, Craig-Hallum $7 -> $11, a MarketBeat item dated 2025-10-20). Those targets sit below today's $13.71 stock, so they're last year's. Nothing dated for 2026. Today's facts: the stock is -5.7% and the tool shows one more Hold. Gate holds; EVENING re-pulls ratings to see whether a new low lands.

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + ask.
- **Dated floor**: binder Tab 6: a Rule 4 target counts only if it's within 60 days and published after the stock's decline.
- **6-K filer**: a foreign private issuer; no 10-Q deadline, so Rule 2 needs both the tool date and last year's date.
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
- **Ramp sell**: selling before the print into the pre-earnings premium (binder Tab 4).
