# Screening log: Fri Oct 16, 2:35pm ET (MIDDAY)

Batch: 10 queue names re-tested on live quotes (~18:35 UTC) + 1 web search (NXT dated floor). No new names (behind-the-queue is empty until EVENING 3's scan).

## Queue re-tests

| Ticker | Contract | Stock | Bid / Ask | BE at ask | Needs | R6 cap | R7 (OI / spread) | Result |
|---|---|---|---|---|---|---|---|---|
| RIOT | Nov20 $13C (paper) | $13.85 (-10.6%) | 2.04 / 2.14 | $15.14 | +9.3% | 10.69% | 568 / 4.8% | PARK, floor gate only |
| NRG | Dec18 $105C (paper) | $103.18 (+0.3%) | 8.20 / 8.70 | $113.70 | +10.2% | 13.42% | 517 / 5.9% | PARK, floor gate only |
| NXT | Nov20 $80C (paper) | $80.42 (-3.6%) | 7.80 / 8.40 | $88.40 | +9.9% | 13.14% | 258 / 7.4% | PARK, floor gate only |
| NXT | Nov20 $85C (paper, alternate) | $80.42 | 5.70 / 6.50 | $91.50 | **+13.8%** | 13.14% | 324 / 13.1% | R6 fails (2nd run running); $80C stays the contract |
| INSM | Nov20 $105C (paper) | $96.505 (-2.7%) | 4.20 / 4.80 | $109.80 | +13.8% | 17.1% | 5,117 / 13.3% | PARK, floor gate only |
| TTWO | Dec18 $190C (paper) | $204.11 (-2.5%) | 25.30 / 27.80 | $217.80 | +6.7% | 7.35% | 850 / 9.4% | WRAP re-vote (margin shrinking) |
| ALGM | Nov20 $35C (paper) | $31.855 (-1.6%) | 1.65 / 2.05 | $37.05 | **+16.3%** | ~15% kill line | 6,822 / 21.6% | over the line 2nd hour running; WRAP kills it if still over at the close |
| PL | Jan15 $10C (paper) | $13.445 (-7.5%) | 4.00 / 4.40 | $14.40 | +7.1% | | 4,139 / 9.5% | floor gate; low $17 still above BE |
| PAAS | Jan15 $40C (paper) | $43.84 | | | | | | R1 (over $42.31) |
| BTBT | Jan15 $1C (real) | $0.943 (-12.7%) | not re-chained | | | | | R6 (further away) |
| ONDS | Dec18 $8C (real) | $5.98 (-5.8%) | not re-chained | | | | | R6 (further away) |

Ratings re-pulled (free): COUR 8/4/0 low $6; RIOT 24/1/0 low $22; NRG 16/4/0 low $159 (record Oct 3); NXT 27/4/0 low $101 (record Oct 13); INSM 24/1/0 low $165; PL 8/5/0 low $17; TTWO 29/1/1 low $270 (record Aug 7); ALGM 14/1/0 low $48; PAAS 6/2/0 low $51; BTBT 6/0/0 low $3.50; ONDS 11/0/0 low $13. Nothing moved since 1:35.

## NXT floor search (1 search)

Query: Nextracker price target October 2026. Every hit was an old Fly/TipRanks headline at the $48-62 target level (Guggenheim downgrade to Neutral removing a $62 target; Barclays $52 -> $50; Piper $50 -> $49; Baird $59 -> $48; Roth $65 -> $55; Wells $64 -> $58). Those targets sit far below today's $80 stock and below the tool's $101 low, so they are from NXT's 2023-24 range, not this fall. **No dated post-Sep 16 target action found. Floor gate holds.** One note for EVENING: a Guggenheim "downgraded ahead of earnings" headline exists; if a 2026 version of that is real, it would change the 27/4/0 count, and the tool still shows 27 Buys, so nothing to act on.

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + ask.
- **Range pct**: (price - 52w low) / (52w high - 52w low). Calls need <= 0.25.
- **Median print move**: the median absolute one-day stock move on earnings, last 6 prints.
- **Dated floor**: binder Tab 6: a Rule 4 target counts only if it's within 60 days and published after the stock's decline.
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
- **Ramp sell**: selling before the print into the pre-earnings premium (binder Tab 4).
