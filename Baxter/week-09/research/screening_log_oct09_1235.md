# Screening log, Fri Oct 9, 12:35pm ET (MIDDAY, DO)

**Session job:** ARDX requote first, then the fresh sub-$10 scan the 11:35 plan named (prints Nov 2-25, Dec18/Jan15 window).
**Rule 5 line:** reserve = spendable = $676.28 -> 3.5/5 line **$0.676**. Quotes pulled live 12:35-12:37pm ET, Oct 8 official closes alongside. Ratings via `get_equity_analyst_ratings` this run. 0 web searches.
**Names moved: 10** (plus the ARDX requote).

## 1. Entry candidate
| Ticker | Contract | Live quote | Close Oct 8 | Stock | Verdict |
|---|---|---|---|---|---|
| ARDX | $3C Nov20 `e500baad` | **0.30 / 0.65**, mark 0.475, OI 49, vol 0 (quote stamp 11:44am, unchanged since) | 0.35 | $3.255 | **NO ORDER: mid $0.475 > the doc's $0.45 ceiling.** Same quote as 11:35. Rest passes: 11/0/0 low $8.00, Q3 `actual: null`, Oct 29 PM (f), LY Oct 30 PM. Zero contracts traded all day on a 49-OI strike. |

## 2. Source: new scan
Saved scan **"Baxter Oct9 sub-10 Nov2-25 prints"** (`f0d34288-e25b-45a8-9533-a80dfd2144c2`): market cap $300M+, earnings Nov 2-25, STOCK, last $2-10, 52-week range pct < 0.25, plus two new display columns: **today's call-option volume** and **30-day average share volume**. 198 matches (under the 200 cap, no split needed).

**Liquidity cut (new this run, a screening preference, not a rule):** kept names with at least 500 calls traded today. That dropped 136 (closed-end funds and names with no listed options, plus thin chains). 62 left.

**Free ratings screen (62 names, 1 call):** R3 + R4 proxy. Most survivors were already worked this week (ONDS, QUBT, TME, BRSL docs; PCT, FRMI, SERV, ENVX floor-blocked; GRAB, DNN, GROY, INDI, NXE, EXK, ALT, PONY, NIO, VNET, AMPX killed on R4/R5/R6). Fails R3 here: XPEV, MARA (2 Sells each), GOOS, JOBY, GTM, LCID, SPCE, DNUT, OPEN, WEN, FLO, UNIT, SMR (Sells or Holds > Buys), CAPR, EOSE, ARRY, LAC, GT (Holds > Buys). No coverage: DJT, POET, BULL, LWLG, UAMY, TMC, NRGV, DGXX, XFOR, ASPI, BBAI. R4 proxy fail: RDW (low $8 < $9.46).

**Picked for chains (10):** KEEL (never seen), ACHR (low target is now $8.00; Oct 5 log had $4.50), BTDR (low $10 now just above the stock), and seven killed earlier this week that have fallen since: RCAT, HIVE, SOUN, TE, WVE, SOC, STUB.

## 3. Chain checks
Expiry per R2: later of tool date and LY date + 21 days. Prints Nov 5-6 -> Nov27 weekly passes (10-Q Nov 14 deadline is 8 trading days before Nov 27). Prints Nov 9-17 -> Dec18 where listed, else Jan15.

| Ticker | Stock | Ratings / low | Print (tool, LY) | Contract | Live quote | R6 (6 prints) / max BE | Verdict |
|---|---|---|---|---|---|---|---|
| **ACHR** | $4.86 (+3.0%) | 7/2/0, **$8.00** | Nov 5 PM (f), LY Nov 6 PM | Nov27 $5C `309e52d9` | **0.46 / 0.52**, OI 8, vol 33 | +22.91 / +7.44 / -7.88 / -10.64 / -2.29 / +8.47: median 8.18%, cap **12.26%**, max BE **$5.456** | **PARKED, R6 by 3.4 cents.** BE at mid $5.49 (+13.0%), at ask $5.52. Passes R1 (0.054), R3, R4 ($8 vs $5.49), R5. Needs mid <= stock x 1.1226 - 5.00 (at $4.86: $0.456). $5.5C 0.26 / 0.35, BE $5.805 = +19.4%: R6 fail. OI 8 on the $5C is thin; the 70-vol $5.5C has OI 30. |
| KEEL | $3.08 (-2.2%) | 12/1/0, $4.50 | Nov 12 AM (f), LY Nov 13 AM | Dec18 $3C `ce4aa258` | 0.51 / 0.57, OI 671 | -6.03 / +3.25 / -17.98 / +5.98 / +8.31 / -12.37: median 7.17%, cap 10.75%, max BE $3.41 | **KILL, R6.** BE at mid $3.54 (+15.0%). $4C 0.23 / 0.24, BE $4.24 (+37.7%). Good, tight chain; the stock just doesn't move enough on prints. |
| SOC | $3.695 (-4.3%) | 8/1/0, $8 | Nov 12 PM (f), LY Nov 13 PM | Jan15 $4C `2a63039b` | 0.60 / 0.63, OI 2,309 | +14.87 / -2.10 / -28.86 / +4.30 / -4.33 / -8.64: median 6.49%, cap 9.73%, max BE $4.05 | **KILL, R6.** BE at mid $4.615 (+24.9%). No Dec18. |
| SOUN | $5.42 (-1.8%) | 6/2/0, $6 | Nov 5 PM (f), LY Nov 6 | Nov27 $5.5C `e213312c` | 0.43 / 0.57, OI 0 | not pulled | **KILL, R4.** BE at mid $6.00 = the $6 low (must be above); at ask $6.07. |
| STUB | $6.155 | 8/4/1, $7 | Nov 12 PM (f), LY Nov 13 | Dec18 $7.5C `71762a4f` | 0.25 / 0.35 | not pulled | **KILL, R4.** BE $7.80 at mid > $7 low. 2.5-wide strike grid; $5C is deep ITM. |
| HIVE | $2.485 (-2.9%) | 8/1/0, $4.50 | Nov 13 PM (f), LY Nov 17 AM | Dec18 $3C `7e070b2e` | 0.20 / 0.30, OI 4,579 | Oct 7 log cap 9.13% | **KILL, R6.** BE at mid $3.25 (+30.8%). No $2.5 strike in Dec18. 6-K filer, both dates present. |
| TE | $3.33 (-3.2%) | 6/3/0, $5 | Nov 13 AM (f), LY Nov 14 | Dec18 $4C `d031171a`; $3C `c7396ee7` | $4C 0.35 / 0.45; $3C 0.70 / 0.85 | Oct log cap 10.61% | **KILL.** $4C R6 (BE $4.40 at mid, +32%); $3C R5 (ask $0.85). |
| WVE | $3.51 (+1.2%) | 18/1/0, $10 | Nov 9 AM (f), LY Nov 10 | Dec18 $4C `7037e645` | 0.55 / 1.75, OI 148, vol 0 | not pulled | **KILL, R5.** Ask $1.75. |
| BTDR | $9.685 | 13/1/0, $10 | Nov 9 AM (f), LY Nov 10 | Dec18 $10C `2b4f68e7` | 1.30 / 1.50 | not pulled | **KILL, R5.** Also R4: BE $11.40 > $10 low. |
| RCAT | $5.755 (-2.6%) | 8/1/0, $9 | Nov 12 PM (f), LY Nov 13 | Jan15 $6C `6530b5c2` | 0.83 / 0.97 | not pulled | **KILL, R5.** No Dec18. |

## 4. Tally
10 moved: **9 killed** (KEEL, SOC on R6; SOUN, STUB on R4; HIVE, TE on R6/R5; WVE, BTDR, RCAT on R5). **ACHR parked** one strike-tick from passing R6. ARDX: no order (mid ceiling).

**What the liquidity column showed:** the chains that pass R5 with real depth (KEEL OI 671, SOC OI 2,309, HIVE OI 4,579) all die on R6. Their stocks don't move enough on earnings to pay for the time value. The ones that pass R6 (ARDX, ACHR) sit on strikes with OI under 50. At a $0.676 line, liquid and reachable haven't shown up together on the same contract this week.

## GLOSSARY
- **R1 / Rule 1:** stock in the bottom 20-25% of its 52-week range.
- **R2 / Rule 2 (Oct 8):** expiry at least 21 days after the later of the tool's date and last year's (LY) date; 10-Q deadline at least 5 trading days before expiry. "(f)" = `verified: false`.
- **R3 / Rule 3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4 / Rule 4:** the lowest Buy target must be above breakeven.
- **R5 / Rule 5:** one contract's ask must fit the tier budget ($0.676/share at 3.5/5 on a $676.28 reserve).
- **R6 / Rule 6:** move to breakeven no more than 1.5x the median earnings-day move (prior close to print-day close for AM prints; print-day close to next close for PM prints). Max BE = stock x (1 + cap).
- **Doc ceiling:** a tighter max price a research doc sets for itself (ARDX: mid at or under $0.45).
- **BE / breakeven:** strike + premium paid.
- **Mark / mid:** halfway between bid and ask.
- **OI:** open interest, contracts outstanding. **Vol:** contracts traded today.
- **Call volume (scan column):** total call contracts traded today across the whole chain, used here as a rough liquidity cut.
- **Nov27 / Dec18 / Jan15:** expirations Nov 27 2026, Dec 18 2026, Jan 15 2027.
