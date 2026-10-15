# SCREENING LOG: Thu Oct 15, 6:00pm ET (EVENING 1)

Fresh $15-50 scanner pass, as the WRAP queue asked. 23 names moved past the ratings screen (14 to earnings + R6 math, 9 chain-checked); 1 advanced (LBRT, paper, gated on a dated floor), the rest killed. Another 62 names were cut free at the ratings screen (R3 or no coverage). One web search (LBRT floor).

## Scan

Preview (not saved): market cap >= $300M, `FILTER_TYPE_EARNINGS_DATE` 20261020-20261218, 52w range pct expression < 0.25, `FILTER_TYPE_LAST` $15-50. 285 rows; pass 1 (sorted Last desc) covered $20.72-50, pass 2 ($15-20.72) returned 86 (complete). Diffed against this week's research files, passes.md, paper_book.md, the queue and the Oct journals: 5 names never seen at all (BKV, HY, LBRT, VTOL, Z), plus ~80 tickers that appear in those files but never got past the Oct 5 sweep table (their prints were outside the 35-day window then). All ~85 went through `get_equity_analyst_ratings`.

## Ratings screen (free)

- **No coverage (killed):** HY, VTOL, AMSC, AMSF, APAM, ASMB, ASTE, AVA, BEPC, BFS, BIPC, BNT, CDNL, CPS, DMC, ETD, GBLI, HYMC, IDR, LMB, LZB, MGPI, NBHC, NTGR, ORI, ROCK, SLVM, SMP, SPH, TDS, TGLS, WD, WLFC.
- **R3 fail (killed):** Z 13/15/0 (Holds > Buys, same as ZG), AB, ARE, BL, EMA, ENB, ENPH, FIG, FISV, GNTX, HESM, HL, HR, KMPR, LAZ, LINE, MIAX, NNN, NVO, NXRT, OCFC, PHG, PPC, PRKS, RCI (2 Sells), ROL, TAP, UDR, UE, WHR, ZG, AMRZ (2 Sells).
- **R4 proxy fail, lowest target under or within reach of the stock (killed):** ACAD (low $16 vs $19.70), BN ($31 vs $36.85), CSGP ($25 vs $32.00), CELH ($26 vs $28.06), OKLO ($14 vs $29.99), BAM ($44 vs $45.96), MDLN ($34 vs $36.06), FOUR ($40 vs $39.34: any call's BE sits over $40), BBUC ($28 vs $26.77).
- **MDA** 15/1/0 passes R3 but `get_earnings_results` returns nothing: no tool date, no LY date, and it's a Canadian filer (no 10-Q backstop). **Killed, R2** (can't be proven).

## R2 + R6 + chain (live quotes ~20:00 UTC close)

R6 base = median absolute next-session close move over the last 6 prints (PXED 4, BBUC 5), from daily bars.

| Ticker | Stock | Print (tool) / LY | Ratings, low | Median move / R6 cap | Contract checked | Bid / Ask | OI | Spread % mid | BE at ask | Needs | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **LBRT** | $16.695 (-7.4%) | **Oct 21 PM verified** / Oct 16 | 9/5/0, low $19 (tool `updated_at` 2024-11) | 13.05% / **19.57%** | **Nov20 $17C** | **1.15 / 1.45** | **20,026** | **23.1%** | **$18.45** | **+10.5%** | **ADVANCE (paper), gated on dated floor** |
| BKV | $22.29 (-3.5%) | Nov 5 AM verified / Nov 10 | 13/0/0, low $27 | 3.68% / 5.53% | Dec18 $20C | 2.50 / 4.60 | 19 | 59% | $24.60 | +10.4% | KILLED, R6 + R7 |
| CG | $36.82 (+2.9%) | Nov 5 AM verified / Oct 31 | 11/11/1, low $41 | 4.09% / 6.13% | Dec18 $35C (Nov20 fails R2: Nov 5 + 21 = Nov 26) | 3.30 / 4.30 | 10 | 26% | $39.30 | +6.7% | KILLED, R6 + R7 |
| DRS | $35.46 (+1.5%) | Oct 29 AM verified / Oct 29 | 11/1/0, low $50 | 6.61% / 9.91% | Nov20 $35C | 1.70 / 2.65 | 2 | 44% | $37.65 | +6.2% | KILLED, R7 (R6 passes) |
| THRM | $29.79 (-2.7%) | Oct 22 AM verified / Oct 23 | 6/2/1, low $40 | 2.86% / 4.28% | Nov20 $30C | 0.00 / 4.90 | 12 | n/a | $34.90 | +17% | KILLED, R7 + R6 |
| ETOR | $24.85 (+1.8%) | Nov 10 AM verified / Nov 10 | 10/5/0, low $27.50 | 10.06% / 15.08% | Dec18 $25C | 1.70 / 2.35 | 23 | 32% | $27.35 | +10.1% | KILLED, R7 (R6 passes; BE 15 cents under the floor) |
| HROW | $28.78 (+5.7%) | Nov 9 PM (f) / Nov 10 | 9/0/0, low $45 | 8.45% / 12.68% | Dec18 $30C | 0.85 / 4.90 | 1 | 141% | $34.90 | +21% | KILLED, R7 + R6 |
| RAPP | $29.51 (+4.2%) | Nov 5 AM (f) / Nov 6 | 16/0/0, low $50 | 3.66% / 5.48% | Dec18 $30C | 3.00 / 7.50 | 39 | 86% | $37.50 | +27% | KILLED, R7 + R6 |
| PXED | $23.96 | Nov 19 PM (f) / Nov 20 | 6/2/0, low $33 | 6.65% / 9.98% | none | | | | | | KILLED, no listed options |
| TATT | $32.15 | Nov 11 PM (f) / Nov 12 | 7/0/0, low $53 | 8.91% / 13.36% | none | | | | | | KILLED, no listed options |

### LBRT Nov20 calls (chain `8bc12542-ac05-4e41-81c6-5c76d9565ed9`)

Prints, next-session close moves: +5.69%, +1.39%, +28.31%, +16.24%, +9.86%, -21.96%. Median 13.05%, cap 19.57%.

| Strike | Bid / Ask | OI | Spread % mid | BE at ask | Needs | R6 | R7 |
|---|---|---|---|---|---|---|---|
| $15C `02bda18e-60dc-4a1b-b201-0355336bd37e` | 2.10 / 2.60 | 0 | 21% | $17.60 | +5.4% | pass | fail (OI) |
| $16C `1b615920-0107-44b9-b8b6-fb34a885c981` | 1.50 / 2.00 | 4 | 29% | $18.00 | +7.8% | pass | fail |
| **$17C `f3734c3c-f822-4d88-b70c-f2798a44f610`** | **1.15 / 1.45** | **20,026** | **23.1%** | **$18.45** | **+10.5%** | **pass** | **pass (barely on spread)** |
| $18C `8f536a4b-7a08-4d13-857c-9bf71c4327da` | 0.75 / 1.15 | 6 | 42% | $19.15 | +14.7% | pass | fail |
| $19C `31e2f985-77cc-4191-a746-aa146236c028` | 0.55 / 0.85 | 206 | 43% | $19.85 | +18.9% | pass | fail |

- R1 0.228 pass. R2: print Oct 21 PM `verified: true`, LY Oct 16; Nov 20 is 30 days after; 10-Q deadline Nov 9 is 9 trading days before expiry: pass. R3 9/5/0 pass (search shows 7/6, still passes). R4: tool low $19 vs BE $18.45 passes on number, but the tool's LBRT record is stamped **2024-11-02**, and the one search found targets of $21-40 (Barclays $32 EW, Morgan Stanley $36 OW, Piper $38 OW) with no dates and no sign of a cut after the stock fell to the bottom of its range. That's an undated, likely pre-decline floor: **dated-floor gate (binder Tab 6)**, same shape as RIOT. R5: 1.45 is over the $0.676 line, **paper only**. R7: OI 20,026, spread 23.1% (2 points of room, a closing quote).
- If entered on paper Friday: ramp sell **Tue Oct 20 3:35pm** (trading day before the Oct 21 PM print). Three trading days of hold, which is short, and the stock fell 7.4% today with no reason found yet.

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **R4 proxy**: free screen check; if the lowest Buy target is under (or within a few percent of) the stock, no call's breakeven can sit under it.
- **BE**: breakeven = strike + ask.
- **(f)**: earnings date `verified: false` (estimated). **LY**: last year's same-quarter date.
- **Range pct**: (price - 52w low) / (52w high - 52w low).
- **Dated floor**: binder Tab 6: a Rule 4 target counts only if it's within 60 days and published after the stock's decline.
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
