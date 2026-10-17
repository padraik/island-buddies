# Screening log, Fri Oct 16, 2026, 8:00pm ET (EVENING 2, VM)

DO slot, up to 25 names. EVENING 2's own job is writing research docs for names that cleared the chain stage, but EVENING 1 left none, so this session did what EVENING 1 asked: (1) chained the 9 names it had queued behind the queue, then (2) ran a sub-$25 band of the same scan (prints Oct 30 - Dec 4) and chained 16 fresh names from it. 25 names moved. All quotes are Friday's closing book (stock closes from `get_equity_quotes` last trade; **note:** the daily bars for CIFR, CLSK and others repeated Thursday's close as the Oct 16 bar, so every "needs" figure below uses the quote's last trade, not the bar).

Rule 2: everything prints Nov 2-25. Nov20 needs the later of (tool, LY) on or before Oct 30, which only BTU and ATEC meet (LY Oct 30). Everyone else goes to Dec18 (later date by Nov 27 at the latest: CLSK Nov 25 + 21 = Dec 16). 10-Q / 10-K deadlines all land >= 5 trading days before expiry. Most of these chains are monthly-only (no Nov27). R6 base = median absolute one-day reaction over the last 4 prints (pm: print-day close to next close; am: prior close to print-day close).

## Part 1: the 9 behind-queue names from EVENING 1

| Ticker | Stock | Ratings / low (stamp) | Print (tool), LY | Last 4 reactions | Median / cap | Contract | Bid / ask, OI | BE (ask) / needs | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| FLUT | $75.54 | 27/9/1, $85 (Oct 16) | Nov 11 PM (f), Nov 12 | -14.27 / -13.80 / +2.11 / -11.48 | 12.64% / 18.96% | **Jan15 $75C** `a5b4198b-f959-4c58-bb29-e759cd0af196` | 8.90 / 9.60, **OI 235**, vol 639 | $84.60 / +12.0% | **PARK (paper):** R1 0.021, R3, R6 pass; R4 $85 > $84.60 by $0.40 (undated); **R7 OI 235 < 250** (spread 7.6% passes). Friday's 639-contract volume should lift Monday's OI. Dec18 $75C OI 25, $80C spread 49.5% + R4 fail ($86.80 > $85), $85C OI 198 + R4 fail; Jan15 $70C OI 14 |
| KKR | $86.23 | 20/5/0, $97 (Oct 13) | Nov 9 AM (v), Nov 7 | +1.68 / -5.35 / -1.29 / +1.71 | 1.69% / 2.54% | Dec18 $90C | 4.10 / 4.80, OI 223 | $94.80 / +9.9% | **KILLED, R6** |
| CENX | $35.04 | 6/1/0, $40 | Nov 5 PM (f), Nov 6 | +14.04 / +0.27 / -2.76 / +11.49 | 7.12% / 10.69% | Dec18 $35C | 3.40 / 3.80, OI 31 | $38.80 / +10.7% | **KILLED, R7** (OI 31; R6 also over by 0.04 pt; every higher strike's BE clears the $40 low = R4) |
| APTV | $44.86 | 18/4/0, $50 | Nov 3 AM (v), Oct 30 | -4.26 / +2.94 / -7.90 / -16.62 | 6.08% / 9.12% | Dec18 $45C `6f545918-dad9-4f60-bf2b-80f123d8f116` | 3.20 / 3.60, **OI 0** | $48.60 / +8.3% | **PARK, R7 re-check:** R1 0.073, R2, R3, R4 ($50 > $48.60), R6 pass; OI 0 on Dec18 $40 / $42.5 / $45 is odd for a $10B name. Re-pull OI mid-day Monday; kill if still < 250. Jan15 $45C: +9.7% vs 9.12% (R6 fail), OI 218 |
| FIGR | $27.12 | 9/2/0, $30 | Nov 12 PM (f), Nov 13 | +16.33 / -25.73 / +1.36 / +3.91 | 10.12% / 15.18% | Dec18 $27.5C | 3.10 / 4.10, OI 10 | $31.60 / +16.5% | **KILLED, R6 / R4 / R7** ($30C OI 1) |
| BWXT | $136.96 | 16/5/0, $150 | Nov 2 PM (v), Nov 3 | -7.17 / +2.95 / -4.86 / -0.80 | 3.91% / 5.86% | Dec18 $140C | 8.40 / 9.50, OI 0 | $149.50 / +9.2% | **KILLED, R6** |
| GFS | $46.69 | 14/9/1, $51 (Oct 15) | Nov 4 AM (v), Nov 12 | -1.84 / +16.32 / +9.28 / -4.92 | 7.10% / 10.65% | Dec18 $45C | 5.50 / 6.10, OI 2 | $51.10 / +9.4% | **KILLED, R4** ($51.10 >= $51 low) and R7 ($50C OI 22, R4 too) |
| SMG | $54.55 | 6/3/0, $60 (Aug 6) | Nov 4 AM (v), Nov 5 | +2.86 / -0.68 / -4.53 / -3.79 | 3.33% / 4.99% | Dec18 $55C | 3.20 / 3.70, OI 50 | $58.70 / +7.6% | **KILLED, R6** (and R7, R4 dating) |
| VST | $152.01 | 22/1/1, $169 (Aug 7) | Nov 6 AM (v), Nov 6 | -2.52 / +0.83 / -2.74 / -0.56 | 1.68% / 2.51% | Nov27 $155C | 8.60 / 10.00, OI 10 | $165.00 / +8.5% | **KILLED, R6** (and R7) |

## Part 2: sub-$25 band of the same scan

Scan `4bc59b84-cc60-4619-870c-359c2daae902`, new config version retitled "Baxter Oct16 E2 sub-$25 Oct30-Dec4 prints": market cap >= $300M, earnings Oct 30 - Dec 4, last $2-24.99, 52w range pct < 0.25 (weekly bars), Friday call volume > 300 (the liquidity pre-cut is in the scan this time). **173 names.**

- No coverage (34): BMNR, CPS, PPTA, CCXI, NN, HE, SGML, ISOU, LPTH, ABTC, RYAM, DJT, CRML, IEP, BULL, RUM, XXI, POET, ASM, BW, EVLV, LWLG, SATL, CDZI, NUAI, HYLN, RLMD, IMSR, NRGV, UAMY, ABR, TMC, VFF, ASPI.
- Rule 3 fail (52): UPST, FIG, HRL, YELP, PZZA, RYN, MOS, SRPT, HL, NCLH, CRK, KD, KLAR, CC, TTD, LI, STNE, NTLA, CSIQ, TRIP, XPEV, XRAY, VITL, NVTS, CCOI, LBTYA, LBTYK, MARA, ARVN, CAPR, NMFC, WEN, WU, FLO, FLNC, SMR, YSS, UNIT, UAA, LUMN, JOBY, GT, GTM, GEMI, RXRX, ARRY, LCID, DNUT, MPT, SPCE, LAC, OPEN.
- **87 pass R3.** Most were already chained and killed in Era 2 logs (ONDS, RIOT, QUBT, WRD, PCT, FRMI, ENVX, ACHR, BILI, TIGR, QBTS, ZURA, VNET, SERV, PONY, KEEL, NB, GRAB, etc., mostly R5/R6/R7 or the R4 proxy). Sixteen that were fresh, or that have re-priced hard since their last look, went to the chain.

| Ticker | Stock (Fri) | Ratings / low | Print (tool), LY | Last 4 reactions | Median / cap | Contract | Bid / ask, OI | BE (ask) / needs | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **CIFR** | $8.9725 (-10.6%) | 23/2/0, $18 (undated) | Nov 2 AM (f), Nov 3 | +22.04 / +12.48 / +23.53 / -15.65 | 18.84% / 28.27% | **Dec18 $10C** `f9efed33-4dbf-4992-bf1e-941128404b84` | 1.26 / 1.32, **OI 3,319** | $11.32 / **+26.2%** | **ADVANCE (paper), floor gate.** R1 below the weekly-bar low, R2, R3, R6 (1.9 pt margin), R7 (spread 4.7%) pass. R4: $18 low is 2x the stock, but the stock went $19.09 (Sep 22) to $8.97 (-53%) and no target dated after the slide was found (one search: aggregator averages $27-31, Macquarie $35 from May). $11C (+34.1%) and $12C (+42.7%) fail R6 at Friday's close. No real-money strike under the $0.676 line passes R6 |
| CLSK | $8.405 (-10.1%) | 15/0/0, $19 | Nov 24 PM (f), Nov 25 | +13.79 / +21.96 / -5.80 / -3.53 | 9.79% / 14.69% | Dec18 $9C | 0.75 / 1.11, OI 391 | $10.11 / +20.3% | **KILLED, R6** ($10C: +28.0%; both strikes were passing on Thursday's $9.35) |
| GDS | $23.06 (-8.9%) | 15/0/0, $45.35 (Oct 1) | Nov 18 AM (f), Nov 19 | +2.52 / +2.55 / -9.28 / +6.20 | 4.38% / 6.56% | Dec18 $23C | 1.70 / 3.60, OI 0 | $26.60 / +15.4% | **KILLED, R6 + R7** |
| RZLT | $3.565 | 11/0/0, $6 | Nov 5 PM (f), Nov 6 | +12.08 / +5.79 / +0.91 / -1.02 | 3.41% / 5.11% | Dec18 $2.5C (strikes 2.5/5/7.5 only) | 0.40 / 2.75, OI 0 | $5.25 / +47% | **KILLED, R6 + R7** |
| AQST | $3.775 | 9/0/0, $6 | Nov 4 PM (f), Nov 5 | +2.17 / -2.52 / +14.53 / -4.08 | 3.30% / 4.95% | Dec18 $4C | 0.25 / 0.60, OI 0 | $4.60 / +21.9% | **KILLED, R6 + R7** |
| EQX | $11.145 | 11/0/0, $13.74 | Nov 9 PM (v), Nov 5 | +7.64 / +8.50 / 0.00 / +4.07 | 5.86% / 8.78% | Dec18 $11C | 1.00 / 1.35, OI 0 | $12.35 / +10.8% | **KILLED, R6 + R7** |
| CDE | $15.455 | 10/3/0, $18 | Nov 4 PM (v), Oct 29 | -3.01 / +6.51 / -3.36 / -10.21 | 4.93% / 7.40% | Dec18 $15C | 1.60 / 1.95, OI 3,425 | $16.95 / +9.7% | **KILLED, R6** |
| BTU | $23.90 | 5/2/0, $27.50 | Oct 29 AM (f), Oct 30 | -4.19 / -2.20 / -5.73 / -10.41 | 4.96% / 7.44% | Nov20 $24C | 1.38 / 1.84, OI 74 | $25.84 / +8.1% | **KILLED, R6** (and R7) |
| ATEC | $10.465 | 14/0/0, $12 | Oct 29 PM (v), Oct 30 | +16.29 / +0.79 / -31.67 / -7.54 | 11.91% / 17.87% | Nov20 $10C | 1.10 / 2.00, OI 206 | $12.00 / +14.7% | **KILLED, R4** ($12.00 BE is not above the $12 low) and R7 (OI 206, spread 58%) |
| WULF | $11.655 | 27/1/0, $15 | Nov 6 AM (v), Nov 10 | -13.50 / -9.28 / -2.62 / -4.29 | 6.79% / 10.18% | Dec18 $13C | 1.43 / 1.50, OI 7,689 | $14.50 / +24.4% | **KILLED, R6** |
| SNDX | $12.91 | 12/0/0, $23 | Nov 2 PM (f), Nov 3 | +11.56 / +5.03 / -10.83 / +4.40 | 7.93% / 11.89% | Dec18 $15C | 0.00 / 1.80, OI 0 | $16.80 / +30% | **KILLED, R7** (no bid, OI 0) and R6 |
| CRVS | $9.535 | 8/0/0, $27 | Nov 3 PM (f), Nov 4 | -1.44 / -4.31 / +6.58 / +0.43 | 2.88% / 4.31% | Dec18 $10C | 0.90 / 1.40, OI 156 | $11.40 / +19.6% | **KILLED, R6** |
| OCUL | $6.87 | 13/0/0, $14 | Nov 3 AM (f), Nov 4 | -4.47 / +4.21 / -0.61 / +2.82 | 3.51% / 5.27% | (no Dec18 $7.5C listed) | | ATM call needs >> 5.3% | **KILLED, R6** (cap 5.27% is below any 2-month ATM call's cost on a 70%+ IV name) |
| SANA | $2.275 | 9/1/0, $6 | Nov 5 PM (f), Nov 6 | +0.99 / -2.80 / -8.43 / +4.99 | 3.90% / 5.84% | Dec18 $2.5C | 0.10 / 0.70, OI 0 | $3.20 / +40.7% | **KILLED, R6 + R7** |
| MNKD | $3.05 | 7/1/0, $4.75 | Nov 4 AM (f), Nov 5 | +10.58 / -7.43 / -0.28 / -5.12 | 6.28% / 9.41% | Dec18 $3C | 0.20 / 0.60, OI 0 | $3.60 / +18.0% | **KILLED, R6 + R7** |
| LUNR | $10.785 | 12/0/1, $13 | Nov 12 PM (f), Nov 13 | +10.05 / +4.42 / +2.35 / +3.60 | 4.01% / 6.01% | Dec18 $12C | 0.98 / 1.42, OI 328 | $13.42 / +24.4% | **KILLED, R6** |

**What part 2 says:** Friday's tape hit the bitcoin miners hardest: CIFR -10.6%, CLSK -10.1%, WULF -7.6%, after RIOT and IREN in EVENING 1. CLSK passed R6 on Thursday's close and failed on Friday's, so one day's slide pushed it out. CIFR is the one name whose own earnings history is violent enough (median 18.8%) to carry a December call through the rule. But it has halved in four weeks, and every target we can see predates the slide. That's the Tab 6 problem: a $18 low set when the stock was $19 is a countdown to a downgrade, not a floor.

## Behind the queue (added tonight)

None of the 16 left behind a live name except CIFR. CLSK goes to the watch line (revive if the stock gets back over ~$9.20 with the $9C ask near $1.10, or if its $8C clears R7 mid-day).

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Pct**: where the stock sits in its 52-week range (0 = at the low, 1 = at the high); negative means under the weekly-bar low.
- **BE**: breakeven = strike + ask.
- **Needs**: the stock move from Friday's close to BE.
- **Median / cap**: median absolute one-day earnings reaction over the last 4 prints, and 1.5x that (the most R6 allows).
- **(v) / (f)**: earnings date company-verified / forecast from cadence, per `get_earnings_results`.
- **LY**: last year's same-quarter report date.
- **Floor gate / dated floor**: binder Tab 6: a Rule 4 target counts only if it's within 60 days and published after the stock's decline. A name that passes everything else but has no dated floor is parked, not killed.
- **Paper / real**: paper-book candidate (Rule 5 waived, 1 contract at the ask) vs. a contract the real fund could afford under the $0.676 line.
- **Watch line**: names kept at the bottom of the queue, re-quoted once a day instead of every run.
- **OI**: open interest, the number of contracts outstanding; updates overnight, so a day's volume shows up in the next session's OI.
