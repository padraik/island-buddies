# Screening Log -- Aug 6, 2026 (Batch 1 of the 500-name sweep)

Michael's ask: screen batches of 50, continue until 500 names total or 2 real 4/5-conviction CALLS plays land, whichever comes first. Doc-and-push after every batch. Reserve is $1,154.96, zero open positions, KR already queued and cleared separately (not re-screened here). This is batch 1.

**Running tally (sweep-wide): 50 screened, 0 CALLS advances to DD, 0 survivors at 3.5+, 0 at 4/5.**

**Sectors, deliberately untouched by any prior batch (checked against passes.md and week-06/07/08 logs):** airlines, aerospace/defense, large-cap biotech, semiconductors, electric/gas utilities, telecom, luxury apparel/accessories, enterprise software.

## Stage 1 -- Range percentile (free, fetch_price.py --range)

50 attempted, 50 valid (no bad tickers this batch).

| Ticker | Price | 52wk Range | Pctile | Direction |
|---|---|---|---|---|
| DAL | $91.98 | 52.88-95.68 | 91st | PUTS (logged only) |
| UAL | $129.25 | 84.64-138.77 | 82nd | PUTS (logged only) |
| AAL | $16.03 | 10.09-18.79 | 68th | MID-OUT |
| LUV | $46.96 | 28.98-55.11 | 69th | MID-OUT |
| ALK | $50.66 | 33.03-65.88 | 54th | MID-OUT |
| JBLU | $6.19 | 3.87-6.62 | 84th | PUTS (logged only) |
| BA | $232.34 | 176.77-254.35 | 72nd | MID-OUT |
| LMT | $585.00 | 423.91-692.00 | 60th | MID-OUT |
| RTX | $223.84 | 150.61-225.65 | 98th | PUTS (logged only) |
| NOC | $567.88 | 479.02-774.00 | 30th | MID-OUT |
| GD | $386.92 | 306.77-400.00 | 86th | PUTS (logged only) |
| **LHX** | **$289.53** | **262.68-379.23** | **23rd** | **CALLS -- advances to chain** |
| TXT | $87.89 | 76.45-101.57 | 46th | MID-OUT |
| HII | $321.75 | 259.00-460.00 | 31st | MID-OUT |
| GILD | $129.89 | 108.46-157.29 | 44th | MID-OUT |
| VRTX | $484.03 | 362.50-533.67 | 71st | MID-OUT |
| REGN | $772.11 | 541.00-821.11 | 83rd | PUTS (logged only) |
| BIIB | $203.92 | 127.00-219.72 | 83rd | PUTS (logged only) |
| AMGN | $404.85 | 269.77-418.40 | 91st | PUTS (logged only) |
| ILMN | $191.53 | 88.00-207.00 | 87th | PUTS (logged only) |
| NVDA | $219.42 | 164.07-236.54 | 76th | PUTS (logged only) |
| AMD | $491.58 | 149.22-584.73 | 79th | PUTS (logged only) |
| INTC | $100.19 | 19.60-142.35 | 66th | MID-OUT |
| QCOM | $160.53 | 121.99-259.92 | 28th | MID-OUT |
| TXN | $279.97 | 152.73-334.03 | 70th | MID-OUT |
| MU | $889.74 | 106.75-1255.00 | 68th | MID-OUT |
| ON | $78.80 | 44.56-134.92 | 38th | MID-OUT |
| MCHP | $80.57 | 48.52-105.91 | 56th | MID-OUT |
| NEE | $84.71 | 69.24-98.75 | 52nd | MID-OUT |
| DUK | $123.86 | 113.89-134.49 | 48th | MID-OUT |
| SO | $92.52 | 83.80-100.83 | 51st | MID-OUT |
| AEP | $125.35 | 105.70-140.58 | 56th | MID-OUT |
| EXC | $45.27 | 42.58-50.65 | 33rd | MID-OUT |
| D | $66.72 | 55.85-72.99 | 63rd | MID-OUT |
| **PEG** | **$75.04** | **74.20-88.65** | **6th** | **CALLS -- advances to chain** |
| T | $23.67 | 19.89-29.79 | 38th | MID-OUT |
| VZ | $46.82 | 38.39-51.68 | 63rd | MID-OUT |
| **TMUS** | **$179.91** | **165.66-261.56** | **15th** | **CALLS -- advances to chain** |
| CMCSA | $25.10 | 21.28-32.85 | 33rd | MID-OUT |
| CHTR | $157.44 | 111.55-285.82 | 26th | MID-OUT |
| RL | $394.10 | 273.04-421.60 | 81st | PUTS (logged only) |
| TPR | $162.00 | 92.62-163.94 | 97th | PUTS (logged only) |
| PVH | $86.00 | 59.60-100.75 | 64th | MID-OUT |
| LEVI | $24.06 | 17.72-25.70 | 79th | PUTS (logged only) |
| VFC | $14.75 | 11.65-22.27 | 29th | MID-OUT |
| CROX | $134.18 | 73.20-141.28 | 90th | PUTS (logged only) |
| CRM | $189.45 | 146.32-269.11 | 35th | MID-OUT |
| WDAY | $172.92 | 110.36-249.85 | 45th | MID-OUT |
| NOW | $119.95 | 81.24-194.73 | 34th | MID-OUT |
| **INTU** | **$324.45** | **252.84-786.28** | **13th** | **CALLS -- advances to chain** |

**Tally: 31 MID-OUT, 15 PUTS-zone (logged, untouched, per no-dedicated-puts-pools rule), 4 CALLS-zone advance to chain: LHX, PEG, TMUS, INTU.**

## Stage 1.5 -- data integrity note (INTU)

INTU's range ($252.84-$786.28 against a $324.45 current price) looked like a stock-split artifact and got checked before trusting the percentile. Confirmed via web search: no INTU split in 2026 (last split was 2006), and the live quote checks out at $323.60 against independent sources -- real data, real 13th-percentile dislocation, not a data bug. Proceeded normally.

## Stage 2 -- Chain feasibility (free scripts, with a bug found and worked around)

**Script bug found and flagged:** `fetch_puts_chain.py` hardcodes its expiration filter to `"2026-08" in d or "2026-07" in d` (source: script line ~90). With today at Aug 6, this silently drops every September+ expiry. All four of this batch's CALLS-zone survivors are large caps with quarterly earnings that don't fall inside a July/August window from here, so the script's blank/near-blank output for their later expiries is a tooling gap, not a real "no instrument" verdict. Worked around using the MCP Robinhood tools directly (`get_option_chains` / `get_option_instruments` / `get_option_quotes`) for the one name (INTU) where a real earnings date fell close enough to check properly. Not fixing the script tonight -- same call as the Aug 4 `fetch_option_history.py` bug (doesn't clear the Fable 5 bar for a routine screening session), but flagging it the same way for whoever picks this up next: `fetch_puts_chain.py`'s date filter needs to move off a hardcoded month string.

- **LHX: KILLED on calendar.** L3Harris already reported Q2 2026 on Jul 23 -- before today. Next print is Q3, ~late October (per company reporting cadence), outside every expiry the fund's Rule 5 chain filter would call affordable. The 23rd-percentile dip is a reaction to news that already happened, not a pre-earnings dislocation. Same shape as AGCO/WU from the Aug 4 batch. No further search needed.
- **PEG: KILLED on calendar.** PSEG's Q2 2026 print landed ~Aug 4 -- two days before this screen. Next print is Q3, ~early November. No confirmed catalyst before any live expiry. Same post-earnings trap.
- **TMUS: KILLED on calendar.** T-Mobile reported Q2 2026 on Jul 22/23 (before today). Next print is estimated ~Oct 22, 2026 -- roughly 11 weeks out, well past any near-dated affordable expiry. The 15th-percentile read is the market's reaction to a report that already happened.
- **INTU: KILLED on Rule 5 (chain filter), real data.** Genuine live catalyst here -- Intuit confirmed its Q4 FY26 earnings for Aug 25, 2026 (press release, `investors.intuit.com`), which lands before the Aug 28 expiry. Pulled the real Aug 28 call chain directly via MCP (`get_option_chains` / `get_option_instruments` / `get_option_quotes`) since the script's date filter suppressed it at the time. Implied volatility on this chain is already running 71-79% (the market has fully priced the earnings event in) -- every strike checked from 5% OTM out to 36% OTM (strike $440, breakeven $441.65) still asks $1.65-$23.70/share. **Correction on the cap used:** the binder's Rule 5 transitional lock (Tab 1) keeps the real cap at $1.00/share regardless of conviction tier until the unlock milestone fires (needs 3+ Rule-6-era closes and $1,500+ reserve -- currently 1 close, $1,154.96, not met), not the generous 20%-of-reserve screening line this doc first cited. At the correct $1.00 cap, the cheapest strike found (36% OTM, $1.65 ask) is still 65% over the real line. No strike anywhere on this chain is both affordable under the live Rule 5 cap and inside a plausible Rule 6 move. Chains are truth: a real, confirmed, well-inside-window catalyst still dies clean on IV pricing. No further search needed.

**Script fixed, same session (see below).** After confirming INTU's kill was genuine (not a tooling artifact), patched `fetch_puts_chain.py`'s hardcoded `"2026-08"/"2026-07"` expiration filter (line ~94) to a rolling 90-day-from-today window instead, so this stops silently dropping every survivor whose earnings fall outside whatever the current month happens to be. Sanity-tested against INTU (now correctly walks Aug 7 through Oct 16 expiries and reproduces the same "no viable calls" result the manual MCP pull found) and KR (the fund's own live queued position, confirms the Sep 4 expiry the pitch doc uses still resolves correctly post-fix). Fix and both sanity checks landed clean before Stage 2 finished. No earlier batch in this sweep (batch 1 is the first) needs a re-check -- this is the only batch run so far.

## Stage 3 -- Full DD

None reached DD this batch. All four CALLS-zone survivors died at the free chain stage (three on calendar, one on Rule 5), so no paid-search budget was spent on the Web-search steps (Rule 3/Rule 4/decline-category) this batch.

## Batch 1 tally

**50 attempted, 50 valid, 4 CALLS-zone advances, all 4 killed in Stage 2 (3 calendar/Rule 2, 1 chain/Rule 5). 0 advances to DD. 0 survivors at 3.5+. 0 at 4/5.**

15 PUTS-zone names logged, untouched, per the no-dedicated-puts-pools rule (back-test still gates live puts entries): DAL (91st), UAL (82nd), JBLU (84th), RTX (98th), GD (86th), REGN (83rd), BIIB (83rd), AMGN (91st), ILMN (87th), NVDA (76th), AMD (79th), RL (81st), TPR (97th), LEVI (79th), CROX (90th). None individually flagged as a standout setup this batch -- straightforward top-quartile names, nothing with a documented fresh downgrade or stalled-high pattern noted in passing.

**Sweep running total: 50/500 screened, 0 CALLS advances to DD, 0 survivors, 0 at 4/5.**

Next: Batch 2, fresh sectors (large-cap banks/brokerages, insurance carriers not yet covered, homebuilders' supply chain, specialty chemicals not yet covered, agricultural commodities, marine/rail equipment, medical devices not yet covered, education/testing services).
