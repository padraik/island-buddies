# Screening log: Thu Oct 29, EVENING 2 (8:00pm ET)

**Source:** saved scan `e6411b30-10ca-446f-a285-d47a7001c9a4`, new config version with the price band moved to **$8.45-25** (all other filters unchanged: market cap >= $300M, prints Nov 2 2026 - Feb 12 2027, stock, R1 range pct < 0.25, call volume >= 300). **93 rows.** Plus NG (parked from EVENING 1).
**Reserve / lines:** spendable $592.15 -> R5 line at 3.5/5 = **$0.59**. At this band almost nothing is real-money size; the chain pass looked for R7-clean contracts that could also go to the paper book.
**Data:** Thursday closing quotes (option quotes stamped 19:59 UTC), analyst counts and earnings dates pulled live this run, earnings reactions from daily closes (`get_equity_historicals`). 0 web searches.

## NG (parked from EVENING 1)

| Ticker | Dir | R1 | R2 | R3 | Chain | R6 | Result |
|---|---|---|---|---|---|---|---|
| NG | CALLS | 0.11 ($6.17; 52w closes $5.18-14.20) | Q4 FY26 Jan 21 2027 AM (f), LY Jan 22; **no Feb19 expiry exists** (chain: Nov20, Dec18, Mar19, Jun17...) -> Mar19 | 6/0/0, low $12.02 | Mar19 $6C 0.80/1.25 (OI 1,718) R5 fail; $7C 0.65/0.75 (OI 1,972) R5 fail; **$8C 0.45/0.50, OI 903, spread 10.5%**: R5/R7 pass, BE $8.50 = **+37.8%** | Last 6 prints: -5.1, +15.0, +5.0, +4.2, -14.1, -1.3 -> median **5.07%**, cap **7.6%** | **KILLED R6** (structural: even the $6C ATM needs ~+17%). Don't bring back this quarter. |

## The $8.45-25 band (93 rows)

**Out on Rule 3 (30):** UPST (2 Sell), CMCSA (4 Sell), FIG (7B/10H), CPB, WSC (4B/7H), PZZA, MOS (2 Sell), SOFI (5 Sell), CRK, HL (5B/6H), CAG, KD, KLAR (11B/15H), PCG (10B/11H), TTD, SBGI, F, INFY, NU (2 Sell), FCEL (2 Sell), LI, SMPL, XRAY, XIFR, CSIQ, TRIP, XPEV (2 Sell), HUN, AGNC (3B/10H), NVTS.
**No coverage (9):** CPS, BMNR, PPTA, CDNL, XRPN, GEL, NN, HIMX, CCXI.
**Out on R4 proxy, tool low under the stock (4):** BETR (low $16 vs $21.89), T ($20 vs $21.02), JANX ($14 vs $17.83), DKNG ($20 vs $20.55; also prints Nov 5).
**Out on R2 timing, prints Mon Nov 2 - Thu Nov 5 (ramp deadline is Friday's or Monday's run; nothing to stand on) (16):** IREN, BTU, BCE, RARE, EYE, SMMT, AG, CPNG, CORZ, CDE, RIOT, EFC, LUNR, PAR, RDW, NXE. ALM (Nov 3) was already dead on R7 (Oct 27).
**Deferred, prints Fri Nov 6 (ramp deadline Thu Nov 5 3:35pm, so an entry window of Mon-Wed only) (6):** GPCR, IMNM, WULF, QBTS, QXO, USAR. R3/R4 proxy pass on all six. Not chained tonight; EVENING 3 chains them only if a contract could be real-money size.
**R3 + R4 proxy pass, print Nov 9 or later (28):** UTI, FIGR, GDS, LINC, CHWY, APLD, FLY, NLY, MIR, GLXY, LBRT (targets stamped Nov 2024, stale), HBAN, XP, PL, BILI, HSAI, NNE, JBS, RGTI, BBAR, WYFI, DX, FLG, INFQ, ORIC, AMPX, EQX (dead on R7/R6 since Oct 27, not re-chained).

## Chain stage (Dec18 calls, Thursday closing quotes)

| Ticker | Stock | Print | Contract | Bid / Ask | OI | Spread | BE / needs | Result |
|---|---|---|---|---|---|---|---|---|
| AMPX | 8.84 | Nov 11 | $9C / $10C / $11C | 1.15/1.25, 0.75/0.90, 0.50/0.65 | 77 / 103 / 20 | | | **KILLED R5** (every ask > 0.59) **and R7** (OI) |
| ORIC | 8.99 | Nov 13 | $9-11C | 1.80/4.90, 0.10/4.90 | 0-1 | | | **KILLED R7** (no market) |
| RGTI | 11.79 | Nov 10 PM (v) | $13C | 0.99/1.08 | 2,147 | 8.7% | $14.08 / +19.4% | R5 fails (real), R7 passes. Last 8 prints median **6.0%**, cap 9.0%. **KILLED R6** (paper too) |
| JBS | 12.16 | Nov 10 | $12.5C / $14C | 0.50/0.65, 0/0.45 | 8 / 0 | | | **KILLED R7** |
| XP | 14.86 | Nov 17 | $15C / $16C | 1.10/1.30, 0.75/0.90 | 26 / 383 | 18% ($16C) | $16.90 / +13.7% | **KILLED R4**: tool low $14.97 < BE $16.90 (and R5) |
| WYFI | 11.15 | Nov 13 | $12.5C / $14C | 1.25/1.65, 0.35/1.40 | 78 / 0 | | | **KILLED R7** |
| BBAR | 11.73 | Nov 25 | $12C / $13C | 0.65/1.05, 0.30/0.95 | 5 / 1 | | | **KILLED R7** |
| BILI | 13.31 | Nov 12 AM (f) | $14C | 0.36/0.61 | 6 | 51% | | **KILLED R7** |
| FLY | 19.25 | Nov 10 | $20C | 2.15/2.90 | 23 | | | **KILLED R7** (and R5) |
| FIGR | 22.99 | Nov 12 AM (v) | $25C | 2.20/2.65 | 286 | 18.6% | $27.65 / +20.3% | R5 fails (real), R7 passes. 4 prints: +16.3, -25.7, +1.4, +3.9 -> median **10.1%**, cap 15.2%. **KILLED R6** (paper too) |
| HSAI | 12.98 | Nov 10 | Dec18 $14C | | | | | No $14 strike listed; not chained. To EVENING 3 with the full strike list. |

**Tally:** 94 names touched (93 + NG). Band: 59 out free (30 R3, 9 coverage, 4 R4 proxy, 16 R2 timing) + 6 deferred + 28 passed = 93. **Killed: 59 free + 11 at the chain/R6 stage (NG, AMPX, ORIC, RGTI, JBS, XP, WYFI, BBAR, BILI, FLY, FIGR) = 70.** 0 advanced. No doc to write.

## What's left for EVENING 3 / Saturday
- Dec18 names not yet chained: **UTI** ($23.21, Nov 19), **GDS** ($22.95, Nov 19, 20-F filer: both dates needed), **LINC** ($22.13, Nov 9), **HSAI** ($12.98, Nov 10, 20-F). All paper-size at best.
- December prints, Jan15 expiry: **CHWY** ($20.88, Dec 10; low $21 barely over the stock), **PL** ($13.81, Dec 10), **NNE** ($12.20, Dec 18), **APLD** ($19.42, Jan 7 -> Feb19), **INFQ** ($9.13, Nov 30 -> Jan15).
- Jan/Feb prints (far; Saturday decides if worth a Mar19 look): MIR, GLXY, HBAN, NLY, DX, FLG; LBRT needs dated targets.
- Nov 6 six: GPCR, IMNM, WULF, QBTS, QXO, USAR (entry window Mon-Wed only).

## GLOSSARY
- **R1-R7**: binder Tab 1 Iron Rules (calls). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest target above breakeven), R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven at expiry = strike + ask.
- **OI**: open interest, contracts outstanding.
- **(v)/(f)**: earnings date verified by the company / estimated from cadence.
- **R2 timing**: the print lands so soon that the ramp-sell deadline leaves no entry run worth taking.
- **Paper-size**: passes everything but R5; belongs in the paper book, not real money.
- **20-F / 6-K filer**: foreign private issuer; no 10-Q deadline, so R2 needs both the tool date and last year's date.
