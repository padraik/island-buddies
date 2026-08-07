# Screening Log -- Aug 6, 2026 (Batch 2 of the 500-name sweep)

**Sweep running total entering this batch: 50 screened, 0 CALLS advances to DD, 0 survivors, 0 at 4/5.**

**Sectors, deliberately untouched by any prior batch:** large-cap banks/brokerages, insurance carriers (P&C and specialty), metals/mining (steel, copper, precious), agricultural commodities/processors, specialty chemicals, packaged food (fresh names), beverages/alcohol, rail/marine equipment, medical devices (fresh names).

## Stage 1 -- Range percentile (free, fetch_price.py --range)

56 attempted, 6 unavailable (X -- bad/delisted symbol via broker API; CVGW -- bad symbol; four list-construction errors caught before they cost anything: AGCO/DE/SJM/CAG duplicate-suffix typos, not real tickers, replaced with fresh names before continuing), 50 valid.

| Ticker | Price | 52wk Range | Pctile | Direction |
|---|---|---|---|---|
| JPM | $356.51 | 279.10-363.00 | 92nd | PUTS (logged only) |
| GS | $1040.50 | 705.55-1153.99 | 75th | MID-OUT |
| MS | $214.18 | 140.60-232.25 | 80th | PUTS (logged only) |
| BAC | $63.02 | 44.78-63.97 | 95th | PUTS (logged only) |
| WFC | $87.72 | 72.78-97.76 | 60th | MID-OUT |
| C | $134.20 | 90.68-147.96 | 76th | PUTS (logged only) |
| SCHW | $107.85 | 83.96-109.05 | 95th | PUTS (logged only) |
| BLK | $1128.00 | 917.39-1219.94 | 70th | MID-OUT |
| TROW | $113.62 | 85.22-122.00 | 77th | PUTS (logged only) |
| STT | $184.92 | 104.64-192.51 | 91st | PUTS (logged only) |
| NTRS | $184.14 | 121.12-191.60 | 89th | PUTS (logged only) |
| RJF | $179.33 | 138.82-182.73 | 92nd | PUTS (logged only) |
| CB | $354.03 | 265.30-365.91 | 88th | PUTS (logged only) |
| TRV | $386.42 | 252.26-398.69 | 92nd | PUTS (logged only) |
| PGR | $215.34 | 189.20-254.93 | 40th | MID-OUT |
| ALL | $274.90 | 188.08-277.22 | 97th | PUTS (logged only) |
| AIG | $80.61 | 71.25-87.29 | 58th | MID-OUT |
| HIG | $144.51 | 120.33-146.06 | 94th | PUTS (logged only) |
| WRB | $72.13 | 62.87-78.96 | 58th | MID-OUT |
| CINF | $179.04 | 149.21-194.81 | 65th | MID-OUT |
| FCX | $68.20 | 35.15-72.28 | 89th | PUTS (logged only) |
| SCCO | $193.03 | 92.56-223.88 | 77th | PUTS (logged only) |
| NUE | $272.00 | 131.32-280.11 | 95th | PUTS (logged only) |
| STLD | $261.48 | 119.89-288.74 | 84th | PUTS (logged only) |
| CLF | $12.26 | 7.73-16.70 | 50th | MID-OUT |
| ATI | $223.43 | 70.42-236.98 | 92nd | PUTS (logged only) |
| CMC | $73.69 | 52.31-84.87 | 66th | MID-OUT |
| RS | $418.13 | 260.31-424.76 | 96th | PUTS (logged only) |
| ADM | $77.25 | 55.58-88.46 | 66th | MID-OUT |
| BG | $109.00 | 76.01-134.87 | 56th | MID-OUT |
| CF | $116.73 | 75.42-141.96 | 62nd | MID-OUT |
| **MOS** | **$23.45** | **19.80-36.99** | **21st** | **CALLS -- repeat name, see note below** |
| NTR | $66.76 | 53.03-85.36 | 42nd | MID-OUT |
| CNH | $10.85 | 9.00-13.31 | 43rd | MID-OUT |
| **TWI** | **$7.21** | **6.43-11.70** | **15th** | **CALLS -- advances to chain** |
| IFF | $84.55 | 59.14-89.31 | 84th | PUTS (logged only) |
| CTVA | $77.10 | 60.53-90.97 | 54th | MID-OUT |
| SMG | $62.06 | 52.00-75.34 | 43rd | MID-OUT |
| LW | $52.05 | 37.62-67.07 | 49th | MID-OUT |
| **FLO** | **$7.24** | **6.80-16.85** | **4th** | **CALLS -- advances to chain** |
| BF.B | $28.27 | 22.61-31.92 | 61st | MID-OUT |
| WAB | $295.23 | 184.26-306.64 | 91st | PUTS (logged only) |
| TRN | $30.97 | 24.76-38.30 | 46th | MID-OUT |
| GBX | $47.50 | 38.23-59.19 | 44th | MID-OUT |
| STE | $231.78 | 195.14-269.44 | 49th | MID-OUT |
| RMD | $212.50 | 180.26-293.81 | 28th | MID-OUT |
| ZBH | $97.19 | 79.12-108.29 | 62nd | MID-OUT |
| BAX | $27.01 | 15.73-30.00 | 79th | PUTS (logged only) |
| **SAM** | **$183.05** | **158.68-264.46** | **23rd** | **CALLS -- advances to chain** |
| **STZ** | **$132.52** | **126.45-174.32** | **13th** | **CALLS -- advances to chain** |

**Tally: 23 MID-OUT, 22 PUTS-zone (logged, untouched), 5 CALLS-zone advance to chain: MOS, TWI, FLO, SAM, STZ.**

## Stage 1.5 -- MOS is a repeat name, checked against passes.md/prior research before spending a slot on it

MOS already has a full 13-line DD on file (`week-06/research/research_MOS.md`, Jul 16, 2026): **permanent KILL on Rule 6**, decisive fail (required move +12.2% vs a ~4% real median historical earnings-day reaction, roughly 3x the 1.5x cap). That verdict didn't depend on the specific price level, and MOS's Aug 3, 2026 earnings (the same catalyst the prior doc used) has now already happened -- three days before tonight's screen -- so this is doubly dead: the original Rule 6 kill stands, and the catalyst that kill was built around is now in the past regardless. No new work done, no chain check spent. Confirmed dead, moving on.

## Stage 2 -- Chain feasibility (free, fetch_puts_chain.py, post-fix)

- **TWI: KILLED on calendar.** Titan International already reported Q2 2026 on Jul 30, 2026 (beat estimates by $0.14 EPS). Next print is Q3, ~Nov 5. The 15th-percentile read is a reaction to news already priced in, not a pre-earnings dislocation. Chain (Aug21/Sep18/Oct16, all with sub-$1.00 asks) is real and cheap, but there's no catalyst inside any of it. Same post-earnings trap as batch 1's LHX/PEG/TMUS.
- **FLO: KILLED on timing.** Flowers Foods reports tonight, Aug 6, after close -- same day as this screen. No viable entry window exists: by the time any research, sizing, or Michael's yes could happen, the print has already fired or is about to. This isn't a pre-earnings dislocation trade, it's an accidental same-day binary bet with no time to size or exit-plan around it. Chain (Aug21 $8C at $0.25, 7.0% needed) looked cheap enough to tempt a second look, but the timing kills it outright regardless of price.
- **SAM: KILLED on chain gap.** Boston Beer's next earnings is ~Oct 22, 2026 (per two independent aggregator estimates). Pulled the real chain directly (`get_option_chains`): SAM's actual listed expirations are Aug 21, Sep 18, then jump straight to **Dec 18** -- no expiry brackets the Oct 22 catalyst inside a reasonable window. Dec 18 technically satisfies Rule 2 (earnings before expiry) but would mean holding roughly 4.5 months for a catalyst that fires 2.5 months in, well outside the fund's short-dated pre-earnings pattern and carrying far more time premium/decay risk than any play in the book. Not chasing it. No search spent confirming the exact date further -- the gap kills it regardless of the precise day.
- **STZ: KILLED on Rule 3 AND Rule 6, real data, real catalyst.** This is the one candidate this batch with everything else lined up -- confirmed Q2 FY2027 earnings **Oct 1, 2026** (before the real Oct 16 expiry, 71 DTE), and a genuinely cheap-looking chain at first glance ($170C Oct16, ask $0.60, 28.7% needed). Two independent kills found on the search pass: **Rule 3** -- 24-analyst consensus is 11 Strong Buy / 3 Moderate Buy / 8 Hold / 1 Moderate Sell / 1 Strong Sell = 2 Sell-class ratings, over the calls max-of-1. **Rule 6** -- Constellation's own reported average post-earnings move is **2.89% over the last four quarters** (per an options-desk estimate ahead of the Q4 FY26 print); 1.5x cap is roughly 4.3%. The cheapest usable strike needs **+28.7%**, roughly **6.7x** the cap -- one of the more decisive Rule 6 fails this fund has logged, worse than MOS's. Worth noting for the record even though it's moot: STZ has beaten EPS four straight quarters (the binder's Unified Screen earnings-history-cap flag would have capped it at 3.5/5 even if everything else passed) while the stock is still down ~20% over three months -- a beat-and-fall pattern, not the beat-and-punish overreaction shape the fund looks for. Reads more like Category 2 (a real demand/GLP-1-adjacent alcohol-sector headwind repricing) than Category 1, though that's moot given the hard Rule 3/6 fails.

## Stage 3 -- Full DD

None reached DD. All five CALLS-zone survivors died at the free/cheap-search stage (1 repeat-kill, 2 calendar, 1 chain-gap, 1 clean Rule 3+6 double fail).

## Batch 2 tally

**56 attempted, 50 valid, 5 CALLS-zone advances (1 already-dead repeat, 4 fresh), 0 reached full DD, 0 survivors, 0 at 4/5.**

22 PUTS-zone names logged, untouched: JPM (92nd), MS (80th), BAC (95th), C (76th), SCHW (95th), TROW (77th), STT (91st), NTRS (89th), RJF (92nd), CB (88th), TRV (92nd), ALL (97th), HIG (94th), FCX (89th), SCCO (77th), NUE (95th), STLD (84th), ATI (92nd), RS (96th), IFF (84th), WAB (91st), BAX (79th). Nothing individually flagged as a standout puts setup this batch.

**Sweep running total: 106/500 screened, 0 CALLS advances to DD, 0 survivors, 0 at 4/5.**

Next: Batch 3, fresh sectors (defense electronics/space, waste management, staffing/HR already touched -- swap for logistics/freight brokers, specialty retail (pets, sporting goods, crafts), semiconductor fabless/analog not yet covered, data center REITs already covered -- swap for hospitals/managed care not yet covered, marine shipping already covered -- swap for auto manufacturers).
