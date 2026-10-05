# Full-Universe Sweep, Oct 5, 2026

*Baxter, Monday Oct 5, afternoon. Era 2's first full sweep. Michael's ask: start fresh with the whole market, not the leftovers.*

## METHOD

One saved scan (`Baxter Oct5 Full Sweep`, plus three price-band copies to get under the scanner's 200-row cap) with Rule 1 computed inside the scanner itself for the first time: an expression filter `(price - 52w low) / (52w high - 52w low) < 0.25`. No more hand-computing percentiles band by band. Other filters: market cap $300M and up, common stock, next print between Oct 7 and Nov 9 (the 35-day Rule 2 window).

Then one free structured pass for Rule 3 and a Rule 4 proxy across everything tradeable: `get_equity_analyst_ratings` takes 75 symbols a call, so 506 names took 7 calls.

## THE FUNNEL

| Stage | Names | What it cut |
|---|---|---|
| Scanner: bottom quartile + print in window + $300M+ | 718 | |
| Tradeable for us | 506 | 166 priced over $70 (no sub-$1.00 contract reaches a breakeven there), 23 closed-end/muni funds and share-class duplicates, 23 under $2 |
| Rule 3 (0-1 Sell, 3+ Buy, Buys at least equal to Holds) | 220 | No coverage, Sell-heavy, Hold-heavy |
| Rule 4 proxy (lowest target of ANY rating at least 10% over last) | **163** | Floor too close to the price |

The Rule 4 proxy is stricter than the rule, because it uses the lowest target of every rating, Holds included. The real check (lowest *Buy* target, dated inside 60 days, above the actual breakeven) still happens at doc stage. Rules 5 and 6 haven't touched these names yet. That's the queue's job, at most 5 chain checks a run.

Already dead today and left off the lists: MRP (R6 killed Oct 5 MIDDAY (median 2.24%)), CDRE (R5/liquidity killed Oct 5 OPEN (OI 0)), MIR (R6 killed Oct 5 OPEN), AEVA (R4 strikes killed Oct 5 MIDDAY), PRME (R4/no market killed Oct 5 MIDDAY), CIFR (R4 strikes killed Oct 5 MIDDAY). Already in the queue before the sweep: CWH, LRMR, MFA, PCT, RWT.

## TIER A: QUEUED NOW (30, in print-date order)

Revenue-stage businesses where an earnings print actually forces a resolution, priced where a sub-$1.00 contract can exist, print far enough out to research and still sell the ramp. Queue order = print date, so nothing ages out before its turn.

| Ticker | Last | Range pct | Print | B/H/S | Low target | Low vs last |
|---|---|---|---|---|---|---|
| PRG | $31.23 | 0.25 | 10/22 | 6/1/0 | $45 | +44% |
| LVS | $36.57 | 0.01 | 10/22 | 17/7/0 | $47 | +29% |
| COUR | $5.18 | 0.10 | 10/23 | 8/4/0 | $6.5 | +25% |
| METC | $8.29 | 0.01 | 10/27 | 6/3/0 | $11 | +33% |
| MMYT | $44.84 | 0.19 | 10/28 | 10/0/0 | $60 | +34% |
| KGC | $23.73 | 0.10 | 10/28 | 18/2/1 | $30 | +26% |
| GIL | $40.46 | 0.02 | 10/29 | 14/1/0 | $54 | +33% |
| ORN | $9.31 | 0.13 | 10/29 | 7/0/0 | $13 | +40% |
| NMRK | $12.62 | 0.06 | 10/29 | 7/1/0 | $17.5 | +39% |
| TREE | $24.36 | 0.02 | 10/30 | 6/0/0 | $45 | +85% |
| ALHC | $8.22 | 0.05 | 10/30 | 12/2/0 | $13 | +58% |
| PHAT | $6.74 | -0.01 | 10/30 | 9/2/0 | $10 | +48% |
| OMCL | $33.81 | 0.18 | 10/30 | 7/1/0 | $45 | +33% |
| APTV | $44.34 | 0.05 | 10/30 | 18/4/0 | $55 | +24% |
| CALX | $34.77 | 0.06 | 11/02 | 8/1/0 | $52 | +50% |
| ADTN | $7.08 | 0.03 | 11/03 | 7/2/0 | $11 | +55% |
| GRAB | $3.16 | 0.11 | 11/03 | 24/0/0 | $4.5 | +42% |
| KTOS | $43.10 | 0.01 | 11/04 | 22/2/0 | $60 | +39% |
| FWRG | $10.15 | 0.03 | 11/04 | 10/0/0 | $15 | +48% |
| UUUU | $10.88 | 0.01 | 11/04 | 9/0/0 | $16 | +47% |
| YUMC | $40.16 | 0.02 | 11/04 | 22/2/0 | $52 | +29% |
| REZI | $18.48 | 0.07 | 11/05 | 6/1/0 | $27 | +46% |
| BROS | $38.02 | 0.02 | 11/05 | 27/0/1 | $50 | +31% |
| AMPX | $9.39 | 0.10 | 11/06 | 11/0/0 | $18 | +92% |
| COLL | $22.03 | 0.02 | 11/06 | 7/1/0 | $43 | +95% |
| KRMN | $33.88 | 0.03 | 11/06 | 13/0/0 | $63 | +86% |
| AORT | $22.68 | 0.12 | 11/06 | 8/0/0 | $38 | +68% |
| QXO | $11.98 | 0.05 | 11/06 | 18/0/0 | $18 | +50% |
| QBTS | $15.39 | 0.08 | 11/06 | 15/2/1 | $22 | +43% |
| CARG | $29.69 | 0.22 | 11/06 | 10/5/0 | $38 | +28% |

## TIER B: NEXT WHEN THE QUEUE RUNS LOW (93, by floor margin)

Same rules passed; lower priority because of thinner floor margin, slower movers (utilities, REITs, insurers: check Rule 6 history before spending a chain check on any of them), or a print too close or too far.

| Ticker | Last | Range pct | Print | B/H/S | Low target | Low vs last |
|---|---|---|---|---|---|---|
| ARDX | $3.31 | 0.00 | 10/30 | 11/0/0 | $8 | +142% |
| PHAR | $9.75 | 0.01 | 11/04 | 7/0/0 | $20.46 | +110% |
| LASR | $40.01 | 0.20 | 11/06 | 8/1/0 | $81 | +102% |
| NG | $6.45 | 0.15 | 10/08 | 6/0/0 | $11.97 | +86% |
| ENVX | $2.72 | 0.02 | 11/05 | 7/3/1 | $5 | +84% |
| WRN | $2.15 | 0.12 | 11/06 | 6/0/0 | $3.89 | +81% |
| TPB | $57.99 | 0.04 | 11/05 | 6/0/0 | $90 | +55% |
| USAR | $13.56 | 0.06 | 11/06 | 7/0/0 | $21 | +55% |
| IE | $10.41 | 0.19 | 11/05 | 7/0/0 | $16 | +54% |
| TBLA | $3.27 | 0.15 | 11/05 | 5/4/0 | $5 | +53% |
| BKSY | $21.61 | 0.23 | 11/06 | 6/1/0 | $33 | +53% |
| CENX | $36.65 | 0.25 | 11/06 | 6/0/0 | $55 | +50% |
| AMRC | $21.36 | 0.11 | 11/03 | 8/4/0 | $32 | +50% |
| INDI | $2.90 | 0.15 | 11/06 | 6/2/0 | $4.25 | +47% |
| BXMT | $10.94 | 0.01 | 10/29 | 5/4/0 | $16 | +46% |
| RITM | $8.74 | 0.08 | 10/30 | 11/0/0 | $12.5 | +43% |
| HLMN | $7.03 | 0.09 | 11/04 | 6/2/0 | $10 | +42% |
| VYX | $6.96 | 0.14 | 11/06 | 6/1/0 | $9.75 | +40% |
| ARLO | $12.86 | 0.20 | 11/06 | 7/0/0 | $18 | +40% |
| TKC | $5.15 | 0.14 | 11/06 | 6/0/0 | $7.07 | +37% |
| TRTX | $6.13 | 0.02 | 10/28 | 5/0/1 | $8.25 | +34% |
| NSSC | $35.98 | 0.12 | 11/03 | 6/0/0 | $48 | +33% |
| MBUU | $22.61 | 0.03 | 10/30 | 5/5/0 | $30 | +33% |
| GRNT | $4.53 | 0.18 | 11/06 | 5/2/0 | $6 | +32% |
| DX | $10.96 | 0.02 | 10/20 | 4/2/0 | $14.5 | +32% |
| ENOV | $18.44 | 0.07 | 11/06 | 12/1/0 | $24 | +30% |
| MNTN | $10.04 | 0.22 | 11/04 | 10/1/0 | $13 | +29% |
| SGI | $62.44 | 0.06 | 11/06 | 11/1/0 | $80 | +28% |
| WY | $18.75 | 0.04 | 10/29 | 9/3/1 | $24 | +28% |
| KRUS | $39.89 | 0.13 | 11/06 | 6/3/0 | $51 | +28% |
| CWEN | $29.83 | 0.10 | 11/04 | 11/1/0 | $38 | +27% |
| PATK | $66.49 | 0.00 | 10/30 | 8/2/1 | $84 | +26% |
| UPBD | $15.86 | 0.08 | 10/30 | 5/1/0 | $20 | +26% |
| CWK | $11.99 | 0.07 | 10/30 | 8/5/0 | $15 | +25% |
| AHCO | $5.62 | 0.05 | 11/04 | 7/0/0 | $7 | +24% |
| SUZ | $8.36 | 0.20 | 11/06 | 11/0/0 | $10.39 | +24% |
| TNL | $62.30 | 0.18 | 10/22 | 11/1/0 | $77 | +24% |
| SMG | $48.56 | 0.02 | 11/04 | 5/3/0 | $60 | +24% |
| EYE | $16.27 | 0.10 | 11/05 | 9/3/0 | $20 | +23% |
| MLCO | $4.33 | 0.05 | 11/06 | 11/4/0 | $5.3 | +23% |
| ATMU | $45.75 | 0.13 | 11/06 | 5/1/0 | $56 | +22% |
| PAR | $14.71 | 0.11 | 11/06 | 7/2/0 | $18 | +22% |
| STEP | $45.02 | 0.16 | 11/06 | 9/1/0 | $55 | +22% |
| ULS | $67.80 | 0.10 | 11/04 | 9/6/0 | $82.8 | +22% |
| NLY | $18.45 | 0.01 | 10/20 | 9/4/0 | $22.5 | +22% |
| PBH | $45.17 | 0.09 | 11/06 | 5/2/0 | $55 | +22% |
| EFC | $11.51 | 0.08 | 11/05 | 5/2/0 | $14 | +22% |
| MP | $47.18 | 0.15 | 11/06 | 16/1/0 | $57 | +21% |
| RKT | $11.63 | 0.03 | 10/30 | 10/8/0 | $14 | +20% |
| GXO | $45.82 | 0.10 | 11/04 | 17/1/0 | $55 | +20% |
| RRR | $51.02 | 0.16 | 10/28 | 18/2/0 | $61 | +20% |
| FNF | $39.34 | 0.06 | 11/06 | 4/2/0 | $47 | +19% |
| BRSL | $9.97 | 0.04 | 11/04 | 7/3/0 | $11.9 | +19% |
| ADNT | $17.65 | 0.11 | 11/05 | 9/3/1 | $21 | +19% |
| AGI | $32.03 | 0.18 | 10/28 | 14/0/0 | $38.1 | +19% |
| LADR | $8.62 | 0.02 | 10/23 | 6/1/0 | $10.25 | +19% |
| AKR | $18.50 | 0.01 | 10/28 | 6/0/0 | $22 | +19% |
| PSN | $42.38 | 0.12 | 11/05 | 12/3/0 | $50 | +18% |
| TFPM | $30.34 | 0.25 | 11/04 | 8/3/0 | $35.66 | +18% |
| PRVA | $20.44 | 0.15 | 11/06 | 17/1/0 | $24 | +17% |
| CX | $9.41 | 0.10 | 10/26 | 15/4/0 | $11 | +17% |
| PLNT | $42.10 | 0.07 | 11/06 | 14/6/0 | $49.2 | +17% |
| SFD | $18.85 | 0.03 | 10/28 | 6/2/0 | $22 | +17% |
| FCPT | $21.45 | 0.02 | 10/28 | 5/5/0 | $25 | +17% |
| EPRT | $25.83 | 0.05 | 10/21 | 18/1/0 | $30 | +16% |
| IRT | $14.65 | 0.09 | 10/30 | 10/3/0 | $17 | +16% |
| ATEC | $10.37 | 0.22 | 10/30 | 14/0/0 | $12 | +16% |
| KVYO | $16.43 | 0.19 | 11/05 | 23/2/0 | $19 | +16% |
| OTF | $9.52 | -0.01 | 11/06 | 5/4/0 | $11 | +16% |
| ONT | $12.99 | 0.04 | 11/04 | 4/2/1 | $15 | +15% |
| AA | $43.09 | 0.18 | 10/16 | 12/5/1 | $49.7 | +15% |
| VICI | $22.64 | 0.01 | 10/28 | 16/9/0 | $26 | +15% |
| NTST | $17.50 | 0.09 | 10/27 | 15/4/0 | $20 | +14% |
| VLRS | $6.50 | 0.14 | 10/27 | 9/4/1 | $7.4 | +14% |
| PFSI | $62.45 | 0.02 | 10/21 | 4/4/0 | $71 | +14% |
| GLPI | $37.96 | 0.05 | 10/29 | 15/8/1 | $43 | +13% |
| HDB | $22.15 | 0.02 | 10/16 | 41/2/0 | $25.08 | +13% |
| MDU | $18.56 | 0.16 | 11/06 | 6/3/0 | $21 | +13% |
| GLXY | $22.99 | 0.22 | 10/21 | 14/2/0 | $26 | +13% |
| FIS | $32.73 | 0.02 | 11/05 | 17/15/1 | $37 | +13% |
| CMG | $31.03 | 0.20 | 10/28 | 26/13/0 | $35 | +13% |
| SRAD | $12.18 | 0.05 | 11/05 | 18/7/0 | $13.67 | +12% |
| FE | $43.75 | 0.11 | 10/22 | 10/8/0 | $49 | +12% |
| CPRI | $14.32 | 0.12 | 11/04 | 10/8/0 | $16 | +12% |
| LPX | $66.30 | 0.11 | 11/05 | 14/2/1 | $74 | +12% |
| HBAN | $15.29 | 0.10 | 10/22 | 16/6/0 | $17 | +11% |
| NHI | $65.68 | 0.04 | 11/06 | 6/3/0 | $73 | +11% |
| ALLY | $37.81 | 0.17 | 10/20 | 17/4/0 | $42 | +11% |
| DEC | $13.52 | 0.18 | 11/03 | 12/1/0 | $15 | +11% |
| FLG | $11.73 | 0.24 | 10/23 | 12/7/0 | $13 | +11% |
| VNT | $31.60 | 0.21 | 10/30 | 7/4/1 | $35 | +11% |
| IP | $31.61 | 0.11 | 10/28 | 9/4/1 | $35 | +11% |
| LKQ | $22.68 | 0.09 | 10/30 | 10/2/0 | $25 | +10% |

## TIER C: BOTZ RISK (30)

Mostly pre-revenue biotech and early-stage miners. They pass Rules 1, 3 and 4 with huge floor margins because analysts price pipelines, not quarters. But their earnings prints rarely force anything: the stock moves on trial data and financings. Rule 2 says earnings has to be the mechanism. Only worth a look if the print itself carries a real catalyst (a launch quarter, first revenue, a guided readout on the call).

| Ticker | Last | Range pct | Print | B/H/S | Low target | Low vs last |
|---|---|---|---|---|---|---|
| ALT | $2.69 | 0.03 | 11/06 | 9/1/0 | $11 | +308% |
| BIOA | $6.31 | 0.06 | 11/06 | 7/2/0 | $20 | +217% |
| GPCR | $26.46 | 0.01 | 11/06 | 16/1/0 | $70 | +165% |
| OCUL | $6.83 | 0.06 | 11/04 | 12/0/0 | $18 | +163% |
| CRVS | $10.46 | 0.20 | 11/04 | 8/0/0 | $27 | +158% |
| GLUE | $10.17 | 0.16 | 11/06 | 9/0/0 | $25 | +146% |
| CTMX | $2.48 | -0.01 | 11/06 | 8/0/0 | $6 | +141% |
| OCS | $8.81 | 0.01 | 11/05 | 11/0/0 | $19.53 | +122% |
| SANA | $2.83 | 0.06 | 11/06 | 9/1/0 | $6 | +112% |
| AVTX | $14.42 | 0.16 | 11/06 | 13/0/0 | $30 | +108% |
| TSHA | $4.46 | 0.21 | 11/04 | 13/0/0 | $9 | +102% |
| MAZE | $25.86 | 0.12 | 11/06 | 13/0/0 | $46 | +78% |
| NAMS | $22.34 | 0.06 | 11/05 | 16/1/0 | $38 | +70% |
| MUX | $17.69 | 0.19 | 11/06 | 6/0/0 | $28 | +58% |
| NUVB | $4.88 | 0.24 | 11/03 | 12/1/0 | $7 | +43% |
| DNN | $2.62 | 0.19 | 11/03 | 16/0/0 | $3.73 | +43% |
| TMQ | $3.04 | 0.10 | 10/07 | 3/3/0 | $4.3 | +42% |
| STOK | $25.07 | 0.24 | 11/04 | 14/0/0 | $35 | +40% |
| GROY | $2.94 | 0.16 | 11/05 | 7/0/0 | $4 | +36% |
| RGNX | $7.62 | 0.20 | 11/06 | 10/2/0 | $10 | +31% |
| VKTX | $29.27 | 0.20 | 10/22 | 18/2/0 | $38 | +30% |
| EQX | $11.06 | 0.25 | 11/04 | 12/0/0 | $14 | +27% |
| IONS | $43.04 | 0.00 | 10/29 | 22/5/0 | $54 | +25% |
| EXK | $8.52 | 0.23 | 11/06 | 7/1/0 | $10.57 | +24% |
| XENE | $37.15 | 0.03 | 11/03 | 18/1/0 | $46 | +24% |
| NKTR | $41.69 | 0.11 | 11/06 | 10/2/0 | $50 | +20% |
| VERA | $28.87 | 0.18 | 11/05 | 13/1/0 | $34 | +18% |
| IMCR | $29.48 | 0.15 | 11/06 | 10/4/0 | $34 | +15% |
| PTCT | $62.84 | 0.05 | 11/04 | 12/2/1 | $70 | +11% |
| RARE | $14.37 | 0.06 | 11/04 | 11/10/0 | $16 | +11% |

## WHAT THIS SWEEP IS GOOD FOR

The pool ages as prints approach. Tier A covers roughly the next two weeks of runs at 5 chain checks per run. Re-run the sweep scan (same saved scans, print window moved forward) around Oct 19, or sooner if Tier A and B are both worked through.

## GLOSSARY

- **52-week range percentile (Rule 1):** where today's price sits between the lowest and highest price of the past year. 0.00 = at the low, 1.00 = at the high. We want the bottom quarter.
- **Rule 2 window:** the company must report earnings before the option expires. 35 days out is how far we look.
- **Rule 3:** analysts who cover it mostly say Buy, with at most one Sell.
- **Rule 4 (bear floor):** the most pessimistic Buy-rated analyst's price target has to sit above our breakeven (strike plus what we pay).
- **Rule 5:** one contract has to be affordable for the fund's size (currently $1.00 a share at most).
- **Rule 6 (reachability):** the stock move needed to reach breakeven can't be more than 1.5 times its typical earnings-day move.
- **BOTZ risk:** named after an old pass. A story with no event that forces the stock to resolve on our clock.
- **Floor margin:** how far the lowest analyst target sits above today's price.
- **Sell the ramp:** sell before the print, while options are still priced for the event, instead of holding through it.
