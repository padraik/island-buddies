# Screening log, Tue Oct 20, MIDDAY (1:35pm ET): DONE

*Quotes 1:35-1:37pm ET. Two web searches (CIFR $18, UEC $10). Live chains: APH Nov20 $80C; MDGL Dec18 $450C-$480C; CIFR Dec18 $10C; UEC Jan15 $7C; UCTT Nov20 $50C/$55C/$60C; SNDX Dec18 $13C-$15C; ACMR Dec18 $55C-$60C. Earnings dates from `get_earnings_results`. UCTT print base from daily bars. Refill: ratings + quotes (free) on APTV, GFS, INSM, PL.*

## Held: COUR $5C Nov20

| Check | Result |
|---|---|
| Quote (1:35) | 0.50 / 0.55 (bid size 52, ask size 20, vol 2), mark 0.525, OI 3,235, IV 82.0% |
| Stock | $5.08 (+1.6%), 5.07 / 5.08 |
| Q3 | Thu Oct 29 PM, `verified: true`, `actual: null` (LY Oct 23 PM) |
| Rule 4 | 8/4/0, low **$6.00** vs BE $5.65: holds |
| Filings | none since Oct 15 (index empty) |
| Tab 4 | nothing fires. Bid 0.50 = -23.1% |

## Queue: names moved

| # | Name | Contract | Stock (1:35) | Live quote | Ratings (B/H/S, low) | Result |
|---|---|---|---|---|---|---|
| 1 | APH | Nov20 $80C `d254aa6a` | $78.985 (-1.6%) | 3.80 / 4.20, OI 5,713, spread 10.0% | 22/2/0, $90 (stamp Oct 3) | **PARK, R6 fails.** BE $84.20 at the ask = **+6.60%** vs 6.07% cap. Needs an ask <= $3.78 at this stock price. Kill **Fri Oct 23**. |
| 2 | MDGL | Dec18 $450C/$460C/$470C/$480C | $463.59 (+3.7%) | 47.30/53.00, 42.90/47.50, 37.60/42.90, 34.00/38.30 | 20/1/0, $533 | **KILLED (R7).** OI 8 / 90 / 9 / 10. R2 would pass (Nov 3 AM verified, LY Nov 4, Dec18 = 44 days). OI hasn't built in four days. |
| 3 | CIFR | Dec18 $10C `f9efed33` | $8.765 (-2.0%) | 1.15 / 1.17, OI 3,484, spread 1.7% | 23/2/0, $18 | **KILLED (R4, Tab 6 stale floor).** R6 passes: BE $11.17 = +27.4% vs 28.27%. R7 passes. R2: Nov 2 AM (f), LY Nov 3, Dec18 = 45 days. The one search found the $18 as **JP Morgan, raised $12 -> $18 on Nov 24, 2025**, with the stock near $19. A year-old raise, pre-decline, not a floor dated after the Oct 14 convert. |
| 4 | UEC | Jan15 $7C `60caab3b` | $7.925 (+0.4%) | 1.48 / 1.61, OI 1,812, spread 8.4% | 8/3/0, $10 | **KILLED (R4, Tab 6 stale floor).** R6 passes: BE $8.61 = +8.6% vs 10.67%. R2: Dec 9 AM (f), LY Dec 10, Jan15 = 36 days. The one search found $10-area lines only from 2025 (National Bankshares $10 Outperform, Roth $9.75 -> $10.25, MarketBeat mean $10.60, all 2025 era); the current-year actions are far higher (HC Wainwright $26.75, Mar 11 2026; Goldman $18). The $10 is a stale 2025 line. |
| 5 | UCTT | Nov20 $55C `62b2ff7b` | $52.405 (-0.7%) | 4.50 / 4.80, OI 734, spread 6.5% | 6/0/0, $120 | **KILLED (R6).** R2 passes (Oct 27 PM verified, LY Oct 28, Nov20 = 23 days). BE $59.80 = **+14.1%** vs cap **9.87%**. Prints (PM, next-day close vs print-day close): Apr 28 '25 -13.90, Jul 28 '25 -0.61, Oct 28 '25 -4.19, Feb 23 '26 +17.18, Apr 28 '26 -7.97, Aug 3 '26 -5.19; median 6.58%. $50C (BE ~$57) OI 11 fails R7; $60C OI 112 fails R7. Note: the $120 low on an $52 stock (down from $89 at the Aug print) is itself a stale-floor shape. |
| 6 | SNDX | Dec18 $13C/$14C/$15C | $13.285 (+1.5%) | 1.70/2.45, 1.25/1.70, 0.95/1.30 | 12/0/0, $23 | **KILLED (R7).** OI 0 on all three. R2: Nov 2 PM (f), LY Nov 3. |
| 7 | ACMR | Dec18 $55C/$57.5C/$60C | $55.14 (-1.7%) | 6.80/7.80, 5.90/6.60, 5.10/5.60 | 8/1/0, $100 | **KILLED (R7).** OI 1 / 1 / 15. R2: Nov 5 AM verified, LY Nov 5. Nov27 not pulled (weeklies are thinner than the monthly on every name this week). |
| 8 | TTWO | (none) | $205.76 (+0.4%) | n/a | 29/1/1, $270 (stamp **Aug 7**, unchanged) | **PARK**, free re-check only. |

**Moved this run:** 8 names. 6 killed (MDGL R7, CIFR R4, UEC R4, UCTT R6, SNDX R7, ACMR R7), 2 parked (APH R6, TTWO floor). 2 searches.

## Refill (free)

| Name | Stock | Ratings (B/H/S, low) | Why it's on the queue |
|---|---|---|---|
| **GFS** | $47.60 (+3.2%) | 14/9/1, **$51**, stamp **Oct 15** | Killed Oct 16 E2 on R4 ($51.10 BE vs $51 low). The tool stamp moved to **Oct 15**, so the $51 may now be a dated post-decline floor. Next: earnings date, chain at the first R2 expiry, R4 at the live ask. |
| APTV | $44.975 (+1.1%) | 17/4/0, $50 | Killed Oct 19 on R7 (Dec18 $45C OI 2). Next: Dec18 OI re-check. |
| INSM | $95.16 (-0.1%) | 24/1/0, $165 | Floor-parked Oct 16 E1. Low is +73% over the stock: the stale-floor shape. Next: earnings date + chain, then one floor search. |
| PL | $13.495 (-0.7%) | 8/5/0, $17 | Floor-parked Oct 16 E1. Next: earnings date + chain. |

Queue after this run: **8 live + 3 watch** (GFS, APH, APTV, INSM, PL, CENX, BX, TTWO; watch ONDS, BTBT, CLSK).

**Pattern, honestly:** this is the fifth MIDDAY in a row where the kills sort into two bins. Names with a real chain have a floor that turns out to be a 2025 line (CIFR, UEC today; ALGM, NXT, NRG, CLS earlier). Names with a fat, current floor have no chain (MDGL, SNDX, ACMR today; MOD, FTAI, AXON, AVAV at 12:35). GFS is the first name all day whose tool stamp is actually recent.

## GLOSSARY

- **R1-R7**: binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 ratings consensus, R4 bear floor (lowest Buy target > breakeven), R5 price cap, R6 reachability (needed move <= 1.5x median print reaction), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + premium paid (at the ask, for screening).
- **OI**: open interest, contracts outstanding.
- **(f)**: `verified: false` earnings date (estimated from cadence).
- **LY**: last year's same-quarter report date.
- **Stamp**: the `updated_at` on the analyst-ratings tool result, the last time the target set changed.
- **Floor gate / stale floor (Tab 6)**: a Rule 4 floor must be dated within 60 days and published after the decline; a year-old raise isn't a floor.
- **Paper**: tracked in `paper_book.md`, no money.
