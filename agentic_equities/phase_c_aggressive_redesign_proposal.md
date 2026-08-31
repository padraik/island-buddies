# Agentic Equities -- Phase C Redesign Proposal (Aggressive Activity)

*Drafted 2026-08-31 for Fable 5 pre-flight review, same pattern as the Rev 1 review that caught the mechanically-impossible exit design before Phase B ever went live (2026-07-21, see `data/agentic_equities/log.md`). Goal of this review: find what breaks, not rubber-stamp what's already decided.*

---

## 1. CONTEXT AND GOAL

Patrick's own words, verbatim, from the session that triggered this doc:

> "I want the money invested. I'm ok with risk. I want this active, aggressive. This is $300 I carved off to see what we can make happen with agentic trading. Let's start using the benefits that come with it. I understand we're risking real money, that's the point -- this agentic account can be more active than I am able to do manually so let's get active. Research, projections, best guesses... activity."

The trigger for this: as of 2026-08-31, the account (Robinhood 408976421, $300 seed, currently ~$299 total value) has been live under Phase B (real-money entries) since 2026-08-13 -- roughly 3 weeks, ~14-15 trading days. In that span it has found exactly **2** tradeable setups (ET on 2026-08-18, BILI on 2026-08-19), both already closed (ET flat -$0.90, BILI flat ~+$0.02), and has sat in **100% cash on every single firing since 2026-08-25**. Nobody built any "park idle cash somewhere safer while waiting" behavior into the original design -- it is a pure selective breakout scanner, and it has been selecting almost nothing. Patrick's instruction is not "fix the idle cash" in the sense of adding a yield sweep -- he explicitly wants **more real trading activity**, accepting more risk to get it. This doc proposes the specific mechanical changes to make that true, and flags the places most likely to break or produce a bad outcome, for Fable 5 to stress-test before any of it goes live.

**What this review needs to answer:** does this design actually produce more real trades without becoming reckless or mechanically broken, or does it just move the bottleneck somewhere else (see open questions in Section 4)?

---

## 2. CURRENT BEHAVIOR AND WHY IT'S BEEN IDLE

Full current prompt: `agentic_equities/prompt.md` in this repo (unchanged since 2026-08-19, per its own file history). The relevant mechanics, quoted exactly:

**Entry-scan frequency (Step 6):** "Phase B (new entries) runs ONLY if ALL of: breaker NOT tripped AND open position count... < 4 AND now_et.hour is 11 or 14 (the two designated entry-scan firings -- 9:35/10:35/12:35/13:35/15:35 ET firings NEVER originate new entries, they only run Steps 1-5)." The routine fires hourly, 7 times a day (9:35-15:35 ET) -- but only 2 of those 7 firings are even allowed to look for a new trade.

**Weekly cap (Step 6):** "If count >= 3 [BUY orders in trailing 7 days], skip Phase B this firing."

**Pathway 1 entry gate (Step 7), all required simultaneously:** market cap >= $2B; price $10-100; relative volume (10d) >= 1.5; RSI(14) between 55-80; ADX(14) >= 20; price > SMA50 > SMA200 (strict order); a Donchian(20) breakout above the *prior* 20-day high; a MACD bullish cross within the last 5 sessions. Eight independent conditions, all must pass. This is an AND, not a scored system -- one failure kills the whole candidate.

**Pathway 2 entry gate (Step 8):** only takes a candidate from Baxter's `passes.md` if it's noted as having *cleared* Rule 3 (near-zero Sell ratings, 60-day floor-freshness, 30-day ratings-momentum) -- a bar Baxter's own options-trading system sets deliberately high for real premium money, and one that in practice is rarely met (per this routine's own firing reports, e.g. 2026-08-19: "No ticker in the source is affirmatively documented as having cleared Rule 3 in the calls zone").

**Diagnosis:** the entry surface is throttled twice over -- only 2 of 7 daily firings can act, and even then the technical gate demands a textbook-perfect breakout on all eight measures at once. Pathway 2 almost never contributes because it's borrowing a bar built for a different, more conservative account. The result is exactly what's been observed: near-total inactivity that isn't a bug, it's the design working as originally specified for a *cautious* account -- which is no longer the mandate.

---

## 3. PROPOSED CHANGES

### 3.1 Entry-scan frequency: every firing, not 2-of-7

**Current:** `now_et.hour is 11 or 14`.
**Proposed:** remove the hour restriction entirely -- Phase B eligibility runs on every firing during market hours (all 7: 9:35, 10:35, 11:35, 12:35, 13:35, 14:35, 15:35 ET), subject to the same breaker/position-count/cap gates as today.
**Rationale:** this alone is the single biggest lever -- 3.5x more looks per day at the same underlying opportunity set.

### 3.2 Pathway 1: replace the all-8-AND gate with a scored, tiered gate

**Current:** all 8 conditions required, no partial credit.

**Proposed -- split into HARD requirements (unchanged, non-negotiable) and SOFT requirements (scored):**

- **HARD (still required, no exceptions):** market cap >= $2B; price $10-100; price > SMA50 > SMA200 (the actual trend-direction confirmation -- loosening this risks buying a stock that isn't actually in an uptrend, which defeats the strategy's whole premise, not just its caution level).
- **SOFT (scored, need 3-of-4 instead of 4-of-4):**
  - Donchian(20) breakout above the prior 20-day high (unchanged definition)
  - MACD bullish cross within the last **10** sessions (widened from 5)
  - ADX(14) >= **15** (lowered from 20)
  - Relative volume (10d) >= **1.2** (lowered from 1.5)
  - RSI(14) between **50-85** (widened from 55-80)

**Rationale:** keeps the structural "this is a real uptrend" confirmation as a hard floor (Fable 5 should specifically check this reasoning -- is SMA-order alone a sufficient trend confirmation, or does dropping the Donchian/MACD/ADX/relvol/RSI combination to 3-of-4 let through setups that are trending in name only?), while loosening the momentum/timing conditions that were most likely overfit to "perfect" setups rather than genuinely necessary. Take the highest-scoring candidate per firing, same as today's "choose at most one."

### 3.3 Position and order caps

**Current:** max 4 open positions; max 3 BUY orders per rolling 7 days.
**Proposed:** max **6** open positions; **remove the weekly BUY cap entirely**, relying on `spendable_cash` (Step 10's existing cap: "Cap cost to spendable_cash from Step 2") as the natural rate limiter -- once cash is deployed, no more entries are mechanically possible regardless of how many firings scan for them.

**Open question for Fable 5, flagged not resolved:** is removing the weekly cap outright correct, or does it just move risk from "too slow" to "front-loads all $300 into the first 1-2 qualifying days and then sits idle again for weeks"? An alternative worth stress-testing: a **daily** cap (e.g. max 2 new positions/day) instead of a weekly one or no cap at all -- paces deployment across the scanning surface instead of either extreme. Section 4 has more on this.

### 3.4 Pathway 2 (Baxter-sourced): loosen the admission bar

**Current:** only takes a `passes.md` name explicitly noted as Rule-3-cleared.
**Proposed:** also accept `passes.md` "Keep Watching" entries carrying documented conviction of 3/5 or higher, run through the exact same independent checks this routine already does (market cap, price band, earnings-proximity, sector correlation, 52-week-low freshness) -- the routine's own gates remain the real filter, this just widens what's eligible to reach them.

**Rationale:** the current bar borrows a threshold built for real options premium in a different account; for this account's more aggressive mandate, a documented 3+/5 idea that hasn't cleared every Island Fund gate is still a real, reasoned candidate, not noise.

**Explicitly NOT proposed:** treating passes.md entries below 3/5, or entries with no conviction score at all, as candidates. That would cross from "aggressive" into "fabricating signal," which the current prompt already correctly forbids ("never fabricate a Baxter-sourced candidate") and this proposal does not touch that line.

### 3.5 Sizing tiers: unchanged, flagged for discussion

**Current:** Tier A 15%, Tier B 25%, Tier C 35% of total_value per position.
**Proposed:** no change to the percentages themselves. More positions (3.3) was the chosen lever for "more active," not bigger single positions -- multiple moderate bets read as more in the spirit of "research, projections, best guesses... activity" (plural) than a few maximum-sized ones. Flagged here explicitly because Patrick said he's open to adjusting this too if Fable 5 or a live check-in decides bigger individual positions serve the goal better.

### 3.6 Circuit breaker: unchanged, deliberately

**Current:** breaker trips at total_value <= $195 (35% drawdown from the $300 basis); tripped state blocks all new entries until a human manually re-enables in an interactive session, never auto-resumed.
**Proposed:** no change. This was set with full awareness of the risk being taken and Patrick's instruction was to get more capital *working*, not to remove the floor underneath it. If Fable 5's analysis suggests the floor itself is now miscalibrated given more frequent/looser entries (e.g. faster to erode without a corresponding faster recovery mechanism), that's worth surfacing as a finding, but this proposal does not preemptively change it.

---

## 4. OPEN QUESTIONS FOR FABLE 5 -- STRESS-TEST THESE SPECIFICALLY

1. **Rate limiting after the weekly cap is removed (3.3).** Does the account risk fully deploying into 6 positions within the first day or two of loosened scanning, then sitting idle again for lack of cash -- the same "long idle stretches" complaint, just shifted? Is a daily cap (proposed alternative: 2/day) mechanically better, and if so what number actually paces deployment sensibly against a ~$300 account and 15%+ position sizes?
2. **The hard/soft split in 3.2.** Is "price > SMA50 > SMA200" alone a sufficient hard trend-confirmation floor, or does allowing 3-of-4 on the remaining conditions let through setups (e.g. no real breakout, stale MACD cross, weak relative volume) that are trending in name only? Should Donchian breakout also be hard, not soft?
3. **Tool-call load per firing with up to 6 open positions.** Step 5's exit management runs quote-plausibility, self-heal, R/ladder derivation, trend-break, time-stop, and earnings checks *per open position, every firing*. At 6 positions that's a meaningfully longer firing than today's near-always-empty book. Does this risk timeouts or incomplete firings, and should anything in Step 5 be batched or simplified to compensate?
4. **Correlation cap interaction.** Step 9's correlation cap (max 2 open positions sharing a sector) is unchanged in this proposal -- does it meaningfully constrain 6 simultaneous positions in a $300 account where the practical universe of $10-100, $2B+ names is already large, or is this a non-issue at this account size?
5. **Small-account mechanics.** With sizing tiers unchanged (15/25/35% of total_value) and total_value around $300, several simultaneous positions could each be 1-3 shares. Does bid/ask spread as a percentage of trade size become a real drag at this scale with more frequent trading, and if so does that argue for fewer, larger positions instead of the 6-position spread proposed in 3.3?
6. **Pathway 2's loosened bar (3.4).** Is 3/5 conviction from a system built for a different account and different instrument (options, not equities) a meaningful signal at all in this context, or does porting a lower tier of that bar risk laundering noise as signal just because it has a number attached?

---

## 5. EXPLICITLY NOT CHANGING

- Circuit breaker threshold and manual-only re-arm (Section 3.6).
- All of Step 5's exit mechanics (quote plausibility, self-heal, R/ladder, trend-break, time-stop, earnings-approaching) -- unchanged logic, just running more often as position count grows.
- `spendable_cash` as the hard ceiling on any single entry's cost (Step 10) -- this is the real backstop against over-deployment regardless of how many candidates qualify in one firing.
- Git-push reporting mechanism (Step 12) -- unchanged, every firing still gets a full report regardless of activity level.
- "Choose at most ONE candidate per firing" -- unchanged. More frequent firings is the lever for more trades, not multiple simultaneous entries in one firing.
- The never-fabricate-a-candidate rule on Pathway 2 -- unchanged and explicitly reaffirmed in 3.4.

---

## 6. WHAT'S BEING ASKED OF FABLE 5

Same shape as the original Rev 1 review: read this as an adversarial pre-flight check, not a confirmation. Specifically:

1. Does anything in Section 3 create a mechanically impossible or self-contradictory instruction (the Rev 1 review's original catch was a stop + ladder that literally could not both rest simultaneously on Robinhood -- looking for this class of error, not just strategy opinions).
2. Answer the six open questions in Section 4 with a real recommendation each, not just "worth considering."
3. Flag anything not raised here that should be, the same way the original review caught the RSI cap clipping the exact breakout days the strategy needed.
4. A bottom-line verdict: does this fly as specified, fly with specific changes (name them), or fail and need a different approach entirely?
