# IRON RULES -- PUTS (DRAFT v2)
*Companion to the Five Iron Rules for calls. Apply to every put entry. Not suggestions.*
*Written June 18, 2026. Revised after independent review. Under ratification before first live puts entry.*

---

## THE FIVE RULES

**Rule 1: Stock in the top 20-25% of its 52-week range, AND has not made a new 52-week high within the prior 5 trading days.**

The mirror of the call Rule 1. We enter puts on strength, not on a stock already falling. A stock in freefall has already repriced -- the thesis has fired without us and the option premium reflects it. A stock near its 52-week high is priced for continued optimism. That optimism is what we are shorting.

The 5-day breakout exclusion catches the momentum spike problem. A stock that hit a new 52-week high last Tuesday is in a different risk environment than a stock that has been rangebound near its high for two months. Fresh breakouts have the full force of momentum buyers, quant trend-followers, and short-covering behind them. We do not step in front of that train. We wait for the stock to stall at its high before entering the short thesis.

*Pass: stock price is within top 20-25% of 52-week range AND no new 52-week high in the prior 5 trading days.*
*Fail: stock is more than 25% below its 52-week high (already repriced), OR stock made a new 52-week high within the last 5 trading days (momentum at peak).*

---

**Rule 2: Earnings catalyst before expiry.**

Same as the call Rule 2. No substitutes. A puts thesis based on "the stock is overvalued" without a binary event is a BOTZ position -- a theme without a mechanism. The market can stay irrational longer than our option stays solvent. The earnings date is the mechanism that forces resolution on a specific day.

*Pass: confirmed earnings date falls before option expiry, with minimum 21 days to expiry at entry.*
*Fail: no scheduled binary event inside the window, OR fewer than 21 days to expiry at entry.*

The 21-day minimum ensures there is enough runway for the thesis to develop if earnings land ambiguously. A 2-week window after earnings with no cushion is a coin flip on IV collapse, not a thesis.

---

**Rule 3: Minimum 2 Sell or Underperform ratings in the covering analyst universe, OR a documented downgrade from Buy to Sell at a major firm within the past 30 days.**

The inverse of the call Rule 3. For calls, near-zero Sells means the analyst floor holds. For puts, we need institutional skepticism already on record. A unanimous Buy consensus means credentialed analysts with full access to management and channel data collectively disagree with our short thesis. That is a structural headwind.

The OR clause is restricted to Buy-to-Sell downgrades only. A Buy-to-Hold downgrade signals the analyst thinks the stock is fairly valued or has limited upside -- it does not signal that the analyst expects the stock to fall. A Hold analyst cannot contribute a bull ceiling to Rule 4 because a Hold is not a bearish target. If the only available signal is a Buy-to-Hold downgrade, the play does not satisfy Rule 3.

Rule 3 is load-bearing: it must pass before Rule 4 can be evaluated. No Sell ratings means no bull ceiling means Rule 4 cannot be applied. If Rule 3 fails, the play is dead regardless of other factors.

*Pass: 2+ Sell/Underperform ratings present, OR documented Buy-to-Sell downgrade at a major sell-side firm within 30 days.*
*Fail: fewer than 2 Sell ratings AND no Buy-to-Sell downgrade within 30 days -- includes Buy-to-Hold-only downgrades.*

---

**Rule 4 (Bull Ceiling): The highest price target among Sell/Underperform-rated analysts must be BELOW the put breakeven.**

Put breakeven = strike price minus premium paid.
Example: $50P at $0.80 → breakeven $49.20. The most optimistic bear on the Street -- the Sell analyst with the highest target -- must still believe the stock is going below $49.20. If that analyst has a $52 target, the bear thesis does not reach our breakeven even from its most favorable form.

This is the structural mirror of the call Rule 4:
- Calls: lowest Buy target (most pessimistic bull) must be above call breakeven.
- Puts: highest Sell target (most optimistic bear) must be below put breakeven.

Rule 4 will be harder to satisfy than its calls equivalent. Sell analysts on stocks near highs often have targets that are pessimistic by broad market standards but still above a reasonable put breakeven. This is a feature, not a bug. The system should fire less frequently on puts until it has a live track record. A play that barely passes Rule 4 is not the same as a play with significant bull ceiling margin -- that margin enters the conviction score.

*Pass: highest Sell/Underperform target is below put breakeven.*
*Fail: highest Sell target is above put breakeven, OR no Sell ratings exist (Rule 3 fail cascades here).*

---

**Rule 5: Option ask at or below $1.50 per share.**

Adjusted from the calls Rule 5 cap of $1.00. The difference is structural: stocks near 52-week highs carry different option premium dynamics than beaten-down stocks. A stock trading at $80 near its high has ATM puts priced off $80 with potentially compressed IV (complacency at highs). A beaten-down stock at $30 near its low has ATM calls in a lower absolute price environment. The $1.00 cap on calls was calibrated for that environment. $1.50 for puts reflects the premium reality of higher-priced stocks near highs.

The cap is still meaningful. $1.50 per share = $150 maximum loss per contract. The defined-risk property of the position is preserved. We are not removing the discipline -- we are calibrating it to the instrument environment.

Note: even at $1.50, high-priced stocks (above $100) will frequently push puts below this threshold only at deep OTM strikes, requiring large stock moves. If no instrument on a stock clears Rule 5 at a strike where Rule 4 also passes, the play fails and does not enter the fund. This will eliminate many otherwise-interesting names. That is the system working correctly.

*Pass: option ask ≤ $1.50.*
*Fail: option ask > $1.50.*

Additionally: the specific contract must have open interest above 100 and a bid-ask spread of less than 20% of the mid price. Thin chains with wide spreads mean we fill at ask and cannot exit without significant slippage. This is not a hard Iron Rule but a pre-entry liquidity check that must be documented in the research file.

---

## PUTS-SPECIFIC PROTOCOL
*Not rules. Standing operating procedure for any play that passes all five.*

**Short interest is a squeeze warning, not a positive signal.** High short interest (above 10% of float) on a puts candidate means other short-sellers are already positioned. This creates squeeze risk: any positive earnings surprise -- even an in-line print the market reads as "not as bad as feared" -- can trigger a violent short-covering rally that wipes out the put. The ruleset previously identified short interest as a corroborating positive signal. This was incorrect. Short interest above 10% is a red flag that raises the conviction threshold required for entry, not a reason to be more confident. Treat it as a volatility amplifier in either direction. It does not disqualify the play, but it requires a specific acknowledgment in the research file and cannot coexist with a 3.5/5 conviction score -- minimum 4/5 if short interest is elevated.

**M&A and buyout risk.** Stocks near 52-week highs are acquisition targets. A buyout announcement typically sends the stock up 20-40% immediately and the put expires worthless with no live-breach exit possible before the open. Before entering any puts position, confirm: no documented M&A rumors, no strategic review process announced, no activist investor running a public campaign that could trigger a takeout. If any of these conditions are present, the play is disqualified regardless of Iron Rules scores. Document the check in the research file.

**IV timing.** Stocks near 52-week highs typically carry lower implied volatility than beaten-down stocks -- the market is complacent at highs. Buying puts when IV is low means a falling stock also delivers IV expansion, which amplifies put gains. This is a structural advantage relative to calls in equivalent setups and should be noted in the research file as a supporting condition.

**Catalyst direction is part of conviction scoring.** The earnings catalyst for a puts play must be specifically expected to disappoint -- guidance cut, margin compression, regulatory exposure, subscriber miss, beat-and-guide-down structure. "Earnings catalyst exists" passes Rule 2. "The catalyst is specifically expected to be negative" determines whether the conviction score reaches 4/5. Conviction cannot exceed 3.5/5 without a documented specific disappointment thesis. Additionally: a company that has beaten and raised EPS estimates for four or more consecutive quarters cannot receive 4/5 conviction regardless of other factors -- the earnings history is structurally against the short thesis.

**Estimate revision check.** Before finalizing conviction, verify the direction of consensus estimate movement in the 30 days prior to earnings. If analyst EPS estimates have been revised upward in the lead-up to earnings, the market has already priced in an optimistic view and a beat becomes more likely. This is not a disqualifier but it caps conviction at 3.5/5 unless a specific fundamental reason overrides the revision trend.

---

## EXIT RULES

- **Primary:** Sell at market open the morning after earnings, regardless of direction.
- **Rule 4 live breach:** If any Sell-rated analyst raises their target above the put breakeven at any point after entry, exit same day. The bull ceiling has lifted.
- **Rule 3 live breach:** If all Sell ratings are upgraded and the structure returns to near-unanimous Buy, exit same day.
- **BOTZ watch:** If the stock is not trending toward the put breakeven two weeks before expiry, sell into remaining value. Themes without data confirmation are dead money in either direction.
- **M&A announcement:** If a buyout or merger is announced after entry, exit at open the next trading day. The thesis is structurally broken regardless of price.
- **No averaging down.** If the stock moves up after entry, hold to the exit rule or let it expire. Do not add contracts.

---

## CONVICTION SCORING AND SIZING

Same fractional Kelly base structure as calls, with puts-specific caps:

| Conviction | Contracts | Max at risk |
|------------|-----------|-------------|
| 3.5/5 | 1 | $75-150 |
| 4/5 | 1 | $75-150 |
| 5/5 | 2 | $150-300 |

**Puts are capped at 1 contract until the system has a live track record.** The calls system earned 2-contract sizing after demonstrating the Iron Rules work in practice. The puts system has no track record. Maximum 1 contract per play until the first three puts plays have closed with documented outcomes. After three closed plays, the sizing table resets to standard: 4/5 = 2 contracts, 5/5 = 3 contracts.

A puts play cannot exceed 3.5/5 without:
- Documented specific disappointment thesis (not just "stock is high")
- No M&A risk present
- No short squeeze warning (or short interest explicitly addressed)

A puts play cannot exceed 4/5 without:
- Bull ceiling margin of at least $3.00 below put breakeven (not barely passing Rule 4)
- Company has not beaten and raised for 4+ consecutive quarters
- Estimate revision trend is flat or negative in the prior 30 days

---

## BACK-TEST PROTOCOL
*Before first live puts entry.*

Run every name currently in passes.md through the puts screen. For each name that passes all five rules, document:
1. What the puts play would have been (strike, expiry, cost, breakeven)
2. What the stock did between the pass date and the catalyst date
3. Whether the play would have been profitable under the exit rules

The purpose is not to cherry-pick wins. The purpose is to calibrate whether the rules select plays that the market subsequently confirmed. If the back-test finds nothing, the opportunity set question is answered. If it finds plays we missed, the back-test output becomes the first evidence base for the system.

---

*Version 2 -- revised June 18, 2026 after independent review.*
*Changes from v1: Rule 3 OR clause restricted to Buy-to-Sell only; Rule 5 cap raised to $1.50 with rationale; Rule 1 adds 5-day breakout exclusion; Rule 2 adds 21 DTE minimum; short interest reframed as squeeze warning; M&A risk added to protocol and exit rules; earnings history cap on conviction; estimate revision check added; puts sizing capped at 1 contract until track record.*
