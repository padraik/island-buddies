# Screening Log -- Aug 7, 2026 (Bearxter's lane, parallel run with Bullxter/Macxter/Calxter)

Four agents running simultaneously against the same 500-name sweep target, each on an independent sector lane to avoid overlap. This is Bearxter's batch: industrials/machinery (non-ag, non-defense), healthcare services/managed care adjacent (not biotech/hospitals, already covered), specialty insurance, staffing/business services, packaging, building products. Reserve $1,154.96, zero open positions, KR pitch-ready and not re-screened here.

## Stage 1 -- Range percentile (free, fetch_price.py --range)

56 attempted, 6 unavailable via broker API (RE, ESGR, ASGN, BERY, GMS, WNS -- all real tickers, all rejected as bad/delisted symbols; WNS and GMS specifically were both acquired/taken private in 2025-2026 and no longer trade), replaced in-line with fresh names before continuing (SIGI, RGP, CTAS, OC). 50 valid.

| Ticker | Price | 52wk Range | Pctile | Direction |
|---|---|---|---|---|
| CAT | $848.31 | 405.46-1073.46 | 66th | MID-OUT |
| PCAR | $132.40 | 92.25-139.24 | 85th | PUTS (logged only) |
| IR | $88.81 | 68.07-100.96 | 63rd | MID-OUT |
| DOV | $212.44 | 158.97-237.54 | 68th | MID-OUT |
| ITW | $296.10 | 238.82-303.15 | 89th | PUTS (logged only) |
| PH | $1084.79 | 708.18-1099.94 | 96th | PUTS (logged only) |
| EMR | $158.18 | 122.64-165.15 | 84th | PUTS (logged only) |
| ROK | $441.62 | 328.70-497.36 | 67th | MID-OUT |
| UNH | $405.61 | 239.50-461.62 | 75th | MID-OUT |
| CI | $277.68 | 239.51-315.47 | 50th | MID-OUT |
| HUM | $372.64 | 163.11-428.88 | 79th | PUTS (logged only) |
| CNC | $64.91 | 25.07-69.36 | 90th | PUTS (logged only) |
| ELV | $389.57 | 274.84-436.24 | 71st | MID-OUT |
| MOH | $193.19 | 121.06-244.89 | 58th | MID-OUT |
| DVA | $178.43 | 101.00-247.49 | 53rd | MID-OUT |
| DGX | $238.00 | 171.18-240.13 | 97th | PUTS (logged only) |
| LH | $316.64 | 244.52-317.50 | 99th | PUTS (logged only) |
| RLI | $63.63 | 47.26-69.19 | 75th | MID-OUT |
| ERIE | $251.19 | 204.63-380.67 | 26th | MID-OUT |
| KNSL | $374.39 | 287.20-485.00 | 44th | MID-OUT |
| MKL | $1868.19 | 1719.41-2207.59 | 30th | MID-OUT |
| ACGL | $98.19 | 82.44-107.08 | 64th | MID-OUT |
| RNR | $320.31 | 231.17-335.97 | 85th | PUTS (logged only) |
| AGO | $77.78 | 72.76-92.39 | 26th | MID-OUT |
| RHI | $42.24 | 21.83-42.25 | 100th | PUTS (logged only) |
| MAN | $56.10 | 25.15-57.08 | 97th | PUTS (logged only) |
| TNET | $66.47 | 33.60-73.08 | 83rd | PUTS (logged only) |
| KFY | $82.70 | 58.95-85.69 | 89th | PUTS (logged only) |
| CBZ | $54.47 | 24.29-67.24 | 70th | MID-OUT |
| HURN | $150.01 | 84.88-186.78 | 64th | MID-OUT |
| FCN | $151.02 | 137.65-189.30 | 26th | MID-OUT |
| PKG | $254.60 | 191.50-258.81 | 94th | PUTS (logged only) |
| IP | $40.75 | 29.26-50.25 | 55th | MID-OUT |
| AVY | $175.34 | 152.42-199.54 | 49th | MID-OUT |
| SON | $57.38 | 38.65-60.67 | 85th | PUTS (logged only) |
| **GPK** | **$12.07** | **8.79-23.47** | **22nd** | **CALLS -- advances to chain** |
| SLGN | $41.86 | 35.68-49.55 | 45th | MID-OUT |
| CCK | $120.75 | 89.21-122.91 | 94th | PUTS (logged only) |
| **BLDR** | **$75.98** | **65.10-151.03** | **13th** | **CALLS -- advances to chain** |
| AWI | $186.10 | 150.28-206.08 | 64th | MID-OUT |
| **JELD** | **$1.91** | **0.93-6.97** | **16th** | **CALLS -- advances to chain** |
| FBIN | $51.55 | 32.34-64.84 | 59th | MID-OUT |
| MHK | $136.16 | 92.99-143.13 | 86th | PUTS (logged only) |
| TREX | $50.08 | 29.77-66.06 | 56th | MID-OUT |
| AAON | $91.81 | 62.00-150.46 | 34th | MID-OUT |
| **LII** | **$441.64** | **411.40-616.50** | **15th** | **CALLS -- advances to chain** |
| SIGI | $95.41 | 72.78-100.40 | 82nd | PUTS (logged only) |
| RGP | $4.24 | 3.06-5.54 | 48th | MID-OUT |
| CTAS | $202.03 | 161.16-226.75 | 62nd | MID-OUT |
| OC | $155.68 | 97.53-159.91 | 93rd | PUTS (logged only) |

**Tally: 27 MID-OUT, 19 PUTS-zone (logged, untouched, per no-dedicated-puts-pools rule), 4 CALLS-zone advance to chain: GPK, BLDR, JELD, LII.**

## Stage 2 -- Chain feasibility (free, fetch_puts_chain.py --calls, post-fix rolling 90-day window)

All four survivors looked promising on cheap-strike geometry alone (GPK $12C at $0.60 needing 8.5%; JELD $2C at $0.75 needing 17.9%; BLDR $85C at $1.00 needing 13.2%; LII's cheapest in-range strike needing 24.8% at the very edge of the $1.00 cap). All four died the same way once earnings dates were checked -- the classic post-earnings trap this sweep keeps surfacing on Aug 7, one to several days after a wave of Q2 prints:

- **GPK: KILLED on calendar (Rule 2).** Graphic Packaging reported Q2 2026 on Aug 4, 2026 (beat, $0.14 vs $0.12 EPS est., revenue down 0.7% YoY) -- three days before this screen. The 22nd-percentile dip is the market's post-earnings reaction, not a pre-earnings dislocation. Next confirmed print: Q3, tentatively **Nov 3, 2026**. GPK's only two listed expiries inside the 90-day window are Aug21 and Sep18 -- both predate Nov 3, and the next available expiry after Sep18 jumps past the 90-day cutoff. No instrument brackets the real catalyst.
- **BLDR: KILLED on calendar (Rule 2).** Builders FirstSource's Q2 2026 print landed ~Jul 30, 2026, before this screen. The 13th-percentile read is a post-earnings reaction (last year's comparable Q3 report came Oct 30 -- this year's is expected on a similar late-October cadence). BLDR's only two listed expiries inside 90 days are Aug21 and Sep18; the next available expiry jumps past a late-October print entirely. No instrument brackets it. (The $85C Aug21 ask was already sitting at the $1.00 hard cap anyway -- STRETCH-flagged -- so even a cost-only view didn't leave real room here.)
- **JELD: KILLED on calendar (Rule 2).** JELD-WEN reported Q2 2026 on Aug 3, 2026 (call Aug 4) -- four days before this screen, first YoY adjusted-EBITDA increase in 10 quarters, guidance raised. The 16th-percentile price is post-earnings, not pre-earnings, despite the ostensibly good print (market shrugged). This name has an Oct16 expiry (70 DTE) inside the window, but next earnings is Q3, expected early-to-mid November per typical cadence -- still outside every listed expiry found. No instrument brackets the real catalyst. (Also worth noting for the record, moot given the calendar kill: this is a distressed micro-cap, buy-consensus is a coin flip per one source [50% buy-rated], and would need its own Rule 3 verification if a catalyst ever aligned.)
- **LII: KILLED on calendar (Rule 2), double-confirmed by chain gap.** Lennox reported Q2 2026 on Jul 29, 2026, and cut its 2026 outlook on the call -- the stock "sank" on guidance, which is the real story behind the 15th percentile (worth flagging as a possible Category 2 name if it ever resurfaces, not a clean overreaction). Next print is Q3, expected late October per prior-year cadence. LII's only two listed expiries inside 90 days are Aug21 and Sep18; Sep18 returned **zero calls in the $0.10-$1.00 range with breakeven above spot** on its own, an independent kill even before the calendar question. No instrument brackets the real catalyst, and the near-term chain doesn't have an affordable one to offer either way.

**Pattern note for whoever runs the next lane:** every CALLS-zone survivor Bearxter found today died on the same root cause -- Aug 7 sits in the trough right after a wave of Q2 prints (late Jul/early Aug reporters), so cheap-looking dislocations in this window are almost all post-earnings reactions with the next real catalyst sitting past the available near-dated chain, not pre-earnings setups. Four independent sub-sectors, same failure mode, no exceptions.

## Stage 3 -- Full DD

None reached DD. All four CALLS-zone survivors died in Stage 2 on calendar/Rule 2 (one, LII, double-confirmed by an independent chain-gap kill). No search budget spent on Rule 3/Rule 4/decline-category -- calendar kills settle before any of that matters.

## Batch tally

**56 attempted, 6 unavailable (delisted/bad symbol), 50 valid, 4 CALLS-zone advances, 0 reached full DD, 0 survivors at 3.5+, 0 at 4/5.**

19 PUTS-zone names logged, untouched, per the no-dedicated-puts-pools rule (back-test still gates live puts entries): PCAR (85th), ITW (89th), PH (96th), EMR (84th), HUM (79th), CNC (90th), DGX (97th), LH (99th), RNR (85th), RHI (100th), MAN (97th), TNET (83rd), KFY (89th), PKG (94th), SON (85th), CCK (94th), MHK (86th), SIGI (82nd), OC (93rd). Two worth flagging in passing (not full workups, just noted): RHI sits at a fresh 52-week high (100th percentile, $42.24 against a $42.25 high) -- textbook stalled-at-the-top shape if the back-test ever unblocks puts; LH (Labcorp) similarly at 99th percentile.

No survivors, no research docs written this batch.
