# Screening log: Sat Oct 31, SATURDAY (9:00am ET)

**Source:** the queue's Saturday list (NIO, B, TTWO, OLMA, LAR, ACHR, UEC), then the sweep's unscreened bands: a preview of the `e6411b30` screen (market cap >= $300M, R1 < 0.25 on the scanner's range, call volume >= 300) with prints Nov 2 - Mar 5, on $25-60 (66 rows) and $60+ (93 rows). Nothing saved.
**Reserve / lines:** spendable $592.15 -> R5 line at 3.5/5 = **$0.592**.
**Data:** Friday closing option quotes, last-trade closes, after-hours prints, analyst counts, earnings dates and daily closes pulled live this run. Analyst dates from MarketBeat's forecast tables.

## Method change this run: R6 uses every print on file

The rule allows 4 to 8 prints. Friday's numbers used 4 for B and 5 for NIO. Filling them out to all 6 cut B's cap 10.2% -> 8.7% and NIO's 6.0% -> 5.36%, and both failed. Four to eight leaves room to pick the count that passes, so from here every R6 uses all prints on the tool, up to eight. Worth a look at the next sweep.

## Chain stage

| Ticker | Dir | Stock | Next print | R3 / tool low | Contract | Bid / Ask | OI | Spread | BE / needs | R6 cap | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **ACHR** | CALLS | 4.20 (AH 4.19), R1 0.067 | Mon Nov 9 PM verified, LY Nov 6 PM | 8/2/0, $7 | **$4C Dec18** `627c0406` | 0.54 / 0.59 | 330 | 8.8% | $4.59, +9.29% | **12.26%** (6 prints: +22.9, +7.4, -7.9, -10.6, -2.3, +8.5; median 8.17%) | **ADVANCED, REAL-MONEY DOC WRITTEN.** R1-R7 pass; R5 by $0.002. Floor: Barclays OW $8 (Oct 9). `research_ACHR_dec18.md`. |
| ACHR | CALLS | | | | $5C Dec18 `6d18d9e6` | 0.19 / 0.23 | 1,216 | 19.0% | $5.23, +24.5% | 12.26% | Fails R6. |
| **NIO** | CALLS | 3.19 (AH 3.20), R1 0.007 | Tue Nov 24 AM (f), LY Nov 25 AM | 16/7/1, $3.70 | **$3C Dec18** `6f04dc70` | 0.34 / 0.39 | 699 | 13.7% | $3.39, +6.27% | **5.36%** (6 prints; median 3.58%) | **DOC WRITTEN, GATED.** R6 at the ask, and no Buy dated after Sep 29. $3.70 is JPM's Neutral. `research_NIO_dec18.md`. |
| **B** | CALLS | 36.97 (AH 37.06), R1 0.232 | Mon Nov 9 AM verified, LY Nov 10 AM | 15/5/1, $42 | $39C Dec18 `bbe37c92` | 1.33 / 1.61 | 1,293 | 19.0% | $40.61, +9.85% | **8.7%** (6 prints: +0.9, -2.5, +5.2, -7.2, +9.0, -6.4; median 5.8%) | **$39C KILLED, R6.** R1 and floor now pass. $38C (1.47 / 1.98, OI 274) BE $39.98 +8.1% passes R6, stays R7 at 29.5%: re-quote. |
| **TTWO** | CALLS | 190.14 (AH 191.20), R1 0.077 | Mon Nov 9 PM verified | 29/1/1, $270 | Dec18 $190C `58617a72` | 15.20 / 17.50 | 576 | 14.0% | $207.50, +9.1% | **7.35%** (6 prints: -2.4, -4.0, -8.1, -5.4, -4.4, +6.0; median 4.9%) | **KILLED, R6 + R7.** Floor dated at last: BofA Buy $330 (Oct 27). But liquid strikes fail R6 ($200C +11.6%) and strikes that reach fail R7 ($185C OI 31, $180C OI 108, $175C OI 41). Five of six prints fell. |
| OLMA | CALLS | 6.985, R1 0.025 | Nov 13 AM (f) | 11/1/0, $16 | Dec18 $7C / $8C | 0.00 / 4.90 | 14 / 34 | n/a | | | **KILLED, R7.** No bid. |
| LAR | CALLS | 4.07, R1 0.053 | Nov 10 AM verified | 8/2/0, $5 | Dec18 $5C `e5439894` | 0.05 / 0.30 | 128 | 143% | $5.30 | | **KILLED, R7 and R4** (BE over the low). No $4 strike. |
| UEC | CALLS | 7.715, R1 0.071 | Wed Dec 9 AM (f), LY Dec 10 AM | 8/3/0, $10 | Jan15 $7C `60caab3b` | 1.28 / 1.48 | 1,861 | 14.5% | $8.48, +9.92% | **8.12%** (6 prints: -4.1, -1.2, -7.5, +6.8, -15.5, +0.9; median 5.42%) | **KILLED, R6.** $8C spread 58.8%, R7; $9C spread 42.7%, R7. |
| OR | CALLS | 32.00 | Wed Nov 11 PM verified | 7/4/0, $36.48 | Dec18 $35C `736c8431` | 0.75 / 1.15 | 3 | 42% | $36.15 | | **KILLED, R7.** |
| GGAL | CALLS | 32.30, scanner R1 under 0 | Tue Nov 24 | 5/3/0, $45 | Dec18 $35C `4444a0f2` | 0.80 / 2.50 | 24 | 103% | $37.50 | | **KILLED, R7.** |
| NB | CALLS | 3.34, R1 0.099 | Nov 12 PM (f) | 6/1/0, $4.70 | Dec18 $4C | | | | | | No such strike on Dec18. Stays dead (R7, Oct 27). |

## B's R1, reconciled

Scanner 0.255, daily bars 0.27, fundamentals 52-week low $31.61 (Nov 4 2025). The scanner's 52 weekly candles still reach the week of Oct 27 2025, low $30.98, which is older than 52 weeks: (37.06 - 30.98) / 23.71 = 0.256. The real window gives (36.97 - 31.61) / (54.69 - 31.61) = **0.232**. The scanner can read a touch high around anniversaries of a low.

**B floor, dated:** RBC Outperform $53 (Oct 22, stock closed $38.65), JPM Overweight $55 (Oct 21). The $42 low is unowned; Freedom's Hold $46 and CIBC's Neutral $49 are not Buys. Goes on the record if the $38C heals; ramp would be Fri Nov 6 3:35pm.

## Free ratings screen

**$25-60 (66 rows; PAAS held on paper):**
- **R3 fails (19):** CRWV, LMND, RBLX, ASTS, NVO, HGV, NKE, LAZ, SYM, ROL, GIS, TSCO, MIAX, GFI, MGM, SEDG, WHR, ENPH, Z.
- **R4 proxy fails, low under or at the stock (11):** BSX, FISV, EGO, ALK, BIRK, CSGP, CPRT, OKLO, JD, SFM, CARR (low only $1.44 over the stock).
- **No coverage (4):** BHF, INOD, BBW, PLAB.
- **Print inside a week, nothing to stand on (13):** ACMR, BROS, GFS, KTOS, FOUR, MP, KRMN, FIS, CENX, MDLN, IONQ, CELH, LTM.
- **Dead on R7 since Oct 26:** SQM.
- **Earlier chain kills, not re-chained (5):** CECO (R7), UCTT (R6), ALLY (R6), ALGM (R6), AA (Rule 425 flag).
- **Pass, not chained today, on the queue (10):** RKLB (R6 Oct 20, re-test), TCOM, AS, FPS, AGI, VKTX, IONS, BAC, AMKR, LVS (last two tight on the proxy).
- OR and GGAL went to the chain and died above.

**$60+ (93 rows):** 19 rated, the ones printing Nov 9 or later and not already open on paper. Most of the other 74 print this coming week or were cut in this month's logs. I didn't re-rate them, and that's a shortcut, not a clean pass.
- **R3 fails:** INTU, DKS, PDD, LULU, LEN, AGX.
- **R4 proxy fails:** BIDU, SE, ORCL.
- **Pass, chain queue:** KKR ($97 vs $94.18, tight), FUTU ($121.97 vs $98.01), CELC, DY (R7 on Mar19, Oct 23), AVAV (R7, Oct 20), FTAI, MTZ, STRL. CCJ's tool ratings are stamped 2021, unusable. ROAD no coverage.

## Watch

ONDS $6.32 (11/0/0, $13), RCAT $4.62 (7/1/0, $6), BTBT $0.811 (6/0/0, $3.50), CLSK $7.655 (16/0/0, $19): no change in the numbers that matter.

## Paper gates checked

**PL:** tool low $17, 8/5/0, no Buy dated after Oct 16 found. Deutsche's $28 ages out Sat Nov 7. **CAVA's $56:** not worked today.

## Real-money read

**ACHR $4C Dec18 is the first name since FRMI to pass every rule at a live price.** Monday's OPEN decides on live numbers. NIO stays gated.

## Tally

11 names to a verdict or a chain (ACHR, NIO, B, TTWO, OLMA, LAR, UEC, OR, GGAL, NB, PL gate). ACHR advanced to a real doc, NIO doc written and gated. 7 killed (TTWO, OLMA, LAR, UEC, OR, GGAL, B $39C). 84 more through the free ratings screen; 74 not re-rated.

## GLOSSARY
- **R1-R7**: binder Tab 1 Iron Rules (calls). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest target above breakeven), R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity.
- **BE**: breakeven at expiry = strike + ask.
- **OI**: open interest, contracts outstanding.
- **AH**: after-hours trade.
- **(f)**: earnings date estimated from cadence, not announced.
- **Tab 6 dating**: a floor only counts if it's dated inside 60 days and published after the stock's decline.
- **R4 proxy**: free check that the tool's low target sits above the stock price.
- **Closing spread**: the wider book quoted in the last minute of the session.
- **Rule 425**: an SEC filing of communications about a business combination.
- **Paper**: tracked in the paper book, no money moves.
