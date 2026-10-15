# SCREENING LOG: Thu Oct 15, 1:35pm ET (MIDDAY)

12 names moved: 5 queue re-tests + 7 new names from a fresh $5-15 scanner pass. 6 killed, 1 advanced (RIOT, paper, gated on a dated floor). One web search (RIOT floor date).

## Part 1: queue re-tests (live quotes ~17:35 UTC)

| Ticker | Contract | Direction | Stock | Bid / Ask | BE at ask | Needs | R6 cap | R7 (OI / spread) | Result |
|---|---|---|---|---|---|---|---|---|---|
| PAAS | Jan15 $40C (paper) | CALLS | $43.145 (+1.9%) | 5.50 / 6.10 | $46.10 | n/a | BE <= $46.34 | 5,368 / 10.3% | PARK, R1: ~0.273, 84 cents over the $42.31 line |
| TTWO | Dec18 $190C (paper) | CALLS | $210.02 (+4.4%) | 28.80 / 31.00 | $221.00 | +5.23% | 7.35% | 854 / 7.4% | PARK, Argus $192 gate (Fri WRAP re-vote) |
| ALGM | Nov20 $35C (paper) | CALLS | $31.81 (-1.3%) | 1.65 / 1.85 | $36.85 | +15.8% | 10.5% | 6,816 / 11.4% | PARK, R6 (Fri WRAP kill if >15% short) |
| BTBT | Jan15 $1C (real) | CALLS | $1.07 (-0.5%) | 0.22 / 0.25 | $1.25 | +16.8% | 8.23% | 3,275 / 12.8% | PARK, R6 |
| ONDS | Dec18 $8C (real) | CALLS | $6.254 (+1.9%) | 0.34 / 0.35 | $8.35 | +33.5% | 20.89% | 37,968 / 2.9% | PARK, R6 |

Ratings re-pulled: no change (PAAS 7/2/0 low $51, TTWO 29/1/1 low $270, ALGM 14/1/0 low $48, BTBT 6/0/0 low $3.50, ONDS 11/0/0 low $13).

## Part 2: fresh scanner pass, $5-15 band

Preview scans (not saved): market cap >= $300M, earnings 20261020-20261211, 52w range pct < 0.25. $5-15 returned 281 rows (capped at 200, sorted Last desc, covering $7.85-14.98); a second pass at $5-7.86 returned 82 (complete). Diffed against every capitalized token in week-08/09 research, passes.md, paper_book.md, research_queue.md and the Oct 10-15 journals: **7 new** (CMCO, RIOT, PWP, SIFY, AESI, PUMP, RUM).

| Ticker | Direction | Price | Range pct | Print | Ratings (B/H/S), low tgt | Result |
|---|---|---|---|---|---|---|
| RIOT | CALLS | $14.92 (-1.2%) | 0.181 | Oct 29 PM (f), LY Oct 30 PM | 24/1/0, low $22 | **ADVANCE (paper), gated on dated floor.** See below |
| AESI | CALLS | $10.195 (-7.9%) | 0.204 | Nov 2 PM (f), LY Nov 3 PM | 7/6/1, low $12 | **KILLED, R7.** Nov20 fails R2's 21-day test (Nov 3 + 21 = Nov 24), so Dec18: $10C 1.25 / 1.55, OI 100; $12.5C 0.40 / 0.65, OI 254 but spread 48% of mid |
| PUMP | CALLS | $7.81 (-5.0%) | 0.216 | Oct 28 AM (verified), LY Oct 29 | 7/5/0, low $11 | **KILLED, R7.** Nov20 $7.5C 0.75 / 1.20, OI 0; $10C 0.05 / 0.30, OI 237, spread 143% |
| CMCO | CALLS | $14.98 | 0.241 | Oct 30 | none | **KILLED, no coverage** |
| PWP | CALLS | $13.76 | 0.093 | Nov 6 | none | **KILLED, no coverage** |
| SIFY | CALLS | $11.83 | 0.224 | Oct 23 | none | **KILLED, no coverage** |
| RUM | CALLS | $5.935 | 0.220 | Nov 12 | none | **KILLED, no coverage** |

Also seen: **FMC -33% today** ($5.405, range pct -0.12, Oct 29 print). Already killed Oct 6 and Oct 8 on R3 (6/12/2); still 6/12/2 today. Stays dead.

### RIOT Nov20 calls (chain `f80d6a24-52bb-40e9-8012-e311c58ccd1e`)

R6 base: last 6 prints, next-day close moves +7.98%, -17.75%, -6.21%, -6.94%, +7.31%, +4.33%. Median **7.12%**, cap **10.69%**.

| Strike | Bid / Ask | OI | Spread % mid | BE at ask | Needs | R6 | R7 |
|---|---|---|---|---|---|---|---|
| $12C `0870b9c1-9fb4-4a44-997c-35a48b31fc6d` | 3.15 / 3.60 | 109 | 13.3% | $15.60 | +4.6% | pass | **fail (OI)** |
| **$13C `e6e7ea4c-a143-42db-8e4d-c64fbdbabf95`** | **2.71 / 2.96** | **568** | **8.8%** | **$15.96** | **+6.97%** | **pass** | **pass** |
| $14C `85ab679a-f7ac-450d-a3ba-dde660dff85d` | 2.18 / 2.27 | 46 | 4.0% | $16.27 | +9.0% | pass | fail (OI) |
| $15C `ee021872-7e38-4dfc-ba52-b378d5a072ed` | 1.73 / 1.78 | 497 | 2.8% | $16.78 | +12.5% | fail | pass |
| $18C `b62d5924-0e73-4b52-9248-ce9e8747077c` | 0.77 / 0.80 | 24,651 | 3.8% | $18.80 | +26.0% | fail | pass |

R1 0.181 pass. R2: Nov 20 is exactly 21 days after the later date (LY Oct 30); 10-Q deadline Nov 9 is 9 trading days before expiry: pass. R3 24/1/0 pass. R4 tool low $22 vs BE $15.96: passes on number. R5: every strike is over the $0.676 real-money line, so **paper only**. 
**Dated-floor gate (binder Tab 6):** one search: the $22 low is JPMorgan, raised $20 -> $22 on **Aug 17, 2026** (59 days old, and it was published with RIOT around $19-20, before the drop to $14.92). That's a pre-decline floor. Next: find a target action dated after the September slide (lowest Buy), or re-score treating $22 as stale. Even a big floor cut keeps clearing: BE $15.96 needs a floor above $16.
Ramp sell if entered: Wed Oct 28 3:35pm (day before the tool's Oct 29 PM). Crypto-correlated with BTBT (correlated cap only matters for real money).

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + ask.
- **(f)**: earnings date `verified: false` (estimated). **LY**: last year's same-quarter date.
- **Range pct**: (price - 52w low) / (52w high - 52w low).
- **Dated floor**: binder Tab 6: a Rule 4 target counts only if it's within 60 days and published after the stock's decline.
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
