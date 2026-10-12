# Screening log: Mon Oct 12, 2026, 10:35am ET MIDDAY (VM, LIVE)

**Session job:** DO, OPEN's MIDDAY plan, up to 10 names. Live quotes 14:35-14:36 UTC. Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676. Ratings via `get_equity_analyst_ratings` this run. 2 WebFetches (MarketBeat TMUS, SE), 1 web search (TMUS upgrade, came back with 2024 articles only).

| # | Name | Direction | Contract | Live quote | Stock | Test | Result |
|---|---|---|---|---|---|---|---|
| 1 | **BTBT** | CALLS (real money) | Jan15 $1C `25ebc8de` | 0.32 / 0.40, OI 2,242, spread 22% | $1.25 (-3.1%) | R6: BE at ask $1.40 vs max $1.3529 (stock x 1.0823): needs +12.0% vs cap 8.23%. R7 now passes (22%). | **PARK, R6.** Needs the stock ~$1.30 at a $0.40 ask, or the ask ~$0.35 here. |
| 2 | **ONDS** | CALLS (real money) | Dec18 $8C `cfbc25b7` | 0.48 / 0.50 (ask size 1), OI 37,622 | $6.765 (+0.5%) | R6: BE at ask $8.50 vs max $8.178 (stock x 1.2089): needs +25.6% vs cap 20.89% | **PARK, R6.** Needs the stock ~$7.03 at a $0.50 ask. |
| 3 | **TMUS** | CALLS (paper) | Nov20 $160C `571117e7-6f1e-4733-be01-b46c852c4fff` | 5.00 / 5.20, OI 540, vol 45, spread 3.9% | $153.17 (+3.1%) | R1: advanced in the Oct 9 paper scan at $149; stock +2.7% since, still bottom quartile. R2: Oct 28 PM **verified**; LY Oct 23 AM; Nov 20 is 23 days after Oct 28 (>= 21); 10-Q deadline Nov 9 is 9 trading days before expiry. R3: 27/4/0. **R4: Raymond James upgrade to Outperform $170, dated Oct 12** (MarketBeat; first Buy-side target published after the Oct 9 -13% drop; Scotiabank Sector Outperform $212 on Oct 9 too). Tool low $169 (stamp Oct 8). Both > BE $165.20. R6: BE $165.20 needs +7.85% vs cap 8.95% (median 5.96%, Oct 9 bars) -> max BE $166.88. R7: OI 540, spread 3.9%. | **PAPER ENTRY @ $5.20.** $150C (OI 242) and $155C (OI 202) fail R7. |
| 4 | **SE** | CALLS (paper) | Dec18 $95C `4fe7f5f7` | 8.80 / 9.35, OI **162** | $95.45 | R4 now dated: MarketBeat lowest Buy after Aug 13 = Arete Buy $152 (Sep 7), inside 60 days. BE at ask $104.35. R7: OI 162 < 250. | **PARK, R7** (R4 cleared). |
| 5 | **HII** | CALLS (paper) | Nov20 $270C `ad19b167` | 13.80 / 15.50, OI **232** | $267.42 | R7: OI 232 (OI updates overnight) | **PARK, R7.** Tuesday OPEN re-check. |
| 6 | **ALNY** | CALLS (paper) | Nov20 $230C `736ea6c9` | 15.70 / 19.10, OI **199** | $229.47 (-1.4%) | R7: OI 199. R6: BE at ask $249.10 vs max 229.47 x 1.082 = $248.29: fails by 81 cents. | **PARK, R7 + R6.** |
| 7 | **ULS** | CALLS (paper) | Jan15 $70C `3bfe8e8e` / $75C `d77c1372` | 4.90 / 8.10 OI 142; 2.70 / 5.70 OI 85 | $71.23 | R7: OI 142 / 85, spreads 49% / 71%. Q3 Nov 3 AM (f). | **KILLED, R7.** |

**Moved:** 7 names. 1 paper entry (TMUS $160C Nov20), 1 killed (ULS R7), 5 parked (BTBT R6, ONDS R6, SE R7, HII R7, ALNY R7/R6).

**Refill:** Tier B of `full_sweep_oct05.md` is fished out (every name checked against this week's logs has been screened at least once). The queue holds 5 live names; EVENING 1 re-runs the Saturday sweep scan with the window moved forward (prints Oct 28 - Dec 11).

**Real-money entry:** none. BTBT and ONDS (the only names under the $0.676 line) both fail R6 on the live ask; neither has a doc with this-run numbers for the exact contract.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability, R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike.
- **Spread % of mid:** (ask - bid) / mid.
- **(f):** earnings date not company-verified.
- **PARK:** alive, waiting on one specific check or price; stays on the queue.
- **Paper entry:** logged in `paper_book.md` at the live ask, no money.
