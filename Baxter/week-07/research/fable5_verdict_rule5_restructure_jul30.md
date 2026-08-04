# FABLE 5 VERDICT: RULE 5 RESTRUCTURE
*July 30, 2026. Response to `fable5_brief_rule5_restructure_jul30.md`. Written for ratification in one sitting. All position data from `positions.md`, candle data from `data/contract_history/`, chain snapshots from the brief itself. No live market data was pulled for this analysis; every price in here is either from the fund's own records or labeled as an estimate with its basis stated.*

---

## SUMMARY VERDICT

Replace the flat $1.00 cap with a cap derived from the sizing table the fund already ratified: **one contract at the ask must fit inside the top of the play's conviction-tier budget from Tab 3, with a $1.00 floor.** That makes Rule 5 scale with both reserve and conviction automatically, using numbers already in the binder, with no new constants to invent or maintain.

But lock the loosening. The caps above $1.00 do not go live until a specific, checkable milestone (three closed Rule-6-era positions plus a $1,500 reserve, reviewed at a sweep), because the backtest of all 15 real positions found **zero trades where a looser cap would have made money, one trade where the proposed structure would have blocked the fund's second-worst loss (NKE, -$70), and two trades where extra price room would plausibly have made real losses bigger (LVS, UBER).** The one data point favoring closer strikes (ABT's near-miss gap) only pays under an exit rule the fund has since abandoned. The structural case for restructuring is strong. The empirical case for loosening today is zero. So: ratify the new form now, change nothing in practice today, and let the fund's own archived candle data decide the unlock at the sweep, where threshold tuning already lives.

---

## 0. DATA HONESTY, UP FRONT

- **DKNG, DSGX, and CHWY contract candle histories are permanently gone.** Those contracts expired before the Jul 13 archiving protocol existed. Every counterfactual touching those three names in this document is chain-shape reasoning from documented fills, explicitly labeled, never reconstructed candles.
- **No entry-day chain snapshots exist for any closed position.** Nobody archived "what did the closer strike cost that day." So every "the $X strike would have cost roughly $Y" statement in here is an estimate built from the only two documented chain-shape anchors in the repo, both from Jul 30:
  - **Strike anchor (DIS, $96 stock):** $105C $0.87, $103C $1.44, $102C $1.62, $101C $1.94. Roughly 2.2x the ask for strikes 4 dollars (about 4% of spot) closer to the money.
  - **Expiry anchor (ZG, same $45 strike):** 21 DTE $0.75, 112 DTE $3.40, 140 DTE $3.90. Roughly 4.5x the ask for going from a 3-week to a 16-week window.
- Everything else (fills, P&L, reserve figures, Rule 6 medians) is from the fund's own verified records.

---

## 1. WHAT RULE 5 ACTUALLY DOES TODAY, AND WHAT CHANGED AROUND IT

The written rationale for Rule 5 (iron_rules_calls.md) gives it two jobs: (a) keep the per-contract loss ceiling knowable and bounded, and (b) filter out chains where the only cheap options are so far OTM the breakeven outruns every analyst target. There is also a third job it does in practice: (c) it is the free bright-line number Baxter uses to kill chains mechanically mid-screen, no judgment call, no cost.

Here is the thing the brief correctly senses but does not quite say: **job (b) was taken over by Rule 6 on July 10.** "Does the required move outrun what this catalyst can plausibly deliver" is now answered directly, quantitatively, per name, by the 1.5x-median-move test, on real print history. Rule 5's chain-quality rationale was written in early June for a rulebook that had no reachability test. It has one now, and it is better at that job than a price cap ever was.

What is left for Rule 5 is job (a), which is a dollars-at-risk function, and job (c), which is a screening-mechanics function. Job (a) is exactly what Tab 3 does, except Tab 3 is denominated in percent of reserve and compounds, while Rule 5 is denominated in flat dollars and does not. Rule 5 is the last non-scaling number in a system whose own stated philosophy (Tab 3, June 20) is that fixed dollar figures accumulate but do not compound. That mismatch is real, it is structural, and it will get worse every month the fund grows. That is the honest case for restructuring, and it stands on its own without needing tonight's DIS trigger to justify it.

---

## 2. THE TRIGGER, RE-EXAMINED (IT DOES NOT SAY WHAT IT SEEMS TO SAY)

The brief's core finding: the DIS $101C ($1.94, +7.2% required) was blocked purely by Rule 5, and Tab 3's sizing math "can already afford it today" at 5/5 conviction. Checked, with two corrections.

**Correction 1: the affordability claim is true at the pre-fill reserve, not the post-fill one quoted next to it.** At the $1,000 reserve that existed at screening time, $194 is 19.4% of reserve, inside the 20% hard cap. At the $912.96 post-DIS reserve quoted in the same sentence, $194 is 21.3%, which breaches the hard cap. So even at 5/5, the $101C is only "affordable" if it is the first trade of the session. This is not pedantry; it is exactly the kind of edge the minimum-1-contract mechanics keep creating, and it is why the proposed rule below hard-couples the cap to the sizing table instead of leaving them to disagree.

**Correction 2, the bigger one: DIS was scored 3.5/5, not 5/5.** The same night this brief was written, the fund's own re-evaluation gave DIS 3.5/5 (thin Rule 6 margin, negative Earnings ESP, a fresh Sell rating). The 3.5/5 tier top at a $1,000 reserve is $100. Every blocked strike in the trigger table costs more than that:

| Strike | Ask | One contract | vs 3.5/5 tier top ($100) | vs Rule 5 |
|---|---|---|---|---|
| $101C | $1.94 | $194 | 1.9x over | blocked |
| $102C | $1.62 | $162 | 1.6x over | blocked |
| $103C | $1.44 | $144 | 1.4x over | blocked |
| $105C | $0.87 | $87 | fits | passes |

**For the play the fund actually scored, Rule 5 and Tab 3 block the same contracts.** The brief's line "Rule 5's flat cap, not the sizing tiers, is the actual wall" is only true for a hypothetical 5/5 play. The fund has never entered a 5/5 play. The trigger, examined closely, is not evidence that Rule 5 cost the fund anything on Jul 30. It is evidence that Rule 5 and Tab 3 currently agree by coincidence at this reserve size, and will stop agreeing as the reserve grows, which is the structural problem from Section 1 wearing a live example.

**What the $101C would actually have bought, if it had been legal.** Worth doing honestly, because it defines the tradeoff the whole question is about. DIS median real print move is 7.5%, Rule 6 cap 11.25%. Required moves: $105C +10.1% (needs a print in the top third of DIS's real history), $101C +7.2% (a median print reaches it). Rough held-to-print payoffs at the fund's own anchor prices (estimates, stated assumptions, roughly 2 weeks of residual time value):

| Stock lands | $105C ($0.87) | $101C ($1.94) |
|---|---|---|
| +7.5% ($103.33) | OTM, residual only, roughly -40 to -55% | $2.33 intrinsic, roughly +35 to +50% |
| +10.1% ($105.83) | at breakeven, roughly +40 to +70% | $4.83 intrinsic, roughly +150 to +170% |
| +11.25% ($106.93), the Rule 6 cap | roughly +160% | roughly +210% |
| +15% ($110.50), beyond the cap | roughly +550% | roughly +400% |

The crossover where the cheap contract wins on percentage sits around +12 to +13%, **above the Rule 6 cap.** Inside the entire band of moves Rule 6 says to count on, the closer strike wins in both dollars and percent if held to the print. That is a genuinely important geometric fact and it is the strongest argument in this document for eventually loosening. It is deliberately presented at full strength here so the ratification is honest. Two things keep it from deciding the question today: the fund's default exit is not held-to-print (Section 5), and one modeled table on one chain snapshot is not evidence (Section 8 says how real evidence gets collected).

---

## 3. THE BACKTEST: ALL 13 CLOSED POSITIONS PLUS 2 OPEN

For each position: the entry ask, whether Rule 5 was actually binding (did it force a farther strike than the fund wanted), and what each candidate structure would have changed. Conviction tiers did not exist before Jun 20, so early plays are marked pre-tier.

| Position | Ask | Ct | Conv | P&L | Was Rule 5 binding? | What would a looser or restructured cap have changed? |
|---|---|---|---|---|---|---|
| CCL $31C | $0.99 | 1 | pre-tier | +$1 | At the line | Nothing. Note: a reserve-scaled cap with no floor would have BLOCKED it ($99 was about 20% of the whole $500 fund). The floor in the proposed rule exists because of this row. |
| NKE $50C | $1.86 | 1 | pre-tier | -$70 | Exceeded the written cap (early-days entry) | The book's only real sample of an expensive, closer-to-money contract. $186 of premium was about 37% of the entire fund. It decayed like any broken thesis and lost more dollars than any other single contract. The proposed rule blocks this entry at every tier at a $500 fund. This row is the whole per-contract-dollar argument in one line. |
| DSGX $90C | $0.45 | 1 | pre-tier | -$30 | No | Nothing. Died from post-event entry, a failure mode no price cap touches. Candles gone; no reconstruction attempted. |
| CHWY $24C | $0.56 | 1 | pre-tier | -$23 | Arguably (Tab 5: strike too far OTM for the implied range) | Genuine unknown. A $22C might have been buyable somewhere above $1.00 and might have lost less or more. Candles permanently gone, entry chain never archived, and this document will not invent the numbers. Marked unknowable, honestly. |
| MDT $85C | $0.54 | 1 | pre-tier | +$23 | No | Nothing, under any candidate. |
| DKNG $27.5C | $0.49 | 1 | pre-tier | +$251 | No | Nothing, and this matters: at a roughly $400 to $500 reserve, no candidate structure (including full removal of Rule 5) makes a closer strike affordable under any sizing tier. **The fund's best trade was only possible because the contract was cheap.** Candles gone; the +512% realized multiple is from the order record, not reconstruction. |
| BSX $60C | $0.70 | 1 | pre-tier | -$15 | No | Nothing. Rule 4 breach on entry day; price caps are irrelevant to it. |
| HITI $2.50C | $0.25 | 4 | pre-tier | -$12 | No | Nothing directly, but note the direction: cheapness bought 4 contracts, and the Jul 13 consult showed the ladder monetizes contract count (+$19 counterfactual on this exact position). Loosening pushes toward fewer, pricier contracts, which is the wrong direction for this mechanism. |
| ABT $100C | $0.78 | 1 | pre-tier | +$27 | Partially | **The one closed data point that favors closer strikes.** Needed +9.2% from the pre-print level; the real earnings gap was +8.7%. Missed breakeven by half a point after being nearly dead ($0.08) the night before. A $98C (estimate from the DIS strike anchor: roughly $1.15 to $1.45 at entry) would have gapped about $2.50 ITM, worth roughly +$130 versus the actual +$27. Honest caveat that halves this point: under the post-audit Tab 4 default (sell the ramp, not the print), BOTH contracts get sold before the print, both at a loss. The counterfactual only pays under the grandfathered hold-through rule the fund has since replaced. |
| LVS $55C | $0.435 | 2 | 4/5 | -$67 | No (and Rule 6 retro-kills every shape of this play) | A looser 4/5 cap invites a $50C or $52.5C at an estimated $1.10 to $1.60. Same process failure (the sell order that never existed), same post-print collapse, on roughly $110 to $160 of premium instead of $87: estimated loss -$90 to -$120 instead of -$67. **Looser cap makes the book's worst process failure more expensive.** |
| TRMB $65C | $0.38 | 2 | 3.5/5 | +$74 | No | Nothing under conviction-linked candidates (3.5/5 keeps $1.00). Note the mechanism: two cheap contracts enabled the Jul 28 ladder trim (+$32 banked leg). A pricier single contract has no ladder. |
| UBER $90C | $0.65 | 2 | pre-cap-era | -$112 | No (Rule 6 retro-kills it entirely) | A closer strike (estimated $2-plus for anything needing under 10%) at minimum-1 sizing is more premium on the same downtrend: bigger dollar loss. And even the closer strikes fail UBER's real Rule 6 cap (7.7%). Loosening hurts or does nothing here. |
| LYFT $16C (partial +$90 banked; runner open) | $0.90 | 2 | 3.5/5 | +$90 realized, runner +$5 | No | Nothing, under every candidate. On a $15 stock, $1.00 already buys a near-the-money strike (breakeven was +8.6% at entry). Rule 5's bite depends on the stock's price: harmless at $15, forces about 9 to 10% OTM at $96 (DIS), excludes the entire reachable chain at $300-plus (the ISRG kill). That gradient is the real long-run problem with a flat dollar cap. |
| DIS $105C (open) | $0.87 | 1 | 3.5/5 | just filled | Yes, but so was Tab 3 | Section 2 in full. As scored (3.5/5), no candidate changes this entry. Only a 5/5 scoring unlocks the $101C, and this play was not a 5/5. |

**Backtest bottom line.** Across 15 positions: 12 completely unchanged under every candidate structure; 1 blocked for the better by the proposed structure (NKE, -$70); 1 genuine unknown (CHWY, data gone); 1 estimate favoring closer strikes that evaporates under the fund's current exit rules (ABT); 2 estimates where price room would have deepened real losses (LVS, UBER). There is no historical trade where a looser Rule 5 makes the fund money under the rules as they now stand. Every argument for loosening is prospective, not retrospective. That is not a reason to refuse the restructure. It is a reason to restructure the form now and gate the loosening on evidence.

---

## 4. THE SIX CANDIDATES

**1. Status quo (flat $1.00).** Survives the backtest better than the brief expected: it cost the fund nothing demonstrable in 15 positions. But it is a flat dollar constant inside a percentage system, its bite is secretly a function of the stock's share price (harmless at $15, prohibitive at $96, absolute at $300), and it goes quietly wrong as the reserve compounds: at a $5,000 reserve the $1.00 cap forces every play into far-OTM contracts and excludes every high-priced underlying regardless of how reachable its chain is. It also carries an accidental birthmark: $1.00 happens to equal the 3.5/5 tier-top single contract at exactly a $1,000 reserve, which is roughly the fund's current size. The rule feels right today because today is the one reserve level where it coincides with the sizing table. Mechanically simplest possible. **Baseline; beaten on structure, not on history.**

**2. Reserve-scaled formula (e.g., ask cap = reserve / 1000, floored at $1.00).** Scales correctly, but gives the same cap to every conviction tier, which prices risk backwards: a 3.5/5 play (6 to 10% of reserve) could buy a cap-priced contract that is 18 to 20% of reserve at minimum-1, recreating the override problem in a worse form. Without a floor it retroactively blocks CCL. It is also a new constant to justify (why 1/1000 and not something else). **Rejected standalone; its scaling idea survives inside candidate 6.**

**3. Milestone-tiered flat steps ($1.00 under $X, $2.00 under $Y).** Simple to apply, but the step values are exactly the kind of round-number-by-feel the brief says to avoid, each step goes stale the way the original $1.00 did, behavior jumps discontinuously at boundaries, and it is conviction-blind like candidate 2. **Rejected; its milestone idea survives as the unlock gate in the recommendation.**

**4. Conviction-linked flat caps (3.5/5 stays $1.00; 4/5 gets $1.50; 5/5 gets $2.00).** Keys off the right variable (Tab 3 already prices risk by conviction) and directly answers the trigger. Two failures. First, the numbers only make sense near a $1,000 reserve: at $600, a $2.00 contract at minimum-1 is 33% of reserve, smashing the hard cap; at $5,000, $2.00 is as arbitrarily tight as $1.00 is claimed to be today. Flat constants rot; that is the original sin being repeated with more digits. Second, on the actual backtest it changes exactly one closed play (LVS, the 4/5), and changes it for the worse. **Rejected standalone; its conviction linkage survives inside candidate 6.**

**5. Fold Rule 5 into Rule 6 (outcome cap only, no price gate).** Philosophically the cleanest, and Section 1 concedes its core insight: Rule 6 now owns chain quality. But operationally it breaks three ways. (a) Minimum-1 blowout: with no price gate, a Rule-6-passing $4.00 contract "passes" and then minimum-1 forces 40-plus percent of reserve or an ad-hoc rejection, which moves the decision from a rule to a judgment call, the exact thing Iron Rules exist to prevent. (b) It deletes the leverage philosophy from the rulebook silently: nothing would stop every entry drifting to the highest-probability, least-leveraged strike that clears Rule 6, and Section 5 shows the fund's realized profit engine runs on the leveraged end. A philosophy change that big should be a decision, not a side effect of deleting a rule. (c) It destroys job (c) from Section 1: the screening protocol kills chains for free on a bright-line ask number ("chains settle Rules 5-6 free"); an outcome-only rule needs per-name print-history medians before the chain check can even run, inverting the free-first screening order Michael ratified Jul 10. **Rejected, with its insight absorbed: the proposed rule text below rewrites Rule 5's rationale to acknowledge Rule 6 owns reachability, and Rule 5 owns affordability, leverage, and the screen line.**

**6. Tie the cap to Tab 3 (the recommendation): one contract must fit the top of the play's conviction-tier sizing range, computed on current reserve, floored at $1.00.** Formula: **max ask = tier-top percent x reserve / 100**, where tier-top is 10% (3.5/5), 16% (4/5), 20% (5/5). This is candidates 2 and 4 merged and, critically, derived rather than invented: it introduces zero new constants (every number is already ratified in Tab 3), it scales with reserve automatically, it prices the cap by conviction exactly the way the fund already prices dollars at risk, it can never breach the 20% hard cap by construction (the 5/5 tier-top IS the hard cap), and it abolishes the minimum-1-contract override exception above the floor (if one contract does not fit the tier, the instrument fails Rule 5, the same way June's DIS entry needed a documented exception and July's did not). Mechanical load: one multiplication, using the same arithmetic Baxter already does at every entry to derive contract count. Worked values:

| Reserve | 3.5/5 cap | 4/5 cap | 5/5 cap |
|---|---|---|---|
| $500 | $1.00 (floor = hard cap here) | $1.00 (floor) | $1.00 |
| $912.96 (today) | $1.00 (floor) | $1.46 | $1.82 |
| $1,000 | $1.00 | $1.60 | $2.00 |
| $1,500 | $1.50 | $2.40 | $3.00 |
| $2,000 | $2.00 | $3.20 | $4.00 |
| $5,000 | $5.00 | $8.00 | $10.00 |

The floor never lets the rule get stricter than today (the brief's own requirement, and the CCL row's lesson), except below a $500 reserve where the 20% hard cap takes over, which is correct (a $100 contract on a $400 reserve should fail). Note what the today-row says: even fully unlocked, this rule changes nothing at 3.5/5 today, and the fund's last four scored entries (TRMB, LYFT, DIS twice) were all 3.5/5. **Recommended, with the loosening gated (Section 8).**

---

## 5. THE LEVERAGE PHILOSOPHY: PRESERVED, WEAKENED, OR TRADED?

The straight answer: **the recommendation preserves the leverage philosophy as the fund's default, and creates one deliberate, evidence-gated channel to trade some of it away at high conviction later.** Nothing is weakened silently. Here is the full accounting.

The philosophy's case, on the fund's own realized record: every dollar of realized profit came from cheap contracts making huge percentage moves before their catalysts (DKNG +512%, LYFT partial +100%, TRMB +95% blended, MDT +43%, ABT +35%). The Jul 10 audit found 100% of realized profit came from mechanism exits, selling appreciation before the print, and Tab 4 made sell-the-ramp the default. That detail decides more of this question than anything else: **pre-print appreciation is where a cheap contract's percentage leverage lives.** Per dollar deployed, a far-OTM contract moves harder on the same pre-print drift than a near-money one (on the DIS anchor, roughly 1.5x harder). If the fund's money is made selling pre-print appreciation, and it demonstrably has been, then the cheap end of the Rule-6-reachable chain is not a constraint on the strategy; it IS the strategy.

Cheapness has a second, quieter product: **contract count.** The scale-out ladder, the only profit mechanism this fund has now validated on live money twice (LYFT +$90, TRMB +$32 leg), requires 2-plus contracts to exist. At this fund's budget sizes, only sub-$1.00 asks buy 2-plus contracts. Every step toward pricier strikes at fixed budget is a step toward single-contract positions, and the single-contract protocol is the fund's demonstrated weak spot (ABT rode +150% to nearly zero; the +150% EV rule was written because singles keep doing this).

The honest case against, at full strength: Rule 6 changed the payoff geometry. Pre-audit, the fund hunted 20 to 30% moonshot moves, where far-OTM lambda wins outright. Post-audit, every entry is capped at moves at or under 1.5x the stock's median print. Inside that band, Section 2's table shows the closer strike beats the cheap one in dollars AND percent if held through the print, and ABT's real gap (+8.7% delivered against +9.2% required) is the live example of a cheap contract dying half a point short of a move that a closer strike would have converted. When Rule 6 forbids counting on the moves where cheap contracts shine, a rule that forces cheap contracts is in mild tension with the exit geometry, for any play that IS held to its print (binary-flagged 4/5-plus entries, per Tab 4).

So the trade is real, two-sided, and currently unresolved by evidence: **leverage and ladder-count (which match the sell-the-ramp default) versus hit-rate and print-conversion (which match held-to-print plays).** The fund has exactly one closed data point on each side, ABT for, NKE against, both from the pre-audit era, both compromised as evidence. That is precisely why the recommendation does not resolve the philosophy question by fiat: the default stays leveraged, the loosening waits for the counterfactual data the archiving protocol now guarantees will exist (Section 8), and when it unlocks it applies where its logic is strongest, at high conviction, where Tab 4 already permits holding through prints.

---

## 6. THE RULE 6 INTERACTION

Yes, loosening Rule 5 mechanically makes Rule 6 easier to pass. Closer strikes need smaller moves; smaller required moves clear the 1.5x-median cap more often. On DIS the effect is the difference between using 90% of the Rule 6 ceiling ($105C, +10.1% vs 11.25%) and 64% of it ($101C, +7.2%), with the required move dropping below the stock's own median print. That is not gaming the gate. Each individual pass is a genuinely more reachable trade; the probability improvement is real, not cosmetic.

The legitimate caution is at the portfolio level, and it is about the funnel, not the gate. The 13-line funnel's brutal selectivity is currently doing risk-control work: 68 names screened Jul 30, zero advances; 198 in the Jul 13 batch, zero entries. Rule 5's price line is one of the two free kills doing most of that filtering. Loosen it and the funnel's yield rises, at higher premium per trade, with less leverage per trade, which is a different fund. Checked against tonight's actual kills to size the effect honestly: **at current reserve, even a fully unlocked cap ($1.82 at 5/5) un-kills almost nothing.** WYNN needed +12.2% against a 4.35% cap; getting under that cap needs a near-ATM contract on a $90-class stock, far above $1.82. Same for ZS (+26.3%) and ISRG (+18.5%). Low-volatility names need near-ATM pricing that exceeds even the loosened caps at this fund's size, so the funnel stays selective today. But the effect grows mechanically as the reserve grows and the caps rise with it. Conclusion: **the Rule 6 interaction is not a reason to loosen (the gate getting easier to pass is a consequence, never a goal), and it is a quantified reason for the sweep review in the proposed rule to track funnel yield after any unlock, so a doubling of advance rate gets noticed as a regime change rather than mistaken for skill.**

---

## 7. SCALE WITH RESERVE, CONVICTION, BOTH, OR NEITHER?

**Both, through a single coupling: conviction picks the percentage (Tab 3's tier tops: 10 / 16 / 20), reserve supplies the base, the product is the cap.** Not reserve alone (conviction-blind caps price risk backwards and recreate the override problem at 3.5/5). Not conviction alone (flat constants rot; candidate 4's numbers are only accidentally correct near $1,000). Not neither (the flat $1.00 is the accidental special case "3.5/5 tier-top at a $1,000 reserve" and stops being defensible the moment the reserve compounds away from $1,000, which is the entire point of the fund).

The exact formula, worked table, floor, and hard-cap behavior are in Section 4, candidate 6, and in the rule text below. Reserve is measured at time of entry, the same instant Tab 3 already measures it, so Rule 5 and the sizing math can never disagree about what day it is.

---

## 8. WHAT HAPPENS NOW VS WHAT WAITS

**Immediately, on ratification:**
1. Tab 1 Rule 5 is replaced with the text below. Practical behavior at every tier today: identical to the old rule ($1.00), because the transitional lock holds every cap at the floor.
2. Two real changes do land immediately, both tightening, neither loosening: the minimum-1-contract override above the floor is abolished (an instrument whose single contract busts the tier top now fails Rule 5 instead of generating a documented exception, the June DIS pattern), and the screening viability line is formalized (the free chain-kill line becomes the maximum any play could use: 20% of reserve / 100, floored at $1.00; today that is $1.00, so screening behavior is unchanged until the reserve grows).
3. The sweep agenda (Tab 6 standing decision, every 5 closes) gains one item: the Rule 5 counterfactual log defined below.
4. Tab 2's puts Rule 5 ($1.50 flat) is flagged for the same restructure, but not changed now. Puts are blocked pending the back-test anyway; restructure it when the puts system earns its first live entry, using whatever this rule's unlock evidence shows by then.

**What waits, and for exactly what:**
The caps above $1.00 unlock at the first take-profit sweep at which both hold: **(a) at least three positions entered under the full post-audit rules (entries dated on or after Jul 10, 2026) have closed, and (b) reserve is at or above $1,500 at sweep time.** Why these two, specifically: (a) is the evidence gate. The fund currently has ZERO closed positions entered under Rule 6; every backtest row above is pre-audit data answering a post-audit question. Three closes is the minimum for the counterfactual log to say anything at all, and the Jul 13 archiving protocol guarantees the candle data for those closes will exist, unlike the June ones. (b) is the affordability gate: at $1,500-plus, a $2.40-class 4/5 contract no longer forces a single-contract book, so unlocking does not immediately strip the fund of ladder eligibility. And the sweep is the venue because the fund already ratified (Jul 13 consult, point 5) that threshold tuning happens at sweeps, on data, never mid-cycle on trigger emotion.

**The counterfactual log (the evidence the unlock runs on):** at every sweep from now on, for each Rule-6-era closed position, record what the nearest archived closer-to-the-money strike at the same expiry would have returned at equal sizing budget, using the archived candles, the same method as the Jul 13 profit-taking consult. The DIS position open right now is the first live A/B of this exact question: the brief's blocked $101C against the filled $105C, both trackable through the Aug 5 print with real data. If, at the unlock sweep, the log shows the cheap strikes outperforming at equal budget, the unlock is deferred to the next sweep, in writing, and that is not a failure of this rule; it is this rule working.

**A variant considered and rejected:** unlocking 5/5 only, immediately (cap $1.82 today), on the argument that the fund has never scored a 5/5 so the unlock is dormant anyway. Rejected because a dormant unlock is pure downside: it changes nothing until the exact moment a maximum-conviction play appears, and that is the worst possible moment to be running an untested cap for the first time. One milestone, one unlock, all tiers, on evidence.

---

## PROPOSED RULE 5 TEXT

Replaces Tab 1, Rule 5 in full. Tab 2's puts Rule 5 is unchanged for now (see Section 8, item 4).

> **Rule 5 (Chain Filter): one contract must fit the tier.**
>
> The option ask, times 100, must not exceed the top of the play's conviction-tier sizing range from Tab 3, computed on reserve at time of entry:
>
> **max ask = tier-top percent x reserve / 100**, where tier-top is 10% (3.5/5), 16% (4/5), 20% (5/5).
>
> **Floor:** the cap is never below $1.00/share, except that it is never above 20% of reserve / 100 (below a $500 reserve, the hard cap governs).
>
> **Transitional lock:** until the unlock milestone, the cap is also never above $1.00/share at any tier. Unlock milestone: the first take-profit sweep at which both (a) three or more positions entered on or after Jul 10, 2026 have closed, and (b) reserve is at or above $1,500. The unlocking sweep must review the Rule 5 counterfactual log (per Rule-6-era close: what the nearest archived closer strike at the same expiry would have returned at equal budget, from archived candles). If the log favors the cheaper strikes, the unlock defers to the next sweep, recorded in writing.
>
> **No minimum-contract override:** if a single contract at the ask exceeds the cap, the instrument fails Rule 5. No exception, no waiver, no "minimum 1 contract" carve-out.
>
> **Screening line:** during batch screening, before conviction is scored, the chain-viability line is the maximum any play could use: 20% of reserve / 100, floored at $1.00. Chains with no instrument passing Rule 4 and Rule 6 at or under that line are dead. The tier-specific cap is re-checked at entry.
>
> **Selection note (preference, not a gate):** when two instruments both pass Rules 4, 5, and 6, prefer the one that buys at least two contracts within the sizing budget. The Tab 4 scale-out ladder, the fund's only repeatedly validated profit mechanism, requires two contracts to exist.
>
> **What this rule is for:** Rule 6 owns reachability. Rule 5 owns affordability (a single contract may never outgrow the risk budget its own conviction score earned), leverage (the fund's default lives at the cheap end of the reachable chain, and moving off that default is a sweep decision made on the counterfactual log, never a per-trade judgment call), and the free screening line. Rule 5 does not get waived for a good thesis.

---

## RATIFICATION CHECKLIST (three yes/no calls for Michael)

1. Replace Tab 1 Rule 5 with the text above (today's behavior unchanged; override abolished; screen line formalized)? 
2. Adopt the unlock milestone as written (3 Rule-6-era closes AND $1,500 reserve, decided at a sweep on the counterfactual log)?
3. Add the Rule 5 counterfactual log to the standing sweep agenda, starting with DIS $105C vs the blocked $101C at the next sweep?

---

## GLOSSARY

- **Ask:** the price sellers are currently offering a contract at; what the fund actually pays to enter. Rule 5 caps the ask, not the mark or the bid.
- **Tier top:** the highest percentage of reserve Tab 3 allows for a conviction score (10% at 3.5/5, 16% at 4/5, 20% at 5/5). The proposed Rule 5 cap is the tier top expressed as a maximum ask for one contract.
- **Minimum-1 override:** the old pattern where Tab 3's "minimum 1 contract" let a single contract exceed its tier's budget with a documented exception (June's DIS entry). Abolished above the floor by the proposed rule.
- **Lambda (elasticity):** percentage change in a contract's price per 1% move in the stock, roughly delta times stock price divided by option price. Cheap far-OTM contracts have higher lambda: bigger percentage swings per dollar deployed. The quantitative form of the fund's leverage philosophy.
- **Required move:** the percentage the stock must rise for the position to break even at expiry (breakeven minus spot, over spot). Rule 6 caps it at 1.5x the stock's median real earnings-day move.
- **Sell the ramp:** Tab 4's default exit, selling into elevated pre-print premium instead of holding through the earnings print. Where pre-print percentage appreciation (and therefore lambda) is the payoff engine.
- **Scale-out ladder:** Tab 4's rule for multi-contract positions, selling half at +100% before the catalyst. Requires 2-plus contracts, which at current budgets only cheap asks can buy.
- **Counterfactual log:** the per-close record, run at each sweep from archived candles, of what the nearest closer-to-the-money strike would have returned at equal budget. The evidence the unlock milestone decides on.
- **Rule-6 era:** positions entered on or after the Jul 10, 2026 audit, when Rule 6 (Reachability) and the rewritten Tab 4 took effect. The only closes that count toward the unlock milestone, because only they test the current rulebook.
- **Hard cap:** Tab 3's absolute limit, no single play above 20% of reserve. The proposed Rule 5 can never breach it by construction, because the 5/5 tier top IS the hard cap.
- **Floor:** the $1.00 minimum cap, guaranteeing the restructured rule is never stricter than the rule it replaces (except below a $500 reserve, where the hard cap correctly governs).
