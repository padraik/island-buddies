# Screening log: Thu Oct 15, 11:35am ET (MIDDAY)

**Source:** the 5-name research queue left by the 10:35 run, re-tested on live quotes pulled 15:35 UTC, plus a re-run of saved scan `4bc59b84-cc60-4619-870c-359c2daae902` ("Baxter Oct14 E3 refill": $300M+ cap, earnings Dec 19 - Jan 31, last >= $25, 52w range pct < 0.25) on today's prices. Reserve $676.28, 3.5/5 line $0.676.

**Moved this session:** 5 queue names re-tested, 6 scan rows checked. 0 killed, 0 advanced, 0 new. PAAS still gated on R1 (further over), TTWO on the Argus R4 question, ALGM / BTBT / ONDS parked on R6.

## Part 1: live re-tests

| Ticker | Contract | Direction | Stock (day) | Bid / Ask | BE at ask | Needs | R6 cap | R7 (OI / spread) | Result |
|---|---|---|---|---|---|---|---|---|---|
| PAAS | Jan15 $40C (paper) | CALLS | $43.48 (+2.7%) | 5.50 / 6.10 | $46.10 | +6.03% | BE <= $46.34 | 5,368 / 10.3% | GATED, R1 **0.282** (52w $33.08-$69.99; needs <= $42.31). $1.17 over, further than 10:35's 45 cents. R6 and R7 pass. Re-test next run |
| TTWO | Dec18 $190C (paper) | CALLS | $207.83 (+3.3%) | 27.60 / 29.80 | $219.80 | +5.76% | 7.35% | 854 / 7.7% | GATED, R4 dating (Argus $192 Oct 7 unconfirmed). R1/R3/R6/R7 pass. Tool 29/1/1, low $270. Fri WRAP re-vote |
| ALGM | Nov20 $35C (paper) | CALLS | $31.67 (-1.7%) | 1.60 / 1.80 | $36.80 | +16.20% | 10.5% | 6,816 / 11.8% | PARK, R6. Friday WRAP kill test (>15% short) still on track to fire |
| BTBT | Jan15 $1C (real) | CALLS | $1.065 (-0.9%) | 0.21 / 0.25 | $1.25 | +17.37% | 8.23% | 3,275 / 17.4% | PARK, R6. Ask widened back to 0.25 |
| ONDS | Dec18 $8C (real) | CALLS | $6.215 (+1.2%) | 0.33 / 0.35 | $8.35 | +34.35% | 20.89% | 37,968 / 5.9% | PARK, R6, ~1.6x its cap. Friday drop-to-bottom test |

## Part 2: scan re-run (Dec 19 - Jan 31 window, $25+)

| Ticker | Last | Range pct | Earnings (scanner) | Result |
|---|---|---|---|---|
| CALM | 63.67 | 0.053 | Jan 7 | already **KILLED R3** (no coverage), Oct 13 |
| FUL | 51.65 | 0.226 | Jan 14 | already killed at the chain, Oct 13 |
| FBK | 51.00 | 0.131 | Jan 21 | already **KILLED R6+R7**, Oct 14 EVENING 3 |
| MKC / MKC.V | 46.44 / 47.12 | 0.109 / 0.101 | Jan 22 | already **KILLED R4+R7**, Oct 15 OPEN (MKC.V is the voting class, no listed options) |
| SHAZ | 30.42 | 0.171 | Dec 31 | already **KILLED R6** (2 reported prints ever) |

Nothing new entered the bottom quartile in this window since last night. The under-$25 scan and the Oct 20 - Nov 20 window wait for EVENING 3 as planned.

## Part 3: facts re-pulled

Ratings (one call, 6 symbols incl. COUR) unchanged: COUR 8/4/0 low $6.00, PAAS 7/2/0 low $51, TTWO 29/1/1 low $270, ALGM 14/1/0 low $48, BTBT 6/0/0 low $3.50, ONDS 11/0/0 low $13.

Tape: COUR held its morning gain (+5.8%). PAAS kept climbing away from its R1 line.

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest Buy target above breakeven), R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + ask.
- **OI**: open interest, contracts outstanding; updates once a day.
- **Range pct**: (price - 52-week low) / (52-week high - 52-week low). Under 0.25 = calls candidate.
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
- **Gated / park / kill**: gated = one named check left; park = stays on the queue for a re-test; kill = off the queue, with the rule that killed it.
- **MIDDAY**: the hourly 10:35am-2:35pm ET runs.
