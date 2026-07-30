# FABLE 5 BRIEF: Should Rule 5 (Chain Filter) scale with fund size?

*Prepared Jul 30, 2026. Michael asked for this to go to a full premium-reasoning pass rather than get resolved on the spot — it could change a standing Iron Rule and the current shape is a real, live design gap, not a hypothetical. Meets the Model Cost Awareness bar ("Analysis whose output could change a standing rule").*

---

## THE QUESTION

Tab 1 Rule 5 currently reads: **"Option ask at or below $1.00/share."** Flat dollar figure, unchanged since the rules were written in early June, never revisited even after the Jul 10 audit rewrote Rules 4 and added Rule 6.

**Should Rule 5 change as the fund's reserve grows — and if so, to what — so the fund isn't structurally locked into far-OTM, high-required-move contracts even once it can genuinely afford better-shaped trades?**

This needs a recommendation with specific proposed wording for Tab 1, not just a discussion of tradeoffs.

---

## WHY THIS SURFACED TONIGHT (concrete trigger, not theoretical)

Screening DIS for entry (Jul 30), the live Aug 21 chain showed:

| Strike | Ask | Required move | Rule 5 status |
|---|---|---|---|
| $101C | $1.94 | +7.2% | **BLOCKED** (over $1.00) |
| $102C | $1.62 | +7.9% | **BLOCKED** |
| $103C | $1.44 | +8.8% | **BLOCKED** |
| $105C | $0.87 (actual fill) | +10.1% | OK |

The $101C needed a third less movement to pay off than the contract we actually bought — Rule 5 excluded it purely on price, with no reference to whether the fund could afford it or whether it was the better trade.

**The surprising finding, checked before writing this brief:** Tab 3's position-sizing math (percentage of reserve, tiered by conviction) can *already* afford the $101C today. At $1.94/contract = $194 at risk, a 5/5-conviction play (17-20% of reserve) fits inside that dollar amount at the fund's *current* ~$913 reserve. Rule 5's flat cap — not fund size, not the sizing tiers — is the actual wall. This means "wait until the fund is bigger" may be the wrong frame entirely; the real question might be whether Rule 5 should key off conviction tier rather than (or in addition to) reserve size.

## SECOND DATA POINT: THE SAME EFFECT ON EXPIRY

From tonight's ZG re-screen, same strike, different expiry, same underlying:

| Expiry | Strike | Ask |
|---|---|---|
| Aug 21, 2026 (21 DTE) | $45C | $0.75 |
| Nov 20, 2026 (112 DTE) | $45C | $3.40 |
| Dec 18, 2026 (140 DTE) | $45C | $3.90 |

Same pattern: a flat $1.00 cap doesn't just push toward far-OTM strikes, it also structurally excludes almost every longer-dated expiry on almost every underlying, regardless of whether a farther-out catalyst window might sometimes be the better trade (more time for a thesis to play out, less forced-exit risk from a single binary print).

---

## RELEVANT STANDING RULES (for Fable 5 to work within, not around)

- **Tab 1, Rule 5:** the rule under review. Currently flat $1.00/share.
- **Tab 3, Sizing:** 3.5/5 = 6-10% of reserve (8% standard); 4/5 = 12-16% (14% standard); 5/5 = 17-20% (19% standard). Contracts = floor(sizing budget ÷ (ask × 100)), minimum 1. Hard cap: single play never exceeds 20% of reserve.
- **Tab 1, Rule 6 (Reachability):** required move ≤ 1.5x the stock's own real median earnings-day move. Note the interaction: pricier, closer-to-the-money contracts need a *smaller* move, which makes Rule 6 easier to pass — so loosening Rule 5 could mechanically increase the fund's hit rate on Rule 6, which is worth quantifying, not just asserting.
- **Correlated cap:** 35% of reserve per macro bucket.
- **The fund's core philosophy** (stated repeatedly across the binder and story docs): small stakes, asymmetric/leveraged payouts, "the math doesn't care that we're in high school." A cheap, far-OTM contract is *more* leveraged (bigger % return per $ of stock move) than a near-the-money one. Rule 5 currently enforces that leverage philosophy as a side effect of its price cap — any restructure has to say explicitly whether it's preserving, weakening, or consciously trading off that leverage for a higher hit rate.

---

## FUND GROWTH CONTEXT (as of Jul 30, 2026)

- Total contributions: $934 ($200 seed + $300 Michael's dad + $434 Michael).
- Current cost basis: $1,090. Current reserve: $912.96 (post-DIS fill). Two open positions (LYFT $90, DIS $87.04).
- Two-month return: +17.2% at mark — but heavily carried by one outlier (DKNG +$251); flagged in-session as not a stable rate, not something to extrapolate on its own.
- Realized P&L breakdown available in `Baxter/positions.md` CLOSED POSITIONS table — 13 closed plays, mix of wins and losses, real dollar figures for every one.

## AVAILABLE DATA FOR BACKTESTING

- `Baxter/positions.md` — full closed and open position history with real fill prices.
- `Baxter/data/contract_history/` — real daily candle pulls for contracts still live when archiving became standing protocol (Jul 13 onward): ABT (closed), LYFT (ladder partial), plus raw pulls from Jul 13. **DKNG, DSGX, CHWY histories are permanently gone (expired before the archiving protocol existed) — do not attempt to reconstruct them.**
- `week-06/research/fable5_consult_profit_taking_jul13.md` — prior Fable 5 pass on real candle data, useful as a methodology reference (how that analysis validated the scale-out ladder against real counterfactuals) even though it answered a different question.
- Live chain-pulling capability (`fetch_options_chain.py TICKER`) if Fable 5's context includes tool access and wants fresh comparison data on closer-to-money or longer-dated strikes for any currently-open or recently-closed name.

---

## CANDIDATE STRUCTURES (evaluate all, don't just pick one to defend)

1. **Status quo.** Flat $1.00 cap regardless of reserve or conviction. Baseline to beat.
2. **Reserve-scaled cap.** e.g., ask ≤ some function of reserve (with a floor so it never gets *more* restrictive than today). Needs a specific formula proposal, not just "scale it."
3. **Milestone-tiered cap.** Flat steps: $1.00 under $X reserve, $2.00 under $Y, etc. Needs specific dollar milestones, justified by sizing math like the DIS example above, not round numbers picked by feel.
4. **Conviction-linked cap.** Since Tab 3 already prices risk by conviction tier, let the ask cap vary by tier (e.g., 3.5/5 stays at $1.00, 4/5 and 5/5 get a higher ceiling) — this directly addresses tonight's finding that sizing math, not reserve size, was the real gate.
5. **Required-move-linked selection (replace price cap with an outcome cap).** Instead of capping ask price directly, let strike selection float and instead require the resulting required-move to sit under some ceiling — Rule 6 already does something like this; consider whether Rule 5 should be folded into Rule 6 rather than existing as a separate price gate.
6. Any hybrid or better structure Fable 5 identifies that isn't listed above — this list is a starting menu, not an exhaustive one.

For each candidate: what would it have changed on the fund's actual 13 closed positions and 2 open ones, does it preserve or erode the leverage philosophy, and is it simple enough for Baxter to apply mechanically mid-session without a judgment call every time.

---

## DELIVERABLE WANTED

A specific, ratifiable recommendation — exact proposed Tab 1 Rule 5 wording, the reasoning, and what (if anything) should happen immediately vs. what should wait for a specific future milestone. Written so it can go straight into a ratification decision the way the Jul 10 audit amendments did, not a menu Michael has to further distill himself.
