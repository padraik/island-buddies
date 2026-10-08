# Screening log, Thu Oct 8, 1:35pm ET (MIDDAY)

**Source:** scanner preview (not saved): market cap $300M+, stock, price $2-25, earnings date **Oct 19 - Oct 30**, 52-week range percentile < 0.25. **116 rows.** This is the hunting ground the corrected Rule 2 opened: a print by Oct 30 (and last year's by Oct 30) leaves 21 days to the Nov 20 expiry.

**Rule 5 line this run:** COUR filled at 1:37pm, so reserve = spendable = **$676.28**. 3.5/5 line 10% x 676.28 / 100 = **$0.676**. Screening line $1.00 (20% of reserve floored at $1.00, held at $1.00 by the transitional lock).

## 1. Free screen (R3 + R4 proxy), 116 names, ~1:41pm

`get_equity_analyst_ratings` on all 116. **~40 pass R3 with the lowest target above the stock price.** Most of them were already in the Oct 5 full sweep. Names this week's logs never took to a verdict were worked first; REITs and mortgage REITs (EPRT, VICI, FCPT, BNL, AKR, NTST, IRT, NLY, DX, RITM, BXMT, TRTX, LADR-type) were set aside as presumed R6 kills (earnings-day moves of 1-4%), not killed.

Fails, sample: WGO 5/9 (R3), KHC 3/14/5, CMCSA 10/16/4, SOFI 10/13/5, RIVN 13/9/5, OLN 4/15/1, F 8/13/1, VFC 9/15/3, RDY 17/10/13, WU 1/10/10, JBLU 0/11/6, QS 0/6/2, STLA 6/16/4, LUMN 3/10/2, TDOC 5/18 (all R3). ALKT (low $14 < $14.39), DQ (low $10 < $10.63), METC (low $8.10 < $8.74): R4 proxy. No coverage: AMSF, GBLI, NTGR, CPS, ETD, HYMC, MNRO, CHCT, NPKI, SHEN, JBGS, CLBK, LXU, CLB, DFH, ARI, FBRT, OPFI, VISN, ORC, FPH, PACK, ABR, FIP, BDN, SSII.

## 2. Funnel: 10 names moved (dates, Nov20 chain, R4, R6)

R2 test for every row: Nov 20 must be >= 21 days after the later of (tool date, last year's Q3 date), i.e. both on or before Oct 30; 10-Q deadline Nov 9 for 40-day filers (not verified per name yet).

| Ticker | Stock | Ratings / low | Print (tool) / last year | R2 | Contract | Bid / ask (OI) | BE at ask | Need | 6-print median, cap | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **ARDX** | $3.265 | 11/0/0, $8.00 | Oct 29 PM (f) / Oct 30, 2025 | PASS (edge: Oct 30 + 21 = Nov 20) | **$3C Nov20** `e500baad-b095-4b1e-8d5e-b374fd3eff3b` | 0.35 / 0.55 (50) | $3.55 | **+8.7%** | 17.4%, cap 26.1% | **ADVANCE.** R1 0.008 (52w $3.22-$8.40). R5 $0.55 <= $0.676. R6 at 33% of cap. Moves: -24.5, +16.9, +21.0, -15.0, +8.7, -17.9. Next: date the $8 floor (Tab 6), find why it's -60% from the high, 10-Q filer status. Thin OI. $4C 0.05 / 0.30 needs +31.7%. |
| **UPBD** | $15.77 | 5/1/0, $20.00 | Oct 29 AM (f) / Oct 30, 2025 AM | PASS (edge) | **$17.5C Nov20** `d768deac-b93d-4133-8bd4-bfcd31e5d45f` | 0.35 / 0.60 (228) | $18.10 | **+14.8%** | 10.8%, cap 16.2% | **ADVANCE, thin R6** (91% of cap at the ask, 84% at mid 0.475). R1 0.071. Moves: +19.1, -15.3, -16.3, +6.3, +4.3, -4.0. AM print, so ramp sell would be the run before the Oct 29 pre-market. Next: floor dating. |
| HAPN | $15.155 | 9/0/0, $20.00 | Oct 28 PM (**verified**) / Oct 22, 2025 | PASS | $17C Nov20 `ae9ab700-9dc0-4ec2-a303-078df628a7d3` | 0.20 / 0.65 (42), ask size 1 | $17.65 | +16.5% | 10.9%, cap 16.35% | **PARK: R6 fails at the ask, passes at mid** (0.425, BE $17.43, +15.0%). Liquidity thin. $15C 0.95 / 1.65 fails R5. R1 0.245 (top edge). |
| RSI | $20.175 | 12/1/0, $30.00 | Oct 28 PM (verified) / Oct 29, 2025 | PASS | $25C Nov20 | 0.15 / 0.65 (439) | $25.65 | +27.1% | 10.15%, cap 15.2% | **KILL, R6.** $22.5C 0.80 / 1.10 and $20C 0.85 / 2.55 fail R5. 2.5-wide grid. |
| GLXY | $19.96 (-6.7% today) | 14/2/0, $24.00 | Oct 20 AM (f) / Oct 21, 2025 | PASS | $25C Nov20 | 0.77 / 0.90 (3,426) | $25.90 | +29.8% | not run | **KILL, R4** (BE $25.90 > $24 low). $22.5C 1.33 / 1.53 and $20C 2.24 / 2.43 fail R5. |
| ATEC | $10.255 | 14/0/0, $12.00 | Oct 29 PM (verified) / Oct 30, 2025 | PASS (edge) | $12.5C Nov20 | 0.30 / 0.35 (3,017) | $12.85 | +25.3% | not run | **KILL, R4** (BE $12.85 > $12 low). $10C 1.10 / 1.20 fails R5. |
| CDE | $16.80 | 10/3/0, $18.00 | Oct 28 PM (f) / Oct 29, 2025 | PASS | $20C Nov20 | 0.40 / 0.50 (10,138) | $20.50 | +22.0% | not run | **KILL, R4** (BE $20.50 > $18 low). $17.5C 1.10 / 1.20 fails R5. |
| MBUU | $22.28 | 5/5/0, $30.00 | Oct 29 AM (f) / Oct 30, 2025 | PASS (edge) | $25C Nov20 | 0.30 / 2.05 (61) | $27.05 | +21.4% | not run | **KILL, R5** (ask $2.05) + liquidity. $27.5C would need +23%+. |
| VLRS | $6.28 | 9/4/1, $7.40 | Oct 26 PM (f) / Oct 27, 2025 | PASS (6-K filer, both dates present) | $7.5C Nov20 | 0.00 / 0.75 (9) | $8.25 | +31% | not run | **KILL, strike grid + liquidity.** 2.5-wide; $5C carries $1.28 intrinsic (R5); $7.5C has no bid, OI 9, and BE > $7.40 low (R4). |
| LADR | $8.85 | 6/1/0, $10.25 | Oct 22 AM (f) / Oct 23, 2025 | PASS | $10C Nov20 | 0.00 / 0.05 (669) | $10.05 | +13.6% | not run | **KILL, strike grid.** $7.5C carries $1.35 intrinsic (R5); $10C prices a ~4% chance (IV 19%), a mortgage REIT that doesn't move 13% on prints. |

## 3. Tally

10 names moved: **2 advance** (ARDX, UPBD), **1 parked** (HAPN, mid-only R6, thin), **7 killed** (RSI R6; GLXY, ATEC, CDE R4; MBUU R5; VLRS, LADR strike grid). ~30 more R3 passes from this scan are left for the next runs (list in research_queue.md).

**What this pass showed:** the Oct 19-30 window is real. Half the names with a Nov20 contract that fits a $0.68 line die on Rule 4 because the lowest target sits only 10-20% above the stock, which is about what an OTM strike needs. ARDX is the exception: an $8 low on a $3.27 stock.

## GLOSSARY

- **R1 / Rule 1:** stock in the bottom 20-25% of its 52-week range (0 = at the low).
- **R2 / Rule 2 (corrected Oct 8, 11:45am):** expiry at least 21 days after the later of the tool's date and last year's same-quarter date, and the 10-Q deadline at least 5 trading days before expiry. "(f)" = `verified: false`.
- **R3 / Rule 3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds (Buy/Hold/Sell like 11/0/0).
- **R4 / Rule 4:** lowest Buy target above breakeven, dated within 60 days and set after the decline (Tab 6). "R4 proxy" = the tool's overall low vs the stock price, before any strike is picked.
- **R5 / Rule 5:** one contract's ask must fit the conviction tier's budget: $0.676 per share for 3.5/5 at a $676.28 reserve.
- **R6 / Rule 6:** the move to breakeven must be no more than 1.5x the median absolute earnings-day move over the last six prints (PM prints: print-day close to next close; AM prints: prior close to print-day close).
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike.
- **Strike grid:** the spacing between listed strikes; a 2.5-wide grid on a cheap stock often leaves no strike that is both affordable and reachable.
- **6-K filer:** a foreign company that files 6-Ks instead of 10-Qs, so it has no 10-Q deadline.
- **Edge (R2):** passes with exactly 21 days.
