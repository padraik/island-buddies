# IRON RULES -- CALLS
*Apply to every call entry. Not suggestions.*
*Written June 1, 2026. Sizing framework revised June 20, 2026.*
*See week-03/story/five_baxters_sizing_debate_jun19.md for the reasoning behind the sizing revision.*

---

## THE FIVE RULES

**Rule 1: Stock within the bottom 20-25% of its 52-week range.**

The entry signal is price dislocation, not value. A stock within 20-25% of its annual floor has been actively rejected by the market. That rejection is the setup. A stock in the middle of its range or near its high has no such thesis -- the market has already assigned it a fair price and we have no edge arguing otherwise.

We are not buying stocks we think are good. We are buying catalysts in stocks the market currently thinks are bad.

*Pass: stock price is within 20-25% of its 52-week low.*
*Fail: stock is more than 25% above its 52-week low.*

---

**Rule 2: Confirmed earnings catalyst before expiry.**

No substitutes. Not product launches, not FDA decisions, not analyst day presentations, not macro events. Earnings is the only event that forces the market to reprice a stock against actual data on a specific day. Everything else is a narrative event -- it can move the stock or it can not move the stock, and the market tends to price narrative events before they happen.

Themes without data mechanisms are dead money. The BOTZ rule: if there is no specific date on which something true is revealed, there is no trade.

*Pass: confirmed earnings date falls before option expiry.*
*Fail: no confirmed earnings date inside the window, or earnings falls after expiry.*

---

**Rule 3: Near-zero Sell or Underperform ratings in the covering analyst universe.**

Analysts who cover a stock have full access to management, channel checks, and sector data that retail does not. If credentialed professionals who have done this work all rate a stock Buy or Better, and the stock is at a 52-week low, the market has made a pricing error that professional research does not support. Near-zero Sells means the floor is a consensus floor -- the most pessimistic professional opinion is still bullish.

If Sell ratings exist, there is credentialed bearish analysis to account for. Two or more Sells is a fail. One Sell is not automatic disqualification but it reduces conviction and activates Rule 4 scrutiny on the Sell analyst's target.

*Pass: zero or one Sell/Underperform rating in the covering universe.*
*Fail: two or more Sell/Underperform ratings.*

---

**Rule 4 (Bear Floor): The lowest price target among Buy-rated analysts must be ABOVE the call breakeven.**

Call breakeven = strike price plus premium paid.

*Example: $65C at $0.38 → breakeven $65.38. The most pessimistic bull on the Street must still believe the stock will reach $65.38. If the lowest Buy target is $60, the trade does not work even from the favorable end of professional consensus.*

Rule 4 is structural: it means the play fails if the stock does something less than what the most cautious professional bull already expects. The bear floor is not a price target -- it is the minimum threshold the thesis must clear.

Rule 4 is monitored throughout the hold period, not just at entry. If the bear floor drops below breakeven after entry, exit same day. No waiting for the next morning.

*Pass: lowest Buy/Outperform/Strong Buy target is above call breakeven.*
*Fail: lowest Buy target is at or below call breakeven, or no Buy ratings exist.*

---

**Rule 5: Option ask at or below $1.00 per share.**

The chain quality filter. One dollar per share = one hundred dollars per contract = maximum loss is knowable and bounded per contract. This is not a position sizing rule -- it is a gate on whether the chain is viable.

The $1.00 cap does two things simultaneously. It keeps the loss ceiling defined. And it filters out high-IV names where the only sub-$1.00 options are so far OTM that the breakeven requires a move past every analyst's target. When a beaten-down stock has cheap near-money options, that is a structurally favorable setup. When the only accessible options require 40% moves, the chain is broken regardless of the thesis.

If no instrument in the chain passes both Rule 4 and Rule 5 at the same strike, the play fails. Rule 5 does not get waived to make a good thesis work.

*Pass: option ask ≤ $1.00/share on an instrument that also passes Rule 4.*
*Fail: no such instrument exists in the chain.*

---

## POSITION SIZING
*Adopted June 20, 2026. See week-03/story/five_baxters_sizing_debate_jun19.md.*

Position size is a **percentage of current reserve at time of entry**, not a fixed dollar amount. A fixed dollar bet on a growing fund accumulates but does not compound. The bet size must scale with the bankroll or the fund never realizes the leverage of its own track record.

**Sizing table:**

| Conviction | Range | Standard |
|---|---|---|
| 3.5/5 | 6–10% of reserve | 8% |
| 4/5 | 12–16% of reserve | 14% |
| 5/5 | 17–20% of reserve | 19% |

**Contract count** is derived from the sizing budget:

> contracts = floor(sizing budget ÷ (ask × 100)), minimum 1

Adding a contract is not a separate decision. If the budget supports a second contract, it enters. If it does not, it does not. The conviction score determines the budget. The budget determines the contracts.

**Intra-score confidence** sets where within the tier you land. Two plays can both score 4/5 and not be the same play. A play where every rule passed with significant margin goes to 15–16%. A play where one rule barely cleared or supporting data required revision at any point goes to 12–13%. This is a judgment call made at entry and documented in the research file with one sentence of explanation.

**Correlated position cap:** Total reserve deployed to plays sharing the same primary macro driver may not exceed 35%. When correlated exposure already sits at or above 35%, any new play in the same theme sizes at the bottom of its conviction range regardless of intra-score confidence. Document the correlated exposure at entry.

**Hard caps:**
- Single play: never exceeds 20% of current reserve, regardless of conviction
- No averaging down: if the stock moves against the thesis after entry, hold the existing position or exit per exit rules. Do not add contracts.

---

## EXIT RULES

**Primary:** Sell at market open the morning after earnings, regardless of direction. The catalyst has fired. The thesis has resolved. Hold past that point is speculation, not a thesis.

**Rule 4 live breach:** If the bear floor drops below call breakeven at any point after entry, exit same day. No waiting.

**Rule 3 deterioration:** If the analyst consensus reaches two Sell ratings after entry, evaluate same day. Does not automatically trigger exit but requires documented re-evaluation.

**Pre-earnings profit target:** If the stock reaches the bear floor price before earnings, evaluate same-day exit. The thesis has resolved early. Holding through a binary event to extract the last increment of gain introduces risk that was not priced at entry.

**BOTZ watch:** If the play is not trending toward breakeven within two weeks of expiry, the theme lacks a data confirmation mechanism. Evaluate exit to recover remaining time value rather than donating it to theta.

---

## CONVICTION SCORING

**5/5:** All five rules pass with margin. Catalyst structure is clean -- single confirmed binary date, unambiguous inside the window. Bear floor materially above breakeven. No data corrections required during research. Near-unanimous analyst consensus with no outliers.

**4/5:** All five rules pass. One or more rules cleared with limited margin, or catalyst structure has a complicating factor (two potential dates, event dependent on a prior result, etc.). Bear floor above breakeven but not by a wide margin.

**3.5/5:** All five rules pass. A notable margin concern, a single data point that required correction, or a Rule 3 outlier (one Sell rating present). Viable, but sized at the low end.

**Below 3.5/5:** Does not enter the fund.

---

## GLOSSARY

**Bear floor:** The lowest price target held by analysts who currently rate the stock Buy, Outperform, or Strong Buy. Hold and Sell targets are excluded. If the bear floor is below the call breakeven, Rule 4 fails and the trade is dead regardless of other factors.

**BOTZ rule:** Themes without catalysts -- without a specific date on which something true is revealed -- are dead money. Named for a robotics ETF that Sheldon's fund held as a macro theme without a catalyst mechanism. The position bled slowly until the exit. Themes are not trades.

**Breakeven:** The stock price at which the position returns exactly $0. Equal to strike plus premium paid. A $65C at $0.38 has a breakeven of $65.38.

**Call option:** A contract giving the right to buy 100 shares at the strike price. Gains value as the stock rises above the strike. Worthless at expiry if the stock is at or below the strike.

**Compounding vs accumulating:** Compounding means bet size grows proportionally with the fund. Accumulating means a fixed dollar bet stays the same while the fund grows around it. A $100 bet on a $500 fund is 20%. The same $100 bet on a $5,000 fund is 2%. Fixed-dollar sizing accumulates. Percentage-of-reserve sizing compounds.

**Conviction score:** Internal rating (3.5, 4.0, or 5.0 out of 5) of how cleanly the Five Iron Rules case holds. Drives the sizing tier. Intra-score confidence drives where within the tier you land.

**Correlated position risk:** When multiple open positions share the same primary macro driver, a negative event in that driver hits all of them simultaneously. Total correlated exposure is capped at 35% of reserve to prevent effective concentration disguised as diversification.

**Fractional Kelly:** Position sizing derived from the Kelly criterion but reduced to account for uncertainty in the edge estimate. Full Kelly maximizes long-run geometric growth but assumes the edge estimate is accurate. With a small sample size (fewer than 30 closed plays), the edge estimate is unreliable and full Kelly sizing produces unacceptable variance. The sizing table above represents approximately quarter-to-half Kelly at typical edge assumptions.

**Intra-score confidence:** The qualitative assessment of how cleanly a play scored within its conviction tier. Two 4/5 plays are not the same play if one passed every rule with significant margin and the other barely cleared one rule and required a data correction. Intra-score confidence sets where within the 12–16% range a 4/5 play lands.

**52-week range position:** Where the current stock price sits within the range from the 52-week low to the 52-week high. Expressed as a percentage: 0% means at the 52-week low, 100% means at the 52-week high. Rule 1 requires the stock be in roughly the bottom 20-25% (0–25% of range).
