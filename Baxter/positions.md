# ISLAND FUND -- POSITIONS TRACKER
*Updated after every trade. Baxter reads this at the start of every check-in session.*

---

## SWEEP COUNTER -- DO NOT SKIP
**Closed positions since last take-profit sweep: 1 of 5.** (Sweep last run Jul 10, 2026, on the first 8 closes. ABT closed Jul 16. NOTE: the LYFT ladder partial of Jul 16 -- 1 of 2 contracts sold at the $1.80 trigger, +$90 -- is a scale-out, not a position close; it does not increment this counter, but its fill data feeds the next sweep's winner distribution.)

Protocol: every time a position closes, the same edit that logs the close in this file increments this counter. When it reads 5 of 5, Baxter runs the take-profit sweep (`week-06/research/take_profit_sweep_jul10.md` is the template) BEFORE the session's check-in, re-derives the ladder thresholds from the new winner distribution, and resets the counter. This is not Michael's job to remember. It is wired into the file Baxter cannot start a session without reading.

---

## FUND STATE

| | |
|---|---|
| Total capital | $1,195.00 |
| Michael seed (birthday money) | $200.00 |
| Dad contribution (Jun 1) | $300.00 |
| Michael contribution (Jun 16) | $434.00 |
| Deployed | $383.00 (TRMB $76 + UBER $130 + LYFT $90 + LVS $87) |
| Reserve | $812.00 |
| Realized P&L | **+$242** (CCL +$1, DSGX -$30, CHWY -$23, NKE -$70, MDT +$23, DKNG +$251, BSX -$15, HITI -$12, ABT +$27, LYFT ladder partial +$90) |
| Unrealized P&L | Jul 20 marks (Monday, ~1 PM): TRMB $0.75 x2 (+$74 -- real chain ask; app showed $0.01 phantom AGAIN, third occurrence, never trust the app mark on this contract), UBER $0.31 x2 (-$68), LYFT $1.06 x1 (+$16), LVS $0.18 x2 (-$51). Book value $354 vs $383 deployed = -$29. Fund at mark: $1,166. |
| All-time high | $1,195.00 cost-basis (Jul 16, post-LYFT-ladder); $1,172 on marks Jul 16 |
| Distance to island | $4,998,805.00 |

---

## OPEN POSITIONS

| Entered | Ticker | Play | Fill | At Risk | Expiry | Catalyst Date | Exit Rule |
|---------|--------|------|------|---------|--------|---------------|-----------|
| Jun 17, 2026 | TRMB | $65C x2 | $0.38 | $76 | Aug 21, 2026 | Jul 30 earnings (Q2 2026) | Sell at open Jul 31. Exit same day if Wells Fargo (Revich) cuts target below $65. No averaging down. |
| Jun 18, 2026 | UBER | $90C x2 | $0.65 | $130 | Aug 21, 2026 | Aug 4 earnings (Q2 2026) | Sell at open Aug 5. Exit same day if any Buy analyst cuts below $90.65. BOTZ watch Aug 1. |
| Jun 18, 2026 | LYFT | $16C x1 (was x2; ladder fired Jul 16: 1 sold @ $1.80 trigger, +$90) | $0.90 | $90 | Aug 21, 2026 | Aug 5 earnings (Q2 2026) | Sell at open Aug 6. Exit same day if BMO cuts below $16.90. BOTZ watch Aug 1. Ladder on the remaining contract now lives as a resting GTC limit, not manual watching (see Jul 20 check-in). |
| Jun 29, 2026 | LVS | $55C x2 | $0.45 / $0.42 (avg $0.435) | $87 | Aug 21, 2026 | **Jul 22 earnings, AFTER CLOSE (date corrected Jul 20; ledger had Jul 21)** | **STANDING ORDER (ratified by Michael Jul 20): sell BOTH Wednesday Jul 22 into the pre-print IV ramp, before the close. Do not hold through the Wednesday-night print.** Straight application of Tab 4 (OTM 24-48h before earnings = sell the ramp; no ITM status, no binary flag at entry). Tripwire unchanged: exit same day if any Buy analyst cuts target to $55.42 or below. |


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

## RATIFIED JUL 10 (all four amendments approved by Michael)

*Full audit: `week-06/story/five_baxters_audit_jul10.md`. Selection-criteria follow-up: `week-06/research/selection_criteria_audit_jul10.md`. Binder updated (Rule 6, Tab 4 rewrite, standing decisions).*

**STANDING ORDERS from the audit:**
1. **ABT $100C Jul17: SELL Wednesday Jul 15 into the pre-earnings IV ramp**, unless stock breaks above ~$98 first (then reassess same day). Do not hold through Thursday's print. EV(ramp sell) ~$50-65 vs EV(hold) ~$15-25.
2. **LYFT ladder LIVE:** 2 contracts at +37% (mark $1.23 vs $0.90 entry). At +100% ($1.80), sell 1 contract, no meeting required. Remainder rides to the Aug 5 catalyst clock.
3. TRMB/UBER/LVS grandfathered to existing exit rules and Rule 4 tripwires. Rule 6 governs entries, not amputations.
4. All future entries (calls and puts) must pass Rule 6 (Reachability) and the upgraded DD checklist.

---

## PENDING ENTRIES

**SOUN $7C Aug21: GATE FIRED, BLOCKED (Jul 10, late evening).** Sole survivor of the 202-name four-screener run; scored 4/5 conditional on the line 11 gate (EPS revision direction). Verified same night via Yahoo EPS Trend: revisions DOWN (curr-qtr -$0.02 to -$0.04, curr-yr -$0.05 to -$0.14 over 30 days; 0 up / 1 down; two consecutive EPS misses). Pre-committed downgrade to 3.5/5 applied; 2-open-3.5/5 cap (TRMB + LYFT) blocks entry. No order. Re-evaluate when TRMB exits Jul 31 (4 trading days before the Aug 6 print): re-run line 11 fresh, re-price the chain. If revisions still falling then, kill permanently. Docs: `week-06/research/research_SOUN.md`, `week-06/story/five_baxters_soun_jul10.md`, `week-06/research/funnel_triage_jul10.md`.

*ZG $40C Aug21 and DIS $115C Aug21 researched and waiting. Both 3.5/5. Both blocked by 2-open-3.5/5 cap (TRMB + LYFT fill the cap). Window opens when TRMB exits Jul 31 or LYFT exits Aug 6. Still blocked as of Jul 6. Per the audit, both must re-pass the new 13-line funnel before entry (no grandfathering).*

**PUTS BACK-TEST: INTERIM RUN COMPLETE (Jul 16), PUTS STAY BLOCKED.** Real-candle outcome pull on the six Jun 22 documented hypotheticals: four clean entries all down 68-90% before any catalyst fired (theta bleed on 6-week-early entries); two entries (TTD, CMG) excluded as corrupted -- built on the pre-fix fetch_price label-desync bug, instruments never existed at documented prices. TSLA's Jul 2 delivery beat and RCL's +26.5% pre-earnings rally both resolved against the bear thesis mid-hold. **Final calibration pass Aug 8-10** after the Aug 4-7 prints, with screen-day price re-verification required for any counted name, and a proposed ≤21-days-to-catalyst entry-timing rule on the table. Calxter's Jul 31 deadline: met. Docs: `week-06/research/puts_backtest_data_jul16.md`, `puts_backtest_verdict_jul16.md`.

**AUGUST RE-SCREEN QUEUE (from Jul 12 batch):** AI (C3.ai, earnings Sep 9) and PATH (UiPath, earnings Sep 8) — both cleared R1 and live chain geometry but their prints fall outside every currently affordable expiry. Re-run with fresh Sep chains when they open in August; AI carries a hard flag (Q1 FY27 revenue guided ~$50-54M vs ~$87M yr-ago, probable Category 2) that must clear the decline-category test first. **TDOC** (91st percentile, cheap, violent prints) logged to the puts watch list — gated until the passes.md back-test unblocks puts (Calxter deadline Jul 31).

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
