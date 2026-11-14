# Screening log: Fri Nov 13, EVENING 2 (8:00pm ET)

**Job:** no name cleared the chain stage in EVENING 1, so there's no doc to write. Started EVENING 3's / Saturday's job early: the AVGO Jan15 chain on Friday's close, the R6 print history, and (because the chain finished fast) Saturday's one floor search.

**Tally:** 1 name moved (AVGO: chain + R6 + R7 done, one floor search). 0 advanced past a gate, 0 buyable. DY noted only (no new quote until Monday). NIO re-pulled: unchanged.

## AVGO (paper)

**Price.** Friday regular close **$346.66** (-4.9% vs $364.36). AH $340.37 at 7:59pm. EVENING 1's $341.01 was an after-hours print, not the close.

**R1 (52-week percentile).** Weekly bars Nov 17 2025 - Nov 13 2026: high **$495.00** (week of Jun 1), low **$289.77** (week of Nov 2). Range $205.23.
- At the $346.66 close: (346.66 - 289.77) / 205.23 = **0.277, OUT**.
- At the $340.37 AH print: 0.246, in. (The scanner's `tradeAllDay.price` uses the all-day print, which is why AVGO showed 0.2497 at 6pm.)
- The R1 line (0.25) is **$341.08**.

**R2.** FQ4 **Wed Dec 9 PM, verified: true**. LY Dec 11 PM. Later of the two + 21 days = Jan 1, so the expiry has to be **Jan 15 2027**. Paper ramp sell would be **Wed Dec 9 3:35pm**.

**R3.** 53 Buy / 3 Hold / 0 Sell. Passes.

**R4 proxy.** Lowest target $398.47 (mean $526.19, high $660), but the ratings record is stamped **Oct 27**, before the Nov 5 rout. Fails the Tab 6 dating test, so the **floor gate is shut**. One search (Saturday's, done early): BofA $530 -> $460 (Buy) and RBC $370 -> $340 (Sector Perform, not a Buy) both turned up, but neither result carries a date I can tie to after Nov 5. Deutsche, Benchmark, TD Cowen, MS raises all read as post-print (Sep) notes. **Nothing dated after Nov 5 from a named Buy analyst. Gate holds.**

**R6 (reachability), last six PM prints, print-day close to next-day close:**

| Print | Close | Next close | Move |
|---|---|---|---|
| Jun 5 2025 | 259.93 | 246.93 | -5.00% |
| Sep 4 2025 | 306.10 | 334.89 | +9.41% |
| Dec 11 2025 | 406.37 | 359.93 | -11.43% |
| Mar 4 2026 | 317.53 | 332.77 | +4.80% |
| Jun 3 2026 | 479.23 | 418.91 | -12.59% |
| Sep 2 2026 | 367.24 | 357.16 | -2.74% |

Median absolute move **7.21%** ((5.00 + 9.41) / 2). Cap 1.5x = **10.81%**.

**Jan15 chain (Friday 4:00pm quotes):**

| Strike | Bid / Ask | OI | Spread % mid | BE at ask | Needed from $346.66 | R6 | R7 |
|---|---|---|---|---|---|---|---|
| $350C | 28.20 / 29.70 | 8,162 | 5.2% | $379.70 | +9.53% | **pass** | pass |
| $360C | 23.85 / 24.85 | 7,500 | 4.1% | $384.85 | +11.02% | fail | pass |
| $370C | 19.70 / 21.90 | 8,600 | 10.6% | $391.90 | +13.05% | fail | pass |
| $380C | 16.55 / 18.15 | 4,704 | 9.2% | $398.15 | +14.85% | fail | pass |
| $390C | 13.70 / 14.50 | 9,780 | 5.7% | $404.50 | +16.69% | fail | pass |
| $400C | 11.35 / 11.90 | 15,293 | 4.7% | $411.90 | +18.82% | fail | pass |

**The window.** R1 and R6 pull opposite ways on the $350C. R1 needs the stock at or under **$341.08**. R6 on the $350C (delta 0.54, first-order: ask moves ~$0.54 per $1) needs the stock at or over about **$338.85**. So the contract passes both only with AVGO between roughly **$338.85 and $341.08** at the moment of entry. Friday's close sat $5.58 above that window; the AH print sat inside it. Cost at the ask: $2,970 (paper; far past Rule 5 for the real fund).

**Verdict:** chain stage done, $350C Jan15 is the contract. Blocked by the **floor gate** (stamp Oct 27). If a dated Buy target above ~$380 shows up after Nov 5 and the stock opens in the $339-341 window, a paper doc can be written same evening. Not writing the doc tonight: the gate is the gating fact, and a doc written behind a shut gate is wasted plan usage.

## DY (paper, watch)
No new data (regular close $221.52, pre-market Monday is the next real quote). Last night's line stands: R6 clears with the stock ~$225.50 at the Dec18 $250C's $11.80 ask. Ratings unchanged 12/1/0, low $375, **no stamp** (floor gate unverifiable from the tool).

## NIO (real)
Close $2.90, AH $2.86. 16/7/1, low $3.6983, **stamp still Sep 1**. Floor gate shut. Q3 Nov 24 AM unverified (EVENING 1 pull).

## GLOSSARY
- **R1:** where the stock sits in its 52-week range; under 0.25 = bottom quartile, required for a call.
- **R2:** the catalyst (earnings) has to land at least 21 days before expiry.
- **R3:** analyst consensus has to lean Buy.
- **R4 proxy / floor gate:** the lowest Buy target has to sit above breakeven, and (Tab 6) it has to be dated after the stock's last big drop, or it's stale.
- **R6:** the move needed to reach breakeven must be no more than 1.5x the median earnings-day move.
- **R7:** liquidity floor: open interest at least 250, spread at most 25% of mid.
- **BE:** breakeven at expiry = strike + premium.
- **AH:** after-hours trading.
- **Ramp sell:** selling before the print to capture the pre-earnings run-up instead of gambling on the report.
