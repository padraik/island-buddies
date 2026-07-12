# SCREENING LOG: JULY 12, 2026 (SATURDAY, INLINE)
*First batch run under the post-mortem's geometry-first protocol (post_mortem_screen_jul12.md). Baxter alone at the desk, market closed, Friday-close data. Local scripts before searches, per the July 10 budget rule.*

**Slice:** 16 names. Two are the free re-checks the post-mortem ordered (OLED, NXST — killed DATA-INSUFFICIENT on chain data Jul 10). The other 14 sourced from the geometry box: sub-$40 (mostly), historically violent earnings movers, declines that printed weeks-to-months ago rather than this week — beaten-down growth/platform names not in the excluded universe.

**Method:** Cost-ordered funnel, strictly. Step 1: `fetch_price.py --range` (free) for R1 direction. Step 2: `fetch_puts_chain.py --calls` (free) for live Rule 5/6 geometry — chains BEFORE searches, which the July 10 run couldn't do (parallel-agent auth conflicts). Step 3: WebSearch only for names still alive after the chain (R2 date, R3 ratings, decline category). Puts-zone names get a watch-list note only — no searches — per the back-test gate and post-mortem Action 3.

**Data integrity note (logged per standing decision):** the first `fetch_price.py` batch run this session produced mislabeled output — robin_stocks silently drops invalid tickers (ZI, LC) from batch results, desyncing prices from labels for every name after the dropped one (CHGG printed as $89.23; the real figure is $0.86). Bug found because two prices failed the smell test, script fixed same session (per-ticker fetch, labels can no longer desync), batch re-run clean. No screening verdict was rendered on the bad data. This is the TRMB-$66.91 lesson doing its job.

---

## SCREENING TABLE

| Ticker | Price | Range % | Direction | Chain (live) | Earnings | Ratings / category | Verdict |
|---|---|---|---|---|---|---|---|
| OLED | $81.04 | 5% | CALLS | Aug 21: ZERO calls in $0.10-1.00 band with breakeven above stock. Only affordable strikes are Jul 17, before the Jul 30 print. | Jul 30 (prior confirm) | not reached | **R5 KILL (chain)** — Jul 10 DATA-INSUFFICIENT resolved: confirmed dead, not thin-data |
| NXST | $174.05 | 20% | CALLS | Both pulled expiries: nothing affordable in band | Aug 6 (prior confirm) | not reached | **R5 KILL (chain)** — Finding 1 geometry confirmed on live chain; Jul 10 kill stands |
| U | $30.89 | 40% | MID-OUT | - | - | - | MID-OUT |
| AI | $8.97 | 6% | CALLS | Aug 28 $9C $0.96 → +11.0%; $10C $0.76 → +14.4%. Geometry live. | **Sep 9 (confirmed, TipRanks)** — outside every affordable expiry | not reached | **R2 OUT-OF-WINDOW → AUG RE-SCREEN** with flag: Q1 FY27 revenue guided $50-54M vs ~$87M yr-ago; probable Category 2 revenue collapse. Re-screen must clear the category test first. |
| PATH | $11.69 | 23% | CALLS | Aug 28 $12C $0.85 → +14.2%; several strikes live | **Sep 8 (confirmed)** — outside window | not reached | **R2 OUT-OF-WINDOW → AUG RE-SCREEN** when Sep chains open. AI-disruption-of-RPA category question open. |
| S | $17.80 | 62% | MID-OUT | - | - | - | MID-OUT |
| ZI | n/a | n/a | - | - | - | - | NOT TRADEABLE (404 on Robinhood; delisted/renamed) |
| BMBL | $3.10 | 9% | CALLS | Aug 21 $3C $0.50 → +13.0% needed; geometry fine | Aug (est) | Hold consensus, 0 Sells BUT blended target cut $5.50→$5.00 (fresh); payers -23% y/y, revenue -14%, share loss to Hinge accelerating | **LINE 5 KILL (Category 2 secular)** + fresh target cuts fail hardened R3. The chain was willing; the business is melting. |
| FVRR | $10.91 | 7% | CALLS | Aug 21 $12C $0.90 → +18.2% (borderline vs 1.5x cap); $13C $0.50 → +23.7% (unreachable) | Jul 29 pre-market (confirmed) | 7 Buy/10 Hold/0 Sell passes count; company guides FY26 revenue -3% to -12% | **LINE 5 KILL (Category 2 secular)** — a marketplace guiding its own revenue down double digits is not an overreaction story; R6 was marginal anyway |
| CHGG | $0.86 | 29% | MID-OUT | - | - | - | MID-OUT (also sub-$1 structural profile) |
| W | $89.23 | 54% | MID-OUT | - | - | - | MID-OUT |
| RKT | $14.40 | 18% | CALLS | Rich chain: Aug 7 $16C $0.72 → +12.6%; Aug 21 $16C $0.77 → +16.5% | Jul 30 AC (confirmed) | Barclays target cut $19→$17 on **Jul 7** (inside 30d) = hardened R3 FAIL; 9 downward estimate revisions; beta 2.25 rate-driven decline | **TRIPLE KILL: R3 (fresh cut) + Category 3 (macro beta/rates) + line 11 (falling revisions)** |
| LC | n/a | n/a | - | - | - | - | NOT TRADEABLE (400 on Robinhood) |
| VFC | $16.77 | 51% | MID-OUT | - | - | - | MID-OUT |
| TDOC | $9.26 | 91% | PUTS zone | not pulled (puts gated) | - | - | **WATCH-LIST ONLY** — puts blocked until passes.md back-test (Jul 31). Cheap stock at 91st pct with violent earnings history = the right geometry if the back-test unblocks the system. No searches spent. |
| GRPN | $26.50 | 51% | MID-OUT | - | - | - | MID-OUT |

## BASE RATES

| Outcome | Count | Names |
|---|---|---|
| MID-OUT (R1) | 6 | U, S, CHGG, W, VFC, GRPN |
| Not tradeable on platform | 2 | ZI, LC |
| R5 chain kill (live, free) | 2 | OLED, NXST |
| R2 out-of-window → Aug re-screen | 2 | AI, PATH |
| Line 5 category kill | 2 | BMBL, FVRR |
| R3 + category + revisions | 1 | RKT |
| Puts watch-list (gated) | 1 | TDOC |
| **ADVANCE** | **0** | - |

**Cost accounting, the point of the whole exercise:** 16 names screened with **5 web searches total** (BMBL, FVRR, RKT, AI, PATH — survivors only). The July 10 protocol spent roughly one search per name at minimum. Geometry-first killed or gated 11 of 16 names for zero tokens, including resolving both DATA-INSUFFICIENT re-checks with certainty instead of a guess. The funnel's verdict quality went up (chain-verified vs web-glanced) while the cost per name went down ~70%. This is the post-mortem's Finding One working on its first live batch.

**What the batch says:** The aged-dislocation thesis (post-mortem Finding Two) got a partial test — BMBL, FVRR, AI all bottomed weeks ago with stale-ish ratings, and all three still died, but on *category*, not on R3 capitulation-in-progress. That is consistent with the post-mortem's geometry-box warning: most residents of the cheap-and-violent box are structurally broken. The screen is finding the right kind of candidate and correctly refusing the broken ones. The two September names (AI, PATH) are the live pipeline; both get fresh chains and the full category test when Sep expiries open in August, alongside the SOUN re-check Jul 31 and ZG/DIS re-funnels.

## GLOSSARY

- **Geometry-first protocol:** Screening order adopted after the July 12 post-mortem: free local data first (price/range via `fetch_price.py`, live chain via `fetch_puts_chain.py --calls`), paid searches only for names still alive afterward. Inverts the July 10 order, where chains came last.
- **Geometry box:** The joint Rule 5 + Rule 6 constraint: a stock cheap enough (~$3-40) and volatile enough on earnings that an option ask ≤$1.00 exists at a strike the catalyst can plausibly reach.
- **52-week range percentile / R1:** Where price sits between the 52-week low (0%) and high (100%). Bottom quartile = calls candidate, top quartile = puts candidate, middle = MID-OUT.
- **MID-OUT:** Killed at R1 for sitting in the middle of the range. Costs one free script call in this protocol.
- **R2 (earnings window):** Confirmed earnings date must fall before an affordable expiry. Out-of-window names are queued for re-screen, not killed, if the date is confirmed and later chains may open.
- **R3 (ratings direction, hardened):** Calls need max 1 Sell AND no downgrades or target cuts inside 30 days. A fresh target cut (RKT's Barclays $19→$17) fails it even with the rating maintained.
- **Rule 5 / R5 (chain filter):** Option ask ≤$1.00/share for calls, ≤$1.50 for puts, verified on the live chain only. An empty band = no instrument = dead play.
- **Rule 6 / R6 (reachability):** Required move to breakeven ≤1.5x the stock's median earnings-day move.
- **Line 5 / decline category:** Every beaten-down candidate's decline must be named: (1) event overreaction — the only tradeable kind, (2) secular decline, (3) macro beta, (4) commodity/cycle unwind.
- **Line 11 (estimate revisions):** Direction of consensus EPS revisions in the trailing 30 days. Falling revisions into a print cap or kill a calls thesis (the SOUN gate).
- **Breakeven / required move:** Strike plus premium (calls); the percentage the stock must rise for the option to be worth its cost at expiry.
- **Back-test gate:** Standing decision — no live puts entry until every passes.md name runs through the inverted Iron Rules. Calxter's deadline: Jul 31, 2026.
- **Watch-list only:** A name logged for future evaluation with no searches or DD spent now (TDOC, pending the puts back-test).
- **DATA-INSUFFICIENT:** A kill rendered because required data couldn't be verified. The post-mortem added a free local-script re-check before such kills become final; OLED and NXST were the first two, and both resolved to confirmed kills.
- **Label desync (the fetch_price bug):** Batch quote requests silently dropping invalid tickers so prices shift against the ticker list — every price after the dropped name belongs to the wrong label. Fixed July 12 by fetching per-ticker.
- **Beta:** A stock's volatility relative to the market (RKT's 2.25 = highly rate/market-sensitive, feeding its Category 3 kill).
- **AC / pre-market:** After close / before market open — when the earnings print lands relative to the trading day.

## SOURCES (survivor searches)

- [MarketBeat — BMBL earnings](https://www.marketbeat.com/stocks/NASDAQ/BMBL/earnings/), [Benzinga — BMBL analyst ratings](https://www.benzinga.com/quote/BMBL/analyst-ratings), [Simply Wall St — BMBL results coverage](https://simplywall.st/stocks/us/media/nasdaq-bmbl/bumble/news/results-bumble-inc-exceeded-expectations-and-the-consensus-h)
- [MarketBeat — FVRR earnings](https://www.marketbeat.com/stocks/NYSE/FVRR/earnings/), [TipRanks — FVRR forecast](https://www.tipranks.com/stocks/fvrr/forecast), [WallStreetZen — FVRR forecast](https://www.wallstreetzen.com/stocks/us/nyse/fvrr/stock-forecast)
- [TipRanks — RKT earnings](https://www.tipranks.com/stocks/rkt/earnings), [CNBC — RKT quote](https://www.cnbc.com/quotes/RKT)
- [TipRanks — AI (C3.ai) earnings](https://www.tipranks.com/stocks/ai/earnings), [C3.ai IR — FY26 Q4 results](https://c3.ai/c3-ai-announces-fiscal-fourth-quarter-and-full-fiscal-year-2026-results/)
- [TipRanks — PATH earnings](https://www.tipranks.com/stocks/path/earnings), [UiPath IR](https://ir.uipath.com/)
