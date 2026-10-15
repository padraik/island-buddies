# Screening log: Thu Oct 15, WRAP (4:15pm ET)

*PREPARE slot (no order tools). Closing quotes (3:59pm ET) on all 6 queue names, free tools only: no chain pulls, no web searches. 0 killed, 0 advanced. Queue stays 6.*

## Part 1: R6 / R7 re-tests at the close

| Ticker | Contract | Direction | Stock (day) | Bid / Ask | BE at ask | Needs | R6 cap | R7 (OI / spread) | Result |
|---|---|---|---|---|---|---|---|---|---|
| RIOT | Nov20 $13C (paper) | CALLS | $15.51 (+2.7%) | 2.77 / 4.05 | $17.05 | +9.93% | 10.69% | 568 / 37.5% | PARK. R6 still passes but the margin shrank to 0.76 pts (the closing ask jumped 3.25 -> 4.05, vol 0, IV 105%). R7 fails at this quote; it's end-of-day width (2:35 was 10.2%). Dated-floor gate unchanged (tool low $22 = JPM, Aug 17, pre-slide). EVENING 2 re-scores; re-quote at OPEN |
| PAAS | Jan15 $40C (paper) | CALLS | $43.76 (+3.4%) | 5.70 / 6.40 | $46.40 | n/a | 9.48% | 5,368 / 11.6% | PARK, R1: $1.45 over the $42.31 line (silver up with the tape) |
| TTWO | Dec18 $190C (paper) | CALLS | $209.43 (+4.1%) | 28.20 / 30.80 | $220.80 | +5.43% | 7.35% | 854 / 8.8% | PARK on the Argus R4 gate; R1/R3/R6/R7 pass. Tool low $270 (stamp Aug 7). Fri WRAP re-vote |
| ALGM | Nov20 $35C (paper) | CALLS | $32.37 (+0.5%) | 1.70 / 2.10 | $37.10 | +14.6% | 10.5% | 6,816 / 21.1% | PARK, R6. Under the 15% kill line at the close, so Friday's close decides per the Oct 14 note |
| BTBT | Jan15 $1C (real) | CALLS | $1.085 (+0.9%) | 0.19 / 0.28 | $1.28 | +18.0% | 8.23% | 3,275 / 38.3% | PARK, R6 + R7 spread |
| ONDS | Dec18 $8C (real) | CALLS | $6.345 (+3.3%) | 0.34 / 0.39 | $8.39 | +32.2% | 20.89% | 37,968 / 13.7% | PARK, R6. Friday drop-to-bottom test |

## Part 2: held and paper-book fact changes found at the close

| Ticker | What changed | Effect |
|---|---|---|
| LVS (paper) | Q3 date now **Wed Oct 21 PM, `verified: true`** (was Oct 26 PM, `verified: false`; LY Oct 22) | Paper ramp sell confirmed at **Tue Oct 20 3:35pm**. Stock $38.315 closed ITM ($37.50 strike), so Tuesday's run decides ITM hold vs sell per Tab 4 |
| COUR (real) | Nothing: Oct 26 PM `verified: false`, LY Oct 23, `actual: null`; 8/4/0 low $6.00 | Ramp sell held Wed Oct 21 3:35pm |

Green tape for the whole list today: every queue name closed up. The closing option spreads widened as usual (RIOT 15.9% at 3:35 to 37.5% at the close), so tomorrow's re-tests use settled quotes, not the opening ones.

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + ask.
- **OI**: open interest, contracts outstanding; updates once a day.
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
- **Park**: stays on the queue, re-tested later; not killed.
- **ITM**: in the money; for a call, stock above the strike.
- **(f) / verified**: earnings date estimated from cadence vs. announced by the company.
- **WRAP**: the 4:15pm ET run; no trading tools, marks the book, prepares the next day's list.
