# Screening log: Mon Oct 19, 1:35pm ET (MIDDAY)

**Session job:** DO, 10 names (the 12:35 plan: COUR first, MSTR R1, FLUT ask, CLSK revive line, NRG R6, then free R6 re-quotes on the floor-gated names). Live quotes 17:35 UTC. Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676. Ratings re-pulled for all 11 queue names. One change: **NRG's low target reads $131 (was $159)** with the stamp still Oct 3. Everything else identical (FLUT stamp Oct 16, NXT Oct 13, TTWO Aug 7).

| # | Ticker | Direction | Contract | Quote | Stock | Check | Result |
|---|--------|-----------|----------|-------|-------|-------|--------|
| 1 | **MSTR** | CALLS (paper) | Nov20 $120C `da3b54fb` | 21.45 / 22.95, OI 1,764, spread 6.8% | **$137.37** (+0.4%) | **R1: under the $137.90 line by $0.53, passes again.** R6 at the ask: BE $142.95, +4.1% vs 7.82% (passes). R7 pass. R3 20/2/0. | **PARK, floor gate.** One search: the dated cuts it found are TD Cowen $260 Buy, Mizuho $265, Monness Crespi $175 (undated in the result), Canaccord $130 Hold (Jun 30, a Hold, doesn't count). The tool's $165 low still has no owner or date. |
| 2 | **CIFR** | CALLS (paper) | Dec18 $10C `f9efed33` | 1.26 / 1.34, OI 3,469, spread 6.2% | $9.085 | R6 at the ask: BE $11.34, +24.8% vs 28.27% | **PARK, floor gate** ($18, nothing dated after Oct 14). Kill Fri Oct 30. |
| 3 | **UEC** | CALLS (paper) | Jan15 $7C `60caab3b` | 1.44 / 1.59, OI 1,812 | $7.90 | R6: BE $8.59, +8.7% vs 10.67% | **PARK, floor gate** ($10, 2025-era). |
| 4 | **RIOT** | CALLS (paper) | Nov20 $13C `e6e7ea4c` | 2.10 / 2.24, OI 669, spread 6.5% | $14.095 (+2.7%) | R6: BE $15.24, +8.1% vs 10.69% | **PARK, no dated floor.** Kill Tue Oct 27. |
| 5 | **FLUT** | CALLS (paper) | Jan15 $75C `a5b4198b` | 8.30 / 10.50, OI 772, spread 23.4% | $75.655 | R4 at the ask: BE $85.50 vs $85 low, **fails by $0.50** | **PARK** (ask <= $9.95 needed). |
| 6 | **NRG** | CALLS (paper) | Dec18 $105C `6fa30201` | 6.10 / 6.60, OI 517, spread 7.9% | $99.545 (-4.1%) | R6: BE $111.60, +12.1% vs 13.42% (margin 1.3 pt). Low target **$131** (was $159): still $19.40 over BE. | **PARK, floor gate** (stamp Oct 3; the drop to $131 is new information about the floor, not a date). Kill Mon Nov 2. |
| 7 | **NXT** | CALLS (paper) | Nov20 $80C `c1c39e5f` | 6.70 / 7.20, OI 275 | $78.95 (-1.4%) | R6: BE $87.20, +10.4% vs 13.14% | **PARK, floor gate** ($101, Oct 13). Kill Mon Oct 26. |
| 8 | **INSM** | CALLS (paper) | Nov20 $105C `dc6214c4` | 4.00 / 4.40, OI 5,116, spread 9.5% | $96.47 | R6: BE $109.40, +13.4% vs 17.1% | **PARK, floor gate.** Kill Mon Oct 26. |
| 9 | **PL** | CALLS (paper) | Jan15 $10C `bb9b3f83` | 4.20 / 4.60, OI 4,181 | $13.65 | R6: BE $14.60, +7.0% | **PARK, floor gate** ($17, undated). |
| 10 | **TTWO / PAAS** | CALLS (paper) | Dec18 $190C / Jan15 $40C | TTWO 24.90 / 27.40 | TTWO $204.715, PAAS $44.46 | TTWO stamp still Aug 7. PAAS over its $42.31 R1 line. | **PARK** (R4 dating; R1). |

**Watch line (free re-quote):** ONDS $6.17 (revive >= ~$6.90: no), BTBT $0.9289 (>= ~$1.10: no), CLSK $8.66 (> ~$9.20: no; Dec18 $9C 1.11 / 1.22).

**Moved this run:** 10 names re-tested. 0 killed, 0 advanced. MSTR cleared R1 again (stock $137.37), so it's waiting on the floor only now; 1 web search, floor still undated. NRG's low target fell $159 -> $131 with no new stamp.

**Real-money entry:** none. No real-money doc exists, and nothing under the $0.676 line passes R6.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability, R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + ask.
- **OI (open interest):** contracts outstanding on that strike, set once a day before the open.
- **Spread % of mid:** (ask - bid) / mid.
- **Floor gate:** the low target exists but isn't dated within 60 days and after the decline (binder Tab 6), so R4 can't pass yet.
- **PARK:** alive, waiting on one specific check or price; stays on the queue.
- **Paper / real:** paper-book candidate vs. a contract the real fund could afford.
