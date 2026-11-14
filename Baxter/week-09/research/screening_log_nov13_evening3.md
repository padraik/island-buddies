# Screening log, Fri Nov 13 EVENING 3 (10:00pm ET)

*Session 3 of 3. Job (from EVENING 2): leave Monday PREMARKET the plan, then start the ~Dec 15 re-sweep band A. Nothing held. Real-money reserve $715.96 spendable, so the 3.5/5 R5 line is $0.716. Prices: Friday close (scanner `Last`). Spring chains (Mar19 / Apr16) don't carry real OI yet, so there were no chain checks tonight. Every pass is a park.*

## Source: band A, new scan `01ce0035-28a6-49c0-aed8-0ee1b83da395` ("Baxter Nov13 E3 DecResweep band A 1-8.19 R1<0.25 Feb13-Mar20 prints")

Filters: the base `a5439121` filters (market cap $300M+, earnings Feb 13 - Mar 20 2027, stock, R1 expression < 0.25) with **no call-volume floor**, plus Last between $1 and $8.19 (band A from `screening_log_nov11_evening2.md` Source 2). **124 rows**, under the 200 cap, so band A is complete.

I diffed the scan against every week-08 and week-09 log and passes.md. **7 names have never been worked.** One free ratings call covered all 124 (two calls, 75 + 49).

### Never-worked names (7)

| Ticker | Last | R1 | B/H/S, low | Verdict |
|---|---|---|---|---|
| NPCE | $7.16 | -0.637 (looks like bad range data; a recent listing?) | 5/4/0, $7 | **KILLED R4 proxy** (low $7 under the stock) |
| EVCM | $6.33 | 0.038 | 2/4/2, $7 | **KILLED R3** (Buys 2 < 3; 2 Sells) |
| PFL | $6.66 | 0.031 | no coverage (PIMCO closed-end fund) | **KILLED R3** |
| PFN | $6.12 | 0.052 | no coverage (PIMCO closed-end fund) | **KILLED R3** |
| PHK | $4.01 | 0.000 | no coverage (PIMCO closed-end fund) | **KILLED R3** |
| ILPT | $6.07 | 0.240 | no coverage | **KILLED R3** |
| STLN | $3.50 | 0.245 | no coverage | **KILLED R3** |

### The other 117, re-rated free (R3 + R4 proxy on Friday's close)

**41 pass R3 + the R4 proxy.** They're parked for the December chain pass (Mar19 / Apr16 per the 10-K R2 rule):

| Ticker | Last | R1 | Print (scanner) | B/H/S | Low (cushion) | Note |
|---|---|---|---|---|---|---|
| AMPX | 7.89 | 0.051 | Mar 5 | 13/0/0 | 14 (77%) | new to the Dec parks |
| NXE | 7.80 | 0.071 | Mar 3 | 19/0/0 | 10.14 (30%) | was paper-size park Nov 9; now under $8.19 |
| BLZE | 7.76 | 0.217 | Feb 23 | 6/1/0 | 15 (93%) | Dec park; back in the scan (was out Nov 12) |
| KURA | 7.74 | 0.138 | Mar 5 | 15/1/0 | 15 (94%) | new to the Dec parks |
| OCS | 7.64 | 0.031 | Mar 3 | 10/1/0 | 19.80 (159%) | new to the Dec parks |
| RGNX | 7.64 | 0.204 | Mar 5 | 10/1/0 | 12 (57%) | new to the Dec parks |
| EXK | 7.63 | 0.088 | Feb 26 | 6/1/0 | 10.64 (39%) | new to the Dec parks |
| ORN | 7.57 | 0.077 | Mar 3 | 7/0/0 | 13 (72%) | new to the Dec parks |
| RDW | 7.56 | 0.124 | Feb 25 | 6/4/1 | 8 (6%) | thin; was R4 proxy Nov 9 |
| OLMA | 7.53 | 0.043 | Mar 16 | 11/1/0 | 16 (112%) | new; Mar 16 print = Apr16 only |
| PUMP | 7.45 | 0.119 | Feb 18 | 10/3/0 | 11 (48%) | Dec park |
| ALHC | 7.33 | 0.069 | Feb 26 | 10/6/0 | 8 (9%) | Dec park, thin |
| ATEC | 7.07 | 0.016 | Feb 24 | 12/2/0 | 8 (13%) | new to the Dec parks |
| METC | 6.74 | 0.044 | Feb 25 | 6/3/0 | 7 (4%) | thin; was R4 proxy Nov 9 |
| CIFR | 6.66 | 0.063 | Feb 24 | 22/3/0 | 9.5 (43%) | Dec park |
| IQMX | 6.66 | -0.085 | Feb 26 | 4/1/1 | 7.30 (10%) | new to the Dec parks |
| TRTX | 6.52 | 0.245 | Feb 17 | 5/0/1 | 8 (23%) | new; R1 on the line |
| UUUU | 6.51 | 0.014 | Feb 26 | 8/0/0 | 14 (115%) | Dec park |
| PHAT | 6.06 | 0.079 | Feb 26 | 9/1/0 | 7.5 (24%) | new to the Dec parks |
| MFA | 5.82 | -0.092 | Feb 18 | 3/3/0 | 7 (20%) | Dec park; R3 on the line |
| AESI | 5.55 | 0.029 | Feb 24 | 8/6/1 | 7 (26%) | new to the Dec parks |
| SBET | 5.54 | 0.133 | Mar 9 | 7/0/0 | 8 (44%) | new to the Dec parks |
| QUBT | 5.50 | 0.012 | Mar 2 | 5/2/0 | 10 (82%) | closed real position Nov 9; next print |
| STUB | 5.30 | 0.006 | Mar 4 | 8/5/1 | 6.5 (23%) | new to the Dec parks |
| ADTN | 4.88 | 0.060 | Feb 25 | 7/3/0 | 6.25 (28%) | new to the Dec parks |
| SVRA | 4.66 | 0.234 | Mar 12 | 9/0/0 | 9 (93%) | new to the Dec parks; Mar 12 = Apr16 only |
| TSHA | 4.10 | 0.168 | Mar 19 | 13/0/0 | 9 (120%) | new; Mar 19 = Apr16 only |
| ACHR | 4.02 | 0.071 | Mar 2 | 8/2/0 | 7 (74%) | closed real position Nov 9; next print |
| NUVB | 3.99 | 0.003 | Mar 2 | 12/1/0 | 7 (75%) | Dec park |
| SOUN | 3.455 | -0.038 | Feb 26 | 6/1/0 | 5 (45%) | Dec park |
| ARDX | 3.11 | 0.049 | Feb 19 | 11/0/0 | 8 (157%) | R7 history (OI 49 in Oct); re-check |
| WVE | 3.11 | 0.004 | Feb 26 | 20/1/0 | 8.37 (169%) | Dec park |
| CINT | 3.07 | 0.090 | Mar 11 | 7/2/0 | 4 (30%) | new to the Dec parks |
| GROY | 2.92 | 0.156 | Mar 18 | 8/0/0 | 4 (37%) | new; Apr16 only |
| DNN | 2.05 | 0.046 | Mar 10 | 15/0/0 | 3.5 (71%) | Dec park |
| CTMX | 2.04 | -0.011 | Mar 16 | 8/0/0 | 5 (145%) | Dec park |
| SANA | 2.01 | -0.064 | Mar 3 | 9/1/0 | 6 (199%) | Dec park |
| PCT | 1.73 | 0.011 | Feb 26 | 3/3/0 | 2 (16%) | was R4 proxy Nov 9; R3 on the line |
| ALT | 1.67 | -0.053 | Mar 5 | 9/1/0 | 11 (559%) | killed R6 + R7 on the Nov chain; next print |
| EVEX | 1.64 | 0.064 | Mar 17 | 7/3/0 | 2.75 (68%) | new; Apr16 only |
| HIVE | 1.55 | -0.008 | Feb 17 | 8/1/0 | 2.5 (61%) | new to the Dec parks |

Thin ones to watch: RDW, METC and PCT were on the R4 proxy line on Nov 9 and pass tonight by 4-16%.

**Killed tonight on R3** (no coverage or Hold/Sell-heavy): SKYD 7/12/8, MARA 10/4/2, ARVN 7/8/0, WU 1/11/9, NMFC 0/6/1, YSS 5/9/0, ADAM 2/4/0, JOBY 3/3/4, LZ 1/6/1, UNIT 2/5/1, ARRY 8/12/0, STLA 6/17/6, BRSP 5/0/2, RXRX 3/4/0, LCID 3/6/3, TROX 2/6/2, TV 3/7/0, CYH 2/5/3, TBLA 2/6/0, EDIT 8/2/2, EOSE 4/7/0, MPT 2/3/3, HTZ 0/6/4, ENVX 4/7/1, UWMC 2/7/0, OPEN 2/6/2, PLUG 8/12/3; plus 45 with no coverage (KODK, NRDS, ERII, LAND, TTI, CION, OPFI, EBS, SVC, RUM, RYAM, TWI, ABTC, SBS, IEP, CRMD, HBNB, DJT, ICL, BW, ASM, GYRE, VISN, ARKO, EVLV, SPRY, METCB, BUR, JBI, SATL, GOGO, MDXG, LWLG, ACDC, NUAI, UAMY, GSM, AGNT, VFF, HYLN, BBAI, SLDP, SNDL, THM, **TMQ**).
**Killed on the R4 proxy:** PRTA ($8 vs $8.17), GNL ($6.50 vs $6.55), GTN.A ($3 vs $6.01), INDI ($1.55 vs $2.05).

**Data flag: TMQ** came back with no coverage tonight. On Nov 12 it was re-rated with ratings unchanged from Nov 9. A one-night null on a park isn't a kill. It stays parked, and Saturday re-pulls it.

**Not in band A (price above $8.19 or out of R1):** OCGN, ALLO (under $1), AQST, BKD, SNDX, GLUE, EFC, ARLO, WULF, CORZ, ZURA, CGEM. Bands B-D settle them.

## Gated names, re-checked (free)

- NIO: 16/7/1, low $3.6983, stamp **2026-09-01** (unchanged). Q3 Nov 24 AM `verified: false`, `actual: null`. Floor gate shut.
- AVGO: 53/3/0, low $398.47, stamp **Oct 27** (unchanged, before the Nov 5 drop). Gate shut.
- DY: 12/1/0, low $375, no stamp. Paper BABA 45/1/0 low $140.92 (Nov 10) vs BE $118.55: Rule 4 holds. Paper GOOGL 64/8/0 low $300.

## Tally

**124 names moved: 7 never-worked to a verdict (all killed: 6 R3, 1 R4 proxy). 117 re-rated free: 41 pass to the December chain pass, 76 dead (27 R3 on ratings, 45 no coverage, 4 R4 proxy), TMQ flagged.** 0 chain checks, 0 searches, 0 advanced, 0 buyable. 21 of the 41 survivors (AMPX, KURA, OCS, RGNX, EXK, ORN, OLMA, ATEC, IQMX, TRTX, PHAT, AESI, SBET, STUB, ADTN, SVRA, TSHA, CINT, GROY, EVEX, HIVE) were never on the Nov 9-12 Dec parks list, because the old base scan's call-volume floor and 200-row cap hid them. Dropping the call-volume floor did what it was meant to do.

**December, next steps for band A:** (1) `get_option_chains` expirations for the 41 (Mar19 vs Apr16 listed?); (2) `get_earnings_results` + LY date for each (Mar19 needs later-of on or before Feb 26 AND large-accelerated filer); (3) chains for R5/R6/R7 once spring OI exists. Bands B-D are still to run (Saturday or December).

## GLOSSARY

- **R1 (range percentile):** (price - 52-week low) / (52-week high - 52-week low). Under 0.25 = calls candidate.
- **R2:** the earnings print is proven to land before expiry: expiry 21+ days after the later of the tool date and last year's date, and the 10-Q / 10-K deadline 5+ trading days before expiry.
- **R3:** at most 1 Sell, at least 3 Buys, Buys >= Holds.
- **R4 proxy / R4:** the lowest analyst target must sit above the stock (screen) and above the call's breakeven (rule).
- **R5:** one contract's ask x 100 fits the conviction tier's share of reserve ($0.716/share at 3.5/5 tonight).
- **R6:** the breakeven move is no larger than 1.5x the median absolute earnings reaction over the last 4-8 prints.
- **R7:** open interest >= 250 and spread <= 25% of mid on the exact contract.
- **Floor gate:** Tab 6 rule. A Rule 4 floor counts only if the target is dated within 60 days and after the stock's decline.
- **Band A:** the $1-8.19 price slice of the December re-sweep scan.
- **Park:** passes the free screen, but the chain can't be judged yet (spring expiries have no open interest), so the name waits for the ~Dec 15 run.
