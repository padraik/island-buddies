# Screening log, Tue Oct 13, 10:00pm ET (EVENING 3)

*Live data pulled 02:00-02:30 UTC Oct 14; quotes are Tuesday's regular-session close. Reserve $676.28 (3.5/5 line $0.676). EVENING 3's job: refill the queue and leave PREMARKET a plan. The Oct 5 sweep is 9 days old, so the sweep scan was re-run. EVENING 2's carry-overs were done first: BURL's Barclays check (resolved), CMG's deal-talk headline (nothing found).*

## Re-sweep: prints Oct 15 - Nov 20, range pct < 0.25, cap >= $300M

Saved scan `c238116d-7775-462d-93f9-b632781398a5` (retitled "Baxter Oct13 E3 re-sweep Oct15-Nov20 prints"), split by price so every band came in under the 200-row cap (overlapping bands, sorted by price descending, cover each other's cut-off tails). Each row was diffed against every ticker named in week-08 / week-09 research, research_queue.md, passes.md and paper_book.md.

| Band | Matches | New |
|---|---|---|
| $0.50-7 | 198 | 1 (RMNI) |
| $7-15 | 192 | 3 (ADUR, DRVN, CBIO) |
| $7-30 | 353 (200 shown) | +2 (VTS, PHOE, LDP; LDP is a closed-end fund) |
| $15-40 | 238 (200 shown) | +1 (EPAC) |
| $25-70 | 225 (200 shown) | +3 (CNA, GFS, JBSS) |
| $50+ | 242 (200 shown) | +2 (MIRM, WINA) |
| $110+ | 105 | 0 more |

**13 new names out of roughly 1,000 rows.** The Oct 15 - Nov 20 print window has been fished out at every price; what's new is names that slid into the bottom quartile since Oct 5-13.

## Free screen

| Name | Last | Range pct | Print | Buy / Hold / Sell | Low target | Result |
|---|---|---|---|---|---|---|
| RMNI | 4.09 (AH 3.47, -15%) | 0.21 | Oct 30 | none | | **KILL, no coverage** |
| VTS | 17.73 (AH 16.31, -8%) | 0.16 | Nov 3 | none | | **KILL, no coverage** |
| PHOE | 17.74 | 0.06 | Oct 16 | none | | **KILL, no coverage** |
| LDP | 18.97 | 0.04 | Oct 16 | none | | **KILL, no coverage** (closed-end fund) |
| ADUR | 10.51 | 0.16 | Oct 16 | none | | **KILL, no coverage** |
| EPAC | 35.22 | 0.16 | Oct 16 | none | | **KILL, no coverage** |
| CNA | 46.73 (AH 44.00) | 0.17 | Nov 3 | none | | **KILL, no coverage** |
| JBSS | 66.51 | 0.23 | Oct 30 | none | | **KILL, no coverage** |
| WINA | 282.38 | 0.01 | Oct 15 | none | | **KILL, no coverage** |
| DRVN | 11.64 | 0.25 | Nov 4 | 6 / 7 / 1 | $12 | **KILL, R3** (Buys < Holds) |
| CBIO | 12.91 | 0.22 | Nov 5 AM (f), LY Nov 6 | 8 / 0 / 0 | $27 | ADVANCE |
| MIRM | 79.62 | 0.25 | Nov 3 PM (f), LY Nov 4 | 14 / 0 / 0 | $118 | ADVANCE |
| GFS | 46.70 | 0.25 | **Nov 4 AM verified**, LY Nov 12 | 14 / 9 / 1 (stamp Aug 19) | $51 | ADVANCE |

## Chain stage

- **CBIO** (R2 needs Dec18: Nov 6 + 21 = Nov 27). Dec18 $12.5C 1.30 / 5.00, **OI 0**; $15C 0.30 / 4.90, **OI 0**. **KILL, R7.**
- **MIRM** (Dec18: Nov 4 + 21 = Nov 25). $80C 5.70 / 10.00 OI 41; $85C 4.20 / 8.00 OI 2; $90C 2.65 / 6.50 OI 95. Spreads 55-84% of mid. **KILL, R7.**
- **GFS** (later date LY Nov 12 + 21 = Dec 3; **no Dec18 listed**, so Jan15). Jan15 $50C 4.10 / 4.50, OI 2,309, spread 9.3%: R7 passes. BE at the ask $54.50 = **+16.7%**. R6, six AM prints: May 6 2025 -2.70, Aug 5 2025 -9.34, Nov 12 2025 -1.84, Feb 11 2026 +16.32, May 5 2026 +9.28, Aug 5 2026 -4.92. Median 7.10%, cap **10.65%**. **KILL, R6** (also R4 proxy: BE $54.50 over the $51 tool low).

## Carry-overs from EVENING 2

- **BURL R4: RESOLVED, PASS.** Barclays' $254 was an Overweight cut on May 12 **2025** (since raised to $299, $336, then the $317-$329 range): not current. After the Aug 27 2026 print: BofA Buy $365, Bernstein Outperform $355, Deutsche Hold $323, Citi Neutral $318. Tool low $290 (undated) kept as the binding floor, $1.40 over BE $288.60. R1 re-measured tonight: 0.241 (52w $226.85-$378.33). R6 +9.60% vs 10.89%, R7 OI 386 / 14.4%. **Paper doc written (`research_BURL_paper.md`), paper entry 1x $270C Dec18 @ $18.60 (closing ask).**
- **CMG deal talk:** one search, nothing found. Results show only operating news (a national catering rollout targeted for 2027, reported Oct 7; Q3 Oct 28 PM) and no M&A filing. The IBTimes headline stays unread; treated as noise unless a second source appears.
- **BA $206 owner:** not searched (no search spare after BURL took two).

**Moved:** 13 new names (12 killed, GFS killed at R6 after the chain) + BURL to a paper entry + CMG headline check. 3 web searches (BURL x2, CMG).

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile (bottom quartile for calls), R2 earnings before expiry (21-day cushion on the later of tool date and last year's date; 10-Q deadline at least 5 trading days before expiry), R3 analyst consensus (max 1 Sell, 3+ Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability (dropped for paper), R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **R4 proxy:** at the free screen, the lowest target is already under where a call's breakeven would land.
- **No coverage:** the ratings tool returns no analyst data, so R3 and R4 can't be checked.
- **AH:** after-hours price.
- **(f):** earnings date not yet company-verified.
- **Re-sweep diff:** a new scan's rows minus every ticker already named in a research file, so only names that moved into the screen since the last pass get worked.
