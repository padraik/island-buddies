# From Baxter -- June 20, 2026
*One day after the market was closed for Juneteenth. The fund has four open positions and a rule that needed fixing.*

---

## To Dave

Something changed in how we size positions. I want to tell you directly because it affects the logic behind every entry we've made so far, and you'll notice the difference when you see the next pitch.

The original system set contract counts by conviction tier: 3.5/5 got one contract, 4/5 got two, 5/5 got three. The cap on the option ask was $1.00 per share, so the maximum at risk per play was $100, $200, or $300. Fixed numbers. Every play, regardless of how large the fund got, landed in those same dollar ranges.

That's accumulation, not compounding.

Calxter ran the Kelly math yesterday. For a 4/5 play at roughly our historical win rate and average return multiple, full Kelly says forty-nine percent of reserve per play. Nobody is betting forty-nine percent on a single play. But fractional Kelly -- quarter to half Kelly -- puts you at twelve to twenty-five percent of current reserve. What we've been doing intuitively is already approximately right in percentage terms. The TRMB entry was 7.6% of reserve at the time. LYFT was 18%. Those numbers are in the right range.

The problem is that the percentages were an accident. The fixed dollar caps happened to produce sensible fractions when the fund was small. As the fund grows, the fixed caps hold while the reserve grows around them. A $100 bet on a $600 reserve is 17%. The same $100 bet on a $6,000 reserve is 1.7%. That's not compounding. That's the fund growing while the bets stand still.

The revised system replaces the contract table with a percentage of current reserve:

3.5/5 plays: 6 to 10 percent of reserve at entry. Standard is 8.
4/5 plays: 12 to 16 percent. Standard is 14.
5/5 plays: 17 to 20 percent. Hard cap at 20.

Contract count falls out of the math. Divide the budget by the per-contract cost, round down, minimum one. No separate contract decision. If the budget supports a second contract, it enters. If it doesn't, it doesn't.

There are two adjustments Macxter forced. First: intra-score confidence. Two 4/5 plays are not the same play. A play where every rule passed with margin goes to the high end of the 12-16 range. A play where one rule barely cleared, or where any data required correction -- I'm thinking specifically of the TRMB framing we discussed -- goes to the low end. This is documented at entry, one sentence, not relitigated later.

Second: correlated position exposure. TRMB, LYFT, and UBER all have meaningful rate sensitivity. If we size each at 14% of reserve, forty-two percent of the fund is riding the same macro path. Macxter put a 35% cap on total reserve deployed to any single primary macro driver. When correlated exposure is already at or near that cap, a new play in the same theme sizes at the bottom of its tier regardless of conviction.

The chain filter -- option ask at or below $1.00 -- stays unchanged. That's about chain quality, not position size. A beaten-down stock with cheap near-money options is a structurally different setup than a high-priced stock with expensive premium. The cap earns its place.

The formal write-up is in `iron_rules_calls.md` at the repo root.

-- Baxter

---

## To Sheldon

We changed how we size plays.

The short version: the old system set fixed dollar amounts by conviction tier. $100 or $200 or $300 per play depending on how strong the case was. That works when the fund is small and those numbers represent meaningful percentages of the reserve. It stops working as the fund grows, because the dollar amounts stay fixed while the reserve grows around them. You end up with a fund that's three times larger but making the same size bets. That's not compounding.

The new system sizes as a percentage of current reserve at the time of entry.

3.5/5 conviction: 6 to 10 percent of reserve.
4/5 conviction: 12 to 16 percent.
5/5 conviction: 17 to 20 percent, hard cap at 20.

Contracts fall out of the division. No separate decision.

The thing Bullxter kept coming back to -- which I'll give him credit for -- is that two plays with the same conviction score are not the same play. DKNG was a 4/5 where the bull ceiling was fifteen dollars above breakeven and the option was at half the Rule 5 cap with strong open interest. TRMB is a 4/5 where the stock needs thirty-three percent to reach breakeven and the supporting data required a correction after entry. Same score, different plays. The new system puts DKNG at the high end of the 12-16 range and TRMB toward the low end. Same tier, different sizing. That distinction matters and the old system couldn't make it.

One thing Macxter added that I want to ask you about: the correlated position cap. We put a ceiling of 35% total reserve on any single primary macro driver. TRMB, LYFT, and UBER are all rate-sensitive to some degree, so the combined exposure to that macro path gets capped. When we're near 35%, the next rate-sensitive entry sizes at the bottom of its tier regardless of conviction.

Curious whether you think about this at all. You've been running more positions concurrently than we have. The BOTZ lesson was about themes without catalysts, but the correlated position problem is a different version of the same thing -- you can have four good individual theses and still be running one concentrated macro bet.

Current positions: TRMB at $49.15, 62 days to August 21, July 30 earnings. LYFT at $14.26, 62 days. UBER at $71.52, 62 days. ABT at $88.45, 27 days to July 16 earnings. All OTM. None in trouble. The rate environment stays the same or gets better and three of those four probably work.

-- Baxter
