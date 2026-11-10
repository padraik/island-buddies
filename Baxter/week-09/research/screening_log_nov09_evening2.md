# SCREENING LOG: Mon Nov 9, EVENING 2 (8:00pm ET), VM

*Session 2 of 3. The session-2 job is research docs for names past the chain stage. EVENING 1 left none (0 advanced), so this session started EVENING 3's refill early with two sources EVENING 1 named: (1) re-quote the Nov 7 sweep's R7 kills for OI build-up, (2) a fresh scan for names that just reported and sit in the bottom quartile. All data is Monday's close (option books are the 3:59pm closing quotes).*

## Holdings fact check

FRMI $2.5C Dec18: close $1.655 (official $1.66), AH $1.68. Book 0.05 / 0.10 (OI 1,042). Q3 **Thu Nov 12 AM `verified: true`**, `actual: null`. 6/2/0, low $6 vs BE $3.15: Rule 4 holds. EDGAR submissions (CIK 2071778): newest is still the Nov 5 Form 4 / 144. **Facts unchanged.** Ramp sell Wed Nov 11 3:35pm.

## Source 1: Nov 7 R7 kills, re-quoted (3 names)

| Ticker | Stock | Contract | Book | OI (Sat -> tonight) | Spread | Verdict |
|---|---|---|---|---|---|---|
| FUL | $51.34 | Feb19 $50C / $55C | 2.50 / 6.90; 0.00 / 4.90 | 13 -> 13; 1 -> 1 | 94% / no bid | **Still KILLED R7** |
| NRIX | $16.14 | Apr16 $15C-$18C | 1.50 / 5.50 ... 0.50 / 4.90 | 3-27 -> 9 / 5 / 3 / 27 | 114%-163% | **Still KILLED R7** |
| SLM | $16.91 | Apr16 $17C-$20C | 0.80 / 3.20 ... 0.05 / 1.25 | 0-24 -> 12 / 24 / 12 / 25 | 63%-185% | **Still KILLED R7** |

No OI built in three sessions. These are long-dated contracts on names with thin options markets; they won't come back this quarter.

## Source 2: just-reported scan (new)

Scan `a5439121` "Baxter Nov9 E2 just-reported R1<0.25 Feb13-Mar20 prints callvol>=100": market cap >= $300M, next earnings Feb 13 - Mar 20, 2027, R1 < 0.25 (52-week expression), call volume >= 100. **162 rows**, 99 not in any week-09 log since Oct 30.

**Free screen (R3 + R4 proxy, 3 ratings calls, all 162):**
- **27 no coverage:** ABTC, ACDC, ARR, ASM, ASTE, BBAI, CSV, CTEV, DJT, ERII, GSM, HE, HY, IEP, INOD, KODK, NRDS, NVCR, PSIX, ROCK, RYAM, SD, SLDP, SNDL, STRA, TPL, VISN.
- **43 R3:** AMR, AMRZ, ARRY, ARVN, BLDR, BXSL, CAR, CC, CRCL, CTRI, DQ, EOSE, FIG, FIS, GOLF, HL, HTZ, JOBY, KGC, LMND, LZ, MIAX, MLTX, MPT, NMFC, OPEN, PRCT, PZZA, ROOT, SEDG, SFM, STLA, TAP, TBLA, TROX, TTAM, UWMC, VRRM, VSNT, WES, WLK, WU, XRAY.
- **32 R4 proxy** (low target at or under ~5% above the stock): AAOI, ACAD, AEVA, AG, AKAM, BKNG, BNTX, CDE, CPNG, CSGP, EQT, FLUT, FSLR, FUN, GIL, HLN, INDI, LKQ, MELI, METC, MKSI, NVTS, OKLO, ORA, PCT, PTCT, QXO, RDW, RUN, SBSW, VERA, VITL.
- **60 pass.**

**Date stage (25 real-money-sized passes, `get_earnings_results` each):**

| Ticker | Stock | R1 | Board, low | Q3 printed | Next print (f) | LY same quarter | Verdict |
|---|---|---|---|---|---|---|---|
| **ALT** | $2.12 | 0.049 | 9/1/0, $11 | **NOT YET: Thu Nov 12 AM (v)** | Mar 4 | Nov 6 | Live window, chained below. **KILLED R6 + R7** |
| OCGN | $0.98 | 0.140 | 6/0/0, $8 | Nov 4 | Mar 3 AM | Mar 4 | Park (Apr16) |
| ALLO | $1.06 | 0.023 | 10/1/0, $4 | Nov 5 | Mar 11 PM | Mar 12 | Park (Apr16) |
| CTMX | $2.03 | -0.013 | 8/0/0, $5 | Nov 5 | Mar 15 AM | Mar 16 | Park (Apr16) |
| TMQ | $2.33 | 0.074 | 3/3/0, $4.30 | Oct 2 (FY Aug) | Feb 16 AM | Feb 17 | Park (Mar19 on (a); 10-Q quarter, check deadline) |
| SANA | $2.51 | 0.089 | 9/1/0, $6 | Nov 5 | Mar 2 PM | Mar 3 | Park (Apr16) |
| WVE | $3.45 | 0.022 | 19/1/0, $8.37 | Oct 27 | Feb 25 AM | Feb 26 | Park (Apr16 unless large accelerated) |
| AQST | $3.57 | 0.168 | 9/0/0, $6 | Nov 3 | Mar 3 PM | Mar 4 | Park (Apr16) |
| NUVB | $4.49 | 0.089 | 12/1/0, $7 | Nov 4 | Mar 1 PM | Mar 2 | Park (Apr16) |
| MFA | $6.32 | 0.025 | 3/3/0, $8 | Nov 4 | Feb 17 AM | Feb 18 | Park (Mar19 if large accelerated, else Apr16) |
| CIFR | $6.85 | 0.071 | 22/3/0, $9.50 | Nov 2 | Feb 23 AM | Feb 24 | Park (Mar19 / Apr16 on filer status) |
| PUMP | $6.95 | 0.079 | 9/4/0, $11 | Oct 28 | Feb 17 AM | Feb 18 | Park (Mar19 / Apr16) |
| ALHC | $7.49 | 0.077 | 10/6/0, $8 | Oct 29 | Feb 25 PM | Feb 26 | Park. R4 thin (low 7% over) |
| BLZE | $8.08 | 0.232 | 6/1/0, $15 | Nov 2 | Feb 22 PM | Feb 23 | Park (Apr16) |
| BKD | $9.27 | 0.052 | 6/0/0, $12 | Nov 6 | Feb 17 PM | Feb 18 | Park (Mar19 / Apr16) |
| SNDX | $9.53 | 0.019 | 11/0/0, $17 | Nov 2 | Feb 25 PM | Feb 26 | Park (Apr16) |
| GLUE | $10.58 | 0.056 | 10/0/0, $15 | Nov 5 | Mar 16 AM | Mar 17 | Park (Apr16) |
| EFC | $11.40 | 0.084 | 6/2/0, $13 | Nov 4 | Feb 24 PM | Feb 25 | Park. R4 thin (14%) |
| ARLO | $12.09 | 0.178 | 7/0/0, $17 | Nov 5 | Feb 25 PM | Feb 26 | Park (Apr16) |
| WULF | $12.52 | 0.148 | 27/1/0, $15 | Nov 6 | Feb 25 PM | Feb 26 | Park (Apr16) |
| CORZ | $12.74 | 0.108 | 21/2/0, $16 | Nov 5 | Mar 1 PM | Mar 2 | Park (Apr16) |
| ZURA | $1.20 | -0.489 | 8/0/0, $5 | Oct 27 | Mar 18 AM | Mar 19 | Park (Apr16). R1 below zero means a new low after the scanner's 52-week window |
| DNN | $2.33 | 0.158 | 15/0/0, $3.50 | Nov 4 | Mar 9 PM | Mar 10 | Park (Apr16). Killed Oct on R4/R6 |
| SOUN | $4.06 | 0.016 | 6/1/0, $5 | Nov 5 | Feb 25 PM | Feb 26 | Park (Apr16). R4 thin (23%) |
| UUUU | $7.34 | 0.052 | 8/0/0, $14 | Nov 4 | Feb 25 PM | Feb 26 | Park (Apr16) |

**R2 note for the parks:** these are December-quarter (10-K) prints. A print by ~Feb 26 clears (a) on Mar19, but (b) needs the 10-K deadline 5+ trading days before Mar 19, which only large accelerated filers (Mar 1) meet. Accelerated (Mar 16) and smaller (Mar 31) filers go to **Apr16**. Filer status gets checked when the chains list OI (~Dec 15), not tonight.

**ALT chain (Dec18, the only live window):**
- R2: Q3 Thu Nov 12 AM (v), LY Nov 6; Nov 12 + 21 = Dec 3, before Dec 18. 10-Q deadline Nov 9/16, well before. **Pass.**
- $2C: 0.10 / 0.45 (OI 264, spread 127%). **R7 fail.**
- $2.5C: 0.10 / 0.15 (OI 283, spread 40% of mid 0.125). **R7 fail.** BE at mid $2.625 = +23.8% from $2.12; the Oct 6 log's median print was ~4.7% (cap ~7.0%). **R6 fail by 3x.**
- $3C: 0.05 / 0.10 (OI 1,757, spread 67%). **R7 fail**, and BE $3.08 needs +45%.
- **KILLED R6 + R7** (third time: Oct 6 R6, Oct 28 R7). Also, the print is Thursday; a Tuesday buy would be a 1.5-day ramp hold, sold Wed 3:35.

**Paper-size passes (35), parked to ~Dec 15 with the rest:** RSI, STWD, JANX, UMAC, MLYS, BKV, RVLV, GPCR, VCYT, AGI, IONQ, KTOS, MP, XENE, PAAS, UCTT, ACMR, CYTK, HUT, PAM, DOCN, SRE, EXE, IRTC, CAMT, INSM, BWXT, AXSM, MTZ, STRL, AXON, EME, FIX, NXE, ARDX (ARDX stays dead for real money per the Oct 9 order).

## Tally

**28 names moved past the free screen** (3 R7 re-quotes, 25 date-staged) plus the 162-row free screen. **0 advanced, 0 buyable, 0 docs to write.** New kill: ALT (R6 + R7, Dec18). FUL, NRIX, SLM stay dead. 24 real-money-sized names and 35 paper-size names parked to ~Dec 15.

**Finding:** "just reported and fell" is the right pool for the Feb/Mar print cycle, and it's a big one (60 survivors of the free screen, 24 at real-money size, most with 8+ Buys and 0 Sells). But every one of them is a 10-K quarter, and Apr16 chains on $1-13 stocks don't carry OI for months. Nothing here is buyable before mid-December. The live Nov/Dec window is still empty at our size.

---

## GLOSSARY

- **R1 (range percentile):** where the stock sits in its 52-week range, 0 = at the low. Calls want under 0.25. Below zero means the price is under the scanner's 52-week low (a fresh low).
- **R2 (calendar):** the print has to land at least 21 days before expiry (later of the tool date and last year's date), with the 10-Q/10-K deadline at least 5 trading days before expiry.
- **R3 (ratings):** 3+ Buys, Buys at least equal to Holds, 0-1 Sells.
- **R4 (floor):** breakeven has to sit under the lowest Buy-side price target. "Proxy" means using the tool's low target against the stock price, before a strike is picked.
- **R6 (reachability):** the move needed to breakeven has to be no more than 1.5x the stock's median earnings-day move.
- **R7 (liquidity floor):** open interest of at least 250 and a spread of at most 25% of mid on the exact contract.
- **OI:** open interest, the contracts currently outstanding.
- **BE:** breakeven, strike plus premium paid.
- **(v) / (f):** verified (company-announced) or forecast earnings date.
- **Large accelerated filer:** a company with $700M+ public float; its 10-K is due 60 days after year end (Mar 1). Accelerated filers get 75 days (Mar 16), smaller ones 90 (Mar 31).
- **Park:** the name passed what can be checked now; the next check waits on a date (here, ~Dec 15, when spring chains carry OI).
- **Ramp hold:** owning the call only through the run-up into the print, sold the last run before it.
