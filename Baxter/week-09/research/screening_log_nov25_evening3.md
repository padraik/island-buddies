# Screening log: Wed Nov 25, EVENING 3 (10:00pm ET)

**Job (from EVENING 2's queue, item 1):** the refill. Band D parks from the Nov 21 log, median-first, up to 25. Nothing held. R5 line: 10% x $715.96 / 100 = **$0.716/share** (3.5/5), so everything here is paper-book size; the paper book applies R7 (OI >= 250, spread <= 25% of mid).

**Source:** Robinhood tools only, run ~03:00-03:05 UTC Nov 26 on Wednesday's close (market closed Thu Nov 26). 0 web searches.

**Picked:** the 25 highest-beta band D parks (semis, optics, AI infrastructure, biotech, alt managers): SITM, FN, NVMI, CLS, MTSI, AEIS, COHR, LRCX, ALAB, VRT, WDC, TER, AMAT, KLAC, MOD, TSEM, SANM, SIMO, IDCC, LAD, ALNY, APO, META, OSIS, SKHY. None had been worked since Nov 21.

**Method (same as Nov 24/25):** moves from daily closes Oct 2025 - Nov 2026 (AM print: prior close to print day; PM print: print day to next day), last 5 prints. R1 = closing-range percentile over the last 252 bars (interpolated bars dropped). Medians >= 8% go to one near-ATM call on the first expiry that passes R2 (later of tool date / last year's date + 21 days). R6 at the ask vs Wednesday's close. R4 against the tool's low target.

## 1. Medians and R1

| Ticker | Next print (f) | Moves (oldest first) | Median | Cap | R1 | Verdict |
|---|---|---|---|---|---|---|
| SITM | Feb 3 PM | +21.8 / +17.9 / +27.9 / +26.6 / -12.0 | **21.8%** | 32.7% | 0.171 | to the chain |
| SANM | Jan 25 PM | +16.6 / -21.6 / +14.6 / -17.5 / +3.9 | **16.6%** | 24.9% | 0.096 | to the chain |
| VRT | Feb 10 AM | -1.8 / +24.5 / -2.3 / -17.3 / +16.5 | **16.5%** | 24.75% | 0.106 | to the chain |
| TER | Feb 1 PM | +20.5 / +13.4 / -19.4 / -0.4 / -3.2 | **13.4%** | 20.1% | 0.141 | to the chain |
| CLS | Jan 27 PM | +8.2 / -13.1 / -14.4 / +10.0 / +12.1 | **12.1%** | 18.15% | 0.000 (new low) | to the chain |
| MTSI | Feb 4 AM | +11.5 / +5.9 / +11.2 / +14.5 / -18.4 | **11.5%** | 17.25% | 0.141 | to the chain |
| AEIS | Feb 9 PM | +15.8 / +10.7 / -10.7 / +15.2 / +9.6 | **10.7%** | 16.05% | 0.067 | to the chain |
| FN | Feb 1 PM | +3.7 / -10.2 / -8.0 / -19.4 / +15.5 | **10.2%** | 15.3% | 0.011 | to the chain |
| IDCC | Feb 4 AM | +3.5 / +9.9 / -15.9 / +16.2 / +4.3 | **9.9%** | 14.85% | 0.029 | to the chain |
| WDC | Jan 28 PM | +8.7 / -10.1 / -0.7 / -13.0 / -3.0 | **8.7%** | 13.05% | 0.207 | to the chain |
| COHR | Feb 3 PM | +18.3 / -0.8 / -7.4 / -8.0 / -13.0 | **8.0%** | 12.0% | 0.170 | to the chain |
| META | Jan 27 PM | -11.3 / +10.4 / -8.6 / -8.0 / -7.0 | 8.6% | 12.9% | **0.335** (Wed $609.99) | **KILLED R1** (MID-OUT; 0.254 on Tue's close, +3.4% Wed) |
| SKHY | Feb 13 PM | -2.6 / +13.3 (2 prints) | n/a | | 0.080 | **PARKED** (only 2 prints, like ELE / INFQ) |
| OSIS | Jan 28 PM | +14.2 / -7.3 / -17.0 / -5.2 / -4.2 | 7.3% | | 0.014 | KILLED R6 structural |
| NVMI | Feb 11 AM | 6.8% | | | 0.037 | KILLED R6 structural |
| TSEM | Feb 10 AM | 6.7% | | | 0.124 | KILLED R6 structural |
| ALNY | Feb 11 AM | 6.7% | | | 0.063 | KILLED R6 structural |
| SIMO | Feb 2 PM | 6.6% | | | 0.202 | KILLED R6 structural |
| KLAC | Jan 28 PM | 5.5% | | | 0.106 | KILLED R6 structural |
| MOD | Feb 3 PM | 5.4% | | | 0.184 | KILLED R6 structural |
| LRCX | Jan 27 PM | 4.5% | | | 0.162 | KILLED R6 structural |
| ALAB | Feb 9 PM | 4.4% | | | 0.238 | KILLED R6 structural |
| AMAT | Feb 11 PM | 2.7% | | | 0.189 | KILLED R6 structural (tool shows FQ1 2027 "actual 4.16, verified" on a Feb 11 2027 date: a data glitch, irrelevant at a 2.7% median) |
| LAD | Feb 10 AM | 5.0% | | | 0.264 | KILLED R1 (MID-OUT) + R6 |
| APO | Feb 8 AM | 2.9% | | | 0.373 | KILLED R1 (MID-OUT) + R6 |

## 2. The chain (11 names), ratings re-pulled this run

| Ticker | Stock (Wed) | Ratings / low | Expiry (why) | Contract | Bid / Ask | OI | BE at ask | Needs | Cap | R4 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SITM | 385.94 | 13/0/0, low $425 (no stamp) | May21 (Feb19 fails R2; no Mar/Apr) | $390C | 86.00 / 100.10 | 6 | 490.10 | +27.0% | 32.7% | fail ($425) | **KILLED R4 + R7** |
| | | | | $300C | 133.00 / 148.00 | 0 | 448.00 | +16.1% | | fail | R4 + R7 |
| SANM | 138.57 | 3/3/0, low $210 (no stamp) | Apr16 (no Feb/Mar) | $140C | 23.50 / 27.30 | 4 | 167.30 | +20.7% | 24.9% | pass | **R7** |
| | | | | $130C | 28.10 / 32.10 | 1 | 162.10 | +17.0% | | pass | R7 |
| | | | | $150C | 19.40 / 22.60 | 60 | 172.60 | +24.6% | | pass | R7 (closest OI) |
| VRT | 173.36 | 30/5/1, low $187 (Nov 18) | Mar19 | $175C | 27.00 / 30.05 | 27 | 205.05 | +18.3% | 24.75% | fail ($187) | **KILLED R4 + R7** |
| TER | 212.43 | 16/5/0, low $260 (Oct 30) | Mar19 | $210C | 37.30 / 44.10 | 2 | 254.10 | +19.6% | 20.1% | pass | **R7** |
| | | | | $200C | 42.20 / 48.10 | 22 | 248.10 | +16.8% | | pass ($11.90) | R7 |
| | | | | $220C | 33.00 / 39.60 | 11 | 259.60 | +22.2% | | pass | R6 fail |
| CLS | 191.90 | 26/0/0, low $325 | Feb19 (Jan 28 + 21 = Feb 18) | $190C | 34.90 / 38.70 | 41 | 228.70 | +19.2% | 18.15% | pass | **KILLED R6** (+ R7) |
| MTSI | 200.06 | 16/3/0, low $220 | May21 (Feb19 fails R2) | $200C | 42.80 / 45.50 | 1 | 245.50 | +22.7% | 17.25% | fail | **KILLED R6 + R4 + R7** |
| AEIS | 197.01 | 14/1/0, low $275 | Apr16 | $200C | 33.00 / 36.00 | 3 | 236.00 | +19.8% | 16.05% | pass | **KILLED R6** (+ R7) |
| FN | 289.61 | 10/2/0, low $364 | Apr16 | $290C | 56.90 / 65.80 | 63 | 355.80 | +22.9% | 15.3% | pass | **KILLED R6** (+ R7) |
| IDCC | 254.77 | 6/0/0, low $425 (no stamp) | Mar19 | $250C | 29.70 / 33.50 | 2 | 283.50 | +11.3% | 14.85% | pass | **R7** |
| | | | | $260C | 24.80 / 28.40 | 2 | 288.40 | +13.2% | | pass | R7 |
| | | | | $240C | 35.00 / 38.50 | 0 | 278.50 | +9.3% | | pass | R7 |
| WDC | 272.45 | 24/6/0, low $300 (Nov 2) | Mar19 | $270C | 45.80 / 54.45 | 94 | 324.45 | +19.1% | 13.05% | fail | **KILLED R6 + R4** |
| COHR | 196.19 | 23/5/0, low $228 (Nov 25) | Mar19 | $195C | 39.90 / 45.80 | 24 | 240.80 | +22.7% | 12.0% | fail | **KILLED R6 + R4** |

- **IDCC is the interesting one:** 49% IV on a 9.9% mover (ratio about 0.8 at mid), the cheapest time value of the 25, and a $425 low target 67% over the stock. It fails only on R7 (OI 0-2 across $240-$260). No stamp on its ratings, so the floor gate would need a dated target too. Weekly re-quote line.
- **TER $200C Mar19** passes R1-R4 and R6 with room ($11.90 under the $260 low, stamped Oct 30); OI 22. Weekly re-quote line.
- **SANM** passes R6 at every strike checked, but R3 is on the line (3 Buys, 3 Holds) and the floor has no stamp. OI 1-60. Weekly re-quote line.
- Big-cap semis and optics in this pool trade 70-95% IV, which is why six of eleven died on R6 at the ask even with 10-12% medians.

## Totals

25 names moved. 0 advanced past the chain, 0 docs, 0 buyable (real or paper). Kills: 10 R6 structural, 3 R1 (META, LAD, APO), 6 at the chain on R6 / R4 (CLS, MTSI, AEIS, FN, WDC, COHR), 2 at the chain on R4 + R7 (SITM, VRT). R7 only, to the weekly line: TER, IDCC, SANM. Parked: SKHY (2 prints).

**Band D parks left (paper only, for Saturday or next week's evenings):** PH, CAT, MLM, RBC, CW, HUBB, CMI, TT, ETN, AXP, HII, EVR, CI, LPLA, LHX (thin), SXI, TEL, COF, TMUS, DLR, AEM, RRX, CHRW, HLI, OSK, CBRE, ENS, PLD, WMS, BX (thin), NVT, PCAR (32). Skip stale stamps: CRS, HWM.

## GLOSSARY

- **R1-R7:** the Iron Rules (binder Tab 1). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 price cap vs reserve, R6 reachability (move to BE <= 1.5x median print), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Median print:** the middle value of the absolute earnings-day moves; sign ignored.
- **R6 structural:** a median so small (under ~8%) that no near-ATM contract can pass R6 once time value is paid.
- **BE (breakeven):** strike + premium paid, here at the ask.
- **IV:** implied volatility, the option market's priced-in yearly move.
- **Floor gate / stamp:** binder Tab 6: a Rule 4 target only counts if dated within 60 days and after the decline. A ratings record with no `updated_at` can't prove that.
- **MID-OUT:** R1 between 25% and 75% of the range; no direction, no play.
- **OI:** open interest, contracts outstanding.
- **Band D:** the scanner's $100+ price slice. Paper-book size at today's reserve.
- **Weekly re-quote line:** contracts that fail only on liquidity, checked once a week instead of every run.
