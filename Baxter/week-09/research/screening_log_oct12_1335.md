# Screening log: Mon Oct 12, 2026, 1:35pm ET MIDDAY (VM, LIVE)

**Session job:** DO. Live queue re-tests (BTBT, ONDS real money; SE, HII, ALNY paper), then a new scanner slice in the **$25-50** band, which earlier runs today hadn't covered. Live quotes ~17:35 UTC. Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676. Ratings via `get_equity_analyst_ratings` this run. No web searches, no WebFetch.

## Live queue re-tests

| # | Name | Direction | Contract | Live quote | Stock | Test | Result |
|---|---|---|---|---|---|---|---|
| 1 | **BTBT** | CALLS (real money) | Jan15 $1C `25ebc8de` | 0.33 / 0.37, OI 2,242, spread 11.4% | $1.25 (-3.1%) | R6: BE at ask $1.37 vs max $1.353 (stock x 1.0823): needs +9.6% vs cap 8.23%. R7 passes. | **PARK, R6.** Passes at stock >= ~$1.266 with a $0.37 ask. |
| 2 | **ONDS** | CALLS (real money) | Dec18 $8C `cfbc25b7` | 0.46 / 0.48, OI 37,622 | $6.736 (+0.1%) | R6: BE at ask $8.48 vs max $8.143 (stock x 1.2089): needs +25.9% vs cap 20.89%. | **PARK, R6.** Needs stock ~$7.01 at a $0.48 ask. |
| 3 | **SE** | CALLS (paper) | Dec18 $95C `4fe7f5f7` | 8.70 / 9.75, OI **162** | $96.03 (+0.8%) | R7: OI 162 < 250. | **PARK, R7.** OI updates overnight. |
| 4 | **HII** | CALLS (paper) | Nov20 $270C `ad19b167` | 12.80 / 14.60, OI **232** | $265.84 | R7: OI 232. | **PARK, R7.** |
| 5 | **ALNY** | CALLS (paper) | Nov20 $230C `736ea6c9` | 15.70 / 18.80, OI **199** | $228.47 (-1.8%) | R7: OI 199. R6: BE at ask $248.80 vs max $247.20 (x 1.082): fails by $1.60. | **PARK, R7 + R6.** |

## Scanner slice (preview, not saved)

Market cap >= $300M, last **$25-50**, earnings (`FILTER_TYPE_EARNINGS_DATE`) **20261028-20261211**, 52w range pct expression < 0.25: **139 names.** 115 already appear in this week's week-09 files. 24 new.

Scanner note: `FILTER_TYPE_INSTRUMENT_TYPE` with `PREDICATE_IN_LIST` `["STOCK"]` is now rejected by the provider ("Predicate 'inList' requires signature 'symbol: string'"). Dropped it; market cap >= $300M kept the pool clean enough.

**R3 / coverage kills (15):**

| Name | Stock | B/H/S | Result |
|---|---|---|---|
| TBBK | $49.04 | no coverage | KILLED, R3 |
| BKE | $44.15 | no coverage | KILLED, R3 |
| SUPN | $42.67 | no coverage | KILLED, R3 |
| UVV | $42.10 | no coverage | KILLED, R3 |
| CCB | $41.57 | no coverage | KILLED, R3 |
| ELVR | $31.33 | no coverage | KILLED, R3 |
| GIII | $27.20 | no coverage | KILLED, R3 |
| WOLF | $26.83 | no coverage | KILLED, R3 |
| BBW | $25.55 | no coverage | KILLED, R3 |
| ROOT | $48.31 | 1/5/0 | KILLED, R3 |
| POR | $45.39 | 4/9/1 | KILLED, R3 (Buys < Holds) |
| FND | $44.77 | 7/14/4 | KILLED, R3 |
| VSNT | $30.81 | 3/4/1 | KILLED, R3 (Buys < Holds) |
| TRUP | $25.86 | 2/4/0 | KILLED, R3 |
| OXM | $25.27 | 0/6/0 | KILLED, R3 |

**R4-proxy kills (2):** tool low target is already under the stock price, so no call breakeven can clear it.

| Name | Stock | B/H/S, low | Result |
|---|---|---|---|
| LIF | $43.39 | 8/2/0, low $40 | KILLED, R4 (low < price) |
| CNM | $40.79 | 10/6/1, low $40 | KILLED, R4 (low < price) |

**R3 survivors taken to earnings + chain (3):**

| Name | Stock | B/H/S, low | Earnings | Median earnings move | Contract checked | Quote / OI | Result |
|---|---|---|---|---|---|---|---|
| **ALGM** | $34.075 (-4.2%) | 14/1/0, low $48 | Oct 29 AM **verified**, LY Oct 30 AM. Nov20 = 21 days past Oct 30: passes R2. 10-Q deadline Nov 9, 9 trading days before expiry. | 7.0% (last 6 tool-dated prints: 12.7, 7.3, 1.5, 9.9, 6.7, 1.8) -> R6 cap 10.5%, max BE $37.65 | Nov20 $32.5C / **$35C** / $37.5C / $30C | 3.90 / 4.30 OI 31; **2.75 / 2.90 OI 6,791 (spread 5.3%)**; 1.85 / 2.00 OI 74; 5.40 / 6.40 OI 34 | **PARK, R6** on the $35C: BE at ask $37.90 vs max $37.65, needs +11.2% vs 10.5%. Passes at stock >= ~$34.30 with a $2.90 ask. R7 passes. Paper candidate (ask x 100 = $290, far over the $67.63 real line). $32.5C passes R6 (+8.0%) but fails R7 (OI 31). Low $48 not yet dated by name. |
| **ATAT** | $32.82 | 25/0/0, low $39.71 | Nov 24 AM (f), LY Nov 25 (ADR, 6-K filer). Needs expiry >= Dec 16: no Dec listed, first is Feb19. | 4.65% -> cap 7.0%, max BE $35.12 | Feb19 $35C | 0.55 / 3.90, OI 106 | **KILLED, R7** (OI 106, spread 151%) and R6 (BE $38.90 at ask). |
| **LGN** | $48.85 (-5.2%) | 16/1/0, low $80 | Nov 13 AM (f), LY Nov 14. Needs expiry >= Dec 5: no Dec listed, first is Feb19. | 9.45% (4 prints only) -> cap 14.2%, max BE $55.79 | Feb19 $50C | 7.30 / 10.00, OI 13 | **KILLED, R7** (OI 13, spread 31%) and R6 (BE $60.00 at ask). |

**R3 survivors not yet chain-checked (queued for the next run):** KNF (6/4/1, low $54, $49.61, Nov 3 AM (f), LY Nov 4 -> Dec18), TPG (13/4/0, low $47, $44.96, Oct 29 AM verified, LY Nov 4 -> Dec18; low $47 leaves almost no room over BE), NYAX (6/2/0, low $68, $44.76, Nov 18 AM (f), LY Nov 19, likely 6-K filer -> Dec18 only if both dates hold, 8 days of slack), GGAL (5/3/0, low $50, $36.79; `get_earnings_results` returns scrambled quarter labels, R2 unverifiable from the tool).

**Moved:** 27 names (5 queue re-tests, 15 R3 kills, 2 R4 kills, 3 to the chain stage, 4 to the queue at R3-passed). 0 entries, 19 kills.

**Real-money entry:** none. BTBT and ONDS still fail R6 on the live ask. No doc with this-run numbers exists for either exact contract.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry (21-day cushion on the later of tool date and last year's date), R3 analyst consensus (calls: at most 1 Sell, at least 3 Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability, R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike.
- **Spread % of mid:** (ask - bid) / mid.
- **(f):** earnings date not company-verified.
- **LY:** last year's same-quarter report date.
- **ADR / 6-K filer:** foreign company; no 10-Q deadline backstop, so R2 needs both dates.
- **Median earnings move:** median absolute close-to-close move on the report day (AM prints) across the listed prints.
- **PARK:** alive, waiting on one specific check or price; stays on the queue.
- **Preview scan:** a scanner run that isn't saved as a scan.
