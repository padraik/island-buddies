# Screening log: Thu Oct 15, 9:35am ET (OPEN)

**Source:** the 8-name research queue left by PREMARKET, re-tested on live quotes pulled 13:35 UTC (first minutes of the session; opening spreads run wide). Reserve $676.28, 3.5/5 line $0.676. MKC's Mar19 $40C instrument pulled for the first time (`0069a3cb-9853-4c9d-9a71-2e4fd66a7307`).

**Moved this session:** 8 names. 3 killed (MKC on R4 + R7; HII and SE on R7), 2 paper names gated (PAAS on R1, TTWO on the Argus R4 question), 3 parked on R6 (ALGM, BTBT, ONDS). 0 advanced.

## Part 1: live re-tests

| Ticker | Contract | Direction | Stock (day) | Bid / Ask | BE at ask | Needs | R6 cap | R7 (OI / spread) | Result |
|---|---|---|---|---|---|---|---|---|---|
| PAAS | Jan15 $40C (paper) | CALLS | $42.58 (+0.6%) | 5.20 / 5.70 | $45.70 | +7.33% | BE <= $46.34 | 5,368 / 9.2% | GATED, R1 0.257 (52w $33.08-$69.99; needs <= $42.31). R6 and R7 pass. Re-test MIDDAY |
| TTWO | Dec18 $190C (paper) | CALLS | $205.00 (+1.9%) | 24.80 / 27.80 | $217.80 | +6.24% | 7.35% | 854 / 11.4% | GATED, R4 dating (Argus $192 Oct 7 unconfirmed). R1/R3/R6/R7 pass. Tool 29/1/1, low $270. Fri WRAP re-vote |
| MKC | Mar19 $40C (paper) | CALLS | $46.155 (+3.0%) | 6.60 / 8.10 | $48.10 | +4.21% | n/a | **231** / 20.4% | **KILL, R4 + R7.** BE $48.10 is over the $47 low target (even the $47.35 mid is over). With the stock at $46.16 the $40 strike has $6.16 intrinsic, so BE < $47 needs under $0.84 of time value on a 5-month contract: not happening unless the stock falls back. OI 231, under 250 for the second day |
| ALGM | Nov20 $35C (paper) | CALLS | $30.885 (-4.1%) | 1.35 / 1.80 | $36.80 | +19.15% | 10.5% | 6,816 / 28.6% | PARK, R6 (further than Wed's +15.4%) |
| BTBT | Jan15 $1C (real) | CALLS | $1.0208 (-5.0%) | 0.16 / 0.27 | $1.27 | +24.4% | 8.23% | 3,275 / 51% | PARK, R6. Opening spread fails R7 too |
| ONDS | Dec18 $8C (real) | CALLS | $5.86 (-4.6%) | 0.20 / 0.26 | $8.26 | +40.96% | 20.89% | 37,968 / 26% | PARK, R6, now 2x its cap. Friday drop-to-bottom test per queue note |
| HII | Nov20 $270C (paper) | CALLS | $267.32 (+1.1%) | 12.10 / 15.80 | $285.80 | +6.91% | not computed | **224** / 26.5% | **KILL, R7.** OI 227 -> 224, falling for the third day, with the print (Oct 29 tool date) 10 trading days out. Spread fails too at the open |
| SE | Dec18 $95C (paper) | CALLS | $95.76 (+0.5%) | 8.40 / 10.10 | $105.10 | +9.75% | not computed | **160** / 18.4% | **KILL, R7.** OI 161 -> 160, never near 250 in three days |

## Part 2: facts re-pulled

Ratings (one call, 9 symbols) unchanged from PREMARKET: PAAS 7/2/0 low $51, TTWO 29/1/1 low $270, MKC 8/8/1 low $47, ALGM 14/1/0 low $48, BTBT 6/0/0 low $3.50, ONDS 11/0/0 low $13, HII 9/6/0 low $281, SE 27/4/0 low $105. MKC earnings: Q4 Jan 21 AM `verified: false`, R2 would have passed (Mar 19 is 57 days later).

Tape at the open: the small caps on the list are red again (ALGM -4.1%, BTBT -5.0%, ONDS -4.6%), the large caps green (TTWO +1.9%, MKC +3.0%, HII +1.1%). COUR +1.9%.

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest Buy target above breakeven), R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + ask.
- **OI**: open interest, contracts outstanding; updates once a day, so an intraday re-pull can't fix it.
- **Intrinsic / time value**: intrinsic is how far the stock is over the strike; time value is the rest of the option price.
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
- **Gated / park / kill**: gated = one named check left; park = stays on the queue for a re-test; kill = off the queue, with the rule that killed it.
- **OPEN**: the 9:35am ET run.
