# Screening Log -- Aug 7, 2026, Round 2 (Macxter's parallel batch)

Second parallel round of the day, run alongside Bullxter, Bearxter, and Calxter's own batches, all covering the remaining ground toward the 500-name target (352 screened before this round started). Sector assignment: oil and gas E&P, oilfield services, midstream/pipelines, marine shipping/ports, solar/renewable equipment, agriculture equipment/inputs (fresh names, distinct from CNH/CTVA/CF/NTR/BG/ADM/SMG/MOS already covered in earlier batches). Reserve $1,054.96, one open position (KR, do not touch, do not re-research).

## Stage 1 -- Range percentile (free, fetch_price.py --range)

40 attempted, 1 unavailable (CTRA -- broker API rejected the symbol, 400 error, no data returned), 39 valid.

| Ticker | Price | 52wk Range | Pctile | Direction |
|---|---|---|---|---|
| XOM | $152.69 | 105.53-176.41 | 67th | MID-OUT |
| CVX | $186.78 | 146.49-214.71 | 59th | MID-OUT |
| OXY | $55.73 | 38.80-67.45 | 59th | MID-OUT |
| DVN | $42.90 | 31.47-52.71 | 54th | MID-OUT |
| EOG | $134.65 | 101.59-151.87 | 66th | MID-OUT |
| COP | $116.65 | 85.57-135.87 | 62nd | MID-OUT |
| CTRA | -- | -- | -- | unavailable (broker API error) |
| APA | $36.59 | 18.84-45.66 | 66th | MID-OUT |
| SLB | $51.41 | 31.64-58.82 | 73rd | MID-OUT |
| HAL | $32.23 | 20.39-43.59 | 51st | MID-OUT |
| BKR | $62.36 | 41.96-70.41 | 72nd | MID-OUT |
| NOV | $19.79 | 11.78-21.55 | 82nd | PUTS (logged only) |
| RIG | $5.17 | 2.76-7.66 | 49th | MID-OUT |
| VAL | $77.48 | 43.53-114.12 | 48th | MID-OUT |
| PTEN | $9.91 | 5.10-13.08 | 60th | MID-OUT |
| HP | $36.93 | 15.51-41.82 | 81st | PUTS (logged only) |
| WMB | $70.89 | 55.82-80.08 | 62nd | MID-OUT |
| KMI | $30.89 | 25.60-34.80 | 58th | MID-OUT |
| OKE | $87.05 | 64.02-96.07 | 72nd | MID-OUT |
| ET | $20.25 | 16.18-20.81 | 88th | PUTS (logged only) |
| EPD | $37.96 | 30.01-40.16 | 78th | PUTS (logged only) |
| TRGP | $261.04 | 144.14-291.04 | 80th | PUTS (logged only) |
| PAA | $22.96 | 15.69-25.03 | 78th | PUTS (logged only) |
| LNG | $262.04 | 186.20-300.89 | 66th | MID-OUT |
| ZIM | $26.18 | 12.33-29.97 | 79th | PUTS (logged only) |
| MATX | $204.55 | 86.97-230.74 | 82nd | PUTS (logged only) |
| SBLK | $28.55 | 16.72-29.50 | 93rd | PUTS (logged only) |
| GOGL | $25.89 | 20.67-30.05 | 56th | MID-OUT |
| FRO | $38.81 | 18.26-43.10 | 83rd | PUTS (logged only) |
| STNG | $75.10 | 43.78-87.39 | 72nd | MID-OUT |
| KEX | $131.14 | 79.52-157.69 | 66th | MID-OUT |
| DAC | $140.63 | 83.56-145.31 | 92nd | PUTS (logged only) |
| SEDG | $33.19 | 23.01-81.25 | 17th | CALLS -- advances to chain |
| ARRY | $5.24 | 4.77-12.23 | 6th | CALLS -- advances to chain |
| SHLS | $8.21 | 4.43-13.18 | 43rd | MID-OUT |
| NXT | $98.73 | 52.61-163.13 | 42nd | MID-OUT |
| DE | $619.42 | 433.00-674.19 | 77th | PUTS (logged only) |
| AGCO | $102.94 | 99.21-143.78 | 8th | CALLS -- advances to chain |
| TITN | $19.39 | 13.21-25.00 | 52nd | MID-OUT |
| LNN | $116.00 | 97.27-148.00 | 37th | MID-OUT |

**Tally: 24 MID-OUT, 12 PUTS-zone (logged, untouched, no searches per the no-dedicated-puts-pools rule), 3 CALLS-zone advance to chain, 1 unavailable.**

Marine shipping/ports was the standout sector this batch, running hot: 6 of 8 names screened landed in PUTS-zone (ZIM, MATX, SBLK, FRO, DAC all 79th-93rd percentile), consistent with a live freight-rate rally across bulk and container shipping. Nothing there for a CALLS screen. Midstream/pipelines split similarly hot (ET, EPD, TRGP, PAA all 78th-88th). Straight E&P and oilfield services sat almost entirely in the dead middle -- no dislocation either direction in a sector that's just tracking crude sideways.

## Stage 2 -- Chain feasibility (free, fetch_puts_chain.py --calls)

**SEDG:** live chain shows workable near-term strikes (e.g. $34C 7d ask $0.52, needs +2.3%), but every listed expiry inside the script's window is 0-42 days out (through Sep 18). Earnings date needed before trusting any of it -- see Stage 3.

**ARRY:** chain shows a clean $5C 14d at $0.70 (+8.9%) and $6C 42d at $0.45 (+23.2%). Cheap stock, cheap contracts, looks like exactly the CALLS shape the fund hunts for on paper. Earnings date check required before anything else.

**AGCO:** chain returned a data integrity flag. Every strike from $115 to $180 across the 14d expiry, and again $130-$170 at 42d, priced at an identical $0.75 ask regardless of strike -- not a real market (a real chain doesn't price a $115 strike and a $180 strike the same on a $102.94 stock). This is the same category of stale/synthetic quote pattern Tab 5 already has two entries for (TRMB phantom -98%, HITI app-mark divergence), just on the ask side instead of the daily-return side. Flagged, not blindly trusted -- carried into Stage 3 as suspect data regardless of the calendar outcome.

## Stage 3 -- Earnings calendar check (web search, chain survivors only)

This is the same wall every parallel agent hit today: Aug 7 sits in a trough right after the Q2 2026 earnings wave. All three survivors already reported.

- **SEDG: KILLED, Rule 2.** Reported Q2 2026 Aug 5, before market open (beat: $0.06 EPS vs $0.04 est., revenue $346.2M, +19.6% YoY) -- two days before this screen. Stock fell anyway on weak Q3 guidance, which is exactly why it's sitting at 17th percentile, but the mechanism already fired. Next print is Q3, ~November, outside every affordable expiry on the chain (max 70 days out, to Oct 16). **Also fails Rule 3 independently:** 1 Buy / 21 Hold / 4 Sell -- 4 Sell ratings is nowhere near the max-1 ceiling for calls. Double kill, doesn't matter which rule gets checked first.
- **ARRY: KILLED, Rule 2.** Reported Q2 2026 after close Aug 5, two days before this screen (beat: $0.24 EPS vs $0.12 est., revenue $342.1M vs $317.9M est. -- a real beat, and the stock still sits at 6th percentile, meaning the market didn't reward it, or rewarded it and then gave it back before this screen). Next print is Q3, ~November, same calendar trap as SEDG. Consensus is Moderate Buy per available sourcing; Sell-rating count wasn't independently broken out, but it's moot -- Rule 2 kills it outright regardless of Rule 3's answer.
- **AGCO: KILLED, Rule 2 and Rule 3.** Reported Q2 2026 Jul 30 ($1.43 EPS, missed the $1.46 estimate by $0.03), a week before this screen. Next print is Q3, ~late October/November, outside every affordable expiry. Independently fails Rule 3: 2 Sell ratings (Morgan Stanley "underweight," $108 target; one other) out of 12 covering analysts, UBS cut its target $123 to $114 on Aug 4 -- exceeds the max-1-Sell ceiling for calls even before the calendar kill. The flat-$0.75 chain data flagged in Stage 2 never mattered to the verdict, but it's noted for the record: this instrument's quotes shouldn't be trusted for a future pass either, until the chain script's behavior on AGCO specifically is understood.

**Zero survivors this batch.** All three CALLS-zone names that cleared the free screen died on the same post-earnings calendar trap flagged in the round's shared context, two of them doubly so on Rule 3. No full 13-line DD written, no research_TICKER.md files created.

## Macxter's read on the sector, for the record

Nothing in this batch touched a live policy or regulatory lever worth flagging on its own. Oil and gas E&P and oilfield services are trading like a sector with no dislocation story right now, just crude tracking sideways with OPEC+ supply decisions already priced in -- nothing at either extreme of any name's range. Midstream and marine shipping both running hot (PUTS-zone heavy) is a genuine macro tell worth carrying forward for a future puts-zone pass once the back-test unblocks live puts entries: freight rates and pipeline throughput both point to the same "demand still strong, capacity still tight" read, not company-specific stories. Solar (SEDG, ARRY) sitting at real 52-week lows despite one clean earnings beat (ARRY) is a policy-adjacent signal worth one line: the sector's guidance-driven selloffs this cycle track federal clean-energy credit uncertainty more than company execution, which is exactly the kind of thing that would matter if either name re-qualifies on a fresh cycle with earnings actually ahead of expiry instead of behind it. Nothing here rises to a sourced filing or a dated policy action, so nothing gets carried into a pitch. Flagging it as a sector to revisit once the calendar clears, not as a signal for today.

## Tally for the round

**40 attempted, 39 valid, 1 unavailable (CTRA). 24 MID-OUT, 12 PUTS-zone, 3 CALLS-zone chain-checked, 0 survivors, 0 research docs written.**

## GLOSSARY

- **Range percentile:** where the current price sits between the stock's 52-week low and high; 0% = at the low, 100% = at the high. Bottom quartile (under 25%) is calls territory, top quartile (over 75%) is puts territory, the middle is a dead screen (MID-OUT).
- **MID-OUT:** a name that failed Stage 1 by sitting in the middle of its 52-week range, no directional edge, screened out before any further work.
- **PUTS-zone:** a name in the top quartile of its range, logged to the watch list only per the no-dedicated-puts-pools rule; not researched further until the puts back-test unblocks live entries.
- **CALLS-zone:** a name in the bottom quartile of its range, the fund's calls-hunting ground, advances to a free chain check.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration. A name that already reported, with its next print outside every affordable expiry, fails Rule 2 regardless of how good the setup otherwise looks.
- **Rule 3 (ratings):** for calls, near-zero analysts rating the stock Sell/Underperform (max 1).
- **Breakeven:** strike price plus premium paid per share, the price the stock must reach for the option to be worth exactly what was paid at expiration.
- **Data integrity flag:** a chain or quote that returns implausible values (e.g. identical ask prices across widely different strikes) and gets treated as unreliable rather than taken at face value, per the standing Tab 5 lessons on phantom quotes.
