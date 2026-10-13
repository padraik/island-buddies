# Screening log, Tue Oct 13, 12:35pm ET (MIDDAY)

*Live data pulled 16:33-16:36 UTC. Reserve $676.28 (3.5/5 line $0.676). Real-money names first, then the four paper advancers from 11:35 through the chain stage.*

## Re-tests (parked on R6)

| Name | Contract | Stock | Quote | BE at ask | Needs | R6 cap | Result |
|---|---|---|---|---|---|---|---|
| BTBT | Jan15 $1C | 1.245 (+0.4%) | 0.34 / 0.38 (OI 2,252) | 1.38 | +10.8% | 8.23% | **PARK** (passes at stock >= ~$1.275 with a 0.38 ask) |
| ONDS | Dec18 $8C | 6.624 (-0.7%) | 0.42 / 0.46 (OI 37,782) | 8.46 | +27.7% | 20.89% | **PARK** |
| ALGM | Nov20 $35C (paper) | 33.185 (-1.8%) | 2.20 / 2.45 x1 (OI 6,793) | 37.45 | +12.9% | 10.5% | **PARK** |

## Chain stage: the 11:35 advancers (all paper; R5 can't pass at a $0.676 line)

| Name | Stock | Expiry | Strike | Quote | OI | Spread % mid | BE at ask | Low Buy target | Result |
|---|---|---|---|---|---|---|---|---|---|
| RPM | 97.84 | Feb19 | $95C | 7.00 / 8.80 | 98 | 22.8% | 103.80 | $107 | R4 ok, **R7 fail (OI)** |
| RPM | | Feb19 | $100C | 4.60 / 6.90 | 110 | 40% | 106.90 | $107 | R7 fail (OI, spread) |
| RPM | | Feb19 | $105C | 2.35 / 5.50 | 71 | 80% | 110.50 | $107 | R4 fail, R7 fail |
| FUL | 49.83 | Feb19 | $50C | 3.60 / 4.80 | 6 | 29% | 54.80 | $62 | **R7 fail** |
| FUL | | Feb19 | $55C | 1.90 / 3.10 | 0 | 48% | 58.10 | $62 | R7 fail |
| MKC | 44.68 | Mar19 (no Feb19 listed) | $45C | 3.30 / 3.60 | 251 | 8.7% | 48.60 | $47 | R7 ok, **R4 fail** (BE $1.60 over the floor) |
| MKC | | Mar19 | $40C | 6.20 / 6.50 | 231 | 4.7% | 46.50 | $47 | R4 ok (+1.1% margin), **R7 fail (OI 231)** |
| HEI.A | 219.93 | Jan15 | | no Jan15 chain listed | | | | | **R7 fail (no contract)** |
| HEI (stand-in) | 293.49 | Jan15 | $290C / $300C | 20.60 / 23.00, 15.60 / 18.50 | 9 / 53 | 11% / 17% | 313.00 / 318.50 | $320 | **R1 fail**: HEI common sits at 31% of its 52-week range (low 256.11 Apr 27 wk, high 376.86 Aug 3 wk), MID-OUT. Also R7 (OI). |

- **RPM KILLED, R7** (Feb19 OI 71-110 across $95-105). The best Rule 1-4 setup of the day, and nobody trades the chain.
- **FUL KILLED, R7** (Feb19 OI 0-6).
- **MKC KILLED, R4/R7 split**: the only strike with OI >= 250 ($45C) has a breakeven over the $47 floor; the strike under the floor ($40C) has OI 231. MKC has no Feb19 expiry; Mar19 is the first that clears R2 (Jan 21/22 print + 21 days = Feb 12).
- **HEI.A KILLED, R7** (no Jan15 chain). **HEI** common doesn't stand in: R1 MID-OUT at 31%.

**Moved:** 7 (3 re-tests, 4 chain checks). 4 kills, 3 parked, 0 advances, 0 entries. No web searches.

**Pattern:** the Dec 12 - Jan 31 window is now worked through in all three price bands (sub-$10, $10-25, $25+). Zero survivors. Mid-cap industrials and staples pass R1-R4 and then have far-dated chains with double-digit open interest: R7 is the wall for anything not in the S&P 100 two months out.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile (bottom quartile for calls), R2 earnings before expiry (21-day cushion on the later of tool date and last year's date; 10-Q/10-K deadline at least 5 trading days before expiry), R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability (ask x 100 <= 10% of reserve at 3.5/5), R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid (at the ask).
- **OI:** open interest, contracts outstanding.
- **Spread % mid:** (ask - bid) / mid.
- **PARK:** alive, waiting on one specific price; stays on the queue.
- **MID-OUT:** stock in the middle of its 52-week range (25-74%), no direction, no further work.
- **Stand-in:** checking the common share class when the share class that screened has no usable chain.
