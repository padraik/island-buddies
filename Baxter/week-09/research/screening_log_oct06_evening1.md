# SCREENING LOG — Tue Oct 6, 2026, 6:00pm ET (VM EVENING, session 1 of 3)

**Source:** research_queue.md (COUR gate check, live-list requotes, Tier B: SUZ, RKT, EFC, plus the ADTN $8C the WRAP run asked for), then a fresh scanner pass for sub-$15 names: price $2-15, market cap $300M+, earnings Oct 12 - Nov 13, 52-week range percentile < 0.25 (expression filter, same as the Oct 5 sweep). 330 matches, 200 returned (the $6.12-$15 slice); 66 of those were already in this week's logs, **134 new**.

**Rule 5 line this run:** reserve = spendable $741.32 (unsettled $0.00). 3.5/5 line **$0.741**, 4/5 $1.00 (lock), screen $1.00.

## Summary

| Step | Count | Tool |
|---|---|---|
| Ratings (queue) | 11 names, no count or low-target changes | get_equity_analyst_ratings |
| Dates (queue) | COUR, BRSL, SUZ, RKT, EFC | get_earnings_results |
| Requotes | COUR, BRSL $10C/$11C, MLCO, PCT, ENVX, BXMT, CWH, ADTN $7C | get_option_quotes |
| Scanner | 1 preview scan, 134 new names | preview_scan |
| R3 / R4 proxy | 134 names, 22 survive | get_equity_analyst_ratings (2 calls) |
| Dates | 22 survivors | get_earnings_results |
| R1 + R6 history | 22 names + SUZ/RKT/EFC/ADTN, 4 prints each | get_equity_historicals |
| Chains | 16 names (Nov20 calls) | get_option_instruments + get_option_quotes |
| Web | none | |
| Killed past R3 | **22** (3 Tier B + 19 new) | |
| Advanced to chain-passed | **4: OBDC, TME, QUBT, ADTN** | |

Funnel moves this session: 26 names (4 queue + 22 new survivors), one over the 25 batch line; five of the kills (WULF, AVBP, WSE, TLK, AGBK) were free math with no chain call. The 112 names cut at the free ratings screen are sourcing, the same way the Oct 5 sweep cut 718 to 163.

## Queue gates (no status change)

| Ticker | Stock | Contract | Bid / Ask | Ratings / low | Status |
|---|---|---|---|---|---|
| COUR | $5.115 | $5C Nov20 | 0.50 / 0.75 | 8/4/0, $6.00 | Oct 22 PM still `verified: false`. Ask $0.75 > $0.741. Both gates shut. |
| BRSL | $10.22 | $11C Nov20 | 0.20 / 0.30 | 7/3/0, $11.90 | R6 passes at the ask (BE $11.30 vs $11.35 max). Nov 3 AM `verified: false`. Doc is EVENING 2's job. |
| BRSL | | $10C Nov20 | 0.20 / 0.80 | | OI 87, unchanged. |
| MLCO | $4.26 | $4C Nov20 | 0.25 / 0.70 | 11/4/0, $5.30 | Blocked, stale floor. |
| PCT | $4.005 | $4C Nov20 | 0.50 / 0.65 | 3/3/0, $6 | Blocked, stale floor. |
| ENVX | $2.70 | $3C Nov20 | 0.25 / 0.29 | 7/3/1, $5 | Blocked, stale floor. |
| BXMT | $11.245 | $11C Nov20 | 0.55 / 0.80 | 5/4/0, $16 | Fails R5 at the ask. |
| CWH | $4.525 | $4C Nov20 | 0.75 / 1.00 | 11/2/0, $6 | Fails R5. |

## Advanced (chain passed)

| Ticker | Stock | R1 | Print | Ratings / low | R6 (4 prints) | Contract | Bid / Ask | BE | Needs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| **OBDC** (Blue Owl Capital Corp, BDC) | $10.04 | -0.05 (new low) | **Nov 4 PM `verified: true`** | 11/2/0, $11.00 | -5.32 / -1.04 / -3.15 / +3.10; median 3.12%, cap 4.69%, max BE $10.51 | $10C (6197e090-d0c2-4f73-bb2b-62dc8e6f9d09) | 0.30 / 0.45, OI 1,632 | $10.45 at ask | +4.1% | Passes R5 and R6 **at the ask**, by six cents. One contract $45, room for 2+ (ladder). Confirmed date. Floor $11 needs dating. BDC: check merger history (M&A flag) and dividend/NAV story in the doc. |
| **TME** (Tencent Music ADR) | $7.94 | 0.02 | Nov 11 AM `verified: false` | 22/14/0, $9.04 | -8.39 / -24.65 / -1.31 / -11.92; median 10.16%, cap 15.23%, max BE $9.15 | $8C (3d63651d-b0cc-443c-a3c5-96ac50fc1d23) | 0.40 / 0.45, OI 50 | $8.45 at ask | +6.4% | Passes at the ask with room. 2 contracts = $90. **All 4 prints fell**: Bearxter's problem, has to be answered in the doc. Floor $9.04 (USD conversion) needs dating. |
| **QUBT** (Quantum Computing) | $7.855 | 0.10 | Nov 13 PM `verified: false` | 5/2/0, $10 | +8.49 / -10.01 / +15.72 / +0.22; median 9.25%, cap 13.88%, max BE $8.95 | $8C (f6a0df8d-f3a0-440f-a802-2d646cc180c0) | 0.47 / 0.84, OI 766 | $8.66 at mid | +10.2% | Passes R5/R6 **at mid only** ($0.655); ask $0.84 fails R5. Print is a week before expiry. |
| **ADTN** | $7.625 | 0.07 | Nov 2 PM `verified: false` | 7/2/0, $11 | (Oct 6 boost run) median 10.95%, cap 16.42%, max BE $8.88 | $8C (630d5a78-c432-43a0-b7cf-8bd585fef422) | 0.50 / 0.75, OI 381 | $8.75 at ask | +14.8% at ask | R6 passes at the ask; R5 fails by $0.009 at the ask, passes at mid $0.625. Stock +6.6% on Oct 6. |

## Killed (past R3)

| Ticker | Stock | Rule | Detail |
|---|---|---|---|
| SUZ | $8.405 | R6 + R5, strike grid | Median print 1.16%, cap 1.75%, max BE $8.55. Only 2.5-wide strikes: $7.5C carries $0.905 intrinsic (over the $0.741 line), $10C BE > $10. |
| RKT | $11.575 | R6 + R5 | Median 4.15%, cap 6.22%, max BE $12.30. $11C 1.25 / 1.47; $12C 0.87 / 0.96, BE $12.92. |
| EFC | $11.67 | R6 + R5, strike grid | Median 2.15%, cap 3.23%, max BE $12.05. $10C intrinsic $1.67; $12.5C BE > $12.5. |
| WULF | $14.99 | R4 + R5 (free math) | Low target $15.00 = price. Any strike >= $15 puts BE above the floor; $14.5C/$14C intrinsic leaves no room under both the floor and the $0.741 line. |
| AVBP | $14.80 | R6 (free math) | Median 1.65%, cap 2.48%, max BE $15.17: a $15C would need an ask <= $0.17. |
| WSE | $11.75 | R6 | No print history in the tool (new listing), can't verify 4 prints. |
| TLK | $12.86 | R2 | Calendar data unusable: three different quarters stacked on Oct 20, plus Oct 29, all `verified: false`. |
| AGBK | $6.67 | R6 | Only 2 reported prints since listing. |
| SGRY | $13.41 | R5 + R6/R4, strike grid | 2.5-wide. $12.5C intrinsic $0.91; $15C BE over the $14.92 max and the $14 floor. |
| CLBT | $11.21 | R4 + R5, strike grid | Low target $12.50: $12.5C BE is above it; $10C intrinsic $1.21. |
| SLRC | $11.43 | R5 + R6, strike grid | $10C intrinsic $1.43; $12.5C BE > $12.05 max. |
| BNTC | $9.00 | R6, strike grid | Max BE $9.37; $7.5C intrinsic $1.50, $10C BE > $10. |
| KYTX | $6.25 | R6, strike grid | Max BE $6.64; $5C intrinsic $1.25, $7.5C BE > $7.5. |
| NOA | $12.24 | R5 + liquidity | $12.5C 0.25 / 1.20, OI 9. |
| JBS | $12.08 | R6 | $12.5C 0.45 / 0.60, BE $13.10 > $12.69 max (cap 5.03%). |
| STWD | $12.94 | R6 | $13C 0.40 / 0.60, BE $13.40+ > $13.27 max (cap 2.54%). |
| CC | $14.08 | R5 + R4 | $14C 1.05 / 1.35, $13C 1.65 / 1.90; $15C+ BE above the $15 floor. |
| REAL | $9.41 | R5 | $10C 0.75 / 0.85, bid alone over the line. |
| OLMA | $8.06 | R5 + liquidity | $8C 0.45 / 1.55 OI 2 ($2.63 phantom close), $9C 0.15 / 0.95 OI 1. |
| CRMD | $7.27 | Liquidity | $7C 0.10 / 1.00 OI 3; $8C no bid. |
| ALMS | $6.945 | R6 | $7C 0.45 / 0.80 OI 4, BE $7.625 at mid > $7.35 max (cap 6.18%). |
| RCAT | $6.345 | R5 | $6C 0.86 / 1.03, bid over the line; $7C would need an ask <= $0.03. |

## Cut at the ratings screen (the other 112)

- **No analyst coverage:** VEL, HNRG, GEL, CHCT, GPGI, MGPI, DOLE, KBDC, QDEL, ELA, NPKI, CCXI, SHEN, CLBK, NCDL, IIM, JBGS, BCSF, POLE, CLB, ADMA, LXU, VELO, ACIC, OFIX, GILT, CIM, VCV, ALIT, HE, IQI, NRDS, VGM, FBYD, OXLC, DJT, SSYS, VKQ, VMO, GMTL, VKI, POET, BKKT, TWI, ERII, CION, JMIA, RYAM, IEP, CV, SVC, ARI, OPFI, TTI (several are closed-end funds).
- **R3:** RIVN, VFC, CRK, TTAM, ARR, MSDL, LBTYA, LBTYB, LBTYK, SBGI, VIV, PCG, HAYW, F, SAFE, CSIQ, STNE, ACI, KD, CCU, MLTX, FSK, CGBD, WBTN, SDHC, SMPL, DEI, PSBD, ERIC, CCAP, FMC, HUN, AGNC, MFIC, FVRR, TRIP, UPWK, SMR, PMT, TU, CAPR, GOOS, MBLY, ARVN, NMFC, ADT, WEN, WU.
- **R4 proxy, lowest target at or under the price (10):** ALKT ($14 vs $14.50), CPNG ($12 vs $14.42), CTVA ($13.20 vs $13.90), TAC ($9.84 vs $13.00), FUN ($10 vs $12.08), KEP ($9.57 vs $11.32), PAX ($9 vs $11.26), DQ ($10 vs $11.08), BTDR ($10 vs $10.94), VERX ($12 vs $12.29).

Every one of the 134 is either in the 22 R3 survivors above or in one of these three lists.

## Not covered yet

The scanner capped at 200 rows: the **sub-$6.12 slice (~130 names)** didn't come back. EVENING 3 re-runs the same filters with price $2-6.12.

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R1 (52w):** (price - 52-week low) / (52-week high - 52-week low); calls need <= 0.25. Negative means the stock is under the old 52-week low.
- **R3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4 proxy:** the lowest analyst target must sit above the stock price before a chain is worth pulling; the real Rule 4 test is lowest Buy target vs breakeven, with a dated floor.
- **R5 line:** max ask per share for one contract at the conviction tier (10% of reserve / 100 at 3.5/5).
- **R6 cap:** 1.5x the median earnings-day move over the last 4 prints; the needed move to breakeven must fit under it.
- **Max BE:** stock price x (1 + R6 cap); the highest breakeven Rule 6 allows.
- **Strike grid:** the spacing of listed strikes; 2.5-wide grids often leave no strike that fits.
- **Passes at mid:** the contract fits R5/R6 only if it fills at the bid/ask midpoint, not at the ask.
- **Stale floor:** a price target set before the stock's decline, or more than 60 days ago; it doesn't count for Rule 4 (binder Tab 6).
- **Phantom print:** a last-trade or close price that no real bid/ask supports.
- **BDC:** business development company, a lender to private mid-size firms that pays out most of its income as dividends.
- **ADR:** a US-listed share of a foreign company.
- **BE:** breakeven, strike + premium. **OI:** open interest. **AM / PM print:** earnings before the open / after the close.
