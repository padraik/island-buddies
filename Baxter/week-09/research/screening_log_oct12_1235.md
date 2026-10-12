# Screening log: Mon Oct 12, 2026, 12:35pm ET MIDDAY (VM, LIVE)

**Session job:** DO. Live queue re-tests (BTBT, ONDS real money; SE, HII, ALNY paper), then a new scanner slice in the $10-25 band, which earlier runs this week hadn't covered on a call-OI basis. Live quotes 16:35 UTC. Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676. Ratings via `get_equity_analyst_ratings` this run. No web searches, no WebFetch.

## Live queue re-tests

| # | Name | Direction | Contract | Live quote | Stock | Test | Result |
|---|---|---|---|---|---|---|---|
| 1 | **BTBT** | CALLS (real money) | Jan15 $1C `25ebc8de` | 0.33 / 0.37, OI 2,242, spread 11.4% | $1.2466 (-3.4%) | R6: BE at ask $1.37 vs max $1.3492 (stock x 1.0823): needs +9.9% vs cap 8.23%. R7 passes. 6/0/0, low $3.50. | **PARK, R6.** Passes at stock >= ~$1.266 with a $0.37 ask. |
| 2 | **ONDS** | CALLS (real money) | Dec18 $8C `cfbc25b7` | 0.45 / 0.48, OI 37,622 | $6.705 (-0.4%) | R6: BE at ask $8.48 vs max $8.106 (stock x 1.2089): needs +26.5% vs cap 20.89%. 11/0/0, low $13. | **PARK, R6.** Needs stock ~$7.01 at a $0.48 ask. |
| 3 | **SE** | CALLS (paper) | Dec18 $95C `4fe7f5f7` | 8.70 / 10.05, OI **162** | $96.49 (+1.3%) | R7: OI 162 < 250. | **PARK, R7.** OI updates overnight. |
| 4 | **HII** | CALLS (paper) | Nov20 $270C `ad19b167` | 12.70 / 13.80, OI **232** | $265.27 | R7: OI 232. | **PARK, R7.** |
| 5 | **ALNY** | CALLS (paper) | Nov20 $230C `736ea6c9` | 15.60 / 18.80, OI **199** | $229.57 (-1.3%) | R7: OI 199. R6: BE at ask $248.80 vs max $248.39 (x 1.082): fails by $0.41. | **PARK, R7 + R6.** |

## Scanner slice (preview, not saved)

Stock, market cap >= $300M, last **$10-25**, earnings (`fundamental.earningsYmd`) **20261028-20261211**, total call OI (1d) >= 2,000, 52w range pct < 0.25: **97 names.** 89 already appear in this week's logs. Eight new: GLIBK, RYN, YELP, WSC, BBWI, DYN, IMXI, HLIT.

Scanner note for the next Baxter: `FILTER_TYPE_EARNINGS_DATE` rejects ISO dates and returns 0 rows on epoch millis; it parses `YYYYMMDD` (e.g. `20261028`) without error.

| Name | Stock | Ratings (B/H/S, low) | Earnings | Contract checked | Quote / OI | Result |
|---|---|---|---|---|---|---|
| GLIBK | $19.93 | no coverage | | | | **KILLED, R3** |
| IMXI | $11.565 | no coverage | | | | **KILLED, R3** |
| RYN | $18.84 | 2/4/0 | | | | **KILLED, R3** (Buys < Holds, < 3 Buys) |
| YELP | $18.56 | 2/8/2 | | | | **KILLED, R3** |
| WSC | $17.545 | 4/7/0 | | | | **KILLED, R3** (Buys < Holds) |
| BBWI | $17.235 | 7/13/1 | | | | **KILLED, R3** (Buys < Holds) |
| **DYN** | $16.205 (-2.6%) | 16/0/1, low $10 | Nov 4 AM (f), LY Nov 5 AM. Nov20 is 15 days past Nov 5: fails R2. Dec18 = 43 days, passes. | Dec18 $16C / $17.5C / $19C / $20C | 1.45 / 2.70 OI 46; 0.45 / 2.00 OI 114; 0.55 / 1.15 OI 17; 0.50 / 0.85 OI 531 (spread 52%) | **KILLED, R7** (no strike near the money with OI >= 250 and spread <= 25%). The $20C ask $0.85 is also over the R5 line. |
| **HLIT** | $10.655 (-3.0%) | 4/2/1, low $8 | Nov 2 PM (f), LY Nov 3 PM. Nov20 = 17 days: fails R2. Jan15 passes. No Dec expiry listed. | Jan15 $12.5C / $15C | 0.60 / 1.40 OI 468 (spread 80%); 0.25 / 0.65 OI 3,308 (spread 89%) | **KILLED, R7** (spreads) |

**Moved:** 13 names (5 queue re-tests, 2 new to the chain stage, 6 R3 kills). 0 entries, 8 kills (6 R3, 2 R7). The $10-25 band with prints Oct 28 - Dec 11 is now almost fully screened this week too: 89 of 97 had already been seen.

**Real-money entry:** none. BTBT and ONDS still fail R6 on the live ask. No doc with this-run numbers exists for either exact contract.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry (21-day cushion on the later of tool date and last year's date), R3 analyst consensus (calls: at most 1 Sell, at least 3 Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability, R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike.
- **Spread % of mid:** (ask - bid) / mid.
- **(f):** earnings date not company-verified.
- **LY:** last year's same-quarter report date.
- **PARK:** alive, waiting on one specific check or price; stays on the queue.
- **Preview scan:** a scanner run that isn't saved as a scan.
