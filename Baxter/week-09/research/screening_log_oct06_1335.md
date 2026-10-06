# SCREENING LOG — Tue Oct 6, 2026, 1:35pm ET (VM MIDDAY)

**Source:** research_queue.md (live-list requotes, then Tier B sub-$15: GRNT, TKC, VYX, ARLO, MNTN, AHCO, MLCO through dates + R6 + chain; CWK, BRSL, PAR through R3). 10 names moved.

**Rule 5 line this run:** reserve = spendable $741.32 (unsettled $0.00). 3.5/5 line **$0.741**, 4/5 $1.00 (lock), screen $1.00.

## Summary

| Step | Count | Tool |
|---|---|---|
| Requotes | 6 (COUR, PCT, ENVX, BXMT, CWH, ADTN) | get_option_quotes |
| Ratings | 16 names; no count or low-target changes on the live six | get_equity_analyst_ratings |
| Dates | COUR + 7 Tier B | get_earnings_results |
| R6 history | 7 names, 4 prints each (daily closes) | get_equity_historicals |
| New chains | 7 contracts on 5 names (TKC $5C, VYX $7.5C, ARLO $12C/$13C, MNTN $10C/$12.5C, MLCO $4C) | get_option_instruments + get_option_quotes |
| Killed | 6 (GRNT, TKC, VYX, ARLO, MNTN, AHCO) | |
| Web | none | |

## Live list

| Ticker | Stock | Contract | Bid / Ask | BE at ask | Needs | R6 cap | Ratings / low | Status |
|---|---|---|---|---|---|---|---|---|
| COUR | $5.175 | $5C Nov20 | 0.55 / 0.75 | $5.75 | +11.1% | 19.89% | 8/4/0, $6.00 | **Ask back over the line** ($0.75 > $0.741). Date still Oct 22 PM `verified: false`. Floor (BMO $6, Oct 5) unchanged. |
| PCT | $4.085 | $4C Nov20 | 0.55 / 0.70 | $4.70 | +15.1% | 18.58% | 3/3/0, $6.00 | Blocked, R4 stale floor. Unchanged. |
| ENVX | $2.72 | $3C Nov20 | 0.26 / 0.29 | $3.29 | +21.0% | 25.27% | 7/3/1, $5.00 | Blocked, R4 stale floor. Unchanged. |
| BXMT | $11.015 | $11C Nov20 | 0.45 / 0.75 | $11.75 | +6.7% | 6.32% | 5/4/0, $16 | Fails R5 and R6 at the ask. |
| CWH | $4.735 | $4C Nov20 | 0.90 / 1.10 | $5.10 | +7.7% | 23.90% | 11/2/0, $6 | Fails R5. |
| ADTN | $7.515 | $7C Nov20 | 0.85 / 1.25 | $8.25 | +9.8% | n/a | 7/2/0, $11 | Fails R5. |
| **MLCO** | $4.295 | $4C Nov20 | 0.40 / 0.60, OI 10 | $4.60 | +7.1% | 6.55% | 11/4/0, $5.30 | **New, alive at the R6 edge.** Fails R6 by 2 cents at the ask (max BE $4.58), passes at mid ($4.50). R5 passes. R4 low $5.30 > BE, undated. |

## Tier B: dates, R6, chains

Print-move = prior close to first close after the print (PM prints: print-day close to next close; AM prints: prior close to print-day close).

| Ticker | Stock | Print (tool) | Last 4 print moves (%) | Median / cap | Max BE | Strikes / contract | Verdict |
|---|---|---|---|---|---|---|---|
| GRNT | $4.615 | Nov 5 PM, **verified** | -4.63, -5.99, -10.71, +4.72 | 5.36 / 8.04 | $4.99 | 2.5-wide only ($2.5/$5/$7.5) | **KILL, R6 (strike grid).** $5C BE is over $4.99 at any price; $2.5C fails R5. |
| TKC | $5.176 | Nov 5 PM, unverified | -3.49, -1.46, +1.51, +0.74 | 1.48 / 2.22 | $5.29 | $5C 0.20 / 0.75, OI 0 | **KILL, R6 + liquidity.** Needs ask <= $0.29; no market. |
| VYX | $6.755 | Nov 5 AM, unverified | -6.47, -9.35, +15.08, +7.21 | 8.28 / 12.42 | $7.59 | $7.5C 0.45 / 0.65 | **KILL, R6.** BE $8.15 needs +20.6% vs 12.42%; $5C fails R5. |
| ARLO | $12.64 | Nov 5 PM, unverified | -12.46, +27.15, +2.35, -1.55 | 7.40 / 11.10 | $14.04 | $12C 1.15 / 1.90 (OI 1); $13C 0.60 / 1.35 (OI 0) | **KILL, R5 + liquidity.** $14C needs ask <= $0.04. |
| MNTN | $10.281 | Nov 3 PM, unverified | -8.08, +37.15, -22.80, +3.78 | 15.44 / 23.16 | $12.66 | $10C 0.80 / 1.35 (OI 0); $12.5C 0.15 / 0.65 | **KILL, R5 + R6.** $10C bid alone over the line; $12.5C needs ask <= $0.16. |
| AHCO | $5.825 | Nov 3 AM, unverified | +17.38, -13.95, -9.89, -38.04 | 15.66 / 23.50 | $7.19 | 2.5-wide only ($5/$7.5) | **KILL, R5 + R6/R4 (strike grid).** $5C intrinsic $0.83 alone fails R5; $7.5C BE over both max BE and the $7 low target. |
| MLCO | $4.295 | Nov 5 AM, unverified | +3.83, -12.50, +4.91, -0.36 | 4.37 / 6.55 | $4.58 | $1-wide; $4C 0.40 / 0.60, OI 10 | **ALIVE, marginal.** Needs fill <= $0.58. Next: requote, date the $5.30 low (MarketBeat), R1 range. |

R1: all seven sit near the bottom of their trailing range per the Oct 5 sweep (prices in Nov 2025 were well above today on all of them, e.g. MLCO $8.10, AHCO $9.09, VYX $11.43). Not recomputed this run since all but MLCO died on chains; MLCO's R1 gets a fresh number before a doc.

## R3 only (new this run)

| Ticker | Stock | Ratings | Low target | Next |
|---|---|---|---|---|
| CWK | $12.335 | 8/5/0 | $15 | date, R6, chain |
| BRSL | $10.215 | 7/3/0 | $11.90 | date, R6, chain |
| PAR | $14.52 | 7/2/0 | $18 | date, R6, chain (likely R5 at this price) |

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R5 line:** max ask per share for one contract at the conviction tier (10% of reserve / 100 at 3.5/5).
- **R6 cap:** 1.5x the median earnings-day move over the last 4 prints; the needed move to breakeven must fit under it.
- **Max BE:** stock price x (1 + R6 cap); the highest breakeven Rule 6 allows.
- **Strike grid:** the spacing of listed strikes; 2.5-wide grids on a $5 stock often leave no strike that fits.
- **Stale floor:** a price target set before the stock's decline, or more than 60 days ago; it doesn't count for Rule 4 (binder Tab 6).
- **BE:** breakeven, strike + premium.
- **OI:** open interest, contracts outstanding.
- **AM / PM print:** earnings released before the open / after the close.
