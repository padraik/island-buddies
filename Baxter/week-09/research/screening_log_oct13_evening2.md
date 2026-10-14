# Screening log, Tue Oct 13, 8:00pm ET (EVENING 2)

*Live data pulled 00:00-00:20 UTC Oct 14; quotes are Tuesday's regular-session close. Reserve $676.28 (3.5/5 line $0.676). EVENING 2's own job (research docs for names past the chain stage) had no new names, so it wrote the three owed paper docs (`research_BA_paper.md`, `research_CMG_paper.md`, `research_LVS_paper.md`) and then started EVENING 3's refill: the **Nov 21 - Dec 11 print window**.*

## Scanner: prints Nov 21 - Dec 11, range pct < 0.25, cap >= $300M (preview, not saved)

| Band | Matches | Not in any week-09 log or passes.md |
|---|---|---|
| $1-10 | 36 | 3 (BRAI, SVRE, TRX) |
| $10+ | 50 | 2 (AGX, BURL) |

This window was already fished on Oct 8 (EVENING 2/3 Dec-print scans) and Oct 12 EVENING 3. 81 of 86 rows were already in a log.

## Free screen

| Name | Last | Range pct | Print (scanner) | Buy / Hold / Sell | Low target | Result |
|---|---|---|---|---|---|---|
| BRAI | 4.93 | 0.03 | Nov 30 | none | | **KILL, no coverage** |
| SVRE | 1.12 | 0.00 | Nov 30 | none | | **KILL, no coverage** |
| TRX | 1.055 | 0.23 | Dec 2 | none | | **KILL, no coverage** |
| AGX | 388.10 | 0.24 | Dec 4 | 4 / 2 / 1 | $273 | **KILL, R4 proxy** (low under the stock) |
| BURL | 263.31 | 0.24 | Nov 25 | 15 / 6 / 0 | $290 (aggregate stamp **2023-06-28**) | ADVANCE |

## BURL through the chain stage (paper-priced)

- **R2:** tool Nov 24 AM (f), LY Nov 25 AM. Later + 21 = Dec 16, before Dec 18. Fiscal Q3 ends ~Oct 31; 10-Q deadline (40 days) ~Dec 10-11, which is 5 trading days before Dec 18: passes at the edge. Nov20 fails the 21-day test.
- **R7, Dec18 calls:** $270C 16.10 / 18.60, OI 386, spread 14.4% **PASS**; $280C 12.50 / 15.10, OI 106 FAIL; $290C 10.30 / 13.00, OI 14 FAIL.
- **R6:** six AM prints (prior close to print-day close): May 29 2025 -4.52, Aug 28 2025 +5.34, Nov 25 2025 -12.24, Mar 5 2026 +6.89, May 28 2026 -7.88, Aug 27 2026 -7.64. Median 7.26%, cap 10.89%. $270C BE at the ask $288.60 needs **+9.6%**: **PASS**.
- **R4: UNRESOLVED.** The tool's $290 low is $1.40 over BE, and the aggregate is stamped June 2023, so it can't be trusted as a dated floor (Tab 6). One search: Barclays cut to **$254 from $329** (rating and date not in the summary); also Wells Fargo $300 (from $325), Loop $305 (from $315), JPM $346, Citi $318 Neutral, Deutsche $323, BofA $365, Goldman $382. If Barclays' $254 is a Buy-side target, R4 fails.
- **Result: PARK.** Next check: Barclays' rating and date on the $254 (one search). If it's Equal Weight/Underweight, find the lowest dated Buy-side target after the Aug 27 print; if that is over $288.60, BURL goes to a paper doc.

## Paper-doc refresh (BA, CMG, LVS), R6 re-measured at the close (entry tests, not exits)

| Name | Stock | BE | Needs | Cap | Tonight |
|---|---|---|---|---|---|
| BA $195C Nov20 | 186.49 | 202.70 | +8.69% | 6.85% | fails (passed at entry by $0.95) |
| CMG $32.5C Nov20 | 30.35 | 33.98 | +11.96% | 11.65% | fails by 0.31 pts |
| LVS $37.5C Nov20 | 37.04 | 38.85 | +4.89% | 11.33% | passes |

**Moved:** 5 new names (4 killed, 1 parked) + 3 paper docs. 4 web searches (BA, CMG, LVS decline causes; BURL floor).

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile (bottom quartile for calls), R2 earnings before expiry (21-day cushion on the later of tool date and last year's date; 10-Q deadline at least 5 trading days before expiry), R3 analyst consensus (max 1 Sell, 3+ Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability (dropped for paper), R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **R4 proxy:** at the free screen, the lowest target is already under the stock price, so no call's breakeven can clear it.
- **Aggregate stamp:** the `updated_at` time on the tool's ratings record; a 2023 stamp means the low/high targets may be years old.
- **AM print:** results before the open; the move is measured prior close to print-day close.
