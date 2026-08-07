# Screening Log -- Aug 7, 2026 (Macxter's parallel batch)

Macxter's lane, run in parallel with Bullxter, Bearxter, and Calxter's own 50-name batches, all pushing to the same repo same session. Sector assignment: independent power producers/utilities (non-telecom), HVAC/climate equipment, industrial gases, cybersecurity, streaming/media (regulatory-content angle), water/infrastructure. Reserve $1,154.96, zero open positions, KR pitch-ready and not re-screened here.

**Cross-agent flag received mid-batch (from Bearxter's run):** GPK, BLDR, JELD, LII all died the same way in Bearxter's batch, real dislocation on stocks that had already reported Q2 1-8 days ago, next real catalyst (Q3) falls outside every affordable expiry. Aug 7 sits in a trough right after a wave of Q2 prints. This batch independently found the identical pattern before the flag arrived (see Stage 2) -- not a coincidence, it's the calendar. No rule change, just confirms the pattern is real and sector-wide this week, not isolated to one screener's names.

## Stage 1 -- Range percentile (free, fetch_price.py --range)

50 attempted, 2 unavailable (CYBR -- bad symbol, broker API rejected; SJW -- bad symbol, broker API 404), 48 valid.

| Ticker | Price | 52wk Range | Pctile | Direction |
|---|---|---|---|---|
| VST | $137.74 (later $136.53) | 132.66-219.82 | 6th | CALLS -- advances to chain |
| NRG | $120.49 | 112.50-189.96 | 10th | CALLS -- advances to chain |
| CEG | $264.78 | 228.63-412.70 | 20th | CALLS -- advances to chain |
| TLN | $337.37 | 301.45-451.28 | 24th | CALLS -- advances to chain |
| AES | $14.72 | 12.33-17.65 | 45th | MID-OUT |
| PPL | $34.87 | 33.16-40.10 | 25th | CALLS -- advances to chain |
| ES | $71.99 | 61.53-76.57 | 70th | MID-OUT |
| ED | $107.40 | 94.96-116.23 | 58th | MID-OUT |
| XEL | $76.76 | 69.16-84.23 | 50th | MID-OUT |
| WEC | $107.58 | 102.95-119.91 | 27th | MID-OUT |
| NI | $42.88 | 38.45-49.21 | 41st | MID-OUT |
| CMS | $70.60 | 68.64-80.36 | 17th | CALLS -- advances to chain |
| LNT | $69.13 | 63.28-78.81 | 38th | MID-OUT |
| PNW | $100.84 | 85.32-111.16 | 60th | MID-OUT |
| OGE | $46.73 | 41.70-50.59 | 57th | MID-OUT |
| CARR | $63.77 | 50.24-76.76 | 51st | MID-OUT |
| TT | $481.45 | 348.06-505.87 | 85th | PUTS (logged only) |
| LII | $442.31 | 411.40-616.50 | 15th | CALLS -- advances to chain |
| JCI | $152.71 | 103.07-157.06 | 92nd | PUTS (logged only) |
| AAON | $91.79 | 62.00-150.46 | 34th | MID-OUT |
| MOD | $192.26 | 111.18-323.25 | 38th | MID-OUT |
| LIN | $491.40 | 387.78-548.20 | 65th | MID-OUT |
| APD | $299.36 | 229.11-314.87 | 82nd | PUTS (logged only) |
| PANW | $367.39 | 139.57-376.98 | 96th | PUTS (logged only) |
| CRWD | $213.67 | 85.68-219.35 | 96th | PUTS (logged only) |
| FTNT | $162.69 | 70.12-172.09 | 91st | PUTS (logged only) |
| OKTA | $147.56 | 62.66-157.00 | 90th | PUTS (logged only) |
| S | $21.34 | 11.81-21.45 | 99th | PUTS (logged only) |
| CYBR | -- | -- | -- | unavailable (bad symbol) |
| QLYS | $180.91 | 74.51-201.54 | 84th | PUTS (logged only) |
| TENB | $35.88 | 15.72-43.67 | 72nd | MID-OUT |
| NET | $320.45 | 158.83-323.62 | 98th | PUTS (logged only) |
| CHKP | $127.03 | 112.23-210.66 | 15th | CALLS -- advances to chain |
| NFLX | $73.92 | 65.08-126.71 | 14th | CALLS -- advances to chain (data verified, see Stage 1.5) |
| PARA | $1.88 | 1.71-85.60 | 0th | KILLED -- delisted (see Stage 1.5) |
| WBD | $26.55 | 10.76-30.00 | 82nd | PUTS (logged only) -- M&A note, see Stage 1.5 |
| FOXA | $62.83 | 48.34-76.39 | 52nd | MID-OUT |
| NWSA | $29.02 | 22.20-31.61 | 72nd | MID-OUT |
| LYV | $182.74 | 125.34-188.00 | 92nd | PUTS (logged only) |
| SPOT | $480.52 | 405.00-748.30 | 22nd | CALLS -- advances to chain |
| ROKU | $151.41 | 78.53-152.60 | 98th | PUTS (logged only) |
| SIRI | $29.62 | 19.77-32.66 | 76th | PUTS (logged only) |
| AWK | $134.63 | 120.57-147.87 | 52nd | MID-OUT |
| WTRG | $39.85 | 36.10-42.37 | 60th | MID-OUT |
| CWT | $49.54 | 41.29-53.82 | 66th | MID-OUT |
| SJW | -- | -- | -- | unavailable (bad symbol) |
| AWR | $85.42 | 69.45-90.11 | 77th | PUTS (logged only) |
| PNR | $70.84 | 57.60-113.95 | 23rd | CALLS -- advances to chain |
| XYL | $121.36 | 105.29-154.27 | 33rd | MID-OUT |
| ECL | $286.55 | 243.15-309.27 | 66th | MID-OUT |

**Tally: 21 MID-OUT, 15 PUTS-zone (logged, untouched), 12 CALLS-zone advance (1 -- PARA -- immediately killed on data integrity before chain, 11 proceed to Stage 2), 2 unavailable.**

## Stage 1.5 -- data integrity checks (NFLX, PARA)

**NFLX:** a 52-week range of $65.08-$126.71 against a $73.92 price looked like a possible split artifact (Netflix has historically traded at three to four figures). Web-searched before trusting it: confirmed via independent sources (investing.com, stockanalysis.com) -- real price, real decline from a $133.91 all-time-high close on Jun 30, 2025. No 2026 split. Genuine dislocation, proceeded normally.

**PARA: KILLED, delisted.** Paramount Global merged with Skydance Media in August 2025; the combined company trades as PSKY. The PARA ticker is a stale/defunct instrument post-merger -- the $1.88 print against an $85.60 high-water mark is leftover data, not a live, tradeable security with a real earnings catalyst. No chain check, no further work. Removed from the CALLS-zone pool before Stage 2.

**WBD note (puts-zone, logged only, not actioned):** same search surfaced that Paramount Skydance (PSKY) is actively pursuing Warner Bros. Discovery in an announced/pending acquisition (UK regulatory approval reported). WBD sits at 82nd percentile this session. Per the binder's Unified Screen, M&A is an automatic puts disqualifier -- moot here since WBD is watch-list only under the standing no-dedicated-puts-pools rule, but flagging so nobody accidentally treats WBD as a clean puts candidate later without checking deal status first.

## Stage 2 -- Chain feasibility (calendar-first this batch, chain math second)

Given the cross-agent flag and this batch's own early pattern, earnings dates were checked before running the slow chain script (cheaper gate, same effect). Nine of eleven CALLS-zone survivors are independent power producers, HVAC-adjacent, and cybersecurity names that all sit inside the same Q2 2026 earnings cluster (last week of July through this week) -- the fund's whole utilities/industrials/cyber sector reported earnings within the same 10 days as this screen:

- **VST: KILLED on calendar.** Reports today, Aug 7, 2026 (before/at this screen -- results already public: Q2 revenue $4.0B, adjusted EBITDA $1.8B beat). Next print ~Nov. No catalyst inside any affordable expiry.
- **NRG: KILLED on calendar.** Reported Aug 4, 2026, three days before this screen. Same trap.
- **CEG: KILLED on calendar.** Reported Aug 6, 2026, one day before this screen.
- **TLN: KILLED on calendar.** Reported Aug 5, 2026, two days before this screen.
- **PPL: KILLED on calendar.** Reported today, Aug 7, 2026, before market open.
- **CMS: KILLED on calendar.** Reported Jul 28, 2026.
- **LII: KILLED on calendar.** Reported Jul 29, 2026 -- same name Bearxter's cross-agent flag cited independently in its own batch; converges with this batch's own finding.
- **CHKP: KILLED on calendar.** Reported Jul 30, 2026.
- **SPOT: KILLED on calendar.** Reported Aug 4, 2026.
- **PNR: KILLED on calendar.** Reported Jul 28, 2026.

All ten: the cheap-looking percentile is a reaction to news already priced in, not a pre-earnings dislocation. No chain script time spent on any of these once the date check killed them -- consistent with the cost-ordered funnel (cheapest disqualifier first).

- **NFLX: KILLED on Rule 5 (chain gap), real catalyst confirmed but unreachable.** Genuine live catalyst: Q3 2026 earnings confirmed Oct 20, 2026, ~74 days out -- the one name this batch with a real, un-fired catalyst. Full chain pulled (`fetch_puts_chain.py NFLX --calls`, then cross-checked directly via MCP `get_option_chains`): listed expirations run weekly/monthly through **Oct 16, 2026**, then jump straight to **Nov 20, 2026** -- a 35-day gap that straddles the Oct 20 print with nothing in between. No expiry brackets the actual catalyst within the fund's near-dated pattern; Nov 20 technically satisfies Rule 2 (earnings before expiry) but would mean holding ~105 days for a catalyst that resolves at day 74, the same shape as batch 2's SAM kill (Dec 18 chain jump over an Oct 22 catalyst). Not chasing it -- no pricing pulled on the Nov 20 chain, the structural gap kills it regardless of premium.

## Stage 3 -- Full DD

None reached DD. All 11 chain-stage CALLS-zone survivors died in Stage 2 (10 on calendar, 1 -- NFLX -- on chain gap). PARA was killed pre-Stage-2 on data integrity (delisted).

## Batch tally

**50 attempted, 48 valid (2 bad symbols: CYBR, SJW), 12 CALLS-zone advances (1 immediate delisting kill, 11 to chain, 0 reached full DD), 0 survivors, 0 at 3.5+.**

15 PUTS-zone names logged, untouched, per the no-dedicated-puts-pools rule: TT (85th), JCI (92nd), APD (82nd), PANW (96th), CRWD (96th), FTNT (91st), OKTA (90th), S (99th), QLYS (84th), NET (98th), WBD (82nd, active M&A target of PSKY -- flag for later, not actioned), LYV (92nd), ROKU (98th), SIRI (76th), AWR (77th). Rate-sensitive names in this list worth a second look if puts ever unlock: none stood out as a fresh-downgrade or stalled-high setup beyond the WBD M&A note above.

**Macro read (Macxter's lane, no live trade implications this batch):** no Truth Social, executive-order, or tariff signal touching any of these sectors found or searched for beyond the WBD/PSKY-WBD deal note above (regulatory approval process, not a fund-relevant signal for any open or pitched position). Utility-sector earnings this week (VST/NRG/CEG/TLN/PPL) landed inside normal seasonal cadence, no rate-policy surprise attached to any of the misses/beats found. Nothing rises to a Macxter standing-alert addition.

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% = at the low, 100% = at the high.
- **MID-OUT:** the Unified Screen's middle band (25-74th percentile) -- no directional edge, screened out immediately, no further analysis.
- **PUTS-zone:** top quartile (>=75th percentile) of the 52-week range -- a puts candidate under the binder's inverted rules, logged to the watch list only per the standing no-dedicated-puts-pools rule (puts remain gated pending the back-test).
- **CALLS-zone:** bottom quartile (<=25th percentile) -- a calls candidate, advances to chain feasibility.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration; a stock that already reported fails this regardless of how cheap its options look.
- **Rule 5 (chain filter):** the cap on how much a single option contract can cost, and (as used here) whether any listed expiry actually brackets a real catalyst within a reasonable window -- a chain gap kills the trade even when the catalyst itself is confirmed and real.
- **Chain gap:** when a stock's listed option expirations jump from well before a catalyst to well after it, with nothing bracketing the event itself at a near-dated cost the fund's rules would accept.
- **Breakeven:** strike price plus premium paid per share -- where the option holder neither gains nor loses at expiration.
- **Post-earnings trap:** a stock sitting at a cheap percentile because it just reported and reacted negatively, with no new catalyst before the next affordable expiry -- looks like a calls setup on range percentile alone but fails Rule 2 on inspection.
