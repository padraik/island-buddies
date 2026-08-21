# ISLAND FUND -- POSITIONS TRACKER
*Updated after every trade. Baxter reads this at the start of every check-in session.*

---

## SWEEP COUNTER -- DO NOT SKIP
**Closed positions since last take-profit sweep: 2 of 5.** (TIGR closed Aug 21, -$1 -- real fill $0.50 against a mark that was quoting $0.725 on a $0.35/$1.10 spread; the mark was never real, the bid was. YALA closed Aug 17, -$10. Sweep run #3 completed Aug 12, 2026, same session as the BTBT close that triggered it, on the 5 closes since Aug 4: LYFT remainder, KR, JMIA, UAMY, BTBT. Full re-derivation: `week-08/research/take_profit_sweep_aug12.md`. Verdict: no threshold changes -- neither winner that round (LYFT +28.9%, BTBT +21.4%) ever reached even a +50% flat cap, so every tested cap level produced an identical result to the actual outcome. Real finding carried forward, not a rule change yet: this is the second independent signal [alongside Brandt's still-unratified DTE question] that the sell-the-ramp default may be capping upside before the profit ladder ever gets a chance to fire.)

Protocol: every time a position closes, the same edit that logs the close in this file increments this counter. When it reads 5 of 5, Baxter runs the take-profit sweep (`week-06/research/take_profit_sweep_jul10.md` is the template) BEFORE the session's check-in, re-derives the ladder thresholds from the new winner distribution, and resets the counter. This is not Michael's job to remember. It is wired into the file Baxter cannot start a session without reading.

**Sweep agenda addition (Jul 30, 2026, ratified):** the next sweep also runs the Rule 5 counterfactual log (`week-07/research/fable5_verdict_rule5_restructure_jul30.md` Section 8) -- for each Rule-6-era close, what the nearest archived closer strike would have returned at equal budget. The Rule 5 unlock (caps above $1.00, see binder Tab 1/Tab 6) stays locked until 3+ Rule-6-era closes exist AND reserve is at or above $1,500, reviewed on this log at the sweep where both conditions are met. **Rule-6-era closes so far: 1 (DIS, Aug 4).** The $101C counterfactual pull was NOT completed in the Aug 4 sweep (live trading session took priority) -- still queued, still the first A/B feeding this log, milestone still unreachable regardless (needs 3+ closes and $1,500+ reserve).

---

## FUND STATE

| | |
|---|---|
| Total capital | $1,075.96 (post TIGR close -$1, cost basis) |
| Michael seed (birthday money) | $200.00 |
| Dad contribution (Jun 1) | $300.00 |
| Michael contribution (Jun 16) | $434.00 |
| Deployed | $128.00 (BILI only, real fill) |
| Reserve | $947.96 |
| Realized P&L | **+$123** (CCL +$1, DSGX -$30, CHWY -$23, NKE -$70, MDT +$23, DKNG +$251, BSX -$15, HITI -$12, ABT +$27, LYFT ladder partial +$90, TRMB (trim + close) +$74, LVS -$67, UBER -$112, DIS +$39, LYFT close +$26, KR close -$40, JMIA close -$24, UAMY close -$34, BTBT close +$30, YALA close -$10, TIGR close -$1) |
| Unrealized P&L | **-$7.00** -- BILI only (mark $0.605/share x2 = $121.00 vs $128.00 cost, 2026-08-21T17:38:26Z). |
| All-time high | $1,202.00 cost-basis (Jul 29, pre-UBER-close) -- still the record; $1,075.96 doesn't clear it |
| Distance to island | $4,998,924.04 (cost basis) |

---

## OPEN POSITIONS

| Ticker | Play | Ask (at approval) | At risk | Expiry | Catalyst | Status |
|---|---|---|---|---|---|---|
| BILI | $17.50C Aug 28 2026 x2 | $0.65/share | $128 (real fill) | Aug 28, 2026 | Q2 earnings, Aug 27 AM (verified) | **FILLED Aug 19, 2026, 9:35:07am ET, avg $0.64/contract ($128 total, real fill, $2 better than the $130 approval estimate) -- order 6a85b10a, confirmed via live order log.** |

Fill correction on BILI: the approval note below said "buying at market open Aug 20" -- that was a same-session dating slip. The approval itself landed in the very early hours of Wednesday (commit timestamp 07:46 UTC = ~3:46am ET, Aug 19), before Wednesday's own market open -- so "the next open" was Wednesday's, Aug 19, not Aug 20. Real fill confirms it: trade_date 2026-08-19, filled 9:35:07am ET, same morning as the approval, not the day after. Corrected here per standing discipline (Tab 6) rather than left to drift.

---

## CHECK-IN -- AUG 21 (Friday) -- TIGR CLOSED ON A THIN-SPREAD MARK, BILI HOLDS

Routine Friday check-in, both positions pulled live before writing anything down. BILI was quiet -- stock $17.06 vs $16.66 prior close, up slightly, still OTM against the $17.50 strike, mark $0.605 vs $0.64 entry (-$7 unrealized), no Rule 4 concern, Aug 27 AM print six days out. Hold, no action.

TIGR was not quiet. Stock jumped from $5.07 to $5.34 intraday (+5.4%) with no dated headline found on a direct search -- checked before saying anything about a catalyst that might not exist. That move put the $4.50C deep ITM, comfortably past the $5.01 breakeven, and the quoted mark ($0.725) implied a +42% unrealized gain on the single contract.

Flagged two real problems with that number before recommending anything: the option market itself was a $0.35 bid against a $1.10 ask on zero volume and 6 open interest -- the mark was the midpoint of a spread that wide, not a price anyone could actually transact at -- and this is a single contract, so the scale-out ladder doesn't apply (the ABT rule: one contract either rides whole or sells whole, no scaling). Earnings print is Aug 26 AM, five days out -- too early for the standard sell-the-ramp window, so nothing here was a mechanism-forced exit. Put the real question to Michael: hold five more days into a print this name has a documented history of getting wrong (4 of last 6 quarters moved down), or bank the move now while it's real.

**Michael's call: take the TIGR money.** Execution note: this account (5UB86831) isn't wired to the agentic connector, so Michael placed the sell himself. Recommended a $0.50-0.55 limit rather than chase the $0.725 mark, since Robinhood's own fill-probability read put $0.496 as the realistic fast-fill price. **Real fill, pulled from the order log before writing it down: $0.50/share, 1 contract, $50 total, order 6a889082, 1:53pm ET.** Entry was $51 -- **-$1 realized.** The lesson isn't the direction call, it was right to take profit off a name with a mixed earnings history rather than press a lucky pre-catalyst pop -- the lesson is that the mark price on a thin contract is not real money until it's a fill, and this is the clean, cheap version of that lesson landing on real dollars instead of an expensive one.

**Fund after the close: $1,075.96 cost basis, $128 deployed (BILI only), $947.96 reserve, realized P&L +$123.** Sweep counter: 2 of 5 since the last re-derivation.

---

## SCREENING -- AUG 19 (Wednesday night) -- FULL-UNIVERSE SWEEP, BILI APPROVED

Michael: "screen fresh names tonight. we are sitting idle. lets go until we're sure its not because we didnt look." Full 7-band scanner sweep, $300M-$150B+, 398 raw earnings-window names, 371 real after excluding closed-end funds. 92-name CALLS-zone. 10 killed on calendar/data integrity before a single search (KDK's real print already happened, WB reports same-day, others had self-contradicting dates). Of the real survivors, FINV/NOAH died on zero bid, LI died on Rule 3 (zero Buy ratings, Hold consensus, five recent cuts -- WB's exact shape). **BILI cleared everything**: 6.7th percentile, Strong Buy consensus, Rule 6 needs +4.8% against a real 6-quarter median of 6.1%. Full five-Baxters meeting held -- Bearxter's real objection was 50-lot open interest, not the thesis; sized to 2 contracts instead of 4 to respect the thin market. **Michael approved. Buying at open Aug 20 himself.**

Full docs: `week-08/research/research_BILI.md`, `week-08/research/screening_log_aug19_fullsweep.md`.

Backlog, queued not urgent: 62 of 92 CALLS-zone names never reached Rule 2 tonight. TIGR and DKS cleared chains clean, need a Rule 3 pass. GME, WDH, XPEV, NIO, PLAY, ABAT, BRAI, CHA, LEN, FIZZ are verified-date survivors never chain-checked.

---

## SCREENING -- AUG 16 (Sunday night) -- 64 NAMES RUN, ZERO ADVANCES, ONE NAME QUEUED FOR AUG 27

Michael's instruction: run 50 names, stop early at 2 plays landing 4/5. Two scanner bands ($300M-$2B, $2B-$10B) produced 64 bottom-quartile CALLS candidates -- past the floor. 17 cleared Rule 2 (earnings inside 31 days); chains and real historical earnings-move data (pulled from actual daily bars, not estimated) narrowed that to 8 with real reachability; 3 (WB, KLAR, GAP) reached full DD.

**All three died or stalled on Rule 3/4, not Rule 6:**
- **WB (Weibo): KILL, Rule 3.** Best Rule 6 margin of the night (needs 1.7% vs a 5.58% cap), but a real, dated Underperform from BofA ($8.00 target, cut from $8.70, tied to Q1's declining MAU/DAU) surfaced once the search moved past a conflicting surface "Buy consensus" label. TipRanks' more current read: Moderate Sell. Decisive Rule 3 fail on real data.
- **KLAR (Klarna): KILL, Rule 4.** Clean Rule 3 (13 Buy / 0 Sell), best-passing Rule 6 on a thin 3-quarter sample. But the lowest confirmed **Buy-rated** target (UBS, $23.00) sits below both viable breakevens ($24.00/$24.35) -- Morgan Stanley's freshly-raised $21 doesn't count, it's Equal Weight, not Buy.
- **GAP: QUEUED, not killed.** The name flagged Aug 8 for "a second look closer to Aug 27" -- this was that look. Rule 6 is now comfortable at the real Aug 28 expiry (10.3% needed vs 22.36% cap, 46% used). No confirmed Sell ratings. But Rule 4's floor is still unresolved: every recent cut found (Barclays $20, Citi/Wells Fargo $22-23) is Hold-rated and doesn't count, and the one dated Buy target found (Telsey, $34) is from May -- likely stale against the 60-day freshness rule. Needs one more clean pull before Aug 27, not scored tonight.

Full log: `week-08/research/screening_log_aug16_50batch.md`. No trades. Fund unchanged: cost basis $1,086.96, deployed $100 (YALA), reserve $986.96.

---

## CHECK-IN -- AUG 17 (Monday) -- YALA SOLD THE RAMP, EARLY AND SMALL, TREND CALLED IT RIGHT

Live-tracked all morning ahead of tonight's PM print. Stock opened flat at $5.48, and the first two-minute read (mark spiking toward +30% on a $0.25-wide bid/ask, 17 open interest) was thin-liquidity opening noise, not a real move -- correctly not acted on. But the trend that followed was real: stock ground down through the session, $5.48 -> $5.365 -> $5.355, and the option mark tracked it down from $0.575 (+15%) to $0.525 to $0.45 (-10%), each check confirmed live, not off the app.

No Rule 4 breach (no fresh downgrade found, Buy-side targets still $6.90+), no stop technically triggered -- but the standing plan already committed to selling before today's close regardless of price, ahead of tonight's PM print, and the premise for waiting on an afternoon IV ramp was failing in real time as the stock kept drifting the wrong way. Called it early rather than wait for the mandatory close-out: sell now, don't hope for a reversal that wasn't showing up.

**Execution, and a real number worth flagging:** Michael's own $0.45 limit didn't fill and was cancelled; the follow-up order was placed at $0.40 but the real fill came in at **$0.45 -- price improvement over his own limit**, both contracts, 1:14 PM ET, confirmed via `get_option_orders`. Michael reported it as a $0.40 sale; the real number was better. Same discipline as every other close in this book (LYFT's $120-vs-$116, KR's $0.70-vs-$0.50) -- this time the surprise ran in the fund's favor instead of against it.

**Final: 2 contracts sold at $0.45/share, $90 total, on a $0.50 entry ($100 cost). -$10 realized (-10%).** The resting $1.20 stretch GTC on the other contract came off with the same cancel -- never close to filling once the stock turned down. Cheap tuition: the entry thesis (9th-percentile low, no bad news, $150M buyback) never got a real test either way, since the earnings-day reaction this was supposed to ride hasn't happened yet as of this close. Small, early loss beats holding a fading OTM position into a binary print with the trend already against it.

**The fund is fully in reserve, zero open positions, for the first time since Aug 6.** Sweep counter: 1 of 5 since the last re-derivation.

---

## CHECK-IN -- AUG 14 (Friday) -- YALA'S RAMP-SELL DATE WAS WRONG, CORRECTED BEFORE ANYTHING GOT SOLD

Today's own ledger entry said sell the ramp today. Checked it before doing that, because "today" felt off against how the fund actually exits into a PM print. It was off. Monday Aug 17 is a real trading day -- the print lands after its close, not before its open -- so Monday is inside the window, the closest real session to the print the fund has, and per the ABT/DIS precedent that's exactly where IV peaks. Selling today instead would hand back three days of premium build for no reason: the Friday date was itself a fix for an earlier "Aug 15-16" weekend error, and the fix overshot past a real trading day instead of landing on it.

Checked the resting $1.20 GTC first: still confirmed, unfilled, untouched since Tuesday -- nothing forced a decision today either way. Live numbers: stock $5.42 (flat since entry, needs +1.5% to the $5.50 breakeven), option mark $0.43 on the $0.50 fill, pure theta decay, no news, ratings floor clean (Buy consensus, targets $6.90-$8.40+, all well clear of breakeven). Nothing here argues for an early exit on the merits -- this was a calendar bug, not a risk call.

**No trade today. Corrected the Open Positions table above: sell the ramp Monday Aug 17, before the close, ahead of the PM print.** Fund unchanged: cost basis $1,086.96, deployed $100 (YALA), reserve $986.96.

---

## CHECK-IN -- AUG 12 (Wednesday) -- YALA FILLED, BTBT UP 30% ONE DAY BEFORE ITS OWN PRINT

Startup routine caught the YALA fill before Michael reported it -- pulling the real order log turned up **2 contracts, $5.00C Aug 21, filled $0.50/share, $100 total, 9:33 AM ET**, better than the $0.65 quoted at research time. Ladder GTC also already resting: sell 1x at $1.20, confirmed `time_in_force: gtc`. One note, not urgent: the $1.20 trigger is 2x the $0.60 limit Michael had set, not 2x the real $0.50 fill (which would be $1.00) -- the binder's own +100% rule technically means $1.00. Flagging it, not fixing it unasked; either number is a real, resting GTC, just a slightly higher bar than the rule states.

**BTBT closed same session -- the "wait until tomorrow" call above was wrong, caught and fixed within the hour.** Every note tonight, including this file's own entry line and `research_BTBT.md`, said the Aug 13 print was PM. It is **AM, verified true** -- Michael questioned it directly and a live `get_earnings_results` pull confirmed the real timing. AM release means the reaction prices in at tomorrow's open, before tomorrow's session even starts trading -- there was no "sell tomorrow before the close" window to wait for. Today, with roughly 25 minutes left in the session, was the actual sell-the-ramp day.

Cancelled the resting $0.70 ladder GTC (moot once the whole position was being sold into the ramp rather than a partial trigger) and sold all 4 contracts same session. **Filled: 2 at $0.42, 2 at $0.43, $170 total, 7:38 PM UTC (~3:38 PM ET), real order-log fill confirmed via `get_option_orders`, matches Michael's report exactly.** **+$30 realized (+21.4%)** on the $140 cost -- banked before an AM print the position would otherwise have ridden into blind, with the stock already up 9% and the option up 30% same-day. Contract archived: `Baxter/data/contract_history/BTBT_1C_Aug21_closed_aug12.txt`.

**This is BTBT's close as the fund's 5th since the last sweep -- the take-profit sweep is due before this check-in closes, per binder Tab 6 (not something to defer to next session). Full re-derivation: `week-08/research/take_profit_sweep_aug12.md`.**

YALA's own ramp-sell is Friday Aug 14 (corrected same session from an initial Aug 15-16 error -- those are the weekend, not tradeable). No action needed there today either.

Fund after YALA: cost basis $1,056.96 unchanged, deployed $240 (BTBT + YALA), reserve $816.96. Two open positions.

---

## CHECK-IN -- AUG 11 (Tuesday) -- JMIA CALLED FOR THE RAMP EXIT, DAY-ORDER GAP FOUND ON BOTH LADDER TRIGGERS

Both scale-out ladder GTCs from yesterday's plan are confirmed resting on the account (JMIA sell 1x at $0.90, UAMY sell 1x at $1.00, both placed ~12:10 PM ET this morning). Neither is close: both contracts are down since entry, not up. **Real gap found checking them: both orders are `time_in_force: gfd` (good for day), not GTC.** The binder's own Jul 20 standing rule ("every armed ladder trigger exists as a resting GTC limit order from the moment it arms") assumes the order persists until it fires or the position closes. A day order does neither -- it vanishes at the close if unfilled, silently, same failure shape as the LVS standing-order gap in July. Needs re-placing each session until one of the two things happens. Flagging in binder Tab 5.

**JMIA called for the sell-the-ramp exit today, per Tab 4 default, not held through tomorrow's print.** Aug 12 AM earnings puts today inside the 24-48h ramp window. Live check: stock $5.77 (down from $6.20 at Saturday's DD, $5.87 at Monday's entry), option mark $0.35 (bid $0.30/ask $0.40), down from the $0.45 entry. The contract is OTM against its own $6.00 strike right now, not just against breakeven. No binary-hold flag was documented at entry (would need 4/5+ conviction and a written Bearxter condition), so the default applies without exception: sell into whatever premium is left rather than hold into a binary print. Recommended cancelling the resting $0.90 GTC and closing both contracts near $0.33-0.35. **Filled: 2 contracts at $0.33/share, $66 credit, 2:10 PM ET, real order-log fill confirmed via `get_option_orders` and matches Michael's report exactly.** The $0.90 GTC came off cleanly with the close (confirmed no longer resting). **-$24 realized** on the $90 cost, better than the ~$30 estimated against the bid at the time of the call. Contract archived: `Baxter/data/contract_history/JMIA_6C_Aug14_closed_aug11.txt`. Sweep counter: this is close #3 of 5 since the Aug 4 re-derivation (LYFT #1, KR #2 backfilled same session, see counter note above).

**UAMY WAS at a decision point today, and every session note since entry had the wrong date.** Michael questioned this from memory around 2 PM and asked for a live re-check. `get_earnings_results` confirmed live: **Aug 11, 2026 PM, verified: true.** Today. Not Aug 14 AM.

Root cause, checked directly: this was never a data-source failure. `research_UAMY.md`, written Saturday Aug 8, has the correct date in plain text: *"Confirmed catalyst: Q2 2026 earnings, Aug 11, 2026, PM, `get_earnings_results` verified: true."* It even flagged the tight buffer this creates (PM release, reaction lands Wednesday's open, three trading days before the Aug 14 expiry). The error was introduced when the position was logged into this file's Open Positions table on Aug 10: written as "Aug 14, 2026 AM" against the research doc's own correctly-verified "Aug 11, 2026 PM," and never cross-checked against the source doc again through Monday's entry, Monday's check-in, or this morning's check-in. Three separate write-ups repeated the wrong date with full confidence, including this file's own Aug 10 and Aug 11 (earlier) entries above. Full postmortem: binder Tab 5.

Live check at the time: stock $6.49, option mark $0.35 (bid $0.30/ask $0.40), ~90 minutes left before the close and the print. Sold the ramp under real time pressure rather than 24-48 hours ahead of it -- same Tab 4 default as JMIA, just discovered hours before the print instead of a day and a half before. **Filled: 2 contracts at $0.33/share, $66 credit, 2:20 PM ET, real order-log fill confirmed via `get_option_orders`, matches Michael's report exactly.** The $1.00 GTC came off cleanly with the close. **-$34 realized** on the $100 cost. Contract archived: `Baxter/data/contract_history/UAMY_6.5C_Aug14_closed_aug11.txt`. Sweep counter: close #4 of 5 -- **the next close triggers the full take-profit sweep before that session's check-in opens.**

**The fund is fully in reserve, zero open positions, for the first time since Aug 6.**

**New position entered same session: BTBT.** After both closes, Michael asked to run the newly-ratified scanner method to source the next play (full detail: `screening_log_aug11_scanner_sweep.md`). Three market-cap bands, 18-name shortlist, full funnel run at Michael's request ("look at the 18 for what they are" rather than pre-filtering to survivors only) -- SOC killed for already having reported (scanner date was stale), KEP/QFIN deprioritized on unverified multi-week date drift, CSAN killed for having no options chain, LI and NNE killed decisively on Rule 6, XPEV and GEMI killed on real Sell-rating counts despite the best Rule 6 math of the batch, STNE and WB flagged soft-kill/uncertain. Two survivors: BTGO and BTBT. BTGO looked strongest on a first pass but died on a deeper check -- every Buy-rated analyst target on file predates its Q1 earnings miss and an active securities lawsuit; the only post-miss analyst action found is a Hold, not a Buy, which fails the binder's own Rule 4 freshness standard (full writeup: `research_BTGO.md`). BTBT is the opposite case: a fresh, dated, reasoned analyst raise (Craig-Hallum, late July, citing a real unpriced asset -- BTBT's 70% White Fiber stake and unrecognized ETH holdings) issued after the sector's worst news, not before it. Pitched at 4/5 conviction. **Filled: 4 contracts, $1.00C Aug 21 2026, $0.35/share, $140 total, 3:03 PM ET, real order-log fill confirmed via `get_option_orders`, matches Michael's report exactly.** Breakeven $1.35, needed +3.1% at entry against an 8.24% Rule 6 cap (38% used) on a full 4-quarter real sample. Full research and Five Baxters debate: `research_BTBT.md`.

Fund closes the session: cost basis $1,056.96 unchanged (two closes and one entry netted against reserve, not cost basis), deployed $140 (BTBT), reserve $916.96. One open position.

---

## CHECK-IN -- AUG 10 (Monday) -- KR CLOSED (-$40), UAMY AND JMIA ENTERED, BTDR KILLED, TASK SCHEDULER FOUND SILENTLY FAILING

The scheduled `IslandFund_MondayVerify` Windows task (7:35 AM ET, running `monday_verify.ps1`) fired on time but did nothing useful -- its log shows the Claude invocation inside it died immediately on `OAuth session expired and could not be refreshed`. No prices were pulled, no rules re-verified, before Michael asked. Re-ran the check live instead, same session.

**KR closed this morning -- a real calendar trap, caught same-day, not a discretionary bail.** Pulling the real order log to verify the UAMY fill turned up a second order: **2x KR $61C Sep 4 sold at $0.30/share, $60 credit, filled 10:36 AM ET** -- before either of today's entries. The reason: `get_earnings_results` on KR this morning now shows Q2 FY2026 earnings at **Sep 10, 2026 AM (verified: false)**, not Sep 4. The contract's own expiry was Sep 4 -- the catalyst it was bought for was never going to happen before the contract died. Same failure family as HIVE's Aug 21 trap and BKE's "exact KR structural problem" from Saturday's screen (both flagged the same week), except caught live instead of lingering -- and worse than either, since this isn't a same-day collision, it's the print landing six days past expiry. Holding to the Sep 2-3 planned ramp-sell window would have meant selling into IV built around a catalyst the contract could never see. Selling now for $0.30 (**-$40 realized** on the $100 cost, still the fund's first loss inside an at-entry-valid Rule 6 read) beat letting it decay toward zero on a dead thesis. **Real gap that remains: the close happened at 10:36 AM and wasn't written into the ledger until this session caught it in the order log three entries later** -- closes need the same same-session logging discipline entries already get. Contract archived: `Baxter/data/contract_history/KR_61C_Sep4_closed_aug10.txt`.

All three Saturday advances (UAMY, JMIA, BTDR) moved against Friday's DD baseline over the weekend:

- **BTDR: killed.** Stock fell from $10.89 (Fri close, DD baseline) to **$9.07**, about -16.7%. The $11.00C Aug 14 now needs **+29.2%** to breakeven ($11.75) against the 18.81% Rule 6 cap -- 155% of the cap, a decisive fail (was 47% of cap Saturday). Not entered.
- **UAMY: entered.** Stock $6.85 -> $6.71. $6.50C Aug 14 needed +8.3% against 11.75% cap on the live chain check (70% of cap, up from 37% Saturday) -- still real margin. **Filled: 2 contracts at $0.50/share, $100 total**, real order-log fill matches Michael's report exactly.
- **JMIA: entered.** Stock $6.20 -> $5.87. Bearxter's Saturday flag (re-pin the $7.37 Rule 4 floor before Monday's fill) independently re-corroborated live before entry -- real, current, reaffirmed Moderate Buy consensus Aug 6. Sizing recomputed against the post-KR-close, post-UAMY reserve ($954.96 at the time) rather than Saturday's stale $1,054.96 figure; live ask had also dropped to $0.50, well inside the recalculated ceiling. **Filled: 2 contracts at $0.45/share, $90 total**, better than the pre-entry estimate.

**Standing item: the Monday-morning auth failure needs a real fix**, not just today's manual workaround -- the task scheduler will silently no-op again next week on the same stale-OAuth failure mode unless the login refresh is addressed.

Fund after all three events: cost basis $1,114.96 (KR's -$40 loss booked), deployed $190 (UAMY + JMIA), reserve $924.96. Two open positions. Realized P&L +$162.

---

## RESEARCH -- AUG 8 (Saturday) -- SIX-NAME BATCH, 0 ADVANCES, ONE REAL FLAG WORTH CARRYING FORWARD

Six names carried in from an earlier screening pass (DQ, CPRT, ENVX, HIVE, BILI, GAP), each with Rule 1/Rule 2 and a chain already found. Full re-verification run tonight: live prices, `get_earnings_results` on every name before trusting any date (per the Aug 7 standing rule), real historical earnings-day moves pulled from actual daily bars for Rule 6 (not estimated), and a straddle cross-check where Rule 6 didn't already kill the name outright. Full detail in each `research_TICKER.md` file, week-08/research. **All six killed. Zero advances.**

**CPRT:** Rule 6 decisive fail. Needed +12.27% to breakeven against a 3.43% cap (median historical move only 2.29%), the worst reachability mismatch of the batch, about 3.6x the ceiling. Also surfaced a live earnings-date disagreement (tool's unverified Sep 3 vs. multiple searches leaning Sep 9), moot here but worth remembering if CPRT resurfaces.

**HIVE:** Rule 6 decisive fail (needed +12.28% vs. a 6.52% cap, about 1.9x over) plus a genuinely unresolved earnings date (tool's unverified Aug 21 PM vs. a search-sourced Aug 18 PM, no company press release found for either). If the worse-case date and timing had been right, the Aug 21 contract would have expired before its own after-hours print ever happened, the same trap that put KR into the ledger on a wrong date, in a structurally worse form. Confirmed a later, tradable expiry chain exists (Aug 28, Sep 4, and beyond) that would fix the timing problem, but Rule 6 kills it regardless of expiry chosen.

**BILI:** Rule 6 fail (needed +10.94% vs. an 8.17% cap, about 1.34x over). Also corrected the earnings date: real, verified date is **Aug 27 AM**, not Aug 26 as carried in from the earlier screen, tightening the buffer to about one day.

**DQ:** No hard rule failure, but everything sits at the edge rather than with margin. Rule 6 passes at 91% of its cap (needed +11.26% vs. 12.32%), the tightest pass of the batch. Rule 3 coverage is only about 3 analysts, disagreeing with each other on Buy vs. Hold. The $16C chain (ask $0.40, bid $0.05, confirmed real and matching the pre-screen) has an 8x bid/ask spread, and a straddle attempt at the $15 strike came back unusable (the call side has a $0.00 bid). One-day earnings buffer (Aug 20 AM print, Aug 21 expiry). Score around 2.5/5, held out.

**ENVX:** The most interesting result of the batch. Best Rule 6 read of the six (needed +10.62% against a 25.27% cap, using only 42% of it) and the straddle confirms it (market-implied move 19.1%, well above what's needed). Killed anyway on decline category: the May 13 print beat on both EPS and revenue and the stock still fell about 17% after hours, because JPMorgan had downgraded to Underweight the week before on smartphone-battery qualification delays and a narrowing competitive edge, not on the numbers. That JPMorgan Underweight also contradicts the "0 Sell ratings" figure most aggregators show, a real Rule 3 discrepancy, not just a decline-category one. Textbook see-through risk: a beat the market priced past because the forward problem wasn't in the print. Score around 2.5/5.

**GAP:** The closest of the six to a real pitch, and the one worth remembering for next time. Clean Rule 3 (12 Buy / 7 Hold / 0 Sell), Rule 6 passes with real margin (needed +13.42% vs. a 16.99% cap, 79% used, the second-best of the batch). But the straddle cross-check disagrees with Rule 6 for once: the live options market implies only a 12.5% move, short of the 13.42% needed, the opposite relationship from every other name checked tonight. Rule 4's floor is unresolved (the visible $20 low target belongs to Evercore, now Hold-rated after a downgrade, so it doesn't count; the real Buy-rated floor could not be pinned to a specific fresh, dated target in the time available). Decline picture leans Category 2: Old Navy guided its full-year outlook down, Athleta is on a second consecutive year of double-digit comp declines, tariffs are a quantified 200bp margin hit, and the Street is actively split rather than settled (Evercore and JPMorgan cutting, UBS and Barclays raising, same week). Score around 2.5 to 3/5, worth a second look closer to the Aug 27 print if the Rule 4 floor and the straddle move together.

No trades tonight. Reserve unchanged at $1,054.96, KR remains the fund's only open position.

---

## RESEARCH -- AUG 8 (Saturday) -- 7-TICKER DD BATCH (PFLT, PLUG, TME, UAMY, BKE, QXO, BTDR), 2 ADVANCES, 5 KILLS

A second name list run the same night as the six-name batch above, with Rule 1/2 and a chain already found going in. Every earnings date re-verified live via `get_earnings_results` first, per the Aug 7 standing rule -- all 7 matched the dates carried into the session, no drift found this time. Real historical earnings-day moves pulled from actual daily bars for Rule 6 on every name (not estimated), plus a straddle cross-check and a decline-category read on each. Reserve: $1,054.96 (unchanged, KR deployed separately).

**UAMY: ADVANCE, 4/5.** $6.50C Aug 14 2026, ask $0.65, breakeven $7.15, needs +4.4% from $6.85. Rule 4 cushion 81.8% (B. Riley Buy $13, raised Jul 2026, inside the freshness window). Rule 6: 4 real prints (+4.97%, -5.64%, -10.43%, -10.03%), median 7.84%, cap 11.75%, requirement uses 37% of cap; straddle corroborates (13.2% implied move vs 4.4% needed). Category 1 (production/capacity-growth story -- 2026 revenue guide $125M on tripled capacity, Galena JV, Nolan Creek Alaska mine advancing -- not deterioration). Caveats disclosed, not fatal: thin analyst bench (5 names covering), 3-day earnings buffer. Sizing: 13% of reserve, 2 contracts, $130 at risk. Full DD: `week-08/research/research_UAMY.md`.

**BTDR: ADVANCE, 4/5.** $11.00C Aug 14 2026, ask $0.85 (STRETCH, near the $1.00 Rule 5 transitional-lock ceiling), breakeven $11.85, needs +8.8% from $10.89. Rule 4 cushion 85.7% (Needham Buy $22, raised early Aug 2026) -- best floor of tonight's batch. Rule 6: 4 real prints (+7.24%, -19.74%, -13.51%, +11.57%), median 12.54%, cap 18.81%, requirement uses 47% of cap; straddle corroborates (15.9% implied vs 8.8% needed). Category 1 (sector-wide crypto/BTC sentiment swings, not company-specific decline -- H.C. Wainwright called the prior earnings selloff "overdone"). Caveat disclosed: underlying business carries real BTC-linked revenue volatility, contained by the option's defined max loss but not erased by it. Sizing: 16% of reserve, floor-divides to 1 contract, $85 at risk. Full DD: `week-08/research/research_BTDR.md`.

**PFLT: KILL, Rule 6 (structural, not this-quarter-specific).** BDC -- structurally too low-volatility on earnings for any workable strike. Median historical move 1.02%, cap 1.52%, requirement 1.6% -- fails by instrument type; three of four real prints moved under 3.5%, and half moved under 1.1%. Rule 3/4 were both clean; irrelevant given Rule 6. `week-08/research/research_PFLT.md`.

**PLUG: KILL, Rule 3 (decisive), kills both candidate strikes.** BMO Underperform ($1 target, reaffirmed Mar 2026) plus up to 3 Sell-class ratings found across coverage, exceeds the max-1 ceiling; average analyst consensus reads Hold, not Buy. Independently, the $2.00C candidate also now fails Rule 6 on live pricing (stock rallied 5.8% intraday since the strike was first flagged, pushing the requirement to 4.1% against a 2.78% cap); the $1.50C passes Rule 6 but is deep ITM with ~$0.04 of time premium on a $0.73 ask -- not a real bet on the catalyst. Rule 3 kills the name regardless of strike. `week-08/research/research_PLUG.md`.

**TME: KILL, decline category (Category 2) -- despite the best Rule 6 math of the batch.** Requirement (2.9%) uses only 19% of a 15.18% cap, corroborated by a 10.0%-implied straddle. Killed anyway: Mar 2026 -28.8% collapse on shrinking free users (-5% MAU) and rising competition, followed by an active, ongoing UBS/Morgan Stanley/JPMorgan downgrade cascade (Buy to Neutral, targets cut 40-70%) citing AI-driven piracy -- analysts following the business down, not correcting an overreaction. Same shape as ZTS (Aug 4). The night's clearest reminder that Rule 6 passing does not override a real decline-category read. `week-08/research/research_TME.md`.

**BKE: KILL, hard-flagged triple kill (the specific concern Michael raised going in).** Earnings (Aug 21 AM) lands on the only affordable expiry (Aug 21) -- the exact KR structural problem, checked live and confirmed real, not assumed. Checked for a later expiry per instruction: Sep 18 exists with real buffer, but every strike there fails Rule 5 (asks $1.85-3.30 vs the $1.00 transitional cap) and Rule 6 fails at every expiry/strike checked regardless (needs 5.1-7.5% vs a 2.78% cap -- this stock's own earnings moves are just too small, 3 of 4 real prints under 2.5%). No real Rule 4 floor either: coverage is 2 analysts, most current read is UBS Neutral $47 (not Buy-rated, doesn't count, and sits below breakeven anyway). `week-08/research/research_BKE.md`.

**QXO: KILL, marginal Rule 6 stacked on a zero-buffer timing collision.** Requirement (5.79%) clears the cap (5.85%, built from 4 real prints) by 0.06 points -- 99% of the cap used, the weakest real margin of anything screened tonight (vs. UAMY's 37% and BTDR's 47%), inside ordinary measurement noise. Combined with an Aug 13 PM print reacting into the Aug 14 expiry's own open -- the same zero-trading-day collision as BKE, one calendar day removed. Rule 3 and Rule 4 both passed with real room; those were never the issue. A later Aug 21/28 expiry with an affordable strike is flagged as worth a fresh look (Rule 4's wide cushion suggests room), not checked tonight. `week-08/research/research_QXO.md`.

No trades tonight -- both advances are pitch-ready for Michael, not yet entered. Reserve unchanged at $1,054.96.

---

## CHECK-IN -- AUG 7 (Friday, morning) -- KR ENTERED, THE FUND IS BACK IN THE GAME

Michael reported the fill as "$0.70." Pulled the real order before writing it down, per standing practice: **the $0.70 was the limit price, not the fill.** Real execution: 2 contracts at $0.50/share, $100 total, filled 10:06 AM ET. Price improvement, not a misreport in Michael's favor this time (LYFT's close two days ago went the other way, reported high; this one reported the ceiling, not the actual print).

This entry closes out a rough morning for Rule 6. KR's stock drifted from Monday's $58.22 down to the mid-$56s overnight and through the open, which pushed the required move up in real time -- the live $0.88-0.91 asks seen earlier this morning were failing the 9.0% cap outright (breakeven $61.88-61.91 against a stock at $56.65 needs 9.2-9.3%, over the line). Also caught and corrected in the same conversation: the previous night's re-verification had used Robinhood's API `break_even_price` field (mark-based) instead of the fund's own strike-plus-ask convention, understating the required move as 7.4% when the real number was closer to 8.0% even before the stock's Friday-morning drift. **The $0.50 real fill clears it for real:** breakeven $61.50, stock ~$56.5-56.65 at the time, required move 8.9-9.2% depending on the exact minute, genuinely at the edge of the cap rather than comfortably inside it like the original Aug 4 read (6.3%/9.0%). This is the thinnest-margin entry the fund has taken under Rule 6 to date. Worth watching closely, not a clean pitch anymore, a real one that needed the price to cooperate to stay legal at all.

Sizing landed better than either version discussed: **2 contracts, $100 total**, well under both the $161.69 nominal and the $184.79 ceiling -- cheaper than the $178 estimate used when planning around the $0.89 ask. Scale-out ladder is live on this position (2 contracts, standard trigger at +100%/$1.00 sells 1 of 2 automatically per Tab 4).

Fund: $1,154.96 cost basis unchanged, $100 deployed (KR), $1,054.96 reserve. First open position since LYFT closed Aug 6.

---

## CHECK-IN -- AUG 6 (Thursday, morning) -- LYFT CLOSED, THE FUND IS ALL CASH

Michael reported the close ("LYFT sold today for $120"); pulled the real order and quote before writing anything down, per standing practice. **Real fill: 1x LYFT $16C Aug21 sold at $1.16, not $1.20 -- $116 total, +$26 realized (+28.9% on the $90 remaining risk).** Filled 10:54 AM ET, well ahead of tonight's Aug 6 PM print, LYFT stock still mid-$16s and OTM against the $16.90 breakeven at the time of sale. This is the same shape as DIS's Aug 4 close: sell the pre-earnings IV ramp rather than hold into the print itself, on a position that was never going to clear breakeven on the stock's own legs.

This was the ladder's designed remainder -- 1 of 2 contracts came off automatically at the $1.80 trigger back on Jul 16 (+$90), and this was the second half, sold on judgment rather than a mechanism rule (no resting order existed by design; Michael cancelled the GTC Jul 20 so the runner could ride bare to the print). Combined, the full LYFT position returned **+$116 on $180 total risked** across both contracts.

**The fund now holds zero open positions -- fully in reserve at $1,154.96.** Realized P&L stands at +$202. Sweep counter: 1 of 5 since the Aug 4 re-derivation. Contract archived: `Baxter/data/contract_history/LYFT_16C_Aug21_closed_aug06.txt` (real order-log fill; `fetch_option_history.py`'s raw pull is still returning the pre-entry corrupted series first flagged Aug 4 -- worked around by hand again rather than debugged, since fixing the script doesn't clear the Fable 5 bar for a routine close). Next session's job is standing here in the open: an idle, fully-cashed reserve and no research queued behind it.

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

**PUTS BACK-TEST: FINAL VERDICT LANDED Aug 7 -- GATE SATISFIED, PUTS RUN UNDER A 21-DAY ENTRY-TIMING RULE, NOT A BLANKET BLOCK.** (Corrected Aug 19 -- this entry sat stale for 12 days citing only the Jul 16 interim.) Interim (Jul 16): six Jun 22 hypotheticals, four clean entries down 68-90% before any catalyst fired (theta bleed on 6-week-early entries), two (TTD, CMG) excluded as corrupted. **Final pass (Aug 7, one to three days early):** all four resolved catalysts confirmed catastrophic (-86% to -99.6%), zero winners, zero ambiguity. Verdict: far-dated (~60-day) entries into thin, single-catalyst OTM puts fail decisively -- a structural problem, not proof that options duration itself is bad (Michael's correction, folded into the final doc). **Rule adopted: no puts entry more than 21 days before the dated catalyst.** This satisfies the back-test requirement for good; puts conviction is still capped at 4/5 until three closed puts plays exist (binder Tab 6), and the back-test itself doesn't count as one of those three. **First real re-screen against this rule ran Aug 19** (Michael: "did we check for puts?") -- 184 PUTS-zone names sourced, 83 inside the 21-day window, 30 screened, zero survived (see `week-08/research/screening_log_aug19_fullsweep.md` Stages 6-7). Docs: `week-06/research/puts_backtest_data_jul16.md`, `puts_backtest_verdict_jul16.md`, `week-08/research/puts_backtest_final_verdict_aug07.md`.

**AUGUST RE-SCREEN QUEUE (from Jul 12 and Jul 20 batches):** AI (C3.ai, earnings Sep 9), PATH (UiPath, earnings Sep 8), **ASAN (Asana, earnings ~early Sep) and DOMO (Domo, earnings ~early Sep, added Jul 20)** — all four cleared R1 and live chain geometry but their prints fall outside every currently affordable expiry. Re-run with fresh Sep chains when they open in August; AI carries a hard flag (Q1 FY27 revenue guided ~$50-54M vs ~$87M yr-ago, probable Category 2) that must clear the decline-category test first. **TDOC** (91st percentile, cheap, violent prints) on the puts watch list — eligible for real screening now that the back-test gate is satisfied; needs its earnings date checked against the 21-day rule before anything else.

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
| Aug 21, 2026 | TIGR | $4.50C Sept4, 1 contract | $0.51 | $0.50 (real fill, order 6a889082, confirmed via live order log) | -$1 | Stock popped 5.4% intraday (no dated headline found) to $5.34, well past the $5.01 breakeven, and the mark quoted $0.725 -- but that mark sat in the middle of a $0.35/$1.10 spread on zero volume, 6 open interest. Flagged the thin-liquidity risk before Michael placed the order and recommended a $0.50-0.55 limit as the realistic fill zone rather than chase the mark. Real fill came in at the bottom of that range, $0.50 -- confirming the mark was never a tradable price. Single contract, no ladder possible (ABT rule), no rule forced the exit -- discretionary call to bank the move rather than ride 5 more days into an Aug 26 print on a name with its own documented mixed directional history (4 of last 6 prints moved down). Net result: essentially breakeven on real dollars despite the mark showing +42% moments earlier -- the lesson is the spread, not the direction call. |
| Aug 17, 2026 | YALA | $5.00C Aug21, 2 contracts | $0.50 | $0.45 (real fill -- Michael's own $0.45 limit missed, $0.40 follow-up got price improvement to $0.45) | -$10 | Standing plan was sell-the-ramp before today's close ahead of tonight's PM print. Stock ground down all session ($5.48 -> $5.355) instead of ramping; no Rule 4 breach, but the premise for waiting on an afternoon IV pop was failing live, so the mandatory close-out was called early rather than held to the wire. Cheapest tuition in the book -- the entry thesis was never actually tested, since the print this was built around hadn't happened yet. |
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
