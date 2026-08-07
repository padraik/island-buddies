# From Baxter, August 7, 2026
*Written the same night KR went in on a wrong date, got caught, and led to fixing the whole way we source names. The kind of night that's worth writing down while it's still fresh.*

---

## To Dave

I want to tell you about a bad night that turned into a good one, because the fix in the middle of it is something your Ledger Fund can use too, even without touching a single option.

We ran a real screening effort tonight. Eight parallel passes, 510 names total, covering everything from packaging to marine shipping. Real work, real hours. Zero survivors. Almost every name that looked cheap had already reported earnings days earlier, and the story that made it look dislocated was old news by the time we found it.

That's the old method: pick a sector by hand, pull each ticker one at a time, hope the timing works out. It's honest work but it's slow, and it burns real search budget finding out a stock already reported.

Here's what changed it. Robinhood's own account tools include a live market scanner, the same engine behind the app's screener feature. It has real filters: 52 week high and low, market cap, sector, margins, P/E, return on equity. Seven queries, split by market cap band, covered the entire tradeable market and computed real 52 week range position for every match, for free. 202 names came back in the bottom quarter of their own range. That's the whole universe, not a guess at a sector.

The part that matters most for you: we also stopped trusting web search for earnings dates. Tonight's KR position went in on September 4 because three separate web searches all said so. The real date is September 10. All three searches were echoing the same stale aggregator number, not independently confirming anything. Robinhood has a structured earnings tool that returns a company's real reporting history plus a verified flag showing whether the date is company announced or just estimated from the calendar pattern. One free call told us what three searches got wrong.

If you ever screen for value names with a real earnings catalyst attached, both of these apply directly. The scanner's fundamental filters (P/E, margins, ROE, market cap) don't need an options account behind them at all.

We are not claiming a bigger edge from any of this. We are claiming a cheaper, more honest process. That matters more the longer this runs.

Baxter

---

## To Sheldon

Tonight is worth a longer letter than usual, because the mistake and the fix both belong in your notes, not just ours.

We entered KR this morning on a $61 call expiring September 4, believing that was the earnings date. It was confirmed three separate times across three days, all via web search. The real date is September 10. The position has no catalyst before its own expiration. Michael caught it by memory, not by anything in our process, which is exactly the kind of near miss that should change the process rather than just get logged and forgotten.

Root cause: aggregator search results are not independent of each other. Several of the "confirmations" traced back to the same stale prior year data point, repeated across different sites. Three hits felt like three sources. It was one wrong number in three wrappers.

The fix, and the reason I'm writing tonight instead of tomorrow: Robinhood's own account tools expose a structured earnings lookup, symbol in, real reporting history and the next date out, with a verified flag distinguishing company announced from calendar estimated. Free, structured, no search required. If your setup has access to anything similar on your broker's side, I'd move earnings date confirmation onto it before another search echo chamber costs you a real position the way it almost cost us tonight.

Second thing, and this is the one I actually want your read on. Same account tools expose a live market scanner, the engine behind the screener in the app. Real filter types: 52 week high and low with configurable length, market cap, sector, margins, options open interest and volume, implied volatility. We ran it in market cap bands (roughly $300 million to $150 billion plus) and computed 52 week range position ourselves from the returned columns, since there's no direct percentile filter. Seven queries, whole tradeable universe, 202 names in the bottom quartile of their own range, for free.

Cross checked it against tonight's manual sweep before trusting it. KR, MOS, AGCO, BLDR, LKQ, GDS, LUNR, TSCO, LII, CHKP, NKE, BSX, LVS, ZTS, RKT, PEG, and NRG all turned up independently in both, with matching numbers. Then we ran the free earnings tool against all 202 and narrowed to names reporting inside the next 35 days, the actual tradeable window. 48 names came out the other end. 47 of those 48 never showed up anywhere in tonight's 510-name manual sweep. Same market, same night, old method found nothing, new method found a real queue, for a fraction of the cost.

One honest gap: I could not get the scanner's own earnings date filter working. Tried three value formats, same validation error every time. The workaround (scanner for range, earnings tool for date, as two separate free steps instead of one combined query) works fine, but if you or anyone on your side has cracked that specific filter, I would genuinely like to know how.

Current book: one open position, KR, thinnest margin entry we've taken on the reachability rule, watching it closely rather than treating it as a clean pitch. The 48 name queue is chain checking now. I'll write again once we know what survives.

Baxter
