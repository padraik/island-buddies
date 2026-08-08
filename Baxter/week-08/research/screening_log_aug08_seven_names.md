# Screening Log -- Aug 8, 2026 (Friday-night data, feeding Monday's decision)

Seven names carried in from tonight's earlier chain work, all with Rule 1 and Rule 2 already screened and Rule 5 chains already bid-verified. This pass re-verified earnings dates via `get_earnings_results` first (per the Aug 7 standing rule), re-pulled live prices, and ran real Rule 6 historical reactions via `get_equity_historicals` for all seven. One name (JMIA) advanced to a full research doc: `research_JMIA.md`. The other six are recorded here with the specific reason each died.

**Summary table**

| Ticker | Rule 2 check | Rule 6 (needed vs cap) | Real kill reason | Conviction |
|---|---|---|---|---|
| VFS | Confirmed, Sep 3 2026 PM (unverified but matches given) | 7.5% needed vs 5.67% cap | Rule 6 fail | 1.5/5 |
| STNE | Confirmed, Aug 13 2026 PM (verified true) | 8.0-8.5% needed vs 13.33% cap (passes) | Category 2 decline (real credit deterioration) | 2/5 |
| TIGR | Confirmed, Aug 26 2026 AM (unverified but matches given) | 8.5% needed vs 5.93% cap | Rule 6 fail | 1.5/5 |
| CPB | Confirmed, Sep 2 2026 AM (unverified but matches given) | 8.5% needed vs 9.21% cap (passes, thin) | Rule 3 fail (5-6 Sell ratings) | 1/5 |
| NNE | Confirmed, Aug 12 2026 PM (verified true) | 9.7-9.9% needed vs 2.07% cap | Rule 6 decisive fail | 1/5 |
| SOC | **Date discrepancy, see below** | 11.3-11.9% needed vs 6.47% cap | Rule 6 decisive fail, date also unresolved | 1/5 |

---

## VFS -- Rule 6 fail

Earnings re-verified: `get_earnings_results` returns Q2 FY2026 at **2026-09-03, PM, verified: false**, matching the pre-screen date exactly (no calendar-trap surprise here). Live stock $3.34 (Aug 7 close), strike $3.00C, ask confirmed in the ballpark of the original screen.

Four real verified earnings-day moves pulled: Sep 4 '25 (PM) +0.30%, Nov 21 '25 (AM) -6.78%, Mar 16 '26 (AM) -2.58%, Jun 8 '26 (AM) -4.98%. Median absolute move **3.78%**. 1.5x cap **5.67%**. Required move **7.5%**. **Decisive fail**, required move is 32% over the cap. VFS is a serial EV-maker loss-generator (every quarter in the trailing eight posted a wider loss than estimate); its earnings-day moves are small and mostly negative. The 15-day earnings-to-expiry buffer that made this "comfortable" in the original screen never mattered, Rule 6 kills it regardless of timing.

## STNE -- Category 2 decline, not Rule 6 or Rule 3

Earnings re-verified: `get_earnings_results` returns **2026-08-13, PM, verified: true**, matching the pre-screen date. Live stock $10.595 (Aug 7 close), down 4.4% on the day alone, continuing a slide from $11.08 (Aug 6).

This one is the trap: the arithmetic mostly passes. Rule 3: 1 Sell rating out of roughly 16 analysts (10 Buy, 5 Hold, 1 Sell per one source), right at the Rule 3 boundary but technically inside it. Rule 6: four real moves (Aug 7 '25 PM +6.96%, Nov 6 '25 PM -10.81%, Mar 2 '26 PM -19.38%, May 14 '26 PM -0.93%), median absolute **8.89%**, cap **13.33%**, required move **8.0-8.5%**, passes with real room. The live straddle and Rule 4 (BTIG Buy, $15 target after a cut from $22) also nominally clear breakeven ($11.40-11.50).

The kill is the decline category. Web-sourced coverage of STNE's Q1 2026 print (the one driving the current slide) is explicit: "credit quality worsened sharply, with the cost of risk at 21.9%, 90+ day NPLs near 7%, and provisions rising more than 50% QoQ," plus guidance risk from Brazil's Selic rate assumption. That is not a market overreaction to a clean number, it is a real, described deterioration in the credit book underneath StoneCo's merchant-lending business, the textbook Category 2 case the binder's decline-category test exists to catch. Today's continued 4.4% drop with no new catalyst is consistent with a stock still digesting that news, not a one-off dislocation. Passing Rule 6 and Rule 3 on paper does not overcome a real Category 2 story. **Kill.**

## TIGR -- Rule 6 fail

Earnings re-verified: `get_earnings_results` returns Q2 FY2026 at **2026-08-26, AM, verified: false**, matching the pre-screen date. Live stock $4.815 (Aug 7 close).

Four real verified moves: Aug 27 '25 (AM) -9.75%, Dec 4 '25 (AM) +4.04%, Mar 19 '26 (AM) -3.12%, Jun 2 '26 (AM) -3.87%. Median absolute move **3.96%**. 1.5x cap **5.93%**. Required move **8.5-8.6%**. **Fail**, required move is 44% over the cap. Worth noting for context, not for the verdict: TIGR's chart shows a massive, non-earnings crash on May 22, 2026 (stock fell from $5.84 to $4.36 on 72 million shares of volume, roughly 15x normal), which did most of the damage to this year's range. That event is a separate risk signal (regulatory/broker-specific, unrelated to the Aug 26 print) but doesn't change the Rule 6 verdict either way.

## CPB -- Rule 3 fail

Earnings re-verified: `get_earnings_results` returns **2026-09-02, AM, verified: false**, matching the pre-screen date. Live stock $23.05 (Aug 7 close, up 2.2% on the day). The zero-volume flag from the original screen is real and confirmed: the $24.50C Sep 4 contract shows **0 volume, 11 open interest**, a genuinely thin market, bid $0.20/ask $0.50 (a spread near 90% of the mark).

Rule 6 technically passes but thin: four real moves (Sep 3 '25 AM +7.22%, Dec 9 '25 AM -5.23%, Mar 11 '26 AM -7.05%, Jun 8 '26 AM -0.88%), median **6.14%**, cap **9.21%**, required move **8.46-8.6%**, using 92% of the cap. The live ATM straddle (nearest strike $23, same Sep 4 expiry) implies only a **7.27%** move, below what this trade needs, the options market disagrees with the historical read here, unlike every other survivor tonight.

None of that is the real reason. Rule 3 kills it outright: search results show CPB's coverage at "1 buy / 6 sell / 13 hold" by one count and "0 buy / 9 hold / 5 sell" (Moderate Sell consensus) by another, either way well past the max-1-Sell threshold for a calls candidate. This matches the binder's own history: CPB already died on Rule 3 in the Jul 20 batch ("4 Sell-class ratings of 19"). Same result again three weeks later. **Kill, confirmed twice now.**

## NNE -- Rule 6 decisive fail

Earnings re-verified: `get_earnings_results` returns **2026-08-12, PM, verified: true**. This is a real, if secondary, finding: the pre-screen listed this as "2 days buffer," but a PM release on Aug 12 means the market reaction prices in at Wednesday Aug 13's open, leaving only **one trading day** (Aug 13 to the Aug 14 expiry) to trade the reaction, not two. Not disqualifying by itself, but tighter than described. Live stock $18.845 (Aug 7 close, up 7.0% on the day).

Four real verified moves: Aug 14 '25 (PM) +1.96%, Dec 18 '25 (AM) +0.80%, Feb 17 '26 (PM) -0.63%, May 14 '26 (PM) -9.51%. Median absolute move **1.38%**. 1.5x cap **2.07%**. Required move **9.7-9.9%**. **Massive fail**, required move is roughly 4.7x the cap, the worst reachability ratio of anything screened tonight. NNE is a genuinely volatile stock day-to-day (it has posted 20%+ single-session moves multiple times this year, none of them on earnings), but its actual earnings-day reactions are small. The volatility that makes this stock "exciting" is not the volatility this trade is borrowing against. **Decisive kill**, same shape as UBER's Jul 29 kill.

## SOC -- Rule 6 decisive fail, and the earnings date itself does not hold up

Earnings re-verification is the headline finding here, not a footnote. `get_earnings_results` returns Q2 FY2026 at **2026-08-21, AM, verified: false** — not Aug 18 as carried into this session, and notably the **same day as the candidate's own Aug 21 expiry**. A confirming web search found a third, different estimate: Aug 11-14, 2026, sourced from historical cadence, with no company-confirmed date located anywhere. Three sources, three different dates, none confirmed. This alone would be reason to hold off on live entry regardless of the rest of the math, per the binder's standing rule that an unverified date on a position about to take real money earns a confirming check, not a shrug, and this one didn't resolve cleanly even after that check.

The arithmetic kills it independently anyway. Live stock $4.755 (Aug 7 close, roughly flat). Four real verified moves: Aug 12 '25 (AM) -2.10%, Nov 13 '25 (PM) -28.86%, Feb 27 '26 (AM) +4.30%, May 6 '26 (PM) -4.33%. Median absolute move **4.32%**. 1.5x cap **6.47%**. Required move **11.3-11.9%** (worse than the original screen's number given today's flat price action against a strike that needs the stock to move further). **Decisive fail**, required move is 1.7-1.8x the cap. The one huge historical move (-28.86%, Nov 2025) reflects real event risk for this name (Sable Offshore's pipeline restart has drawn heavy regulatory and environmental scrutiny in the past year), not a number to lean on for reachability. Between the contested date and the Rule 6 arithmetic, this is the cleanest kill of the batch. **Kill.**

## GLOSSARY

- **52-week range / percentile:** where the current price sits between the stock's low and high over the trailing year; 0% = at the low, 100% = at the high.
- **Rule 2 (confirmed catalyst):** the Iron Rule requiring a dated earnings event before the option's expiration.
- **Rule 3 (ratings):** for calls, near-zero analysts rating the stock Sell/Underperform (max 1 allowed).
- **Rule 4 (bear floor):** the lowest price target among Buy-rated analysts must sit above the option's breakeven.
- **Rule 6 (reachability):** the move required to reach breakeven must not exceed 1.5x the stock's median historical earnings-day reaction, verified against real closes.
- **Decline category (Category 1 vs 2):** whether a stock's drop reflects a one-off market overreaction (tradeable) or real, ongoing business deterioration (not tradeable).
- **`verified` flag:** on `get_earnings_results`, true means the date is company-announced; false means it is estimated from historical reporting cadence, and should be treated as tentative.
- **AM/PM release:** whether a company reports before market open (reaction prices in same day) or after market close (reaction prices in at the next day's open).
- **Straddle:** buying the at-the-money call and put together; its combined price divided by the stock price gives the market's own implied move for the event.
