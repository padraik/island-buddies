# Screening Log -- Aug 7, 2026 (Calxter, parallel agent run)

Calxter's lane in the four-agent parallel screen (Bullxter, Bearxter, Macxter running simultaneously, each on a separate 50-name batch): a deliberately unthemed control-group sample, avoiding the sequential sweep's already-covered ground (airlines, defense, biotech large-cap, semis, utilities, telecom, apparel, software, banks, insurers, metals, ag, chemicals, food, beverages, rail equipment, medical devices, waste management, freight, retail, fabless semis, hospitals, autos, defense/space -- see `screening_log_aug06_batch1/2/3.md`). Reserve is $1,154.96, zero open positions, KR already cleared for entry separately (not re-screened here).

**Sectors this batch:** mid-cap biotech (fresh names, distinct from the large-cap names already screened Aug 6), casual dining, media/entertainment, education services, real estate services, specialty chemicals, misc industrials.

## Stage 1 -- Range percentile (free, fetch_price.py --range)

50 attempted, 2 unavailable (DENN -- broker API 400 error, bad symbol; EXPI -- broker API 404, not found), 48 valid. Hard cap reached at 50 attempts per protocol; no replacement names pulled in.

| Ticker | Price | 52wk Range | Pctile | Direction |
|---|---|---|---|---|
| EXEL | $53.19 | 33.76-57.57 | 82nd | PUTS (logged only) |
| SRPT | $16.67 | 14.68-25.32 | 19th | CALLS -- advances to chain |
| BMRN | $63.40 | 49.26-66.28 | 83rd | PUTS (logged only) |
| INCY | $118.84 | 76.79-132.60 | 75th | PUTS (logged only) |
| UTHR | $529.06 | 292.34-609.35 | 75th | PUTS (logged only) |
| RARE | $26.25 | 18.29-39.89 | 37th | MID-OUT |
| IONS | $55.03 | 40.03-86.74 | 32nd | MID-OUT |
| NBIX | $163.32 | 122.14-186.12 | 64th | MID-OUT |
| HALO | $99.02 | 61.23-99.15 | 100th | PUTS (logged only) |
| AXSM | $212.88 | 101.88-260.19 | 70th | MID-OUT |
| CAKE | $106.93 | 43.07-107.95 | 98th | PUTS (logged only) |
| DRI | $214.90 | 169.00-220.65 | 89th | PUTS (logged only) |
| TXRH | $208.87 | 153.82-213.26 | 93rd | PUTS (logged only) |
| BLMN | $11.05 | 5.19-12.63 | 79th | PUTS (logged only) |
| EAT | $227.25 | 100.30-229.99 | 98th | PUTS (logged only) |
| DENN | -- | -- | -- | unavailable |
| CBRL | $57.48 | 24.85-63.61 | 84th | PUTS (logged only) |
| DIN | $35.26 | 19.76-39.68 | 78th | PUTS (logged only) |
| JACK | $17.21 | 8.91-23.86 | 56th | MID-OUT |
| RRGB | $8.39 | 2.46-8.49 | 98th | PUTS (logged only) |
| WBD | $26.55 | 10.76-30.00 | 82nd | PUTS (logged only) |
| PARA | $1.87 | 1.71-85.60 | 0th | CALLS -- advances to chain (flagged, see Stage 1.5) |
| LYV | $182.93 | 125.34-188.00 | 92nd | PUTS (logged only) |
| FUBO | $9.37 | 7.95-56.64 | 3rd | CALLS -- advances to chain |
| CNK | $37.23 | 21.60-38.98 | 90th | PUTS (logged only) |
| IMAX | $49.41 | 24.20-51.60 | 92nd | PUTS (logged only) |
| SIRI | $29.63 | 19.77-32.66 | 77th | PUTS (logged only) |
| NWSA | $29.01 | 22.20-31.61 | 72nd | MID-OUT |
| LOPE | $150.07 | 134.27-223.04 | 18th | CALLS -- advances to chain |
| STRA | $83.63 | 69.70-89.73 | 70th | MID-OUT |
| LRN | $81.07 | 60.61-171.17 | 19th | CALLS -- advances to chain |
| CHGG | $0.88 | 0.45-1.90 | 30th | MID-OUT |
| COUR | $5.61 | 5.00-12.80 | 8th | CALLS -- advances to chain |
| DUOL | $125.86 | 87.89-468.00 | 10th | CALLS -- advances to chain |
| CBRE | $149.68 | 121.69-174.27 | 53rd | MID-OUT |
| JLL | $367.90 | 259.83-373.29 | 95th | PUTS (logged only) |
| CWK | $13.86 | 11.56-17.40 | 39th | MID-OUT |
| OPEN | $3.54 | 1.70-10.87 | 20th | CALLS -- advances to chain |
| EXPI | -- | -- | -- | unavailable |
| MMI | $32.13 | 24.43-33.62 | 84th | PUTS (logged only) |
| ASH | $72.69 | 46.30-74.99 | 92nd | PUTS (logged only) |
| FUL | $59.02 | 48.71-68.63 | 52nd | MID-OUT |
| OLN | $18.54 | 17.73-30.46 | 6th | CALLS -- advances to chain |
| CC | $15.50 | 10.44-28.67 | 28th | MID-OUT |
| HUN | $10.07 | 7.29-16.09 | 32nd | MID-OUT |
| CBT | $87.36 | 58.33-94.53 | 80th | PUTS (logged only) |
| PNR | $70.84 | 57.60-113.95 | 23rd | CALLS -- advances to chain |
| XYL | $121.36 | 105.29-154.27 | 33rd | MID-OUT |
| FLS | $79.92 | 48.71-92.41 | 71st | MID-OUT |
| DOV | $212.44 | 158.97-237.54 | 68th | MID-OUT |

**Tally: 16 MID-OUT, 22 PUTS-zone (logged, untouched, per no-dedicated-puts-pools rule), 10 CALLS-zone advance to chain: SRPT, PARA, FUBO, LOPE, LRN, COUR, DUOL, OPEN, OLN, PNR.**

## Stage 1.5 -- PARA data-integrity flag

PARA's range ($1.71-$85.60 against a $1.87 current price, 0th percentile) is not a real dislocation -- it's a dead ticker. Confirmed via web search: Paramount Global merged with Skydance in a deal that closed in 2025, and the combined company (Paramount Skydance Corp) now trades under **PSKY**. PARA/PARAA were delisted; whatever residual quote the broker API is still returning is stale/orphaned, not a tradeable instrument. Chain pull (below) confirms this independently -- no options chain exists at all.

## Stage 2 -- Chain feasibility (free, fetch_puts_chain.py --calls, post-fix version)

- **PARA: KILLED on no instrument, confirmed real (not the old script bug).** `fetch_puts_chain.py` returned a 404 on the options chain lookup itself -- there is no chain because there is no PARA anymore (see Stage 1.5). Cross-checked before trusting the kill per this run's standing instruction; confirmed genuine.
- **SRPT: real chain, several strikes in range (e.g. $17C Aug14, 3.6% needed).** Web search before spending DD time: **already reported Q2 2026 earnings Aug 5, 2026** (2 days before this screen). Next print not confirmed but standard cadence puts it ~November. **KILLED on calendar** -- the 19th-percentile dip is a post-earnings reaction, not a pre-earnings setup.
- **FUBO: real chain, cheap (e.g. $10C Aug14, 6.3% needed).** Web search: **already reported Q3 FY2026 earnings Aug 5, 2026.** Next print not confirmed, likely ~November. **KILLED on calendar.**
- **LOPE: real chain, cheapest usable strike ~10% needed.** Web search: **already reported Q2 2026 earnings Jul 30, 2026** (call after close). **KILLED on calendar.**
- **LRN: real chain, cheapest usable strike ~12% needed.** Web search: **already reported Q4 FY2026 earnings Aug 4, 2026.** **KILLED on calendar.**
- **COUR: real chain, very cheap near-ATM strike (~1.3% needed at the $5 strike).** Web search: **already reported Q2 2026 earnings Jul 29, 2026** (revenue beat, stock ran on it -- explains the low percentile being misleadingly "cheap-looking" post-pop). **KILLED on calendar.**
- **DUOL: real chain, several usable strikes (~12-20% needed at 7-14 DTE).** Web search: **already reported Q2 2026 earnings Aug 5, 2026.** **KILLED on calendar.**
- **OPEN: real chain, dirt cheap (2-3% needed at the nearest strikes).** Web search: **already reported Q2 2026 earnings Aug 4, 2026** (Financial Open House). **KILLED on calendar.**
- **OLN: real chain, cheapest usable strike ~10% needed.** Web search: **already reported Q2 2026 earnings Jul 30/31, 2026.** **KILLED on calendar.**
- **PNR: real chain, cheapest usable strike ~7.4% needed.** Web search: **already reported Q2 2026 earnings Jul 28, 2026.** **KILLED on calendar.**

**Pattern note, flagged by Bearxter's parallel batch and confirmed hard here: nine of this batch's ten CALLS-zone chain survivors died on the identical calendar trap** -- all reported Q2/fiscal-Q4 earnings between Jul 28 and Aug 5, 2026, the week immediately before this screen. Every one of them looked like a fresh bottom-quartile pre-earnings dislocation on Stage 1 data alone; every one was actually a post-earnings reaction with no confirmed near-dated catalyst left. Aug 7 sits in a real trough right after a broad wave of Q2 prints, exactly as flagged mid-run. Checked every survivor's last-reported date by search before any chain-affordability math was trusted as a real setup -- this is what caught it. PARA is the tenth, killed on a different mechanism (dead ticker) entirely.

## Stage 3 -- Full DD

None reached DD. All ten CALLS-zone survivors died in Stage 2 (nine on calendar, one on no-instrument/dead-ticker).

## Batch tally

**50 attempted, 48 valid, 10 CALLS-zone advances, all 10 killed in Stage 2 (9 calendar, 1 dead ticker). 0 advances to DD. 0 survivors at 3.5+. 0 at 4/5.**

22 PUTS-zone names logged, untouched, per the no-dedicated-puts-pools rule (back-test still gates live puts entries): EXEL (82nd), BMRN (83rd), INCY (75th), UTHR (75th), HALO (100th), CAKE (98th), DRI (89th), TXRH (93rd), BLMN (79th), EAT (98th), CBRL (84th), DIN (78th), RRGB (98th), WBD (82nd), LYV (92nd), CNK (90th), IMAX (92nd), SIRI (77th), JLL (95th), MMI (84th), ASH (92nd), CBT (80th). Nothing individually flagged as a standout puts setup this batch (no fresh downgrades or stalled-high patterns noted in passing).

**This batch: 50/50 screened, 0 CALLS advances to DD, 0 survivors, 0 at 4/5.**

Hard cap of 50 names reached. Stopping per protocol.
