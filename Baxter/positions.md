# ISLAND FUND -- POSITIONS TRACKER
*Updated after every trade. Baxter reads this at the start of every check-in session.*

---

## SWEEP COUNTER -- DO NOT SKIP
**Closed positions since last take-profit sweep: 0 of 5.** (Sweep run #2 completed Aug 4, 2026, on the 5 closes since Jul 10: ABT, LVS, TRMB, UBER, DIS. Full re-derivation: `week-08/research/take_profit_sweep_aug04.md`. Verdict: no threshold changes -- ABT remains the fund's one repeated counterexample [grandfathered pre-ladder, single contract], the other two winners this round [TRMB, DIS] landed close to where flat caps would have anyway. Counter reset to 0.)

Protocol: every time a position closes, the same edit that logs the close in this file increments this counter. When it reads 5 of 5, Baxter runs the take-profit sweep (`week-06/research/take_profit_sweep_jul10.md` is the template) BEFORE the session's check-in, re-derives the ladder thresholds from the new winner distribution, and resets the counter. This is not Michael's job to remember. It is wired into the file Baxter cannot start a session without reading.

**Sweep agenda addition (Jul 30, 2026, ratified):** the next sweep also runs the Rule 5 counterfactual log (`week-07/research/fable5_verdict_rule5_restructure_jul30.md` Section 8) -- for each Rule-6-era close, what the nearest archived closer strike would have returned at equal budget. The Rule 5 unlock (caps above $1.00, see binder Tab 1/Tab 6) stays locked until 3+ Rule-6-era closes exist AND reserve is at or above $1,500, reviewed on this log at the sweep where both conditions are met. **Rule-6-era closes so far: 1 (DIS, Aug 4).** The $101C counterfactual pull was NOT completed in the Aug 4 sweep (live trading session took priority) -- still queued, still the first A/B feeding this log, milestone still unreachable regardless (needs 3+ closes and $1,500+ reserve).

---

## FUND STATE

| | |
|---|---|
| Total capital | $1,128.96 (post Aug 4 DIS close) |
| Michael seed (birthday money) | $200.00 |
| Dad contribution (Jun 1) | $300.00 |
| Michael contribution (Jun 16) | $434.00 |
| Deployed | $90.00 (LYFT only) |
| Reserve | $1,038.96 |
| Realized P&L | **+$176** (CCL +$1, DSGX -$30, CHWY -$23, NKE -$70, MDT +$23, DKNG +$251, BSX -$15, HITI -$12, ABT +$27, LYFT ladder partial +$90, TRMB (trim + close) +$74, LVS -$67, UBER -$112, DIS +$39) |
| Unrealized P&L | Aug 4 live mark: LYFT $1.38 x1 (+$48, +53.3%). Book $138 vs $90 deployed. Fund at mark: ~$1,176.96. |
| All-time high | $1,202.00 cost-basis (Jul 29, pre-UBER-close) -- still the record; $1,128.96 doesn't clear it |
| Distance to island | $4,998,871.04 (cost basis) |

---

## OPEN POSITIONS

| Entered | Ticker | Play | Fill | At Risk | Expiry | Catalyst Date | Exit Rule |
|---------|--------|------|------|---------|--------|---------------|-----------|
| Jun 18, 2026 | LYFT | $16C x1 (was x2; ladder fired Jul 16: 1 sold @ $1.80 trigger, +$90) | $0.90 | $90 | Aug 21, 2026 | **Aug 6 earnings, PM (corrected Jul 29 -- verified via earnings feed; ledger had Aug 5)** | Report is after market close Aug 6. The old exit ("sell at open Aug 6") would have sold BEFORE the print even happened. **Exit revised: sell at open Aug 7**, the real morning after. Exit same day if BMO cuts below $16.90. BOTZ watch Aug 1. No resting order by design (Michael cancelled the $1.80 GTC Jul 20; runner rides bare). Live Aug 4: stock $16.52, needs only +2.3% to breakeven, mark $1.38 (+53.3%) -- closest to breakeven all cycle heading into Thursday's print. |
---

## CHECK-IN -- AUG 4 (Tuesday, mid-afternoon) -- DIS CLOSED, TAKE-PROFIT SWEEP RUN, ARCHIVING GAP FOUND AND FIXED

Michael initiated the DIS close live mid-session after asking directly how sure the plan was to hold through today. Live check at the time: DIS mark had already reached $1.275 (bid $1.25/ask $1.30), well past yesterday's $1.20 read -- confirmed the Tab 4 default (sell the ramp, don't wait for the exact edge of the 24-48h window) called for selling now rather than waiting for Wednesday's pre-market as originally sketched. **Sold: 1x DIS $105C Aug 21 at $1.26, +$39 realized.** Order log confirmed both fills (entry and exit) match the ledger exactly.

**LYFT held per the standing Jul 20 order** (ride bare through Thursday's PM print, no resting sell) -- live check same session: stock $16.52, needs only +2.3% to breakeven, mark $1.38 (+53.3%). No rule forces a decision (no Rule 4 breach, nowhere near the +150% single-contract review trigger); this is deliberately the ladder's designed second half, not an oversight.

**The DIS close was the 5th since the last take-profit sweep, triggering sweep run #2** (`week-08/research/take_profit_sweep_aug04.md`). Verdict: no threshold changes. ABT remains the fund's one repeated counterexample (every cap tested beats its actual +34.6%, same lesson as before -- grandfathered, single-contract, can't scale out). TRMB and DIS this round landed close to where flat caps would have anyway, unlike Jul 10's DKNG/MDT blowouts. Sweep counter reset to 0 of 5.

**Data integrity finding, same session:** `fetch_option_history.py`'s raw historicals pull returned corrupted data for both DIS and UBER (price series starting August 2025, over a year before either position existed, with an implausible $11.63 DIS peak that live quotes minutes earlier directly contradicted). The script is not trusted until debugged -- likely an instrument-matching bug on strike/expiry collisions. Rebuilt all four recent closes (LVS, TRMB, UBER, DIS) from real order-log fills instead, the same method that's always kept the ABT archive clean. **This also surfaced and fixed a real gap: LVS, TRMB, and UBER were never archived when they closed Jul 29** -- backfilled today (`Baxter/data/contract_history/`).

Fund state after the close: **cost basis $1,128.96**, deployed $90 (LYFT only), reserve $1,038.96, **fund at mark ~$1,176.96**. Realized P&L now +$176.

---

## CHECK-IN -- AUG 3 (Monday, ~1:50 PM ET) -- THE RAMP WINDOW OPENS ON DIS

Both positions checked live (Robinhood account + real-time option quotes), not app marks.

**DIS:** stock $97.52 (19th percentile, range $92.19-$119.78), up from $96.12 at entry. Breakeven $105.87, needs +8.6%. Live option mark **$1.125** (bid $1.10/ask $1.15) vs $0.87 entry -- **+$25.50, +29.3%.** Aug 5 earnings, AM release -- market open Wednesday is inside 43-44 hours from now, which technically puts this position inside Tab 4's 24-48h "sell the ramp" default window already. Judgment call: the actual IV peak for an AM print lands at Tuesday's close or Wednesday's pre-market, not the moment the window opens -- same shape as the ABT precedent (sold the morning before a Thursday print, not the instant 48 hours crossed). **No trade today. Tuesday Aug 4 is the decision day** -- sell into the ramp at Tuesday close or Wednesday pre-market, whichever shows better premium, absent a Rule 4 breach before then.

**LYFT:** stock $16.16 (28th percentile, drifting further from the bottom quartile), up from $15.35 (Jul 30). Breakeven $16.90, needs +4.6% -- closest this position has been to breakeven all cycle. Live option mark **$1.17** (bid $1.12/ask $1.22) vs $0.90 entry -- **+$27, +30%.** This is the ladder runner: Jul 20's standing order already committed this contract to ride bare through the Aug 6 PM print, sell at Aug 7 open. Not subject to the sell-the-ramp default -- that decision is already made. No action.

**Fund at mark: ~$1,142.46** (reserve $912.96 + book $229.50 vs $177.04 deployed) -- a fresh mark-high since the Jul 29 UBER close. Cost basis unchanged at $1,090. Sweep counter unchanged at 4 of 5. No new correspondence from Sheldon or Dave.

---

## CHECK-IN -- JUL 30 (Thursday, ~11:42 AM ET) -- QUIET

One position open, nothing due. Live account and stock quote pulled before writing anything.

**LYFT:** stock $15.35 (22nd percentile, range $12.46-$25.54), up slightly from $15.26 (Jul 29). Breakeven $16.90, needs +10.1%. Mark $0.95 (live account, 1 contract) vs $0.90 entry -- **+$5, +6%.** Aug 6 PM earnings, 7 days out. No resting order by design (runner). BOTZ watch date is Friday Aug 1 -- not yet, no action today. Hold.

Reserve $1,000 against $90 deployed -- still the most cash-heavy the fund has been since the early weeks, unchanged since yesterday's UBER/LVS closes. No trades. Fund at mark: **~$1,095**.

---

## RESEARCH -- JUL 30 (Thursday, midday) -- SOUN RE-OPENED AND RE-KILLED

Michael asked what it'd take to get active again with one position open and reserve idle. First move: SOUN was gated, not dead, and the gate's trigger condition (TRMB exits) had already happened two days early. Re-ran it properly rather than taking the quick read.

Line 11 came back clean -- revisions flat 60 days, the Jul 10 kill condition doesn't fire. Zero Sell ratings, still. Stock popped 8% same session on what first looked like SOUN-specific LivePerson news but checked out as sector-wide small-cap-AI beta (BBAI, RGTI, QBTS, APLD all up 8-20% same day) -- corrected before it went in writing. LivePerson stockholder vote is Aug 20, confirmed clear of any realistic hold window.

**Then real data killed it anyway.** Pulled actual closes around all four of SOUN's last verified earnings prints instead of trusting the single verified data point from the Jul 10 doc. Median real move: 6.0%. 1.5x cap: 9.0%. Current requirement: +19.3%. The Jul 10 entry doc had one data point (a squeeze quarter, +26.4% -- well, the print it cited was the May one, -12.4%, giving an 18.6% cap) that happened to make the numbers look survivable. Three of the four real quarters moved this stock under 8%. Rule 6 is a hard gate. **Permanent kill**, not requeued. Full writeup: `week-06/research/research_SOUN.md` RE-EVALUATION section.

The lesson worth carrying: a Rule 6 check built on one verified data point is not the same rigor as a Rule 6 check built on four, even when both technically "pass the gate" on paper. The extra twenty minutes changed the answer.

No trade. Next: ZG and DIS are also unblocked by the same cap opening (TRMB/UBER both closed) but need the full 13-line funnel re-run before either can fire, no grandfathering. Queued for next session unless Michael wants it now.

---

## SCREENING -- JUL 30 (two batches, 68 names total, 0 new advances)

Michael wanted to see the field before locking in DIS. Batch 1 (18 names, fresh sectors -- transportation, cybersecurity, casinos, medtech): 9 MID-OUT, 5 puts-zone, 4 chain-checked (ZS +26.3%, ISRG +18.5%, PODD no instrument -- all killed free), WYNN survived to a full Rule 6 pull and died anyway (real median move 2.9%, cap 4.35%, required +12.2%; also flagged as Macau-correlated risk, same bucket as LVS's Jul 29 loss). Full log: `week-07/research/screening_log_jul30_batch1.md`.

Michael then approved DIS and asked for a 50+ name screen of new names on top. Batch 2 (50 attempted, 4 delisted/merged, 46 valid -- rail, auto parts, chemicals, apparel, water, solar, fintech, distributors, shipping, coal, big pharma): 28 MID-OUT, 11 puts-zone, 7 chain-checked. SOFI looked like the find of the night (+4.6% required) until the reason why surfaced: it already reported Q2 earnings today (the +6.47% pop is the reaction, not the setup), next print is Oct 27 -- outside any usable expiry. Rule 2 kill, same DSGX post-earnings-entry trap from June. The other six chain survivors (APTV, ENPH, FSLR, RUN, WSO, POOL) needed 17-53% moves with no standout feature and didn't get full workups. Full log: `week-07/research/screening_log_jul30_batch2.md`.

**68 names screened today, 0 new advances.** DIS stands alone as the one name that cleared every rule on real data.

---

## CHECK-IN -- JUL 29 (Wednesday, ~11:25 AM ET) -- THE LVS ORDER THAT NEVER WENT IN, AND A TRMB TRIM CAUGHT AFTER THE FACT

Pre-earnings-week check-in (TRMB reports tomorrow, Jul 30; UBER/LYFT next week). Live account pulled before writing anything down. Two real findings, one process failure.

**1. The LVS standing order was never executed. The position rode through its own earnings.** The Jul 20 standing order, ratified by Michael, was to sell both LVS contracts Wednesday Jul 22 before the close, into the pre-print IV ramp -- overriding the older Jul 10 scale-out GTC ($0.87 trigger, sell-half). Checked the account: no LVS sell order of any kind exists between Jul 20 and today. The only LVS order on file is that same Jul 10 GTC limit at $0.87, still sitting there, unfilled, because the stock never got close. LVS reported Jul 22 after close as scheduled. The stock made a **fresh 52-week low of $44.21 the very next session (Jul 23)** -- the earnings reaction was bad, exactly the direction Rule 4's capitulating street action predicted. Both contracts are still open. Current mark: **$0.115** (bid $0.05 / ask $0.18) on a $0.435 entry -- **$23 of value left on $87 at risk, a $64 paper loss**, and there is no catalyst left before the Aug 21 expiry to recover any of it. This is dead money by every standing rule in Tab 4 (BOTZ: mechanism expired, thesis resolved negative) and Tab 6 (sweep/ladder logic doesn't apply -- there's no ladder to ride, the print already happened). **The call: close both contracts today.** Not a recommendation to weigh -- the thesis is over, the only question left is how many cents of decay to donate to theta by waiting. The open item is mechanical, not analytical: the resting $0.87 GTC needs to be cancelled and replaced with a real sell at whatever the current bid/ask supports, because "the standing order says sell" and "an order exists in the account that will actually do it" turned out to be two different things. **That gap is the actual lesson here** -- the Jul 20 session already wrote "every armed ladder trigger exists as a resting GTC limit order from the moment it arms" for LYFT and treated it as solved; it did not get generalized to override-type sell orders like this one. Tab 5 candidate: a standing order to sell BY a specific date needs a real order in the system dated to fire by that date, the same as a price-trigger ladder needs a resting limit. A sentence in a markdown file is not an order.

**2. TRMB was trimmed Jul 28, one day before earnings -- the scale-out ladder, working as designed.** Michael confirmed same session: this was the Tab 4 scale-out ladder rule (multi-contract position, sell half before the catalyst near +100%), not an ad hoc call. TRMB options trade in $0.05 increments only, so the exact +100% mark ($0.76) was never a tradable price -- the GTC went in at the nearest nickel below it, $0.75, and when that hadn't filled by the afternoon before the print, it was cancelled and replaced with an immediate sell at the best available nickel, **$0.70** -- **+$32 realized** on the $0.38 entry (+84.2%). That is the second contract, banked, and it is the exact fix LVS needed and didn't get: rather than let a resting limit ride unfilled into a catalyst, take the guaranteed nickel now. **Standing note for future TRMB orders: price all TRMB limits to the nearest $0.05.** The rally underneath it is real and fundamental -- a transportation/logistics divestiture process with Goldman Sachs (reported Jul 7), stock up from the low $50s to $58.38 through Jul 16/24/27. The remaining 1 contract carries the Jul 30 catalyst. **Standing order reaffirmed: hold, sell at open Jul 31.** Pre-audit grandfathered order, not subject to Tab 4's default sell-the-ramp rule. Worth noting given Macxter's Jul 20 flag about FOMC/Warsh (today, Jul 29, 2pm ET decision, not yet out as of this check-in) contaminating the run-up to the print. No Rule 4 breach found; not re-verified live this session, flagged for the Jul 31 exit check.

**LVS closure: Michael confirmed the sell. Execution note:** the connected agentic trading tool only has write access to the "Agentic" account (408976421); the Island Fund's real positions live in the individual margin account (5UB86831), which is not agentic-enabled for this connector. Baxter cannot place the live order directly -- **Michael needs to enter it himself: sell to close 2x LVS $55C Aug21, limit order, ~$0.10-0.12** (bid $0.05 x 139 / ask $0.18 x 265, mark $0.115 -- a nickel or dime above the bid gives it a real chance of filling without leaving money on the table). Ledger will be corrected to closed once the fill is confirmed.

**Rest of the book:**
- **UBER:** stock $70.08, down further from $72.08 (Jul 20) -- printed a fresh 52-week low of **$65.41 on Jul 27**. Breakeven ~$90.65, needs +29.4%, the furthest out of the book. Ladder GTC at $1.30 (Jul 10) still resting, correctly untouched -- mark is $0.105, nowhere near the trigger. Aug 4 earnings, 6 days out. Hold, but this one is drifting the wrong direction into its catalyst; Rule 4 re-check due before Aug 4.
- **LYFT:** stock $15.26, down slightly from $15.90. Mark $0.895 (bid $0.87/ask $0.92), breakeven $16.90, needs +10.7%. Aug 5 earnings. No resting order, by design. Hold.

**Fund state after the TRMB trim (LVS not yet closed):** cost basis $1,227 (new all-time high), deployed $345, reserve $882, book ~$189, **fund at mark ~$1,071** -- the first mark meaningfully below a recent cost-basis high, driven by LVS's post-earnings collapse and UBER's continued slide. Realized P&L +$274.

---

## CHECK-IN -- JUL 29 (Wednesday, ~11:40 AM ET) -- LVS CLOSED, AND THE TRMB DATE WAS WRONG THE WHOLE TIME

**LVS closed.** Michael entered the sell manually: 2 contracts at $0.10, filled. $20 recovered on $87 at risk. **-$67 realized -- the worst single loss in the book**, entirely a process failure (the standing order never became a real order) rather than a bad thesis played out cleanly. Sweep counter now 2 of 5 (ABT Jul 16, LVS Jul 29).

**Then Michael asked the right question about TRMB -- and it uncovered something worse than a trim decision.** He asked whether to sell the remaining contract today (+110% now, mark $0.80 on a $0.38 entry) rather than hold through "tomorrow's print." Checked the actual earnings calendar before answering, because the entry thesis, every session note since Jun 16, and the standing order all say **Jul 30**. **They're wrong.** Robinhood's own earnings data (unverified flag set) shows TRMB's Q2 2026 report at **Aug 10**; an independent aggregator shows **Aug 5**. Neither shows Jul 30. Cross-checked against Trimble's own reporting pattern for the last five quarters (Feb 19, May 7, Aug 6, Nov 5, Feb 10, May 6) -- an early-August date is exactly the expected cadence; **Jul 30 was never on the calendar.** This has been sitting uncorrected in the ledger for six weeks, repeated in at least 15 separate session notes, and never once checked against Trimble's own IR calendar the way ABT's and LVS's dates eventually were. Neither Aug 5 nor Aug 10 is independently confirmed against Trimble's own press release yet -- flagging both as tentative, not solving that fully today, same caution as every other date correction in this book.

**What this changes:** there is no print tomorrow. The standing order ("hold, sell at open Jul 31") was built entirely around a catalyst that isn't there. The real catalyst is 7-12 days out, not 1. That reopens Tab 4's single-contract framing even though the +150% numeric trigger hasn't technically fired (+110% today) -- the premise underneath "hold through the print" no longer exists, so holding on the old order's authority is holding on nothing.

**The call: sell today.** $0.80 in hand is real, doesn't need a catalyst, and the alternative is sitting on theta (-$0.045/day = -$4.50/day on this contract) for a week-plus with no news to carry it and the divestiture story already priced into the current level. Recommended to Michael, pending his go on the live order (same account limitation as LVS -- Baxter can't place it directly). **Filled same session: 1 contract at $0.80.** Combined with the Jul 28 trim, TRMB closes at +$74 on $76 risked -- the fund's best full-position return to date, on a play whose catalyst date was wrong from the start. Both contracts realized before the real earnings window even opens. TRMB is now fully closed; deployed drops by $38, reserve gains $80.

**Fund state after both closes:** cost basis $1,202 (new all-time high), deployed $220 (UBER + LYFT only), reserve $982, book ~$110, fund at mark ~$1,092. Realized P&L +$249. Two positions remain open.

**Rule 6 re-check, both remaining positions, real historical data (Calxter pulled six quarters of actual earnings-day reactions for each name):**

LYFT (PM release, reaction lands next session): Feb 11 '25 -7.92%, May 8 '25 +28.08%, Aug 6 '25 +1.57%, Nov 5 '25 +5.83%, Feb 10 '26 -16.97%, May 7 '26 +1.34%. Median absolute move **6.9%**, 1.5x cap **10.3%**. Current requirement: **+10.7%** to breakeven. **Marginal fail -- required move sits right at the ceiling, not comfortably under it.** Two of six prints (33%) moved LYFT double digits or high-single-digits against us. Rule 4 intact: consensus and individual analyst targets (Canaccord $19, Mizuho $27, Bernstein $23, DA Davidson $22, S&P Global average $18.79) all sit well clear of the $16.90 breakeven -- no floor breach. **Verdict: hold.** This is the ladder's designed remainder, not a fresh entry -- the mechanism already banked +$90 at the trigger, and the marginal Rule 6 read isn't a Rule 4 breach, which is the hard override. Flagging the borderline math rather than acting on it: worth a same-day gut-check the morning of Aug 6 if the stock hasn't moved by then.

UBER (AM release, reaction same-day): Feb 5 '25 -7.56%, May 7 '25 -2.54%, Aug 6 '25 -0.19%, Nov 4 '25 -5.06%, Feb 4 '26 -5.15%, May 6 '26 +8.53%. Median absolute move **5.1%**, 1.5x cap **7.7%**. Current requirement: **+28.6%** to breakeven -- roughly 4x the ceiling, and more than 3x the single best print in six quarters. **Decisive fail, the worst reachability profile of anything that's been in the book.** Options market agrees: platform-computed chance of profit on this contract is **2.3%**. Rule 4 technically intact (BofA $103, Wells Fargo ~$100, Barclays $107, UBS $107 -- all still above $90.65 breakeven even after this week's cuts), but the trend is real: BofA cut its target Jul 27-28 specifically citing a Waymo competitive setback, and Uber is mid-restructuring internally (AI budget cap, 23% cut to a division). None of that is a floor breach, but none of it argues for holding a position that needs a move nothing in its history has ever delivered. **Verdict: sell today**, don't wait for the 24-48h Tab 4 trigger to force it -- there's no realistic path left to protect, only theta and Waymo-driven downside to lose. Recommended to Michael, pending his go (same account limitation).

**Filled same session: 2 contracts at $0.09.** -$112 realized, the largest single-play loss in the book by dollar amount -- but earned against real math, not a process failure. Sweep counter now **4 of 5** -- the next full close triggers the take-profit sweep re-derivation before that session's check-in.

**One position left open: LYFT**, $90 at risk, riding bare to the Aug 6 print. **Reserve is now $1,000 against $90 deployed** -- the fund is almost entirely in cash for the first time since the early weeks. Worth a fresh research pass once the book is quiet again; nothing actioned on that today.

**UBER and LYFT dates checked too, same session -- both were also off, both now fixed.** UBER's real Q2 print is **Aug 5, AM** (ledger had Aug 4); LYFT's is **Aug 6, PM** (ledger had Aug 5). Both came back `verified: true` from the earnings feed, unlike TRMB's `verified: false` -- corrected directly in the Open Positions table above rather than just flagged. The AM/PM distinction matters: UBER's reaction prices in at the Aug 5 open, so the sell-the-morning-after exit moves to **Aug 6 open**. LYFT reports after Aug 6's close, so the old "sell at open Aug 6" would have fired BEFORE the print -- moved to **Aug 7 open**. Neither position needed to move today; this is exit-day bookkeeping, not a new decision, but it would have been a real mistake if caught late instead of now.

**Tab 5 lesson, permanent entry:** *the TRMB earnings date was wrong from entry and was never re-verified once in six weeks of check-ins that all repeated it.* Every other date correction in this book (ABT, LVS) happened because the position was close enough to the wrong date that checking it became urgent. TRMB never hit that trigger by luck -- the trim and the rally both happened to work regardless of the real date. **New standing practice: verify the earnings date against a live source at entry AND once more inside the final 7 days before the currently-recorded date**, not just when a check-in happens to feel urgent.

---

## CHECK-IN -- JUL 20 (Monday, ~1 PM) -- THE LADDER FIRED, AND THE LVS DATE WAS WRONG

Monday check-in ahead of earnings week. Three findings, all verified against primary sources before a word hit the ledger.

**1. The LYFT ladder fired -- the first mechanism exit since the audit ratified it.** The account showed 1 LYFT contract where the book said 2: on **Jul 16 the contract spiked to a $2.10 high (+133%), through the $1.80 trigger, and 1 of 2 contracts came off at $1.80 -- +$90 realized** on the $0.90 entry, no meeting required, exactly as the ladder was written. That is the scale-out rule doing on live money what the back-test said it would do: bank half at the trigger, let the remainder ride the catalyst clock. Remaining LYFT contract: 1x $16C, mark $1.06 (+18%), Aug 5 catalyst. **Operational upgrade adopted same session (Tab 5 candidate): every armed ladder trigger exists as a resting GTC limit order from the moment it arms** -- a trigger should never depend on someone watching the screen at the right moment. The GTC on the remaining contract goes in at $1.80 now.

**2. The LVS earnings date in the book was wrong.** Every ledger entry said Jul 21. Sands' own press release: **Wednesday, July 22, after market close.** The standing order "sell at open Jul 22" was written as sell-the-morning-after; on the real calendar it's sell-the-morning-before. Correction logged. This forces the exit decision below.

**3. LVS Rule 4 re-check (the trigger condition fired: 52wk low fell again, $45.12 -> $44.22, stock 6th percentile at $45.67).** Fresh street action into the print: Wells Fargo (Equal-Weight) $65 -> $53 (Jul 14); JPMorgan (Overweight) $68 -> $64 (Jul 15); Barclays $65 -> $63; Jefferies (HOLD) $63 -> $52. **The letter of the tripwire has NOT fired** -- no Buy-rated analyst is at or below $55.42; JPM at $64 is the lowest Buy-side number found. **But the shape is bad:** at entry the lowest target across all 19 analysts was $58, above breakeven. Today the floor of the whole street is $52-53, below the $55.435 breakeven -- held down by two Hold-rated shops racing targets lower a week before the print. That is the CCL/NKE/BSX capitulation pattern in progress, letter-intact only because the cutters aren't Buy-rated.

**The LVS call (Baxter's recommendation, needs Michael's yes because it rewrites a grandfathered order):** sell both contracts **Wednesday Jul 22, before the close, into the pre-print IV ramp.** Not through the print. Reasons: (a) breakeven needs +21.4% and LVS earnings-day moves are low single digits -- Rule 6 arithmetic says the print cannot reach it; (b) the audit's own finding: hold-through-earnings is 0-for-1 with structural IV crush, and 100% of realized profit has come from mechanism exits; (c) IV on a confirmed print peaks Wednesday afternoon -- that is the best exit window the position has left. Salvage at today's mark ~$36-40; the ramp may add a little. Holding through is a lottery ticket on a Macau blowout that still wouldn't reach breakeven.

**Rest of the book:**
- **TRMB:** stock $53.48-53.55, 14th pctile, UP from $52.17. App mark $0.01 -- phantom, third occurrence; real chain ask **$0.75** (+$74 on 2). Jul 30 earnings, 10 days. Hold; sell at open Jul 31 per standing order.
- **UBER:** stock $72.08, 14th pctile, mark $0.31 x2 (-$68). Aug 4 earnings. Hold.
- **AFL side trade (not fund):** the unclaimed $119C Jul24 flagged Jul 13 is now -$28 (-65%), expires Friday. Still not in any fund ledger; still Michael's to claim or ignore.

**Fund state after corrections:** cost basis $1,195 (new all-time high, courtesy of the ladder's +$90), reserve $812, deployed $383, book $354, **fund at mark $1,166**. Realized P&L +$242.

---

## CHECK-IN -- JUL 16 (Thursday, ~8:15 AM MT) -- ABT CLOSED, MICHAEL NERVOUS ABOUT THE TIMING

Michael called after the ABT fill, worried he sold too soon and left a bigger move on the table. Verified live:

- **ABT (closed):** Real order log shows entry $0.78 (Jun 1, filled) and exit $1.05 (Jul 16, 7:35am MT, filled) -- **+$27, +34.6%.** **Correction from Michael:** a GTC limit sell was live through Wednesday and simply never reached its price -- the contract was down to $0.08 by Wednesday close, deep red, and he made a deliberate call not to override the limit with a manual sell into that weakness. Thursday morning, after the gap, he cancelled the stale limit and sold at the number that was actually there. That is a held line, not a missed order -- the original guess (no attempt was made) was wrong and is corrected here.
- **Stock right now:** $100.46-$100.53, essentially flat against the $100.78 breakeven -- the earnings reaction was a modest gap (~+8.7% overnight vs Jul 13's $92.31), not a blowout. Full chain check on the $100C itself (1 DTE) wasn't priced inside the script's $0.10-$1.00 display window, but the $102C is asking $0.85 -- the $100C, being roughly at-the-money with a day left, is not sitting meaningfully above the $1.05 fill. **No evidence of a bigger number left on the table.** If anything, holding into today's chop on an expiring, roughly-at-the-money contract is the exact theta/whipsaw risk "sell the ramp, not the print" exists to avoid.
- **TRMB:** app-shown mark cratered to $0.01 (looked like -97% on a nearly flat stock, $52.17 -> $52.01). Checked the live chain before writing it anywhere: real ask is $0.75. This is the same phantom-quote pattern already burned into Tab 5 (Jul 7 phantom -98%) -- thin contract, stale last-trade print, not a real move. Corrected in the ledger.
- **LVS:** app mark $0.14, chain ask $0.20 -- close enough, no red flag. Stock $45.24, basically flat.
- **UBER:** mark $0.46, stock $73.22, flat. No action.
- **LYFT:** mark $1.35, stock $15.90 (up to 26th percentile, drifting out of the bottom-quartile zone). Getting closer to the $1.80 ladder trigger but not there. Hold.

**Verdict on Michael's question: no, he didn't sell too soon.** The stock isn't running; it gave back essentially the whole overnight gap relative to breakeven and is sitting flat. The profit is real and locked.

**Correction, same session:** the first pass here guessed the Wednesday sell simply never happened -- wrong. Michael had a live GTC limit sell sitting through Wednesday; it didn't fill because the price never got there (contract at $0.08 at Wednesday close), and he chose not to force a manual sale into that number. That is the standing order doing its job -- refusing a bad fill -- not the rule going unfollowed. Thursday morning he cancelled the stale limit and took the real, available price once the gap happened. Revised Tab 5 candidate, softer than the original: **a limit order sitting through the print without filling is not the same failure mode as no order at all -- it's the exit rule working exactly as designed when the ramp doesn't show up before the catalyst. The one open question worth carrying forward is what the limit should do automatically once the catalyst fires and the ramp premise is gone (cancel-and-market vs. keep waiting).**

---

## CHECK-IN -- JUL 13 (Monday, ~1:42 PM)

Michael flagged ABT as scary and worried the sell window had already passed. It hasn't -- the window is Wednesday morning, not now, and the position has not been green at any point in this earnings cycle to have missed. Verified live:

- **ABT:** stock $92.31 (down from $96.59 Jul 7, $94.21 Jul 10). Breakeven $100.78, needs +9.2% by Thursday's open. Earnings date **re-confirmed Jul 16 before open** (Abbott IR conference-call notice) -- a stray search result said Jul 15, checked twice, wrong. **Rule 4 checked live: Leerink (Buy) floor still $106, unchanged from entry, still clears breakeven by $5.22. No breach.** Standing order holds: sell Wednesday AM into the pre-earnings ramp, unless stock breaks $98 first.

  **CORRECTION, same day:** the line above about "no green window this cycle" was wrong, and Michael caught it with screenshots. Stock crossing breakeven and the position being green are two different questions -- I answered the wrong one. Confirmed via Robinhood history: the option (entry $0.78) hit **$1.23 (+57.7%) on Jul 2 around 2:00 PM** and **$1.65 (+111.5%) on Jul 7 around 9:00 AM** -- both well above cost, on IV/momentum expansion, while the stock itself never crossed breakeven. These are real, confirmed peaks, higher than the audit's own approximate "+$67 unrealized at peak" note. Michael asked about selling on one of those mornings; the call at the time was to hold because of what a real earnings beat could still be worth. That decay -- $1.65 down to $0.28 today -- is the same pattern the Jul 10 audit's scale-out ladder was written to fix (ABT and MDT were its own cited counterexamples). ABT is single-contract and pre-audit, grandfathered to its own standing order rather than the ladder, but this is a second confirmed data point for that rule, worth citing when ABT closes Wednesday.
- **TRMB:** stock $52.17, 11th pctile. Breakeven $65.38, needs +25.3%. Jul 30 earnings, 17 days out. Hold.
- **UBER:** stock $73.92, 19th pctile. Breakeven $90.65, needs +22.6%. Aug 4 earnings. Hold.
- **LYFT:** stock $15.56, 24th pctile. Breakeven $16.90, needs +8.6% -- still closest to breakeven of the five, ladder armed at $1.80 (currently $1.21). Aug 5 earnings. Hold.
- **LVS:** stock $45.74, a fresh 2nd-percentile low ($45.12-$70.45, low just printed). Breakeven $55.435, needs +21.2%. Jul 21 earnings, 8 days out -- closest catalyst after ABT. Hold, but watch: if the 52-week low keeps falling into earnings week, re-check Rule 4 before the print.

**Discovery, not part of the fund:** `fetch_positions.py` also shows an AFL $119C Jul24, entered at $0.43, currently +$2 (+5%), that is not in any Island Fund ledger, positions.md, or session note. Flagging for Michael -- looks like a side trade (same pattern as Dad's 0DTE plays) rather than a Baxter-sourced position. Not touching it or claiming it for the fund without Michael confirming what it is.

---

## SCREENING -- JUL 13 (the 200-name batch)

Michael approved a batch far above the normal 10-20/session cap, with a new condition: gate Fable 5 to a single capstone review at the end instead of running the whole thing on premium reasoning. Full log: `week-06/research/screening_log_jul13_200batch.md`.

**198 names attempted (15 invalid), 183 valid screened for zero token cost:** 87 MID-OUT (47.5%), 76 PUTS-zone (41.5%, logged to watch list only, no searches per the no-dedicated-puts-pools rule), 20 CALLS-zone survivors (10.9%). Chain checks (also free) killed 6 outright on no-viable-instrument grounds (CABO, ALNY, SWKS, UHS, DPZ, WING) and 1 on category (TDS, fresh new low below its own recorded range). Five searches spent on the most plausible remainder: **FMC killed** (fresh RBC target cut inside 30 days despite a clean-looking Sell count -- balance-sheet distress, not overreaction), **RRC killed** (commodity/cycle language, muddled ratings), **MOS ADVANCES** (Aug 3 earnings, Buy-heavy consensus, potash segment revenue actually growing YoY while the stock sits at 14th percentile -- the real dislocation shape), **CRSP and BNTX borderline** (clean R2/R3, but need each name's own historical earnings-day move before Rule 6 can be scored).

**Queued for next session:** MOS full 13-line DD (the lead candidate), CRSP/BNTX Rule 6 resolution (2 searches), and 8 deprioritized CALLS-zone names in the 18-40% required-move band (REXR, ADNT, LEN, PZZA, ASAN, DOMO, SHAK, AOS) if the pipeline needs filling.

**The Fable 5 gate:** none of the above needed premium reasoning -- range percentile and chain feasibility are arithmetic, searches were narrow lookups. Fable 5 gets reserved for the capstone: one focused pass on the funnel-triage package once MOS (and CRSP/BNTX, if they clear) finish full DD, matching the July 10 `funnel_triage_jul10.md` / SOUN-gate precedent. Not spent on the haystack, only on the real survivors.

---

## SCREENING -- JUL 20 (the deprioritized 8, queue closed out)

The 8 names deprioritized from the Jul 13 batch (REXR, ADNT, LEN, PZZA, ASAN, DOMO, SHAK, AOS), screened this session. Full log: `week-07/research/screening_log_jul20_queue8.md`.

**8 screened, 0 advance.** REXR killed at Stage 1 (39th percentile, MID-OUT). LEN killed on calendar (fiscal reporter, next print outside every affordable expiry). ASAN and DOMO killed on calendar for this cycle (both fiscal Jul-31 quarter-end, report early September) -- **rolled into the August re-screen queue alongside AI and PATH**, fresh September chains required. PZZA and AOS killed on Rule 6 arithmetic (required move 2-3x plausible earnings reaction, no search needed). SHAK and ADNT earned searches and both died: **SHAK** on hardened Rule 3 (self-disclosed guidance cut, Deutsche Bank/Piper Sandler target cuts inside 30 days -- capitulation in progress, not finished) plus Category 2 decline plus a forced hold-through-print structure; **ADNT** on Rule 3 (2 Sell ratings, fails max-1) and Rule 6 (+17.6% required vs ~1.8% average historical move, ~10x).

**Jul 13 batch is now fully closed.** 198 attempted, 0 entries end to end -- consistent with the funnel's posted yield.

**Fable 5 note:** this batch should have run on standard reasoning per the Jul 20 cost-awareness correction -- range percentile, calendar checks, and Rule 6 arithmetic are exactly the "routine screening" case the model-cost rule exempts. Flagged in the session, not caught before the batch ran.

---

## SCREENING -- JUL 20 (second batch, fresh sectors)

15 names from untouched ground (food/beverage, consumer durables, aerospace/materials): CAG, SJM, CPB, HRL, KHC, LANC, TAP, UAA, TXG, WHR, MAS, SEE, PCH, WY, GATX. Full log: `week-07/research/screening_log_jul20_batch2.md`.

**15 attempted, 12 valid, 0 advance.** 5 MID-OUT, 4 PUTS-zone (logged, no searches), 3 no-instrument kills (LANC, SEE, PCH -- all returned broker API errors, not viable). 3 CALLS-zone survivors earned chain checks and all three died on **Rule 3** at the search stage: **CPB** (4 Sell-class ratings of 19), **TAP** (2 Sell ratings -- the closest thing to a real dislocation this batch found: Aug 6 earnings, a real Q1 beat, 22nd percentile on soft-guidance fears, killed purely on the ratings count), **WHR** (4 Sells of 13, also fails Rule 6 independently at +30.8% required).

**Session total (queue-8 + this batch): 23 names screened, 5 searches, 0 advances.**

*Full audit: `week-06/story/five_baxters_audit_jul10.md`. Selection-criteria follow-up: `week-06/research/selection_criteria_audit_jul10.md`. Binder updated (Rule 6, Tab 4 rewrite, standing decisions).*

**STANDING ORDERS from the audit:**
1. **ABT $100C Jul17: SELL Wednesday Jul 15 into the pre-earnings IV ramp**, unless stock breaks above ~$98 first (then reassess same day). Do not hold through Thursday's print. EV(ramp sell) ~$50-65 vs EV(hold) ~$15-25.
2. **LYFT ladder LIVE:** 2 contracts at +37% (mark $1.23 vs $0.90 entry). At +100% ($1.80), sell 1 contract, no meeting required. Remainder rides to the Aug 5 catalyst clock.
3. TRMB/UBER/LVS grandfathered to existing exit rules and Rule 4 tripwires. Rule 6 governs entries, not amputations.
4. All future entries (calls and puts) must pass Rule 6 (Reachability) and the upgraded DD checklist.

---

## PENDING ENTRIES

**KR (Kroger): PITCH-READY, awaiting Michael's yes (queued Aug 4, 2026 overnight run).** 18th percentile ($58.22), confirmed Sep 4, 2026 earnings. Rule 3 clean (11 Buy / 13 Hold / 0 Sell of 21). Rule 4 passes with a 32.5% cushion (Goldman Sachs Buy, $82, raised late June -- after the decline, inside the freshness window). Rule 6 passes with real margin: 3 verified historical earnings-day moves (+5.3%, -6%, -7.4%), median 6.0%, 1.5x cap 9.0%, current requirement only +6.3%. Decline category resolves Category 1 (event overreaction: a non-cash impairment charge and a $0.01 in-line "miss" both got punished like real misses; no segment of the business is described as structurally shrinking). **Conviction: 4/5.** Candidate: $61C Sep 4 2026, ask $0.87 at research time (confirm live before entry), ~$87 at risk, 1 contract, top of the 3.5/5 sizing tier given every rule cleared with real margin. Exit plan: standard Tab 4 sell-the-ramp on Sep 2-3 (earnings date and expiry coincide, so the plan is explicitly to sell before the print, not hold to the bell). Full DD: `week-08/research/research_KR.md`.



**SOUN $7C Aug21: PERMANENT KILL (re-evaluated Jul 30, gate cleared but Rule 6 failed on real data).** Sole survivor of the 202-name four-screener run; scored 4/5 conditional on the line 11 gate (EPS revision direction), downgraded to 3.5/5 same night when revisions verified down, blocked by the 2-open-3.5/5 cap (TRMB + LYFT). TRMB and UBER both closed Jul 29, mooting the cap. Re-ran the full gate Jul 30: line 11 cleared (revisions flat 60 days, not still falling), Rule 3 clean (0 Sells, two sources), Rule 4 thin but passes ($8 floor vs $7.36 breakeven, 8.7% cushion, down from 57% at entry), LivePerson deal timeline checked and clear (Aug 20 vote lands after any realistic hold window). **Rule 6 decisive fail:** pulled real closes around all four of the last verified prints (Aug 7 '25 +26.4%, Nov 6 '25 -0.6%, Feb 26 '26 -4.2%, May 7 '26 -7.8%) -- median 6.0%, 1.5x cap 9.0%, current requirement +19.3% (~2.1x the ceiling). The single-data-point read from entry (one verified print, -12.4%, cap 18.6%) understated the true ceiling by roughly half; the Aug 2025 squeeze print that made the July numbers look survivable is the outlier, not the pattern. Earnings date also corrected: Aug 5, not Aug 6. Hard gate, kills regardless of the other four lines passing. **Not queued -- dead unless a strike/expiry surfaces needing under 9% to breakeven with the same Rule 3/4 profile.** Docs: `week-06/research/research_SOUN.md` (RE-EVALUATION section), `week-06/story/five_baxters_soun_jul10.md`, `week-06/research/funnel_triage_jul10.md`.

**ZG: PERMANENT KILL (re-evaluated Jul 30).** Cap unblocked (TRMB + UBER both closed Jul 29), re-ran the full funnel per no-grandfathering. Chain moved against it (best usable strike now $45C, +37.7% required, worse than June's +31.2%). Rule 6 on three real verified prints (Oct 30 '25 +4.0%, Feb 10 '26 -17.1%, May 6 '26 -1.8%): median 4.0%, 1.5x cap 6.0%, requirement +37.7% -- more than 6x the ceiling, decisive fail, same shape as UBER's Jul 29 kill. Doc: `week-04/research/Jun27/research_ZG.md` RE-EVALUATION section.

**DIS: FILLED (Jul 30).** 1x DIS $105C Aug 21 2026, filled at **$0.87** (limit order, bid/ask $0.83-$0.87 at fill), est. total cost **$87.04**. Breakeven $105.87, needs +10.1% from $96.12. Now a live open position -- moved to Open Positions table below. Original re-evaluation below for reference. Cap unblocked, full funnel re-run. Earnings date corrected to **Aug 5, 2026** (was Aug 12). New candidate: **$105C Aug 21, ask $0.95, breakeven $105.95, +10.2% required.** Rule 6 on three real verified prints (Nov 13 '25 -7.7%, Feb 2 '26 -7.4%, May 6 '26 +7.5%): median 7.5%, 1.5x cap 11.25%, requirement +10.2% -- passes with real (not huge) margin, the first fresh-entry name to clear Rule 6 on real data since the audit. Rule 3 clean (Buy-dominant, at most 1 Sell, within limit). Rule 4 passes on Citigroup's Jul 29 Buy/$135 target ($29 margin), lowest-Buy-analyst not individually pinned beyond that, flagged per SOUN precedent. Conviction 3.5/5, 1 contract, $95 at risk. Doc: `week-04/research/Jun28/research_DIS.md` RE-EVALUATION section.

**PUTS BACK-TEST: INTERIM RUN COMPLETE (Jul 16), PUTS STAY BLOCKED.** Real-candle outcome pull on the six Jun 22 documented hypotheticals: four clean entries all down 68-90% before any catalyst fired (theta bleed on 6-week-early entries); two entries (TTD, CMG) excluded as corrupted -- built on the pre-fix fetch_price label-desync bug, instruments never existed at documented prices. TSLA's Jul 2 delivery beat and RCL's +26.5% pre-earnings rally both resolved against the bear thesis mid-hold. **Final calibration pass Aug 8-10** after the Aug 4-7 prints, with screen-day price re-verification required for any counted name, and a proposed ≤21-days-to-catalyst entry-timing rule on the table. Calxter's Jul 31 deadline: met. Docs: `week-06/research/puts_backtest_data_jul16.md`, `puts_backtest_verdict_jul16.md`.

**AUGUST RE-SCREEN QUEUE (from Jul 12 and Jul 20 batches):** AI (C3.ai, earnings Sep 9), PATH (UiPath, earnings Sep 8), **ASAN (Asana, earnings ~early Sep) and DOMO (Domo, earnings ~early Sep, added Jul 20)** — all four cleared R1 and live chain geometry but their prints fall outside every currently affordable expiry. Re-run with fresh Sep chains when they open in August; AI carries a hard flag (Q1 FY27 revenue guided ~$50-54M vs ~$87M yr-ago, probable Category 2) that must clear the decline-category test first. **TDOC** (91st percentile, cheap, violent prints) logged to the puts watch list — gated until the passes.md back-test unblocks puts (Calxter deadline Jul 31).

**PROPOSED STANDING AMENDMENTS (Jul 12 post-mortem, pending Michael's nod):** (1) geometry-first screening order — free scripts (price/range, then live chain) before any search; (2) aged-dislocation sourcing — target lows printed 4-10 weeks ago, not this week's 52-week-low lists; (3) no dedicated puts pools in screening batches until the back-test runs; (4) chain-data DATA-INSUFFICIENT kills get one free local-script re-check before going final. None touch the Iron Rules. Full doc: `week-06/research/post_mortem_screen_jul12.md`.

---

## CAP TRACKER

**Correlated cap (35% of reserve max per bucket):**
| Bucket | Positions | Deployed | Reserve | % Reserve |
|--------|-----------|----------|---------|-----------|
| Consumer / Rideshare | UBER + LYFT | $310 | $569 | 54.5% -- OVER CAP |
| Macau Gaming | LVS | $45 | $569 | 7.9% |
| Precision Ag / Tech | TRMB | $76 | $569 | 13.4% |
| Healthcare | ABT | $78 | $569 | 13.7% |

*UBER + LYFT entered before correlated cap was ratified Jun 28. No additional Consumer/Rideshare plays may be entered.*

**3.5/5 conviction cap (max 2 open when reserve < $1,000):**
| Position | Conviction | Status |
|----------|------------|--------|
| TRMB | 3.5/5 | Open -- slot 1 of 2 |
| LYFT | 3.5/5 | Open -- slot 2 of 2 |
| LVS | 4/5 | Open -- **CAP EXCEPTION** (documented Jun 29). Upgraded to 4/5 per Bearxter monitoring commitment. |

*Cap exception rationale: LVS earnings Jul 21 falls before TRMB exits Jul 31. Waiting = passing. LVS correlation to TRMB and LYFT is near zero (Macau gaming vs. precision ag vs. rideshare). Exception approved Jun 29. No further 3.5/5 exceptions without explicit session review.*

---

## CLOSED POSITIONS

| Date closed | Ticker | Play | Entry | Exit | P&L | Result |
|-------------|--------|------|-------|------|-----|--------|
| Aug 4, 2026 | DIS | $105C x1 Aug21 | $0.87 | $1.26 | +$39 | Sold same-day ahead of the Aug 5 AM print, per Tab 4's default sell-the-ramp exit (3.5/5 conviction, no binary hold-through flag). Stock was still ~$98, well OTM, meaning the +45% gain was pure pre-earnings IV expansion, not the stock closing the breakeven gap -- exactly the premium the rule exists to capture before it either crushes on the print or evaporates on an adverse move overnight. Order log confirmed: entry filled 2026-07-30T19:17:04Z, exit filled 2026-08-04T17:21:16Z. Archived: `Baxter/data/contract_history/DIS_105C_Aug21_closed_aug04.txt`. |
| Jul 29, 2026 | UBER | $90C x2 Aug21 | $0.65 | $0.09 | -$112 | Rule 6 re-check found the required move (+28.6%) at roughly 4x the 1.5x-median ceiling built from six real quarters of UBER earnings-day reactions, the most decisive Rule 6 fail the fund has seen -- worse than TRMB or LVS were at entry. Platform-computed chance of profit: 2.3%. Rule 4 technically held (Buy floor still ~$100-107) but a fresh BofA cut (Waymo competitive threat, Jul 27-28) and internal restructuring news gave no reason to wait out the Aug 5 print for a move nothing in its history has delivered. Sold into the pre-print premium rather than let it decay to zero. Worst full-position loss of the closed book by dollar amount, but the correct exit against the math -- this one earns its loss instead of being a process failure like LVS. |
| Jul 29, 2026 | TRMB | $65C Aug21, 2 contracts | $0.38 x2 | $0.70 (1, Jul 28) / $0.80 (1, Jul 29) | +$74 | The scale-out ladder banked half at $0.70 the day before a print the ledger thought was coming. Checking the date to answer Michael's sell-today question found the print was never Jul 30 -- real date is early-to-mid August, still unconfirmed to the day. With no near-term catalyst left to hold for, sold the runner same-day at $0.80 (+110.5%) rather than sit on theta into an uncatalyzed gap. +$74 total on $76 risked, the fund's best full-position return to date, and it happened despite the earnings date being wrong the entire time -- the divestiture-driven rally did the work the (wrong) catalyst was supposed to. |
| Jul 29, 2026 | LVS | $55C x2 Aug21 | $0.435 avg | $0.10 | -$67 | The standing Jul 20 sell-both-before-earnings order never became a real order in the account (see Jul 29 check-in). LVS reported Jul 22 after close, printed a fresh 52-week low the next session, and the position rode through it fully exposed. Closed Jul 29 for whatever was left -- $20 recovered on $87 at risk. Worst realized loss in the book. Lesson (Tab 5): a sell-by-date standing order needs a real resting/timed order in the system, same as a price-trigger ladder needs a resting limit -- a line in a file is not an order. |
| Jul 16, 2026 | ABT | $100C Jul17 | $0.78 | $1.05 | +$27 | **Corrected same session -- Michael's account, not the order-log guess:** a GTC limit sell was live and sitting through Wednesday; it never reached its limit price because the contract was down to $0.08 by Wednesday close. Michael deliberately did not override it with a manual sell into that weakness -- "I wouldn't have sold manually yesterday at all, it was always super negative." Thursday morning, after the earnings gap, he cancelled the stale limit and sold at the achievable $1.05. Not a missed order -- a live order that correctly declined to sell at a terrible price, plus a manual decision not to force one. Real peak was $1.95 (Jul 7, +150%) -- the scale-out ladder would have banked that if ABT weren't pre-audit and grandfathered to its own rule. Recovered $105 on $78 at risk. |
| Jun 16, 2026 | HITI | $2.50C x4 | $0.25 | $0.22 | -$12 | Revenue beat 42% ($179M vs $126M). Stock ran to $3.14 AH, faded to $2.58 at open. Sold limit at $0.22, $88 recovered. Exit rule held. HITI at $2.48 by mid-morning -- below strike. Rule vindicated. |
| Jun 15, 2026 | BSX | $60C Aug21 | $0.70 | $0.55 | -$15 | Rule 4 broke Jun 12 (bear floor moved to $55, below $60.73 breakeven). Exited Monday open. $55 recovered. New rule: Rule 4 on live position = same-day exit. |
| Jun 3, 2026 | CCL | $31C | $0.99 | $1.00 | +$1 | Thesis broken (stock below bear analyst floor). Cut and rotated to MDT. |
| Jun 5, 2026 | DSGX | $90C Jun18 | $0.45 | $0.15 | -$30 | Gap-and-fade. Sold early Jun 5 at $0.15 vs $0 expiry — recovered $15. Post-earnings entry at tail end of spike. Lesson: short-dated OTM entries on post-earnings gaps are structurally disadvantaged. |
| Jun 5, 2026 | CHWY | $24C Jun18 | $0.56 | $0.33 | -$23 | $24 strike too far OTM with stock at $20.50. Sold Jun 5 pre-earnings to free capital for DKNG. Recovered $33 vs $0 projected at expiry. |
| Jun 10, 2026 | NKE | $50C Jul17 | $1.86 | $1.16 | -$70 | RBC downgraded to Sector Perform, cut target from $70 to $50. Analyst specifically cited World Cup as insufficient catalyst. Thesis weakened — cut with 20 days left rather than hold a broken thesis. Recovered $116. |
| Jun 10, 2026 | MDT | $85C Jul17 | $0.54 | $0.77 | +$23 | Catalyst (Jun 3 earnings beat) already fired. Stock fading with no remaining catalyst before Jul 17 expiry. Applied Sheldon's BOTZ lesson: themes without catalysts are dead money. Cut at +52%, recovered $77. |
| Jun 12, 2026 | DKNG | $27.5C Jul02 | $0.49 | $3.00 | +$251 | Exited at open on World Cup Day 2. Sentiment window closed. Handle is real but invisible until Aug 5 earnings -- no visible data mechanism before Jul 2 expiry. Michael applied BOTZ rule. Baxter agreed. Sold the door when the door was open. |

---

## PASSES AND WATCH LIST

See  at repo root. Full monitoring system with three outcomes (Keep Watching / Stop Watching / Create New Pitch) updated every Monday.

**Quick screen-outs (not in passes.md -- failed first filter):**
| Date | Week | Ticker | Reason | Research file |
|------|------|--------|--------|---------------|
| Jun 1 | 1 | KBH | Beat-then-fall confirmed Q4 2025, no differentiating catalyst | none |
| Jun 1 | 1 | WGO | Negative expected value (-11%) | none |
| Jun 1 | 2 | CALM | Commodity earnings cliff -- 52-week low is a supply-shock unwind, not a beaten-down setup | week-02/research/research_CALM.md |

---

## DAILY CHECK-IN FORMAT
*For morning car ride update to Patrick:*

```
DATE:
NKE ($50C Jul17): Stock at $[price] | Option ~$[price] | [any news]
ABT ($100C Jul17): Stock at $[price] | Option ~$[price] | [any news]
Action needed: [none / sell / watch closely]
Next catalyst: [date and event]
```

---

## MACXTER STANDING ALERTS
*Political/macro items to check weekly:*

- Any Trump Truth Social mention of NKE, ABT, DKNG, or their sectors
- Any executive financial disclosure filings for NKE/ABT/DKNG insiders
- World Cup news that touches Nike brand or US viewership numbers
- Healthcare regulatory announcements affecting device/diagnostics sector
