# Research: BTGO (BitGo Holdings, Inc.) -- Aug 11, 2026

**Verdict: KILL. Decline category / Rule 4 freshness failure, not a Rule 6 or Rule 3 letter-of-the-rule failure.**

## Setup

- Price: $5.04 (Aug 11, 2026)
- 52-week range: $4.67 - $24.50
- Percentile: **1.9th**, deepest dislocation of tonight's scanner batch
- Confirmed catalyst: **Q2 FY2026 earnings, Aug 12, 2026, PM, `get_earnings_results` verified: true**

## Why this looked good on the surface

Rule 1 clears with the most room of any name screened tonight. Rule 2 verified true. A first-pass Rule 3 read (one aggregator: 12 analysts, 10 Buy, 0 Sell, 2 Hold) looked clean. Rule 6 passed at 32% of a 24.70% cap. Generic price-target aggregators showed a $10-11.5+ floor against a stock at $5.04 -- on paper, the widest Rule 4 cushion of anything screened tonight.

## Why it's dead anyway

**IPO'd Jan 22, 2026 at $18. Fell below the IPO price by its second day of trading.** Q1 2026 EPS missed badly (-$0.62 actual vs -$0.14 to -$0.01 depending on the estimate source), driven by non-cash mark-to-market losses on BitGo's own bitcoin treasury holdings plus IPO-related stock comp. Management's own forward guidance says digital-asset-sales revenue will "remain broadly consistent" with the weak Q1 level -- not a recovery signal. The company cut 15% of staff. **A securities class-action lawsuit is active** (Kaplan Fox & Kilsheimer, Robbins LLP, Levi & Korsinsky all separately alerting investors), class period Jan 22-May 13 2026, alleging the IPO documents and subsequent statements were materially misleading about how exposed the business was to declining crypto prices. Lead plaintiff deadline was Aug 7, 2026 -- four days before tonight's screen.

**The Rule 4 floor doesn't survive a freshness check.** The binder's own standing rule (Tab 6, written after CCL/NKE/BSX): a bear floor must be dated within 60 days and published *after* the stock's decline to count. Every Buy-rated BTGO target locatable tonight (Goldman Sachs $11.5, Cantor Fitzgerald $18, both Feb 17 2026; Citigroup $17, Mar 18 2026) predates the Q1 earnings miss (reported after Feb/Mar) and predates the lawsuit entirely. **The only analyst action found dated after the Q1 miss is KBW, holding Market Perform (Hold, not Buy) at $12** -- maintained, not raised, specifically despite the miss. That's not a floor under Rule 4, that's a Hold-rated analyst declining to call it a Buy after seeing the real numbers. No fresh Buy-rated floor exists for this name as of tonight.

**Decline category: Category 2, not Category 1.** This isn't the market overreacting to a good business having one bad print. Revenue collapsed on a real, structural driver (BTC price -23.8% in Q1, and BitGo's revenue recognition is directly tied to digital-asset mark-to-market), guidance points to more of the same next quarter, headcount got cut, and there's active litigation over whether the company misrepresented this exact risk at the IPO. That is the CCL/NKE/BSX capitulation shape the binder was written to catch, not a UAMY-style production-growth story the market is temporarily mispricing.

## The lesson worth carrying

This is the ENVX/TME pattern again: a name that clears Rules 1, 2, 5, and 6 cleanly, and looks clean on Rule 3 from a generic aggregator, but dies on a real, dated, specific check that a fast read would have missed. The aggregator's "10 Buy / 0 Sell" count either includes stale pre-crisis coverage or simply hasn't caught up -- either way, it wasn't trustworthy without the freshness check. Same discipline that killed TME in the Aug 8 batch despite its clean Rule 6 math: passing rules is necessary, not sufficient.

Screened alongside BTBT tonight (same sector, same scanner pass, same night's bad BTC macro) -- BTBT got the opposite freshness result (a fresh analyst raise, not a stale target or a post-crisis Hold) and advanced. Full comparison in `research_BTBT.md`.

## GLOSSARY

- **Rule 4 (bear floor):** the lowest price target among Buy-rated analysts must sit above the option's breakeven, and per binder Tab 6, that target must be dated within 60 days and published after the stock's decline to count.
- **Decline category (Category 1 vs 2):** whether a stock's drop reflects a one-off market overreaction (tradeable) or real, ongoing business deterioration (not tradeable).
- **`verified` flag:** on `get_earnings_results`, true means the date is company-announced; false means it is estimated from reporting cadence.
