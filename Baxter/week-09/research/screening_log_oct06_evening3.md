# SCREENING LOG — Tue Oct 6, 2026, 10:00pm ET (VM EVENING, session 3 of 3)

**Source:** the sub-$6.12 slice EVENING 1 couldn't reach (the scanner's 200-row cap cut it off). Same filters: price $2-6.12, market cap $300M+, common stock, earnings Oct 12 - Nov 13, 52-week range percentile < 0.25 (expression filter). **117 matches, all returned**; 32 were already in this week's logs, **85 new**.

**Rule 5 line this run:** reserve = spendable $741.32 (unsettled $0.00). 3.5/5 line **$0.741**, 4/5 $1.00 (lock), screen $1.00.

**Prices:** stock prices are the official Oct 6 close (`get_equity_quotes`); option quotes are the Oct 6 4pm close (market closed at run time).

## Summary

| Step | Count | Tool |
|---|---|---|
| Scanner | 1 preview scan, 117 rows, 85 new | preview_scan |
| R3 / R4 proxy | 85 names, 19 survive | get_equity_analyst_ratings (2 calls) |
| Dates | 19 survivors | get_earnings_results |
| R6 history | 18 names, 4 prints each (ZURA has 3) | get_equity_historicals (daily, from Nov 2025) |
| Chains | 17 names (Nov20 calls, near-the-money strikes) | get_option_instruments + get_option_quotes |
| Queue ratings | 11 queue names, no count or low-target changes | get_equity_analyst_ratings |
| Web | none | |
| Killed past R3 | **16** | |
| Advanced to chain-passed | **3: GAU, SERV (both at the ask), FRMI (at mid)** | |

Funnel moves this session: 19 names past the free ratings screen (under the 25 line). The 66 cut at the ratings screen are sourcing.

## Advanced (chain passed)

| Ticker | Close | R1 | Print | Ratings / low | R6 (4 prints) | Contract | Bid / Ask | BE | Needs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| **GAU** (Galiano Gold) | $2.06 | 0.21 | Nov 5 PM `verified: false` | 5/1/0, $2.99 | -12.82 / +10.62 / +0.77 / +5.64; median 8.13%, cap 12.19%, max BE $2.31 | $2C (aeaa5c2a-c579-4830-9979-5ec6e155fb44) | 0.20 / 0.25, OI 1,784, ask size 6 | $2.25 at ask | +9.2% (75% of cap) | Passes R5 and R6 **at the ask**. Max price $0.31. One contract $25; the 3.5/5 budget (8% of $741 = $59) buys 2. $2.99 low looks like a CAD-converted target: needs a name and a date. Gold miner: gold price is the macro driver (correlated bucket). |
| **SERV** (Serve Robotics) | $4.77 | ~0.04 | Nov 11 PM `verified: false` | 6/2/0, $7.00 | -10.03 / +10.13 / -3.52 / -10.48; median 10.08%, cap 15.12%, max BE $5.49 | $5C (f8655e65-b40f-45e9-ba03-b33f8993f4b7) | 0.36 / 0.46, OI 6,501 | $5.46 at ask | +14.5% (96% of cap at ask, 86% at mid) | Passes **at the ask by 3 cents**; max price $0.49. Deep, liquid chain. Pre-profit robotics (losses widening): whether a print forces a re-rate is the doc's question. Low $7 needs dating. |
| **FRMI** (Fermi) | $4.23 | 0.01 | Nov 10 AM `verified: false` | 6/2/0, $6.00 | -13.43 / -13.27 / +22.83 / -13.16; median 13.35%, cap 20.02%, max BE $5.08 | $4C (9cd4939b-9c9d-42ce-bff8-47b95b16d917) | 0.65 / 0.75, OI 964 | $4.70 at mid | +11.1% at mid (56% of cap) | R6 has room; **R5 fails at the ask by $0.009**, passes at mid $0.70. Three of four prints fell 13%. Listed Oct 2025, so these four prints are its whole history. |

## Killed (past R3)

| Ticker | Close | Rule | Detail |
|---|---|---|---|
| USAS | $4.47 | R2 | `get_earnings_results` has no upcoming quarter at all (last row Aug 14). Scanner says Nov 10; unverifiable. |
| ZURA | $3.94 | R6 | Only 3 prints on record (median 2.17%). Pre-revenue biotech. |
| OI | $5.77 | R4 + R5, strike grid | Low target $6 (ratings data dated Nov 2025). $6C BE is at/above the floor; $5C carries $0.77 intrinsic, over the $0.741 line. |
| SOUN | $5.715 | R4 + R5, strike grid | Low $6: $6C BE above it. $5C intrinsic $0.715 leaves $0.026 of time value under the line. |
| STUB | $5.70 | R5 + R4, strike grid | 2.5-wide. $5C intrinsic $0.70 leaves $0.04; $7.5C BE above the $7 low. |
| LAR | $5.60 | R5 | $5C 0.65 / 1.15, OI 220, vol 0; $7.5C BE > $6.23 max. |
| TE | $3.83 | R6 | No $3.5 strike. $4C 0.40 / 0.55, BE $4.475 at mid > $4.24 max (cap 10.61%). |
| HIVE | $2.90 | R6 | No $2.5 strike. $3C 0.25 / 0.35, BE $3.30 at mid > $3.16 max (cap 9.13%). |
| AIOT | $2.69 | R5 + liquidity | $2.5C 0.10 / 1.20, OI 0. |
| CABA | $2.02 | Liquidity | $2C no bid / 1.00. |
| SOC | $3.59 | R5 | No $3.5 strike. $3C 0.79 / 1.01, bid over the line. |
| WVE | $3.55 | R5 | No $3.5 strike. $3C 0.55 / 1.35, OI 26. |
| NB | $3.50 | R6 + R5, strike grid | No $3 or $3.5 strike. Max BE $3.81 (cap 8.84%): any $4C fails R6; a $2.5C carries $1.00 intrinsic. |
| CINT | $3.21 | R6, strike grid | Median print 1.63%, cap 2.44%, max BE $3.29. Only $2.5 / $5 / $7.5: $2.5C intrinsic $0.71 leaves $0.03. |
| ITRG | $2.68 | R6, strike grid | Median 2.78%, cap 4.17%, max BE $2.79. No $2.5 strike; a $2C would carry $0.68 intrinsic and need under $0.06 of time value. |
| HUYA | $2.29 | R6 + R4, strike grid | No $2 strike. Max BE $2.46; a $2.5C BE is above it (and near the $2.70 low). |

## Cut at the ratings screen (the other 66)

- **No analyst coverage (35):** PSNY, BW, PLBL, ASM, LWLG, YALA, ICL, XNET, EVLV, FPH, METCB, JBI, SPRY, ARKO, KPLT, UAMY, PACK, AGNT, TMC, DGXX, BUR, CDZI, RLMD, ECC, VVR, ALTI, PUSA, OGG, SSII, BDN, SWRD, BBAI, SLDP, DDL, IHRT.
- **R3 (28):** DCH (6/7), LUMN (2 Sells), LZ (2/6), JOBY (3 Sells), IVR, FLO, AQN (6/7), PTON (2 Sells), UAA, UA, GT (3/5), QS, STLA, ESRT, LCID, JBLU, GTM, MPT, LPL, SPCE, DNUT, VRRM (0 Buys), CYH, LAC, BMBL, PLTK, TV, BLDP.
- **R4 proxy, lowest target at or under the price (3):** LUCK ($5 vs $5.29), ACHR ($4.50 vs $4.68), TLS ($4 vs $4.46).

Already in this week's logs and skipped (32): TRTX, AHCO, GTN.A, TKC, COUR, ORC, NUVB, GRNT, TSHA, MLCO, PCT, ARRY, TROX, BRSP, RWT, PRME, ABR, ARDX, EOSE, TBLA, GRAB, GROY, INDI, SANA, ENVX, ALT, FIP, CTMX, OPEN, WRN, ABAT, HTZ.

## Queue gates (no status change)

All 11 queue names: ratings counts and low targets unchanged from 8pm. COUR Oct 22 PM still `verified: false`. Closes: COUR $5.12, BRSL $10.21, TME $7.93, OBDC $10.03, QUBT $7.86, ADTN $7.62, MLCO $4.24, PCT $4.005, ENVX $2.70, BXMT $11.25, CWH $4.53.

## What the sub-$6 slice taught

Under $6 the strike grid does most of the killing: 9 of the 16 died because no listed strike sits between "too much intrinsic for the $0.741 line" and "breakeven past the Rule 6 cap or the floor". The ones that survived (GAU $2C, SERV $5C, FRMI $4C) all have a strike within about 5% of the stock, which is the shape to look for first next time.

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R1 (52w):** (price - 52-week low) / (52-week high - 52-week low); calls need <= 0.25.
- **R3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4 proxy:** the lowest analyst target must sit above the stock price before a chain is worth pulling; the real Rule 4 test is lowest Buy target vs breakeven, with a dated floor.
- **R5 line:** max ask per share for one contract at the conviction tier (10% of reserve / 100 at 3.5/5).
- **R6 cap:** 1.5x the median earnings-day move over the last 4 prints; the needed move to breakeven must fit under it.
- **Max BE:** stock price x (1 + R6 cap); the highest breakeven Rule 6 allows. **Max price:** max BE minus the strike, the most the contract can cost and still pass Rule 6.
- **Strike grid:** the spacing of listed strikes; wide grids often leave no strike that fits.
- **Intrinsic:** how far a call is already in the money (stock minus strike). **Time value:** premium above intrinsic.
- **Passes at mid:** the contract fits R5/R6 only if it fills at the bid/ask midpoint, not at the ask.
- **Stale floor:** a price target set before the stock's decline, or more than 60 days ago; it doesn't count for Rule 4 (binder Tab 6).
- **CAD-converted target:** a Canadian-dollar price target shown in US dollars, which is why GAU's low is $2.9859 and not a round number.
- **BE:** breakeven, strike + premium. **OI:** open interest. **AM / PM print:** earnings before the open / after the close.
