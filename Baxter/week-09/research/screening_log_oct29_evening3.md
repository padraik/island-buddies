# Screening log: Thu Oct 29, EVENING 3 (10:00pm ET)

**Source:** EVENING 2's leftovers from saved scan `e6411b30-10ca-446f-a285-d47a7001c9a4` ($8.45-25 band): the four Dec18 names it couldn't chain (UTI, GDS, LINC, HSAI), the six Fri Nov 6 printers, and the eleven Saturday/later names re-rated free.
**Reserve / lines:** spendable $592.15 -> R5 line at 3.5/5 = **$0.59**. Every name here is paper-size at best.
**Data:** Thursday closing option quotes (stamped 19:59 UTC), stock quotes with after-hours prints to ~02:01 UTC Oct 30, analyst counts and earnings dates pulled live this run, HSAI earnings reactions from daily closes (`get_equity_historicals`). 0 web searches.

## Chain stage (Dec18 calls, Thursday closing quotes)

| Ticker | Dir | Stock | Print | R3 / tool low | Contract | Bid / Ask | OI | Spread | BE / needs | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| UTI | CALLS | 23.59 | Wed Nov 18 PM (v) | 6/1/0, low $25 | $22.5C / $25C / $27.5C | 2.70/2.95, 1.50/1.75, 0.75/1.05 | 71 / 74 / 18 | | $25.33+ on every strike | **KILLED R7** (no strike near 250 OI) **and R4** (low $25 under every BE) |
| GDS | CALLS | 23.16 (AH 22.70) | Wed Nov 18 AM (f), LY Nov 19; 20-F | 16/0/0, low $35.20 (updated Oct 1) | $23C / $24C / $25C / $26C | 2.05/3.30, 1.90/2.65, 1.65/2.55, 0.75/1.70 | 27 / 83 / **362** / 101 | $25C 42.9% | $27.55 / +19.0% | **KILLED R7** (the only 250+ OI strike has a 43% spread) |
| LINC | CALLS | 22.13 | Mon Nov 9 AM (v) | 6/0/0, low $40 | $22.5C / $25C / $30C | 1.85/2.05, 0.95/1.15, 0.20/0.35 | 15 / 50 / 151 | | | **KILLED R7** |
| HSAI | CALLS | 12.98 (AH 12.75) | Tue Nov 10 AM (v), LY Nov 11 2025 AM; 6-K filer, both dates present, Dec18 is 38 days past | 24/1/0, low $15.51, mean $26.47 | **$12.5C** / $14C / $15C / $16C | **1.55/1.70** / no quote / 0.65/0.75 / no quote | **226** / - / 356 / - | **9.2%** / - / 14.3% / - | **$14.20 / +9.4%**; $15C $15.75 / +21.3% | **$15C KILLED R4** (low $15.51 < BE $15.75). **$12.5C: R1-R4 pass, R6 PASS** (last 6 prints -0.9, +9.7, -9.9, -14.2, -9.0, -5.3 -> median **9.38%**, cap **14.06%**, needs 9.4%), R7 spread passes, **R7 OI FAILS (226 < 250)**, R5 fails for real money (1.70 > 0.59). **PAPER CANDIDATE, gated on OI.** |

EVENING 2's note that HSAI Dec18 had no $14 strike was half right: the $14C is listed (`e3c191b1`) but has no quote.

**HSAI $12.5C, what Saturday checks before a paper doc:** (1) OI on Friday's print (needs 250; was 226 with 118 traded Thursday, so it may cross); (2) whether the $15.51 low is dated inside 60 days (the tool shows no `updated_at`; Tab 6 dating rule); (3) direction: four of the last five prints went down (-9.9, -14.2, -9.0, -5.3). The rule is about size, not sign, and that history is Bearxter's whole argument. Ramp sell would be **Mon Nov 9 3:35pm** (pre-market print Tue Nov 10).

## The Nov 6 six (prints Fri Nov 6)

| Ticker | Stock (AH) | R3 / tool low | Result |
|---|---|---|---|
| GPCR | 21.94 (21.78) | 16/1/0, $70 | **DROPPED, R2 timing + R5 structural** |
| IMNM | 18.29 | 16/1/0, $24 | same |
| WULF | 12.75 (12.02, -5.7%) | 27/1/0, $15 | same |
| QBTS | 11.56 (11.13) | 15/2/1, $22 | same |
| QXO | 11.38 (11.08) | 19/0/0, $14 | same |
| USAR | 10.52 (10.08) | 8/0/0, $21 | same |

Not chained. The ramp deadline for a Nov 6 print is Thu Nov 5 3:35pm, which leaves Mon-Wed as the only entry runs. At $10-22 stocks with this IV, a Dec18 call that asks $0.59 or less sits ~30-40% out of the money, far past any R6 cap these names have printed. That's an estimate from the strike/IV structure, not a pulled chain; it's written that way on purpose. They come off the queue for this quarter.

## Re-rated free (Saturday and later names)

| Ticker | Stock (AH) | Buy/Hold/Sell | Tool low | R4 proxy | Next |
|---|---|---|---|---|---|
| CHWY | 20.83 | 22/9/0 | $21 (Oct 1) | **fails**: low only $0.17 over the stock; every call BE is above $21 | **KILLED R4 proxy** (structural) |
| PL | 14.31 (13.71) | 8/5/0 | $17 | pass | Jan15 chain (print Dec 10) |
| NNE | 12.21 (11.75) | 7/1/0 | $19 | pass | Jan15 chain (Dec 18 print) |
| INFQ | 9.43 (9.08) | 6/1/0 | $12 | pass | Jan15 chain (Nov 30 print) |
| APLD | 19.41 (18.33, -5.6%) | 18/2/0 | $22 | pass | Feb19 chain (Jan 7 print) |
| MIR | 18.67 (17.98) | 10/1/0 | $20 | pass, thin | Jan/Feb print, Saturday |
| GLXY | 18.13 (17.09, -5.7%) | 15/1/0 | $20.50 | pass | Saturday |
| HBAN | 15.97 | 16/7/0 | $17 (Oct 22) | pass | Saturday |
| NLY | 18.47 | 9/4/0 | $19.50 | pass, thin | Saturday |
| DX | 10.89 | 4/2/0 | $11.50 | pass, thin | Saturday |
| FLG | 10.47 | 12/7/0 | $11 | pass, thin | Saturday |

**After hours tonight:** the crypto/quantum/AI-infrastructure group sold off together (WULF -5.7%, GLXY -5.7%, APLD -5.6%, PL -4.2%, USAR -4.2%, NNE -3.8%, QBTS -3.7%, QUBT -3.4%, FRMI -3.1%). Cause unread (no search spent). PREMARKET should look at the open before reading anything into it.

## Tally

21 names touched. **Killed 4:** UTI (R7 + R4), GDS (R7), LINC (R7), CHWY (R4 proxy). HSAI $15C killed R4; HSAI $12.5C goes to paper watch, gated on R7 OI. **Dropped 6** (Nov 6 printers: R2 timing + R5 structural, not chained). 11 re-rated and kept (10 after CHWY). 0 advanced to a doc.

## GLOSSARY
- **R1-R7**: binder Tab 1 Iron Rules (calls). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor (lowest target above breakeven), R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven at expiry = strike + ask.
- **OI**: open interest, contracts outstanding.
- **AH**: after-hours trading price.
- **(v)/(f)**: earnings date verified by the company / estimated from cadence.
- **R4 proxy**: the screen-stage check that the tool's lowest target is above the stock with room for a breakeven; the real R4 is on the exact contract.
- **R2 timing**: the print lands so soon that the ramp-sell deadline leaves no entry run worth taking.
- **Paper-size**: passes everything but R5; belongs in the paper book, not real money.
- **6-K / 20-F filer**: foreign private issuer; no 10-Q deadline, so R2 needs both the tool date and last year's date.
- **Ramp sell**: selling before the earnings print, into the elevated premium, instead of holding through it.
