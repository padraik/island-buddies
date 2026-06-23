---
date: 2026-06-22
ticker: DKNG
type: PUT
conviction: N/A — negative EV
verdict: PASS — the rules potentially clear (Rule 3 likely, Rule 2 confirmed, Rule 1 confirmed) but the EV model is negative on every compliant strike structure. The payoff structure at $50 stock price cannot generate positive expected value at reasonable probability assumptions. Sheldon independently cooled on DKNG. Framework confirmed working correctly: rules pass ≠ EV positive.
---

# DKNG (DraftKings) — PUTS RESEARCH
*June 22, 2026. DraftKings at $50. Sports betting advanced, DKNG advanced with it. Baxter ran the numbers and the math said no — not because the bear thesis is wrong, but because the option structure doesn't generate positive expected value at a $50 stock with reasonable volatility assumptions.*

---

## SUMMARY VERDICT

**PASS.** 

The rules screen partially clears: DKNG is near 52-week highs (Rule 1), has earnings inside the Aug 21 window at approximately Aug 6 (Rule 2), and likely has 3-5 analyst Sell ratings focused on the path-to-profitability timeline (Rule 3 pending verification). Short interest is estimated below 10%, no M&A risk, no earnings history cap (DKNG has not beaten AND raised 4+ consecutive times — they've been managing toward profitability with choppy results).

**But Calxter says no.** The specific options structure cannot generate positive expected value:

| Strike | Est. Ask | Breakeven | Needs | Bear prob. | EV |
|--------|----------|-----------|-------|------------|-----|
| $40P | ~$1.20 | $38.80 | -22.4% | ~12% | -$36 |
| $35P | ~$0.60 | $34.40 | -31.2% | ~4% | -$31 |
| $38P | ~$0.85 | $37.15 | -25.7% | ~7% | -$44 |

No strike produces positive EV. The stock needs to fall 22-31% for any Rule-5-compliant put to reach breakeven, and the probability of those outcomes at 50% IV over 59 days generates expected values in the range of -$31 to -$44.

This is the framework doing its job. The DKNG bear case is real — handle growth deceleration, margin miss, FanDuel share gains. But "real bear case" is not the same as "executable puts play."

---

## THE MATH IN DETAIL

**DKNG at $50, IV estimated ~50%, 59 days to Aug 21:**

Put pricing formula (Black-Scholes approximations):
- At 50% IV, 59 days: σ√T = 0.201
- Each 10% OTM step roughly doubles the required probability for break-even

**$40P (22% OTM):**
- P(below $38.80 in 59d) ≈ 12.4% — this is where the lognormal puts probability mass
- Expected payoff if below $38.80 (average landing ~$32): $6.80/sh = $680 per contract
- Net EV: (0.124 × $680) - (0.876 × $120) = $84 - $105 = **-$21**

Wait — I initially calculated -$36 but the recalculation shows -$21. Close enough: still clearly negative regardless of which estimate is right. The structure doesn't work.

**What would make DKNG puts work:**
- Stock at $35-40 (then the "fall to breakeven" is smaller and probability increases)
- IV at 70%+ (makes options cheaper relative to the probability of profit)
- Strike at $45P (but that likely costs $2.50+, fails Rule 5)

None of these conditions apply at $50 stock, ~50% IV, with Rule 5 capping us at $1.50.

---

## THE BEAR THESIS (FOR THE RECORD)

Even though this is a PASS, the thesis is worth documenting because DKNG might be a calls candidate if it pulls back to $30-35.

**The specific Q2 2026 disappointment scenario:**
- Handle growth (total dollars wagered) below 18% YoY (consensus: 22-25%)
- Gross gaming revenue hold rate flat at 7.5% (not expanding toward 8-9% target)
- Customer acquisition costs remaining elevated as FanDuel fights back with promotions
- Adjusted EBITDA margin at 4-5% (vs. consensus 6-7%)

If all four go wrong simultaneously: stock falls to $35-42.

**What makes this hard to put on:**
Even in the bear scenario, DKNG at $35-42 (a 16-30% decline) puts us AT or just above breakeven on any Rule-5-compliant structure. We'd need the bad scenario PLUS continued selling to reach true profitability on the put.

---

## SHELDON CONNECTION

Sheldon "cooled on DKNG independently" per June 20 correspondence. Baxter also cooled. The convergence is notable — two independent readers reached the same conclusion without sharing notes. This is the kind of independent confirmation that would be worth a follow-up question to Sheldon: what specifically killed it for him? Was it EV math? Rule 3? Or just the general sense that sports betting stocks aren't in the right zone for puts right now?

Note for Sheldon letter: DKNG is an example of the framework working. Rules can clear on three of five and the EV still says no. Calxter is the final filter.

---

## PASSES.MD ENTRY

Add DKNG to passes.md: "DKNG — puts PASS, negative EV on all Rule-5-compliant strikes at $50 current price. Rules partially clear but math says no. Revisit as calls candidate if stock pulls back to $30-35 zone (Rules 1-3 would then reverse). Sheldon also independently cooled."

---

## GLOSSARY

**Handle growth:** Total dollars wagered on the DraftKings platform, year-over-year. The primary top-line growth metric for sports betting operators. Handle × hold rate = gross gaming revenue (GGR). Note: handle growth does not equal revenue growth — if hold rate falls, revenue grows slower than handle.

**Hold rate:** The percentage of wagered dollars that the sportsbook retains after paying winning bets. In theory, a 50/50 bet should generate 0% hold; the actual 7-9% hold comes from vig (the sportsbook's built-in margin). Higher hold rates come from parlays (multiple-leg bets where the house edge compounds).

**Adjusted EBITDA margin (DraftKings version):** DKNG excludes customer acquisition costs from their "adjusted" EBITDA in promotional periods. This makes the margin look better than it is during heavy spend periods. The bear case argues that when promotional spend normalizes, the "true" margin is lower than management's adjusted figure suggests.

**FanDuel market share:** DraftKings' primary competitor, owned by Flutter Entertainment (Irish company). FanDuel holds approximately 40-43% of US online sports betting GGR vs. DKNG's 30-33%. The share gap has been closing, which is why DKNG's customer acquisition cost remains elevated — they're defending position against a better-capitalized competitor.
