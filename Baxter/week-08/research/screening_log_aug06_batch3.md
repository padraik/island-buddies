# Screening Log -- Aug 6, 2026 (Batch 3 of the 500-name sweep)

**Sweep running total entering this batch: 106 screened, 0 CALLS advances to DD, 0 survivors, 0 at 4/5.**

**Sectors, deliberately untouched by any prior batch:** defense electronics/space, waste management, logistics/freight brokers, pet retail/specialty retail, sporting goods/off-price retail, fabless/analog semiconductors, hospitals/managed care, auto manufacturers (fresh names).

## Stage 1 -- Range percentile (free, fetch_price.py --range)

60 attempted, 10 unavailable (SRCL, ECOL -- both real tickers, broker API rejected both as bad/delisted symbols; CHRW_DUP, LSTR_DUP, ODFL_DUP, CHWY_DUP, SWKS_DUP, UHS_DUP, MOH_DUP, CNC_DUP -- list-construction typos caught before costing anything, replaced with 7 fresh names before continuing), 50 valid.

| Ticker | Price | 52wk Range | Pctile | Direction |
|---|---|---|---|---|
| LDOS | $135.51 | 98.86-205.77 | 34th | MID-OUT |
| SAIC | $124.28 | 81.08-125.63 | 97th | PUTS (logged only) |
| KBR | $37.57 | 29.94-52.23 | 34th | MID-OUT |
| PLTR | $156.90 | 106.37-207.52 | 50th | MID-OUT |
| RKLB | $76.63 | 37.57-151.00 | 34th | MID-OUT |
| **LUNR** | **$15.13** | **7.78-46.75** | **19th** | **CALLS -- advances to chain** |
| ASTS | $68.09 | 36.08-133.86 | 33rd | MID-OUT |
| **RCAT** | **$8.30** | **5.77-18.78** | **19th** | **CALLS -- advances to chain** |
| **AVAV** | **$173.00** | **135.20-417.86** | **13th** | **CALLS -- advances to chain** |
| WM | $229.12 | 194.11-248.13 | 65th | MID-OUT |
| RSG | $208.00 | 196.41-238.62 | 27th | MID-OUT |
| WCN | $167.39 | 146.89-191.00 | 46th | MID-OUT |
| CLH | $307.64 | 201.34-335.94 | 79th | PUTS (logged only) |
| EXPD | $178.56 | 112.94-187.74 | 88th | PUTS (logged only) |
| FWRD | $17.99 | 7.86-32.00 | 42nd | MID-OUT |
| RXO | $20.61 | 10.43-29.90 | 52nd | MID-OUT |
| WERN | $36.87 | 23.06-47.49 | 57th | MID-OUT |
| ULH | $18.38 | 11.73-27.24 | 43rd | MID-OUT |
| **PETS** | **$1.97** | **1.57-4.10** | **16th** | **CALLS -- advances to chain** |
| WOOF | $2.77 | 2.24-4.19 | 27th | MID-OUT |
| **DKS** | **$198.62** | **186.67-244.38** | **21st** | **CALLS -- advances to chain** |
| ASO | $47.40 | 41.29-62.45 | 29th | MID-OUT |
| **OLLI** | **$77.97** | **60.29-141.08** | **22nd** | **CALLS -- advances to chain** |
| FIVE | $231.12 | 131.40-251.63 | 83rd | PUTS (logged only) |
| MTCH | $36.52 | 28.81-41.40 | 61st | MID-OUT |
| BBY | $80.21 | 55.10-91.27 | 69th | MID-OUT |
| BBWI | $20.55 | 14.28-32.32 | 35th | MID-OUT |
| ADI | $379.85 | 221.15-445.91 | 71st | MID-OUT |
| MRVL | $212.70 | 61.44-329.88 | 56th | MID-OUT |
| QRVO | $93.98 | 74.92-109.49 | 55th | MID-OUT |
| LSCC | $131.00 | 58.53-157.01 | 74th | MID-OUT |
| MPWR | $1369.09 | 785.00-1714.09 | 63rd | MID-OUT |
| TER | $388.20 | 104.58-487.91 | 74th | MID-OUT |
| ENTG | $142.95 | 67.97-186.94 | 63rd | MID-OUT |
| CYH | $2.99 | 2.40-4.43 | 29th | MID-OUT |
| THC | $256.64 | 157.58-265.31 | 92nd | PUTS (logged only) |
| HCA | $408.89 | 353.99-556.52 | 27th | MID-OUT |
| GM | $86.93 | 52.54-91.85 | 87th | PUTS (logged only) |
| F | $13.81 | 11.06-17.78 | 41st | MID-OUT |
| **STLA** | **$5.57** | **5.25-12.22** | **5th** | **CALLS -- advances to chain** |
| **TSLA** | **$320.47** | **297.38-498.83** | **11th** | **CALLS -- advances to chain** |
| RIVN | $15.43 | 11.58-22.69 | 35th | MID-OUT |
| **LCID** | **$6.96** | **2.37-25.23** | **20th** | **CALLS -- advances to chain** |
| **GXO** | **$46.98** | **45.40-66.85** | **7th** | **CALLS -- advances to chain** |
| ARCB | $135.25 | 59.43-176.69 | 65th | MID-OUT |
| SNDR | $35.22 | 20.11-39.27 | 79th | PUTS (logged only) |
| HTLD | $12.29 | 7.00-16.64 | 55th | MID-OUT |
| HMC | $30.75 | 23.25-34.89 | 64th | MID-OUT |
| TM | $187.49 | 166.10-248.90 | 26th | MID-OUT |
| RACE | $405.05 | 312.51-504.49 | 48th | MID-OUT |

**Tally: 33 MID-OUT, 7 PUTS-zone (logged, untouched), 10 CALLS-zone advance to chain -- the largest single-batch CALLS haul of the sweep so far: LUNR, RCAT, AVAV, PETS, DKS, OLLI, STLA, TSLA, LCID, GXO.**

## Stage 2 -- Chain feasibility (free scripts + MCP where the script's own chain-fetch got slow on wide/liquid names)

Ran all 10 chains before spending any search budget, per the cost-ordered funnel. Six died outright on cost/timing grounds without needing an earnings-date search:

- **PETS: KILLED on Rule 6, no search needed.** Penny stock ($1.97); coarse strike grid means the only tradeable call in range is $2C Sep18 at $0.15, needing +34.5%. No realistic earnings-day move justifies that gap regardless of date.
- **STLA: KILLED on calendar.** Stellantis already reported Q2 2026 on Jul 30, 2026. The tight-looking chain ($6C Sep18 at $0.25, 12.2% needed) is pricing a stock that's already had its catalyst. Next print not confirmed but well outside any near expiry.
- **TSLA: KILLED on Rule 5 (chain filter), real data.** Confirmed Q3 2026 earnings Oct 28 -- a real catalyst -- but pulled the real Nov 20 chain (the nearest expiry that brackets it) directly via MCP after the script's own fetch bogged down on TSLA's unusually large multi-page chain. IV is elevated enough that even 31% OTM ($420 strike, breakeven $421.65 vs $320.47 spot) still asks $8.40/share, nowhere near the live $1.00/share cap. Same shape as INTU in batch 1: a real catalyst, priced completely out of reach.
- **LCID: KILLED on calendar.** Lucid reported Q2 2026 on Aug 4, 2026 -- two days before this screen. Next print ~November. The cheap 20th-percentile chain is a post-earnings read, not a pre-earnings setup.
- **GXO: KILLED on calendar.** GXO Logistics reported Aug 5, 2026 -- one day before this screen. Same trap: the attractive-looking chain (8.1% needed at the cheapest Aug21 strike) is pricing a stock that already had its move.
- **AVAV: KILLED on chain gap.** AeroVironment's next earnings is confirmed Sep 9, 2026 (fiscal Q1 2027). The only cheap strikes on the free scan sat at the Aug 7 (1 DTE) expiry -- a coincidental weekly, not earnings-related. The Sep 18 expiry, which would bracket the real catalyst, returned no usable calls in range. No affordable instrument brackets the actual catalyst.

Two died on timing, no chain math needed:

- **RCAT: KILLED on timing.** Red Cat Holdings reports tonight, Aug 6, after close -- literally hours from this screen. Same as batch 2's FLO: no viable entry window exists between now and the print.

Two required the deeper look (earnings date + ratings + Rule 6):

- **OLLI: KILLED on chain gap.** Ollie's confirmed Q2 FY2026 earnings **Aug 27, 2026**. OLLI's real listed expiries jump Aug 21 -> Sep 18 (no Aug 28-style bracket the way INTU had). Sep 18 would technically bracket the catalyst, but the free scan found zero calls in the $0.10-$1.00 range at that expiry -- confirmed via the same script pass, not assumed. No affordable instrument for the real catalyst.
- **DKS: KILLED on Rule 5, real data.** Confirmed Q2 FY2026 earnings **Aug 25, 2026** (call scheduled). DKS's real expiries also jump Aug 21 -> Sep 18 (no Aug 28 bracket) -> Dec 18, so Sep 18 is the nearest expiry that brackets the catalyst. Pulled real Sep 18 asks via MCP: even the cheapest strike checked ($230, breakeven $233.43, +17.5% needed) still asks $4.60/share -- more than 4x the live $1.00 cap. Same IV-already-priced-in shape as TSLA and INTU.
- **LUNR: KILLED on Rule 6, marginal but decisive.** The one name this batch with a real near-term catalyst (**Q2 2026 earnings confirmed Aug 13, 2026**) and an actually-affordable chain (Aug 14 expiry, one day after the print, $16C at $0.72-$1.00, 12.4-13.8% needed). Rule 3: 9-analyst consensus is 7 Buy / 1 Hold / 1 Sell -- passes, but sitting exactly at the max-of-1-Sell limit, not comfortably under it (worth flagging, not blocking). Rule 4: Deutsche Bank cut its target to $20 from $34 on Jul 31, 2026 (fresh, inside the 60-day window) -- if DB is still Buy-rated post-cut, $20 clears the $16.72-$17.00 breakeven range with real margin; not independently confirmed DB's post-cut rating stayed Buy rather than dropping to Hold, flagged as a gap rather than assumed. **Rule 6 is the kill:** LUNR's own reported average earnings-day move is **7.92%**. 1.5x cap: **11.88%**. The cheapest usable strike needs 12.4-13.8% -- **1.04x to 1.74x the cap**, over the line at both ends of the available chain. This is a marginal fail in the same shape as the fund's own LYFT precedent (a required move sitting right at the ceiling rather than comfortably under it), but Tab 1's Rule 6 language is a hard gate ("no greater than 1.5x... fails regardless of Rules 1 through 5"), not a discretion call for a fresh entry the way it can be for an already-open position. No entry.

## Stage 3 -- Full DD

None reached DD. All ten CALLS-zone survivors died in Stage 2 (6 on calendar/chain-gap/timing with no search spent, 2 with one search each confirming the calendar/chain-gap kill, 1 -- LUNR -- on a real Rule 6 read after both searches).

## Batch 3 tally

**60 attempted, 50 valid, 10 CALLS-zone advances (the sweep's biggest single-batch haul), 0 reached full DD, 0 survivors, 0 at 4/5.** Notable: this batch is where the post-fix chain script proved its worth twice over -- TSLA and DKS both looked temptingly cheap on cursory inspection and both needed the real (post-earnings-window) chain pulled to confirm they were priced completely out of reach, not just "no data available."

7 PUTS-zone names logged, untouched: SAIC (97th), CLH (79th), EXPD (88th), FIVE (83rd), THC (92nd), GM (87th), SNDR (79th). Nothing individually flagged as a standout puts setup.

**Sweep running total: 156/500 screened, 0 CALLS advances to DD, 0 survivors, 0 at 4/5.**

Next: Batch 4, fresh sectors (utilities-adjacent independent power producers, homebuilders' building products already partly covered -- swap for HVAC/climate equipment, biotech mid-cap not yet covered, restaurants already covered -- swap for casual dining chains not yet in the book, media/entertainment streaming, cybersecurity fresh names, industrial gases/specialty materials).
