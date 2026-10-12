# Screening log: Mon Oct 12, 2026, 11:35am ET MIDDAY (VM, LIVE)

**Session job:** DO, the 10:35 MIDDAY's plan (BTBT and ONDS R6 re-tests), the rest of the live queue, then a small sub-$10 scanner slice for new real-money names. Live quotes 15:34-15:36 UTC. Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676. Ratings via `get_equity_analyst_ratings` this run. No web searches, no WebFetch.

## Live queue re-tests

| # | Name | Direction | Contract | Live quote | Stock | Test | Result |
|---|---|---|---|---|---|---|---|
| 1 | **BTBT** | CALLS (real money) | Jan15 $1C `25ebc8de` | 0.33 / 0.37, OI 2,242, spread 11.4% | $1.245 (-3.5%) | R6: BE at ask $1.37 vs max $1.3475 (stock x 1.0823): needs +10.0% vs cap 8.23%. R7 passes. Low target $3.50 (6/0/0). | **PARK, R6.** Passes at stock >= ~$1.266 with a $0.37 ask. |
| 2 | **ONDS** | CALLS (real money) | Dec18 $8C `cfbc25b7` | 0.47 / 0.50, OI 37,622 | $6.755 (+0.4%) | R6: BE at ask $8.50 vs max $8.166 (stock x 1.2089): needs +25.8% vs cap 20.89%. 11/0/0, low $13. | **PARK, R6.** Needs stock ~$7.03 at a $0.50 ask. |
| 3 | **SE** | CALLS (paper) | Dec18 $95C `4fe7f5f7` | 8.70 / 10.15, OI **162** | $96.635 (+1.5%) | R7: OI 162 < 250 (spread 15.4% passes). | **PARK, R7.** OI updates overnight. |
| 4 | **HII** | CALLS (paper) | Nov20 $270C `ad19b167` | 13.80 / 15.50, OI **232** | $266.20 | R7: OI 232. | **PARK, R7.** |
| 5 | **ALNY** | CALLS (paper) | Nov20 $230C `736ea6c9` | 16.50 / 18.90, OI **199** | $229.53 (-1.4%) | R7: OI 199. R6: BE at ask $248.90 vs max $248.35 (x 1.082): fails by $0.55. | **PARK, R7 + R6.** |

## Scanner slice (preview, not saved)

Market cap $300M+, stock, earnings **Oct 28 - Dec 11**, last $1-10, 52w range pct < 0.25, call volume today >= 300: **87 names.** Checked each against this week's logs: 83 already screened at least once in week-09. Four never seen: CTNM, MNKD, KDK, GEVO. R3 re-pulled on those plus 17 names with only one prior mention.

| Name | Stock | Ratings (B/H/S, low) | Earnings | Contract checked | Quote / OI | Result |
|---|---|---|---|---|---|---|
| **CTNM** | $9.63 (**-28.0% today**) | 7/1/0, $17 (pre-drop) | Oct 29 PM (f), LY Oct 30 PM -> Nov20 = 21 days, passes R2 | Nov20 $10C `f7f32669`; $12.5C `60d15183` | 0.80 / 1.75, OI **3**; 0 / 4.40, OI 1 | **KILLED, R7** (also R4: every target predates today's drop, cause unknown) |
| **MNKD** | $3.14 (-4.6%) | 7/1/0, $4.75 | Nov 4 AM (f), LY Nov 5 AM -> Nov27 = 22 days | Nov27 $3C `6cdb6207`, $4C `ed0cd855`; Jan15 $3C `a1907c10`, $4C `6878bbd4` | Nov27: OI 0 / 1. Jan15 $3C 0.30 / 1.00 OI 3,169 (spread 108%); $4C 0.15 / 0.75 OI 1,971 (spread 133%) | **KILLED, R7** (Nov27 no OI, Jan15 spreads way over 25%; Jan15 $3C ask also over the R5 line) |
| **KDK** | $1.715 (+2.7%) | 8/2/0, $8 (stale vs a $1.7 stock) | Nov 11 PM (f), LY Nov 12 PM -> Dec18 | Dec18 $2C `b2aae634`; $1.5C `7fb03607` | 0.15 / 0.25, OI **81**; 0.15 / 1.00, OI 0 | **KILLED, R7** |
| GEVO | $1.305 | no coverage | | | | **KILLED, R3** |
| SGML, ABTC, SSYS, CRML, JMIA, ASM, NAK | | no coverage | | | | **KILLED, R3** (re-confirmed) |
| NVTS 2/4/1, ADT 2/5/1, GEMI 3/4/3, UWMC 3/7/0, IQ 8/9/1, PLUG 8/12/3 | | Buys not a majority / Sells | | | | **KILLED, R3** (re-confirmed) |
| UEC, TIGR, NB, KEEL | | pass R3 | | | | Already killed this week (UEC/TIGR R4, NB/KEEL R6). Not re-chained. |

**Moved:** 8 names through a funnel stage (5 queue re-tests, 3 new to the chain stage), plus R3 on 17 more. 0 entries, 3 new kills on R7. The sub-$10 universe for Oct 28 - Dec 11 prints is close to fished out on this filter set; EVENING 1's full sweep should widen it (drop the call-volume floor, add the $10-25 band).

**Real-money entry:** none. BTBT and ONDS still fail R6 on the live ask. No doc with this-run numbers exists for either exact contract.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry (21-day cushion on the later of tool date and last year's date), R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability, R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike.
- **Spread % of mid:** (ask - bid) / mid.
- **(f):** earnings date not company-verified.
- **LY:** last year's same-quarter report date.
- **PARK:** alive, waiting on one specific check or price; stays on the queue.
- **Preview scan:** a scanner run that isn't saved as a scan.
