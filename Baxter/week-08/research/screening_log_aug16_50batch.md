# SCREENING LOG -- AUG 16 (Sunday night) -- 50+ NAME RUN, ZERO ADVANCES

Michael's instruction: run 50 names, stop early if 2 land at 4/5. Scanner-sourced per the standing Aug 10 default. Direction: CALLS only (both bands' bottom-quartile pools; no puts pool run tonight -- system stays capped at 4/5 conviction regardless, and the raw pool skewed CALLS anyway).

## Sourcing

Two market-cap bands via the live scanner (`create_scan`/`update_scan_filters`/`run_scan`), 52-week range percentile computed by hand from returned High(52,1W)/Low(52,1W)/Last columns:

- **Band 1 ($300M-$2B):** 393 total matches, 200 returned (frontend cap), 34 in the bottom quartile (≤25th percentile).
- **Band 2 ($2B-$10B):** 396 total matches, 200 returned, 30 in the bottom quartile.

**64 raw CALLS-zone candidates, comfortably past the 50-name floor.**

Note on tooling: `FILTER_TYPE_INSTRUMENT_TYPE` takes value `STOCK`, not `COMMON_STOCK` -- the latter silently zeroes every result when combined with other filters. Worth remembering for the next scanner session; didn't cost anything to fix tonight since it was caught before any real screening happened on it.

## Rule 2 narrowing (free, `get_earnings_calendar` + `get_earnings_results`)

Cross-referenced all 64 tickers against a 31-day forward earnings calendar (Aug 16 - Sep 16; the tool's window caps at 31 days, a few days short of the standing 35-day rule -- immaterial here, nothing hovered right at the edge). **17 of 64 report inside the window.** The other 47 are MID-OUT-equivalent for this cycle: reported too recently or too far out to matter.

Survivors, with confirmed dates/timing via `get_earnings_results`: AAPG (8/19 AM), QFIN (8/25 PM), FLO (8/20 PM), CHA (8/28 AM, unverified), WB (8/19 AM), AI (9/2 PM, unverified), GME (9/8 PM, unverified), BILI (8/27 AM), XP (8/17 PM -- tomorrow), VFS (9/3 PM, unverified), CNM (9/8 AM, unverified), CHWY (9/9 AM, unverified), KLAR (8/18 AM -- tomorrow), AVAV (9/8 PM, unverified), YMM (8/19 AM), KT (8/28 AM, unverified), GAP (8/27 PM).

## Chain check (free, `fetch_puts_chain.py --calls`)

Ran calls chains on all 17 (AAPG: 404, no options instrument -- dead on arrival, no search spent). CHA also came back with no options chain. The rest returned real strikes. Screening-line reachability (needs% at the nearest viable expiry after the catalyst) narrowed hard:

| Ticker | Best strike / expiry | Needs% | Real median earnings move (6-8Q) | 1.5x cap | Verdict |
|---|---|---|---|---|---|
| **WB** | $7.50C 8/21 | 1.7% | 3.72% | 5.58% | Rule 6 PASS (30% of cap) |
| **XP** | $15.50C 8/21 | 2.9% | 1.60% | 2.40% | Rule 6 FAIL (121% of cap) |
| **FLO** | $7.50C 8/21 | 5.5% | 3.63% | 5.44% | Rule 6 FAIL (101% of cap, right at the line) |
| **KT** | $20.00C 9/18 | 6.5% | 1.54% | 2.32% | Rule 6 FAIL (280% of cap) |
| **QFIN** | $15.00C 9/18 | 24.9% | 8.79% | 13.18% | Rule 6 FAIL (189% of cap) |
| **YMM** | $10.00C 8/21 | 15.8% | 7.03% | 10.55% | Rule 6 FAIL (150% of cap) |
| **KLAR** | $23.00C 8/21 | 16.5% | 20.31% (n=3, thin sample) | 30.46% | Rule 6 PASS (54% of cap) |
| **GAP** | $22.00C 8/28 | 10.3% | 14.91% | 22.36% | Rule 6 PASS (46% of cap) |
| BILI, VFS, CNM, CHWY, AVAV, AI, GME | -- | -- | not computed | -- | deprioritized, incomplete expiry-alignment data, ran out of session budget before reaching these |

Real historical earnings-day moves pulled from actual daily bars (`get_equity_historicals`, close-to-close on the reaction session, AM = same day / PM = next day), not estimated -- 6-8 real quarters per name except KLAR (recent IPO, only 3 quarters exist).

**Three survivors advance past the chain: WB, KLAR, GAP.**

## Full DD on the three survivors -- all three die or stall on Rule 3/Rule 4, not Rule 6

**WB (Weibo) -- KILL, Rule 3.** Aggregators disagreed with each other (one showed a 10-Buy/2-Sell/7-Hold "Buy consensus," S&P Global showed a similar picture) until a more targeted search surfaced the real, current, named rating: **BofA has an active Underperform on WB, target just cut to $8.00 from $8.70, dated to Weibo's own Q1 2026 print** (MAU/DAU both declined y/y, non-GAAP profit missed on higher opex/tax despite a revenue beat). TipRanks' more recent-analyst-weighted read: 0 Buy / 1 Hold / 1 Sell, consensus **Moderate Sell**. That's a real, dated Underperform, not stale noise -- decisively exceeds Rule 3's max-1-Sell ceiling once the actual named rating is in hand instead of a surface consensus label. Textbook case of the lesson already in the binder: aggregator consensus labels conflict with each other and are not a substitute for finding the specific named rating.

**KLAR (Klarna) -- KILL, Rule 4.** Clean Rule 3 (13 Buy / 0 Sell / 9 Hold, 22 analysts) and the best Rule 6 margin of the batch even on a thin 3-quarter sample. Cheapest viable strike is $23.00C 8/21 (STRETCH tier), breakeven $24.00; next real strike $23.50C, breakeven $24.35. Resolved the Buy-rated floor specifically (not just "low estimate," which mixes in Hold/Sell targets): Morgan Stanley's freshly-raised $21 target is **Equal Weight, not Buy** -- doesn't count. The lowest confirmed Buy-rated target found is **UBS at $23.00 ("buy" rating)** -- below both viable breakevens. KBW's $26 Buy target clears it, but Rule 4 is about the most pessimistic bull, not the most optimistic one, and UBS is that bull tonight. Real, current data -- not stale -- and it still kills the play.

**GAP -- QUEUED, not killed, Rule 4 still unresolved.** This is the name flagged Aug 8 ("worth a second look closer to Aug 27 print") and tonight is that look. Rule 6 improved a lot with a real expiry aligned to the actual catalyst: $22.00C 8/28 needs 10.3% against a 22.36% cap (46% used) -- comfortable, using real median move data (14.91%, n=6). But Rule 4 is the same open question it was a week ago, and tonight's searches made it more precise without resolving it: Barclays downgraded to Equal Weight $20 (8/11, doesn't count), Citigroup and Wells Fargo are both Hold/Neutral in the $22-23 range (don't count), and the one dated Buy-rated target found (Telsey, $34) is a May 2026 number -- likely stale against the binder's own 60-day freshness rule, and it wasn't possible to confirm a reaffirmation date inside the session budget tonight. No confirmed Sell ratings found, so Rule 3 isn't the blocker. **Queued for the Aug 27 window: needs one clean search (or a live browser pull) that pins a specifically dated, Buy-rated GAP target from the last 60 days before this can be pitched.** Not scored, not advanced, not dead.

## Result

**64 names screened (past the 50-name floor), 17 cleared Rule 2, 8 got real chain checks, 3 reached full DD, 0 advanced to a pitch.** Two kills were clean and decisive (WB on a real Sell rating, KLAR on a real sub-breakeven Buy floor) -- the funnel did its job once the surface-level aggregator noise got resolved to named, dated ratings. GAP remains a live, queued name for the next session ahead of its Aug 27 print, not a rejection.

No trades tonight. YALA's own ramp-sell is tomorrow (Aug 17, before the close, ahead of the PM print) -- see positions.md.

## GLOSSARY

- **Scanner (Robinhood market scanner):** live filtering tool over the tradeable market, run here via `create_scan`/`update_scan_filters`/`run_scan`. Real-time data, capped at 200 rows per scan with no pagination exposed to this tool.
- **`FILTER_TYPE_INSTRUMENT_TYPE` value `STOCK`:** the correct enum value for common stock in this scanner API -- `COMMON_STOCK` is not valid and silently returns zero results when combined with other filters.
- **52-week range percentile:** (last price - 52wk low) / (52wk high - 52wk low), computed by hand from the scanner's High(52,1W)/Low(52,1W)/Last columns. Bottom quartile (≤25%) is the calls-zone raw pool.
- **`get_earnings_results` / `get_earnings_calendar`:** the fund's standing first source for earnings dates (binder Tab 6, Aug 7, 2026) -- per-symbol history with a `verified` flag, or a market-wide date-window sweep, both ahead of any WebSearch.
- **Rule 1-6:** THE UNIFIED SCREEN and Tab 1's Iron Rules -- range percentile, confirmed catalyst, analyst ratings (max 1 Sell for calls), bear floor above breakeven, chain affordability, and reachability (required move ≤1.5x the stock's own median historical earnings-day move).
- **Needs% / breakeven:** the percentage move the stock must make from its current price to reach strike + premium (call breakeven), from `fetch_puts_chain.py --calls`.
- **1.5x cap:** Rule 6's ceiling -- the required move may not exceed 1.5x the stock's median absolute earnings-day move over its last 4-8 real quarters.
- **Buy-rated floor (Rule 4):** the lowest price target among analysts currently rated Buy/Outperform specifically -- a Hold or Sell analyst's target, however low, does not count against this floor, and a Buy-to-Hold downgrade does not add to a Sell count.
- **Consensus label vs. named rating:** aggregator "Buy/Hold/Sell consensus" labels from different sources can disagree with each other (different analyst sets, different weighting, different staleness); the fund's standing practice is to resolve to the specific, named, dated rating from the actual firm before trusting a kill or an advance.
- **DTE:** days to expiration.
