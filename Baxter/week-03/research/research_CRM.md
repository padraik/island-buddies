# CRM — Salesforce, Inc.
*Research file: June 16, 2026 | Analyst: Five-Baxter Panel*

> **CORRECTION — June 17, 2026:** Chain script bug (`expirations[:8]`) returned pricing from a short-dated expiry instead of Sep 18, 2026. All instrument data below has been corrected with verified Robinhood prices. Rules 1-4 remain valid. Rule 5 fails at all verified strikes. Rule 4 also fails independently: bear floor $215 (BMO Outperform, lowest confirmed Buy) is below any strike where Rule 5 could be satisfied. **No qualifying instrument exists. Do not enter.** Baxter independent analyses are preserved as written with original (erroneous) pricing.

---

## RAW DATA

| Field | Value |
|---|---|
| Ticker | CRM |
| Company | Salesforce, Inc. |
| Sector | Enterprise Software / AI CRM |
| Current price | $161.87 (Robinhood live, June 16, 2026) |
| 52-week range | $161.40 (low, set June 12, 2026) — $276.80 (high) |
| Distance from low | ($161.87 - $161.40) / ($276.80 - $161.40) = **0.4%** |
| Distance from high | -41.6% |
| Proposed instrument | **None** — no qualifying instrument under Iron Rules (see correction note) |
| Option ask | ~$14.55/share verified ($165C Sep 18, 2026, Robinhood) — original script reported $0.72 |
| At risk | N/A |
| Breakeven | N/A |
| Needs | N/A |
| Sep 18 expiry | 93 days out |

---

## FIVE IRON RULES

| Rule | Requirement | CRM | Status |
|---|---|---|---|
| 1 | Bottom 20-25% of 52-wk range | 0.4% from low | OK |
| 2 | Earnings catalyst before expiry | Q2 FY2027: Aug 26, 2026 | OK |
| 3 | Near-zero Sell ratings | 38 Buy / 12 Hold / 1 Underperform (B of A) | OK |
| 4 | Bear floor above breakeven | Bear floor ~$190 (excl. B of A Underperform) vs breakeven $168.22 | OK |
| 5 | Option ask ≤ $1.00 | Verified min ~$14.55/share ($165C Sep 18); no sub-$1.00 options visible on chain | **FAIL** |

---

## COMPANY OVERVIEW

Salesforce is the world's largest CRM platform. $11.1 billion Q1 FY2027 revenue (+13% YoY). Its current strategic pivot: Agentforce, an AI autonomous agent layer that sits on top of the Salesforce data platform and executes tasks — customer service, sales follow-up, account management — without human intervention. The bull case is that Agentforce accelerates Salesforce's growth by monetizing AI on top of existing subscriptions. The bear case is the opposite: AI agents displace the human workers who held the Salesforce seats, shrinking the addressable market.

---

## RECENT FUNDAMENTAL DATA

**Q1 FY2027 (reported May 27, 2026):**
- Revenue: $11.1 billion (+13% YoY, +12% constant currency)
- Non-GAAP EPS: $3.88 (+50% YoY) — record
- GAAP operating margin: 21.1%
- Non-GAAP operating margin: 34.8%
- Subscription & support revenue: $10.6B (+14% YoY)

**FY2027 guidance (full year):**
- Revenue: $45.8B–$46.2B (+10-11% YoY)

**Post-earnings stock reaction (May 27):**
- Beat on both top and bottom line by significant margins
- Stock continued to make new 52-week lows through June 12
- BMO Capital lowered target from $225 to $215, kept Outperform
- BMO commentary: *"results and guidance not likely sufficient to convince bears or bulls to switch sides"*

---

## ANALYST TABLE

| Analyst | Rating | Target | Bear floor eligible? |
|---|---|---|---|
| Bank of America | **Underperform** | $160 | No — Sell equivalent |
| BMO Capital | Outperform | $215 | Yes |
| Piper Sandler | Buy | $395 | Yes |
| Evercore ISI | Buy | $420 | Yes |
| JMP Securities | Buy | $430 | Yes |
| Consensus (37 non-BofA analysts) | Buy | $255 median | — |
| Range (non-BofA) | — | $190–$475 | — |

**Bear floor: $190** (lowest non-Underperform target in pool)
**Lowest confirmed Buy target: $215** (BMO Outperform)
**Breakeven: N/A** (no qualifying instrument; original $168.22 based on erroneous chain data)
**Buffer: N/A** (Rule 4 also fails: bear floor $215 is below any breakeven where Rule 5 could be satisfied)

---

## THE BEAR CASE — B OF A UNDERPERFORM NOTE (May 18, 2026)

Analyst Tal Liani reinstated coverage with Underperform at $160. Three pillars:

1. **Muted net new customer additions** — seat model approaching saturation in enterprise
2. **Limited upsell potential** — existing customers at spend ceiling
3. **Underwhelming AI monetization** — Agentforce pipeline converting too slowly to revenue; risk that AI agents replace seats before Agentforce revenue materializes

Stock was already down 41.8% from its April 2026 peak when this note dropped. The note did not cause the sell-off — it confirmed the bear narrative that was already in the stock.

---

## SELL-THE-NEWS RISK

CRM's Q1 FY2027 (May 27) was a **record quarter** by most metrics:
- +50% EPS growth
- 21% GAAP operating margin

The stock made new 52-week lows afterward. The market is not rewarding earnings beats. It is waiting for evidence that Agentforce revenue is ACCELERATING — not just growing, but accelerating faster than seat compression is shrinking. Any Q2 result that doesn't show that acceleration (even if it beats EPS consensus) risks repeating the May 27 pattern.

This is the core risk of the play. It is known and priced into the conviction level.

---

## INDEPENDENT ANALYSES

*Each Baxter reads the raw data and writes independently. No collaboration before the meeting.*

---

### BULLXTER

The stock is $161.87. The 52-week low is $161.40. It set that low on June 12 — four days ago — and has been bouncing between $162 and $170 since. The market has put its floor in. It took the best Q1 Salesforce has ever reported and made a new yearly low out of it. That is exhaustion, not momentum.

Thirty-eight analysts covering this stock think it goes to $190 or higher. The median target is $255. The gap between $162 and $255 is $93 — 57%. The entire Island Fund didn't make $93 per contract on its best trade. This is what maximum analyst-versus-price divergence looks like.

Agentforce is not pie in the sky. Q1 saw subscription revenue grow 14%. That is accelerating from prior quarters. The pipeline is converting. The B of A note is a data point, not a verdict — B of A had the same note on CRM in Q3 2024 and was wrong.

$0.72 for 93 days and a 3.9% breakeven. This is the instrument. Enter.

**Bullxter verdict: ENTER. $167.50C Sep 18.**

---

### BEARXTER

Let's talk about what the stock actually did.

Salesforce reported Q1 on May 27. Non-GAAP EPS up 50%. Revenue up 13%. By any measure, a beat. The stock went to a new 52-week low within three weeks. It is sitting right on that low right now. Record earnings + new lows = the market knows something the bulls don't.

What the market knows: seat compression is real. Agentforce is being deployed as a replacement for human agents, not as an addition. Every Agentforce deal that saves a company 10 human seats is 10 seats they're not paying Salesforce for anymore. The Q1 guidance confirmed this: 10-11% growth for FY27. For a company that grew 20%+ just two years ago, 10-11% is deceleration, not stabilization.

B of A has $160. The stock is $162. We're two bad days away from the bear floor being lower than our current price. If CRM prints a disappointing Q2 on August 26 — or even beats but guides conservatively — the stock could fall to $145-$150. Our $167.50C is worthless.

The post-earnings sell (August 27 morning) is 23 days before Sep 18 expiry. If the stock sells off on Q2 like it did on Q1, we have 23 days to recover or we lose $72. That is not a lot of time.

**Bearxter verdict: PASS. Pattern established. Market is not rewarding beats.**

---

### CALXTER

Running the numbers.

**Scenario analysis ($72 at risk):**

| Scenario | Probability | Stock outcome | Option value | Return |
|---|---|---|---|---|
| Q2 beats + Agentforce narrative flips | 30% | $185–$205 | $17–$37 | ~2,400% to ~5,000% |
| Q2 beats, muted reaction (same as Q1) | 40% | $160–$175 | $0–$7 | -100% to +870% |
| Q2 disappoints or guides down | 30% | $145–$160 | $0 | -100% |

**Expected value:**
- Scenario A: 0.30 × $25 (midpoint) = $7.50
- Scenario B: 0.40 × $2 (midpoint) = $0.80
- Scenario C: 0.30 × $0 = $0.00
- Total EV: $8.30 per contract vs. $0.72 cost → **positive 11.5x EV**

**Fractional Kelly (1/4):**
- Win probability roughly 40-45% (Scenarios A + partial B)
- Average win: $12-15
- Average loss: $0.72
- Kelly fraction: (p × avg_win - q × avg_loss) / avg_win → favors a bet
- At 1/4 Kelly: one contract ($72) is appropriate

Time-value note: With stock at $162 and breakeven $168.22, there's meaningful probability the stock touches $168+ at some point over 93 days even without the earnings catalyst. Any two-standard-deviation up day gets us there.

**Calxter verdict: ENTER. One contract. Kelly supports it.**

---

### MACXTER

Macro, political, and filing review.

**AI narrative split:** The market has bifurcated on AI. Infrastructure plays (NVDA, SMCI) are up. Implementers and users (CRM, MSFT, ADSK) have been punished. The thesis is: AI will commoditize enterprise software and compress margins. This ignores that enterprise AI REQUIRES a CRM data layer — Agentforce runs on Salesforce's proprietary customer data, which can't be replicated by a generic LLM. The moat is the data, not the interface.

**Macro risk:** Enterprise IT budgets have been under pressure since the tariff environment tightened in Q1 2026. However, Q1 CRM revenue grew 13% — budgets have not frozen for CRM. AI spending is being prioritized even as other IT spending is cut.

**Catalyst risk calendar (B/W Aug 26):**
- June 17: FOMC Warsh press conference — macro event, rates movement could affect growth stock sentiment
- August 26: CRM Q2 FY2027 earnings — the primary catalyst

**Insider activity:** No red flags surfaced. No Form 4 filings indicating executive selling pressure during the June 2026 low.

**FIFA/M3ter deals:** CRM announced partnerships with FIFA and acquired M3ter (usage-based billing) in the past 30 days. These are incremental, not thesis-changing. The market did not react to them. Relevant only as evidence that CRM is expanding its platform, not contracting.

**Macxter verdict: NEUTRAL / conditional ENTER.** No political or macro event overrides the thesis. FOMC on June 17 is a risk to growth stocks broadly. If 10-year yields spike significantly after Warsh's conference, revisit entry decision tomorrow. Otherwise, enter.

---

### BAXTER-PRIME

The system says enter. Every box is checked. The question is whether we trust the system when the market has already heard the good news and priced in pessimism anyway.

Here is what I keep coming back to: the market set a 52-week low on CRM four days after Salesforce posted the best Q1 in its history. That is not a company in trouble. That is a company whose narrative has gotten ahead of its fundamentals in the wrong direction. The data says $162. Thirty-eight analysts say $255. The gap between those two numbers is the trade.

Bearxter is right that the sell-the-news pattern is real. Q2 on August 26 might look like Q1 on May 27 — beat, stock falls. If that happens, we lose $72 and write it in the closed positions log. That is the risk. But the risk is $72, and the upside if the Agentforce narrative finally catches is a 20-30x on the option.

The exit rule is non-negotiable: sell at open August 27. We don't hold through a post-earnings fade. If the stock opens at $155, we sell. If it opens at $190, we sell. The system decides, not us.

One concern I'm flagging for the meeting: the B of A $160 target is $1.87 below current price. If the stock touches $160, B of A becomes the bear floor breaker. Rule 4 breach trigger should be: any stock close below $160 before Aug 26 → exit same day. Not a bear floor revision, just the stock validating the bear thesis.

**Prime verdict: ENTER. One contract. $167.50C Sep 18. Exit morning of August 27.**

---

## FIVE-BAXTER MEETING

*Held June 16, 2026*

**Attendance:** Prime (chair), Bullxter, Bearxter, Calxter, Macxter

**Bullxter opens:** Maximum analyst divergence from price. 38 Buy analysts at median $255, stock at $162. This is the Island Fund setup in its purest form.

**Bearxter responds:** The setup has been pure since May. The stock has been at the low and kept making new lows. Pure setup doesn't protect against a falling knife.

**Calxter:** EV is positive at 11.5x. Kelly supports one contract. The $72 at risk is defined. Scenario B (muted reaction) gives us partial recovery, not total loss.

**Macxter:** No macro override. FOMC tomorrow is a variable but doesn't invalidate the thesis. If yields move significantly, entry can wait until June 18.

**Bearxter presses:** What is the catalyst that changes the narrative? Q1 was a record and it didn't change it.

**Prime:** The Q2 catalyst is different. Q1 was measuring growth against expectations. Q2 is measuring Agentforce REVENUE ACCELERATION against the B of A thesis. If Agentforce revenue shows clear sequential acceleration in Q2, the market narrative flips from "AI is destroying CRM" to "CRM is monetizing AI." That flip is the trade. It either happens on August 26 or it doesn't. We're buying 93 days of time for $72 to find out.

**Bearxter:** And if it doesn't happen?

**Prime:** Then we lose $72 and the exit rule protects us from holding through a collapse. The rule was written before entry. It doesn't move.

**Vote:**
- Bullxter: Enter
- Bearxter: Pass
- Calxter: Enter
- Macxter: Enter (conditional on FOMC not creating major rate spike)
- Prime: Enter

**Result: 4-1 ENTER.**

---

## DECISION

**HOLD — No qualifying instrument. Do not enter.**

Rule 5 fails at all verified Sep 18, 2026 strikes. Additionally, Rule 4 fails independently: the bear floor ($215, BMO Outperform — lowest confirmed Buy) is below the breakeven of any option that could satisfy Rule 5. At the strike price where a Sep 18 option might cost under $1.00 (~$225+), the breakeven ($225+) exceeds the bear floor ($215). Both rules fail simultaneously — CRM cannot be structured as a qualifying trade under the Iron Rules at current pricing.

**Thesis conviction: 4/5 (thesis valid; no qualifying instrument exists)**

The underlying analysis (Rules 1-4) is sound except for Rule 4 interaction with Rule 5. CRM at 0.4% from its 52-week low with 38 Buy analysts and a Q2 FY2027 earnings catalyst is a textbook setup. The problem is the combination of high IV and a bear floor too close to current price. Watch list: revisit if IV drops materially, bear floor improves, or Oct 16 chain opens at better pricing.

---

## GLOSSARY

**Agentforce** — Salesforce's AI autonomous agent platform. Agents execute CRM tasks (customer service, sales outreach, billing follow-up) without human intervention, running on the customer's proprietary Salesforce data.

**Seat compression** — The bear thesis: AI agents replacing human workers who held enterprise software subscriptions, shrinking the addressable market for seat-based software like CRM.

**FY2027 / FY27** — Salesforce's fiscal year ending January 31, 2027. Q1 FY27 ended April 30, 2026 (reported May 27). Q2 FY27 ends July 31, 2026 (reports August 26).

**Non-GAAP EPS** — Earnings per share excluding stock-based compensation, amortization of acquired intangibles, and other one-time items. Salesforce's operating performance metric. Q1 FY27: $3.88.

**Bear floor** — Lowest price target from Buy/Outperform/Strong Buy rated analysts only. Hold and Sell targets excluded. CRM bear floor: ~$190 (lowest non-Underperform target in pool; lowest confirmed Buy is BMO Outperform at $215).

**Underperform** — Sell-equivalent rating from Bank of America. B of A's $160 target is excluded from bear floor calculation per Iron Rules methodology.

**IV crush** — Implied volatility compression that occurs after a scheduled earnings event, reducing option premium rapidly regardless of stock direction.

**Breakeven** — Strike price plus option premium paid. For $167.50C at $0.72: breakeven = $168.22. Stock must be above $168.22 at expiry for the trade to profit.

**Non-GAAP operating margin** — Operating income as a percentage of revenue, excluding stock-based compensation and amortization. Q1 FY27: 34.8% — Salesforce's highest ever.

**ARR** — Annual recurring revenue. The annualized value of Salesforce's subscription contracts. The key forward metric for subscription software businesses.

**Fractional Kelly** — Position sizing using 1/4 of the Kelly Criterion-optimal bet size to reduce variance. One contract ($72) is Calxter's recommended size.
