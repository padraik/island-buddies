# Fable 5 Verdict -- Phase C Aggressive Redesign (2026-08-31)

*Adversarial pre-flight review of `phase_c_aggressive_redesign_proposal.md`, run at Patrick's explicit request on Fable 5. Same mandate as the Rev 1 review (2026-07-21): find what breaks before real money finds it.*

---

## VERDICT: FLIES WITH SPECIFIC CHANGES

The core direction is sound -- the observed inactivity is correctly diagnosed (a 2-of-7 firing gate stacked under an 8-condition AND), and the chosen levers (scan frequency, scored gate, more slots) are the right ones. But the proposal as written contains one self-contradictory instruction, one genuine mechanical hole that hourly scanning converts from theoretical to near-certain, and one statistical bias that explains part of the historical inactivity and changes how the new gate should be structured. Deploy only after the changes below.

---

## MECHANICAL CATCHES (Rev-1 class -- these block deployment as-written)

### C1. The routine can buy a stock it already owns, and hourly scanning makes this near-certain. **[BLOCKING]**

Nothing in the current prompt or the proposal excludes **currently-held symbols** from either pathway's candidate list. Under the old design this hole was masked: entry scans ran twice a day, the weekly 3-buy cap throttled everything, and the book was almost always empty. Under Phase C, a breakout that wins the 9:35 scan will very likely still be the top-scoring candidate at 10:35, 11:35, and 12:35 -- a Donchian breakout doesn't un-happen intraday. The routine would re-buy the same name firing after firing, silently pyramiding one position to 2-4x its tier size while the report shows "chose the strongest candidate" each time, technically true and completely wrong. Same family as the Rev 1 stop+ladder catch: each step is individually valid, the combination is broken.

**Fix (required):** in Step 9's shared filters, add: *exclude any symbol with a current open position in this account.* One sentence, closes the hole entirely.

**Related, strongly recommended:** a re-entry cooldown -- no entry into any symbol this account exited within the trailing 5 trading days. Without it, a trend-break exit at 10:35 can be re-bought at 11:35 if the daily indicators still qualify (they will -- trend-break triggers on close-below-EMA20 + RSI<45, while entry qualifies on SMA order + soft score; both can be true the same day on a whipsaw). This is the churn scenario that turns spread costs and whipsaws into the account's main activity.

### C2. The proposal's soft gate says "3-of-4" but lists five conditions. **[BLOCKING -- spec bug]**

Section 3.2 enumerates five soft conditions (Donchian, MACD-10, ADX>=15, relvol>=1.2, RSI 50-85) under a "need 3-of-4" rule. An unattended routine handed this will improvise a resolution, and unattended improvisation on entry criteria is precisely what this system is designed to never do. The fix is not just editorial -- see C3 for which way to resolve it.

### C3. With Donchian soft, the strategy stops being trend-following. **[BLOCKING -- resolves C2]**

Under 3-of-5, a candidate passes on {ADX>=15, relvol>=1.2, RSI 50-85} alone -- no breakout, no MACD cross. That describes a large fraction of any bull-market universe: mildly active stocks drifting upward. The Donchian breakout is not one momentum indicator among five; it is the *entry trigger* -- the event that says "the move is starting now." Trend-following without an entry trigger is just buying beta with extra steps, and the "highest-scoring candidate" tiebreak can't rescue it because dozens of drift names will tie.

**Fix (required):** promote Donchian to HARD. Final gate:
- **HARD:** market cap >= $2B; price $10-100; price > SMA50 > SMA200; **Donchian(20) breakout above the prior 20-day high**.
- **SOFT (need 2-of-4):** MACD bullish cross within 10 sessions; ADX(14) >= 15; relative volume >= 1.2; RSI(14) 50-85.

This resolves the 3-of-4/five-items bug, keeps the strategy's identity intact, and is still dramatically looser than today (where all four soft conditions were mandatory at tighter thresholds).

### C4. Morning firings structurally can't pass the relative-volume condition -- and this partly explains historical inactivity. **[insight, shapes the design]**

The scanner's relative volume compares *today's cumulative volume so far* against a trailing full-day average. At 9:40am even a genuinely hot stock has traded a fraction of an average day -- relvol >= 1.5 at that hour requires an explosive open, and relvol >= 1.2 is still biased heavily against morning hours. Under the old design relvol was mandatory, which quietly disadvantaged the 11am scan (one of only two entry windows) and is consistent with the observed record: the account's only Pathway 1 entry (ET) came from the 2:41pm firing with relvol 1.52. This is the same class of finding as Rev 1's "RSI cap clips the exact breakout days the strategy needs."

**Implication:** the scored gate fixes this naturally -- a morning candidate can pass 2-of-4 via MACD+ADX or MACD+RSI without relvol -- but only if relvol stays SOFT. Do not be tempted to harden it later "because volume confirms breakouts"; at hourly granularity the metric doesn't measure what it claims until mid-afternoon.

### C5. Settlement / good-faith-violation check: verified safe as designed. **[no change needed -- recording the verification]**

Aggressive turnover in a **cash account** raises the good-faith-violation question (buy with unsettled proceeds, sell before they settle; three GFVs = 90-day restriction). Verified: the existing `spendable_cash = cash - unsettled_funds` mechanic means the routine only ever buys with settled cash, which makes a GFV mechanically impossible regardless of turnover; and PDT rules don't apply to cash accounts at all. This invariant is load-bearing under Phase C in a way it never was before -- add one line to the prompt naming it as deliberate ("spendable_cash excludes unsettled proceeds; this is the GFV guard, never bypass it") so a future edit doesn't optimize it away as redundant.

---

## THE SIX OPEN QUESTIONS -- ANSWERS

**Q1 (rate limiting): daily cap of 2 new positions/day. Not zero cap, not the weekly 3.**
Removing all caps doesn't create sustained activity -- it creates one deployment event. With 7 scans/day and a loosened gate, all 6 slots could fill in a single hot session, and 6 entries drawn from one tape are one regime bet wearing six tickers; the sector cap only partially helps because momentum days cluster across sectors. A 2/day cap forces deployment across >= 3 distinct trading days (time diversification of entries -- the one free diversifier available), still reaches full deployment within a week, and keeps any single bad market day from writing the whole book. It also keeps per-firing runtime bounded. **Recommendation: replace the weekly cap with "max 2 filled BUY entries per trading day," counted from Step 4's live order history.**

**Q2 (hard/soft split):** answered by C3 above -- SMA order alone is a *state*, not a *signal*; Donchian must be hard. With Donchian hard and 2-of-4 soft, every entry still has a concrete trigger event plus at least two corroborating conditions. Estimated activity at this gate, given the $2B+/$10-100 universe: roughly 2-6 entries/week in a normal tape versus ~0.7/week observed under Phase B -- "active" without being indiscriminate.

**Q3 (tool-call load): real but manageable; three specific mitigations.**
(a) **Batch the position sweep:** `get_equity_quotes` and `get_equity_historicals` both accept multiple symbols per call -- one call each for the whole book instead of per-position calls. (b) **Earnings check once per day, not per firing:** the next earnings date does not move intraday; run 5g on the first firing of each day only, carry the answer forward via that firing's report. (c) **Cap Pathway 1 technical confirmation at the top 8 scan survivors by relative volume** (down from ~15) -- with 7 scans/day the marginal value of candidates 9-15 per scan is near zero and the indicator calls are the expensive part. With these three, a 6-position firing stays comfortably inside the hourly window on the VM.

**Q4 (correlation cap): keep unchanged -- it binds exactly when it should.**
At 6 slots, max-2-per-sector forces at least 3 sectors. The universe is large enough that this rarely blocks a genuinely diverse book; the times it does bind are hot-sector momentum days, which is when concentration risk is actually highest. Non-issue as a constraint, valuable as a guardrail. No change.

**Q5 (small-account mechanics): spreads are minor; share granularity is the real effect -- acknowledge two consequences and add one rounding rule.**
Spread drag on $2B+, $10-100 names is ~0.1-0.3% per round trip, position-weighted well under 1%/month of account value even at elevated turnover; commission-free execution means churn risk lives in whipsaws (addressed by C1's cooldown), not spreads. The genuine small-account effects: **(1)** Tier A (15% of ~$300 = ~$45) floors to 0 shares for any stock above ~$45 -- those candidates get skipped today, silently shrinking the tradeable universe per tier; **(2)** the profit ladder needs >= 3 shares, which at these sizes means price <= ~$15 -- so under Phase C nearly every position will be stop-only and the ladder is effectively dormant (fine, but it should be known, not discovered). **Recommendation:** allow rounding up to 1 share when floor() = 0, provided cost <= 1.3x target_dollars and <= spendable_cash (a $50-58 stock at Tier A becomes buyable at ~17-19% weight -- still below Tier B); and note the ladder dormancy in the prompt so no future session "fixes" its silence.

**Q6 (Pathway 2's bar): loosen to >= 3.5/5, not 3/5 -- and treat it as bonus flow, not the activity driver.**
Baxter's conviction score measures an *options* setup -- strike reachability against an earnings date -- not standalone equity merit; a 3/5 frequently means "thesis fine, instrument marginal," which says little about owning the shares. 3.5/5 is where Baxter's own system starts committing real money, making it the lowest tier with demonstrated skin-in-the-game meaning. The independent gates (market cap, price band, earnings-proximity, sector, 52-week-low freshness, and now C1's held-symbol exclusion) remain the real filter. Expect Pathway 2 to contribute occasionally, not steadily -- the activity mandate is served by Pathway 1's changes, and stretching Pathway 2 further would be laundering noise through a number.

---

## ADDITIONAL FINDINGS (not raised in the proposal)

**F1. Breaker calibration under Phase C: verified still sane.** Worst plausible single-day damage: six Tier A positions all stopped at the maximum 12% stop distance = 6 x 15% x 12% ~= 11% of account (~$32); even doubling for gap-through slippage leaves total_value far above the $195 breaker. The breaker is realistically reachable only through sustained sequential losses over weeks -- which is exactly the failure mode it exists to catch. Keep at $195, manual re-arm, unchanged.

**F2. Sizing tiers: leave unchanged for launch.** With 6 slots and 2/day pacing, tier percentages are no longer the activity bottleneck. Revisit only after ~20 closed Phase C trades produce a real win/loss distribution to calibrate against -- resizing now would be guessing twice.

**F3. Deployment mechanics reminder.** The live executor is the VM cron running `run_agentic.sh` -> `prompt.md`, not the RemoteTrigger (intentionally disabled since 8/19). Implementation = rewrite `prompt.md` (repo + VM copy), leave the RemoteTrigger config parked and untouched. Do not re-enable it -- two executors firing the same account remains the standing hazard flagged in the migration notes.

**F4. Measurement window.** "Flies or fails" needs a defined test: recommend running Phase C for 4 weeks or 20 closed trades, whichever comes first, then a full post-mortem against Phase B's baseline (2 trades, ~$0 P&L, ~95% idle). Judge on: deployment rate, trade count, win/loss distribution, whipsaw frequency (exits within 3 days of entry), and total P&L vs a same-window SPY hold of the same $300 -- the honest benchmark for "should this money have just sat in an index."

---

## FINAL SPECIFICATION DELTA (implementation checklist)

1. Step 6: remove the hour-11/14 restriction -- Phase B eligibility on every market-hours firing.
2. Step 6: replace weekly 3-buy cap with **max 2 filled BUY entries per trading day**.
3. Step 6: position cap 4 -> **6**.
4. Step 7: gate becomes HARD {mktcap >= $2B, price $10-100, price > SMA50 > SMA200, Donchian(20) breakout} + SOFT 2-of-4 {MACD cross <= 10 sessions, ADX >= 15, relvol >= 1.2, RSI 50-85}; confirm top **8** scan survivors by relvol; tiebreak by soft-score then relvol.
5. Step 8: Pathway 2 admits passes.md entries at **>= 3.5/5** documented conviction; all independent checks unchanged.
6. Step 9: add **exclude currently-held symbols**; add **5-trading-day re-entry cooldown** on exited symbols.
7. Step 5g: earnings-approaching check runs on the **first firing of each day** only.
8. Steps 5a/5f: batch quotes and historicals across all open positions (single multi-symbol calls).
9. Step 10: allow **round-up to 1 share** when floor()=0, if cost <= 1.3x target_dollars and <= spendable_cash; add a one-line note that the profit ladder is expected to be dormant at this account size.
10. Step 2: add one line naming spendable_cash as the GFV guard (cash-account invariant -- never bypass).
11. Unchanged, deliberately: circuit breaker ($195, manual re-arm), all exit mechanics' logic, sector cap (2), choose-at-most-one-per-firing, never-fabricate-a-candidate, git-push reporting.
12. Review clock: post-mortem at 4 weeks or 20 closed trades, benchmarked against SPY-hold of the same capital.

*Verdict recorded 2026-08-31. Implementation awaits Patrick's explicit go-ahead on this delta, per the standing rule that changes to the live routine happen in interactive sessions only.*
