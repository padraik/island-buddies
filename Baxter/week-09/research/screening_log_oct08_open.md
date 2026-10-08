# Screening log, Thu Oct 8, 2026, OPEN (9:35am ET, VM)

Reserve $741.32 settled. Rule 5 lines: 3.5/5 $0.741, 4/5 $1.00 (transitional lock), screen $1.00.

## 1. Doc names at the open (R2 dates + requotes, ~9:36am)

`get_earnings_results`: all six still `verified: false`, dates unchanged (COUR Oct 22 PM, ONDS Nov 12 AM, QUBT Nov 13 PM, BRSL Nov 3 AM, WRD Nov 23 AM, TME Nov 11 AM). No entry possible under the current Rule 2 reading (`call_me.md` still OPEN).

| Name | Stock | Contract | Bid / Ask | Max price (doc formula) | Verdict |
|---|---|---|---|---|---|
| COUR | $5.131 | $5C Nov20 | 0.30 / 0.75 | $0.741 (R5 line) | Opening spread is wide. Ask fails by a cent; mid 0.525 passes. |
| ONDS | $7.045 (-2.0%) | $8C Nov20 | 0.41 / 0.44 | 7.045 x 1.2089 - 8 = $0.517 | Passes at the ask. |
| ONDS | $7.045 | $8C Dec18 | 0.59 / 0.65 | $0.517 | Fails R6 at the bid. |
| QUBT | $7.54 (-1.0%) | $8C Nov20 | 0.43 / 0.55 | 7.54 x 1.1388 - 8 = $0.587 | Passes at the ask. |
| WRD | $4.685 (-5.5%) | $5C Jan15 | 0.40 / 0.60 | 4.685 x 1.1397 - 5 = $0.339 | **R6 FAIL at current price**, even at the bid. Doc kept (price can come back before the floor dies Oct 18). |
| BRSL | $9.91 | $11C Nov20 | 0.00 / 0.30 | 9.91 x 1.1101 - 11 = $0.001 | Fails. |
| TDUP | $2.18 | $2.5C Nov20 | 0.15 / 0.35 | ~$0.30 | Fails at ask, passes at mid. Floor-blocked anyway. |
| FRMI | $3.815 (-3.9%) | $4C Nov20 | 0.45 / 0.60 | n/a | BE $4.60 = +20.6%. Floor-blocked. |
| GAU | $2.00 | $2C Nov20 | 0.15 / 0.25 | n/a | Floor-blocked. |
| TME | $7.90 | $8C Nov20 | 0.15 / 0.50 | n/a | Floor dies Sun Oct 11. |
| SERV | $4.596 | (not requoted) | | | Floor dies after Fri Oct 9. |

Queue ratings (19 names, `get_equity_analyst_ratings`, ~9:45am): all unchanged. COUR 8/4/0 low $6, QUBT 5/2/0 low $10, ONDS 11/0/0 low $13, WRD 13/0/0 low $10.51, BRSL 7/3/0 low $11.90, TME 22/14/0 low $9.05 (updated Aug 12), OBDC 11/2/0 low $11, FUBO 8/2/0 low $12, FINV 6/1/0, TDUP 6/1/0 low $5.70, GAU 5/1/0, SERV 6/2/0 low $7, FRMI 6/2/0 low $6, ADTN 7/2/0, MLCO 11/4/0, PCT 3/3/0, ENVX 7/3/1, BXMT 5/4/0, CWH 11/2/0.

## 2. passes.md review

Not owed. The header says it was un-staled Oct 5 (VM OPEN run) and corrected Oct 7, so it's 3 days old. The queue plan's "owed since Oct 5" line was wrong. Next due Mon Oct 12.

## 3. New source: $25-40 band, prints Oct 20 - Nov 20

Scan (preview, not saved): market cap $300M+, stock, price $25-40, earnings Oct 20 - Nov 20, 52-week range percentile < 0.25 (same expression filter as the Oct 5 sweep). **116 matches, all returned.** TAP.A dropped as a share-class duplicate of TAP. 115 screened on ratings (`get_equity_analyst_ratings`, two calls).

| Result | Count | Names |
|---|---|---|
| No coverage | 25 | ASTE, GBX, ROCK, SFBS, ORI, BIPC, NBHC, TGLS, UHT, BNT, SMP, TDS, AVA, CSV, WD, APAM, AMSC, SLVM, BFS, DMC, BEPC, LZB, IDR, CDNL, TRN |
| R3 fail | 34 | NNN 4/12/3, CNP 10/12/0, FBIN 9/12/1, NVO 1/3/2, TAP 5/13/5, GLOB 11/13/0, AMRZ 14/12/2, LAZ 4/5/2, STAG 5/6/1, AB 1/6/0, PEGA 5/9/0, HGV 4/8/0, LINE 7/8/4, CNX 2/9/4, HESM 0/4/3, UDR 9/11/3, ENPH 13/17/3, SEDG 1/20/6, TSCO 16/18/0, PRKS 5/8/0, ROL 8/11/3, BLSH 6/7/0, RCI 16/3/2, MGM 12/13/2, MIAX 3/4/0, WHR 3/10/3, PPC 3/7/0, BL 3/8/2, DOCS 8/13/2, ZG 14/15/0, Z 13/15/0, GTY 4/5/0, LQDA 4/5/0, KMPR 2/3/2 |
| R4 proxy fail (lowest target under the stock) | 7 | ALK (low $37 vs $38.97), BN ($31 vs $36.56), OKLO ($14), CSGP ($25 vs $27.91), CPRT ($25 vs $26.59), JD ($25.13 vs $26.89), CELH ($26 vs $26.80) |
| Pass R3 + R4 proxy | 49 | NKTR, KRUS, LASR, FNF, FOUR, BROS, GLPI, TCOM, IREN, CG, XENE, CENX, DRS, CALX, LVS*, BSY, NSSC, OMCL, SLGN, AD, FIS, KBR, TATT, VNT, AGI, IP, KRMN, PRG*, CMG, GDS, RAPP, CWEN, TFPM, HROW, THRM, VERA, IVT, IMCR, CARG, MDA, VKTX, FIGR, AS, GPCR, MAZE, BBUC, PXED, BTU, ETOR |

\* LVS and PRG were already killed on chains Oct 5 (R5 + R6); not re-checked.

### Chain checks (5, the highest-volatility / earliest-print survivors), expiry = first after the scanner's print date

| Name | Stock | Print (scanner) | Expiry | Nearest strikes, bid / ask | Verdict |
|---|---|---|---|---|---|
| IREN | $37.155 | Nov 6 | Nov13 | $38C 3.15/3.50, $40C 2.51/2.86, $42C 2.00/2.29, $44C 1.38/1.86 | **KILLED R5**: $44C (BE $45.86, +23%) still asks $1.86. A strike under $0.741 sits around $52+, BE +40%: R6 fails too. |
| BROS | $38.385 | Nov 5 | Nov13 | $39C 2.20/3.40, $40C 2.00/3.20, $42C 1.30/2.05, $44C 0.85/1.60 | **KILLED R5**: $44C asks $1.60 (BE $45.60, +18.8%). OI 1-3 on every strike: liquidity too. |
| VKTX | $27.78 | Oct 22 | Oct30 | $28C 1.56/2.51, $30C 1.05/1.34, $32C 0.43/1.18, $34C 0.14/0.89 | **KILLED R5**: $34C asks $0.89 (BE $34.89, +25.6%). R6 fails before R5 passes. |
| LASR | $39.19 | Nov 6 | Nov13 | $40C 2.45/4.70, $42C 1.80/3.90, $44C 1.30/3.10, $46C 0.90/3.10 | **KILLED R5 + liquidity**: OI 0-1, $2.20 wide spreads. |
| CALX | $35.42 | Oct 29 | Nov20 (monthly only) | $37.5C 0.30/2.30, $40C 0.45/1.30, $42.5C 0.10/0.80 | **KILLED R5 + R6**: $42.5C asks $0.80 (BE $43.30, +22.2%), OI 0. |

**Finding:** at a $741 reserve the $25-40 band is structurally dead on Rule 5. A $0.741 ask on a $30-40 stock six weeks out buys a strike 20-40% out of the money, and no name here prints that big a median move. The other 42 R3 survivors go to the queue as Tier C, low priority: they only become live if the reserve grows (Rule 5 line scales with it) or a name has a documented median print over ~15%.

## GLOSSARY

- **R1 / Rule 1:** stock in the bottom 20-25% of its 52-week range (here done inside the scanner as "Range pct (52W) < 0.25").
- **R2 / Rule 2:** confirmed earnings date before the option expires. `verified: false` = the date is estimated, not company-announced.
- **R3 / Rule 3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds. Written as Buy/Hold/Sell counts (e.g. 10/12/0).
- **R4 proxy:** lowest analyst price target above the current stock price. The real Rule 4 (lowest Buy target above breakeven, dated within 60 days) is checked only for names that reach a doc.
- **R5 / Rule 5:** one contract's ask must fit the conviction tier's budget; at this reserve that's $0.741 per share for 3.5/5.
- **R6 / Rule 6:** the move to breakeven must be no more than 1.5x the stock's median earnings-day move.
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike; near zero means no real market.
- **Max price (doc formula):** the highest ask at which a doc's contract still passes R6 at the current stock price, from the doc's own median-move math.
- **Tier C:** names that passed the free screens but are expected to die on R5 at the current reserve.
