# Screening log, Tue Oct 20, MIDDAY (12:35pm ET): DONE

*Quotes 12:35-12:37pm ET. No web searches. Live chains: APH Nov20 $80C; MOD Nov20 + Dec18; FTAI Nov20; AXON Nov27 + Dec18; AVAV Jan15. Earnings dates from `get_earnings_results`. Refill: ratings + quotes (free) on eight earlier week-09 R7 / floor-gate kills.*

## Held: COUR $5C Nov20

| Check | Result |
|---|---|
| Quote (12:35) | 0.50 / 0.55 (bid size 49, ask size 19, vol 1), mark 0.525, OI 3,235, IV 82.8% |
| Stock | $5.0715 (+1.4%), 5.07 / 5.08 |
| Q3 | Thu Oct 29 PM, `verified: true`, `actual: null` (LY Oct 23 PM) |
| Rule 4 | 8/4/0, low **$6.00** vs BE $5.65: holds |
| Filings | none since Oct 15 (index empty) |
| Tab 4 | nothing fires. Bid 0.50 = -23.1% |

## Queue: names moved

| # | Name | Contract | Stock (12:35) | Live quote | Ratings (B/H/S, low) | Result |
|---|---|---|---|---|---|---|
| 1 | APH | Nov20 $80C `d254aa6a` | $79.14 (-1.4%) | 3.90 / 4.20, OI 5,713, spread 7.4% | 22/2/0, $90 (stamp Oct 3) | **PARK, R6 still fails.** BE $84.20 at the ask = **+6.39%** vs the 6.07% cap (needs an ask <= $3.94 at this stock price). The ask widened 4.10 -> 4.20 even though the stock went up a little. Kill **Fri Oct 23**. |
| 2 | MOD | Nov20 $150C `62003c6d`; Dec18 $150C `9f224b9a`, $160C `cb99d50f` | $149.48 (-0.1%) | Nov20 15.00 / 16.20, **OI 5**; Dec18 $150C 18.60 / 19.90, **OI 0**; $160C 14.50 / 15.80, **OI 27** | 11/0/0, $260 | **KILL R2 (Nov20) + R7 (Dec18).** The tool date is now **Tue Nov 3 PM** (`verified: false`; LY Oct 28 PM). Nov 20 is 17 days after it, short of the 21 needed. Dec18 passes R2 but the near-money OI is 0 and 27. |
| 3 | FTAI | Nov20 $160C / $165C / $170C | $160.51 (-1.7%) | 13.20 / 15.40 (**OI 12**), 10.90 / 13.30 (**OI 9**), 9.30 / 10.20 (**OI 7**) | 13/0/0, $275 | **KILL R7.** R2 passes (Oct 29 AM `verified: true`, 22 days). No near-money strike has more than 12 contracts open, and the $160C spread is 15%. |
| 4 | AXON | Nov27 $400C / $410C; Dec18 $400C / $410C | $397.67 (+3.8%) | Nov27 34.00 / 40.30 (**OI 1**), 29.10 / 35.90 (**OI 2**); Dec18 41.60 / 45.90 (**OI 52**), 37.10 / 40.90 (**OI 46**) | 21/3/0, $470 (stamp Oct 8) | **KILL R7.** Q3 Nov 3 PM (f), LY Nov 4: Nov20 fails R2 (16 days), Nov27 and Dec18 pass. All four near-money contracts are under 60 OI. |
| 5 | AVAV | Jan15 $120C / $125C / $135C | $118.63 (+0.6%) | 14.30 / 16.50 (**OI 148**), 12.30 / 14.60 (**OI 36**), 9.10 / 10.70 (**OI 127**) | 20/5/0, $165 | **KILL R7.** R2 passes (Dec 8 PM (f), LY Dec 9; Jan 15 is 37 days later). OI went up from 93 on the $135C, but it's still 127. |
| 6 | TTWO | n/a | $205.505 (+0.3%) | not pulled | 29/1/1, $270 (stamp Aug 7) | **PARK.** Stamp unchanged, now 74 days old. |

## Refill (free re-check of week-09 kills; each goes on the queue with its next check)

| Name | Stock (12:35) | Ratings (B/H/S, low) | Original kill | Why it's back / next check |
|---|---|---|---|---|
| MDGL | $464.14 (+3.8%) | 20/1/0, $533 | R7 (Dec18 $450C OI 12, Oct 16 E1); passed R6 and R4 | R4 margin is still wide. Next: re-check Dec18 $450C/$460C OI + spread, then R6 at the live ask |
| CIFR | $8.894 (-0.5%) | 23/2/0, $18 | Floor gate (Dec18 $10C, Oct 16-17) | $18 low needs a date after the Oct 14 convert. Next: Dec18 $10C re-quote (R6 was +26.2% vs 28.27%), then one floor search |
| UEC | $7.94 (+0.6%) | 8/3/0, $10 | Floor gate (Jan15 $7C, Oct 16 E3) | Next: Jan15 $7C re-quote + R6, then one search for who owns the $10 and when |
| SNDX | $13.31 (+1.7%) | 12/0/0, $23 | R7 (Oct 16 E2) | Next: re-pull the chain at its post-print expiry, OI on near-money |
| CENX | $33.685 (-2.0%) | 6/1/0, $40 | R7 (Oct 16 E2) | Next: OI re-check on near-money; R4 room only ~19% |
| ACMR | $55.34 (-1.3%) | 8/1/0, $100 | R7 (Oct 17 Sat) | Next: OI re-check |
| UCTT | $52.40 (-0.8%) | 6/0/0, $120 | R7 (Oct 17 Sat) | Next: OI re-check |
| BX | $110.83 (+3.5%) | 15/11/1, $116 (stamp Oct 13) | R7 (Oct 17 Sat) | R3 passes (15 >= 11, one Sell). R4 room is thin ($116 vs $110.83). Next: OI re-check, and it's last in line |

**Moved this run:** 6 names. 4 killed (MOD R2 + R7, FTAI R7, AXON R7, AVAV R7), 2 parked (APH R6, TTWO floor). 0 searches. 8 refilled. Pattern: every one of the four "fat floor, thin chain" names is still thin. OI on mid-cap $100-400 names barely moves day to day, so these four shouldn't come back without a fresh scan saying their volume changed.

## GLOSSARY

- **R1-R7**: binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 ratings consensus, R4 bear floor (lowest Buy target > breakeven), R5 price cap, R6 reachability (needed move <= 1.5x median print reaction), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + premium paid.
- **OI**: open interest, contracts outstanding.
- **(f)**: `verified: false` earnings date (estimated from cadence).
- **LY**: last year's same-quarter report date.
- **Floor gate**: the lowest Buy target passes on price but isn't proven dated within 60 days and after the decline (Tab 6).
- **Paper**: tracked in `paper_book.md`, no money.
