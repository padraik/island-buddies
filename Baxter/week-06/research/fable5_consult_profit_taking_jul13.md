# FABLE 5 CONSULT: THE PROFIT-TAKING QUESTION, RUN ON REAL CONTRACT DATA
*July 13, 2026. Michael asked for an impartial re-run of the July 13 Calxter consult on Fable 5, with no skin in the game, incorporating his rebuttal. This document contains: (1) his rebuttal verbatim, (2) the prior consult's verdicts, (3) new primary data -- actual daily contract candles pulled from Robinhood for every position whose contract still exists -- and (4) the counterfactuals his question demands, run on that data instead of memory.*

---

## 1. THE EXCHANGE THIS DOCUMENT ANSWERS

**Michael, verbatim (Jul 13):**

> "I just worry that we're hunting the huge single win, instead of growing by 10+% when we can guarantee them. Isn't that what the compounding strategy is supposed to take advantage of? I mean... we were even up by 20% one week on NKE. I would think the scale-out strategy lets us do that to some degree... but if we're looking at Lyft right now, we could take $68 and walk away with a 37.78% profit in the month that we've had it. That's insane growth in a month... Don't placate me right now Baxter, and don't just agree with me because I said something."
>
> And after the first pass: "The NKE stock price stayed under breakeven, yes, but there was a period where the contract, our position, was up. There have been very few of these that never went positive the whole time. You're right that if we took DKNG out of the ledger altogether, we'd be negative. But if we had sold *every* position we had so far as soon as we could make 10% or maybe even 20% we'd be positive too. I don't know if it would be as positive as we are after the full DKNG win, but we'd be looking at a positive return on almost every position and could be talking about how we adjust position sizing for bigger bets, because we're consistent. (we need to be tracking the history of our CONTRACT value for these positions so we have the real data to postmortem)"

**The first consult (calxter_consult_scaleout_jul13.md) concluded:** (a) the fund's realized record is one trade deep -- subtract DKNG and it's -$126; (b) four of five open positions were stretch plays Rule 6 would have blocked, and Michael's critique restates the audit's own Finding; (c) don't sell LYFT -- it's the one Rule-6-reachable position, and the ladder's trigger hasn't fired; (d) proposed tiering the scale-out ladder by Rule 6 status, with a lower (30-50%) trigger for stretch plays. It also said NKE's green window was "unconfirmed" from checkpoint notes.

That consult argued from session-note checkpoints. This one doesn't have to.

## 2. THE NEW PRIMARY DATA

`fetch_option_history.py` (built this session) pulls daily open/high/low/close candles for any option contract Robinhood still lists. Pulled today for all 11 reachable contracts; raw archives in `Baxter/data/contract_history/`. Three contracts -- DKNG Jul02, DSGX Jun18, CHWY Jun18 -- are already expired and their histories are **permanently gone**. Four more (NKE, CCL, MDT, HITI, ABT -- all Jul 17 expiries) would have been gone Friday. Michael's tracking demand was not a nice-to-have; it was days from being unanswerable forever.

**In-window contract peaks (daily highs, from entry date to exit or today):**

| Position | Entry | In-window peak | Peak % | When | Exit / today | Ever green? |
|---|---|---|---|---|---|---|
| CCL 1x | $0.99 | $1.22 | **+23.2%** | Jun 1 (entry day) | $1.00 (+$1) | YES |
| NKE 1x | $1.86 | $2.04 | **+9.7%** | Jun 1 (entry day) | $1.16 (-$70) | Barely -- one day, never reached +10% |
| MDT 1x | $0.54 | $2.14 | **+296%** | Jun 4 (day 2) | $0.77 (+$23) | YES, massively |
| HITI 4x | $0.25 | $1.40* | **+460%*** | Jun 9 | $0.22 (-$12) | YES, repeatedly (*thin-print caveat) |
| DKNG 1x | $0.49 | data gone | (realized +512%) | -- | $3.00 (+$251) | YES (the win) |
| DSGX 1x | $0.45 | data gone | -- | $0.15 (-$30) | Presumed never (gap-and-fade) |
| CHWY 1x | $0.56 | data gone | -- | $0.33 (-$23) | Presumed never (declined throughout) |
| BSX 1x | $0.70 | $0.70 | **0.0%** | Jun 15 | $0.55 (-$15) | NO -- confirmed never green in window |
| ABT 1x | $0.78 | $1.95 | **+150%** | **Jul 7** | $0.28 today | YES -- green on ~14 of 28 days |
| TRMB 2x | $0.38 | $1.05* / ~$0.70 ex-spike | +176%* / ~+84% | Jun 18* / Jul 7 | $0.45 today | YES, most days (*Jun 18 spike is a suspect thin print -- close was $0.38 same day; phantom-print lesson applies) |
| UBER 2x | $0.65 | $1.33 | **+104.6%** | Jun 29 (also $1.31 Jun 24) | $0.54 today | YES |
| LYFT 2x | $0.90 | $1.54 | **+71.1%** | Jul 10 | $1.24 today | YES -- green 24 of 28 trading days |
| LVS 2x | $0.435 | $0.63 | **+44.8%** | Jun 29 (entry day) | $0.32 today | YES |

**Michael's factual claims, graded against the data:**
- *"There was a period where the NKE contract was up"* -- TRUE. Jun 1, high $2.04, +9.7%. One day, and it never touched +10%. The "up 20% one week" memory is not in the data: +9.7% was the ceiling.
- *"Very few of these never went positive the whole time"* -- TRUE, and the first consult undersold it. Of 11 verifiable positions, only BSX is confirmed never-green (plus DSGX/CHWY presumed). **8 of 11 had real green windows, most of them double-digit.**
- *"We need contract-value history tracking"* -- TRUE and urgent. Three histories are already unrecoverable; five more had four days to live.

## 3. THE COUNTERFACTUALS, RUN HONESTLY

Method: first daily-high touch of the threshold fills the order (generous to the strategy -- assumes selling at the day's high); positions that never touch it follow their actual history; open positions harvest from entry. TRMB's Jun 18 spike excluded as a suspect print (conservative). All 13 positions.

**Strategy A -- sell everything at first +10%:**
Closed set: CCL +$10, DSGX -$30, CHWY -$23, NKE **-$70 (never fills)**, MDT +$5, DKNG +$5, BSX -$15, HITI +$10 = **-$108**.
Open set harvested: ABT +$8, TRMB +$8, UBER +$13, LYFT +$18, LVS +$9 = +$56.
**Total: -$52.** Michael's claim "we'd be positive too" is FALSE at +10%.

**Strategy B -- sell everything at first +20%:**
Closed set: CCL +$20, DSGX -$30, CHWY -$23, NKE -$70, MDT +$11, DKNG +$10, BSX -$15, HITI +$20 = **-$77**.
Open set: ABT +$16, TRMB +$15, UBER +$26, LYFT +$36, LVS +$17 = +$110.
**Total: +$33.** Positive -- barely -- so half of Michael's claim survives at +20%. But reality (realized +$125, open book +$26, ~+$151 economic) beats it by ~$118.

**Why the flat harvest loses:** the arithmetic is structural, not bad luck. Wins capped at 10-20% of premiums this size pay $5-$36 each. The positions that never go green -- and there were at least three, likely five -- lose $15-$70 each. NKE alone (-$70) eats seven Strategy-A wins by itself. A flat low cap keeps every loser whole and shrinks every winner. That is the opposite of the asymmetry an options book runs on.

**Strategy C -- the ladder Michael already ratified on Jul 10, backtested as if it had existed from June 1** (multi-contract: sell half at +100% pre-catalyst; single contract: +150% with >7 days to catalyst = default sell; mechanism expiry overrides):

| Position | Ladder action | Result vs actual |
|---|---|---|
| ABT | +150% trigger hit **Jul 7** ($1.95), 9 days pre-catalyst, default sell ~$1.90 | **+$112 instead of today's -$50** |
| UBER | +100% hit Jun 24 and Jun 29; sell 1 of 2 at ~$1.30 | +$65 banked; remainder rides (-$11 today). Net +$54 vs -$22 |
| MDT | +150% ($1.35) hit Jun 4; catalyst already fired = mechanism override, sell | +$81 minimum vs actual +$23 |
| HITI | +100% ($0.50) hit Jun 5; sell 2 of 4 at ~$0.50 (+$50); rest ride to exit (-$6) | +$19 net (even halving the fill for thinness stays positive) vs -$12 |
| DKNG | +150% window inside 7 days of the World Cup mechanism -- no forced sell; rides to the actual BOTZ exit | **+$251 preserved, exactly as designed** |
| CCL, NKE, DSGX, CHWY, BSX | never reach a trigger; actual outcomes unchanged | -$137 unchanged |
| TRMB | +100% = $0.76: only the suspect print reaches it; conservatively no fill | +$14 book, unchanged |
| LYFT | +100% = $1.80: max was $1.54. No trigger. Both contracts ride to Aug 5 | +$68 book, unchanged |
| LVS | +100% = $0.87: never post-entry. Rides | -$23 book, unchanged |

**Strategy C total: ~+$214 realized on the closed set (vs +$125 actual) plus ABT +$112 (vs -$50) plus UBER's banked half. Economic total ≈ +$439 vs reality's ≈ +$151.** The ladder, had it existed five weeks earlier, is worth roughly +$290 over what actually happened -- and it beats the +10% flat rule by ~$490 and the +20% rule by ~$400.

**And the first consult's own proposal -- a lower 30-50% trigger for stretch plays -- TESTED:** ABT at +50% sells Jun 4 for +$39 (the ratified +150% got +$112). UBER at +50% banks ~+$33 (the ratified +100% got +$65). LVS at +50% never fills (peak +44.8%) -- no help. TRMB at +50% banks ~+$19 -- the only position it helps. **The data kills most of my own Jul 13 proposal: lowering thresholds costs more on the positions that run than it saves on the ones that stall.** Withdrawn except as a footnote for the sweep counter (below).

## 4. VERDICT

1. **Michael is right that the fund bled real, recoverable profit, and right that most positions had green windows.** The data confirms it: 8 of 11 verifiable positions went green; ABT alone gave back $112 twice-confirmed, UBER gave back $65 of banked money, MDT left $58+, HITI $31. Total recoverable by rule: roughly $290. That's not placation; that's the candle data.
2. **But the specific mechanism he proposed -- flat +10%/+20% harvesting -- is the wrong tool, and the data is unambiguous.** At +10% the fund would be NEGATIVE (-$52). At +20%, +$33 -- worse than what we actually did. The flat cap can't pay for never-green losers and gives up every run. His premise "we'd be positive on almost every position" is true position-by-position and still loses money in aggregate, because the wins are capped small and the losses aren't.
3. **The right tool already exists and Michael already ratified it: the Jul 10 scale-out ladder.** Backtested on real candles it captures ~$290 of the bleed while preserving DKNG intact -- which is the entire tension (compounding vs moonshot) resolved by one rule. The fund's sin was not "no profit-taking philosophy." It was that the ladder arrived July 10 instead of June 1. Every dollar Michael is mourning was lost BEFORE the rule existed. Nothing about the current book violates it.
4. **LYFT: the answer stands, now with data.** Green 24 of 28 days -- Michael's compounding instinct is real and LYFT is its best evidence -- but the ladder trigger ($1.80) hasn't fired, max was $1.54, and the Aug 5 catalyst is the thesis. Hold both contracts. The ladder will bank half automatically at +100% if it gets there.
5. **Threshold tuning happens at the sweep, not mid-cycle.** n=3 winners is not a calibration set. The sweep counter (every 5 closes) re-derives ladder thresholds from the winner distribution -- that is the correct, already-ratified mechanism for Michael's "adjust as we get consistent" idea. The 40-85% mid-peak class (TRMB, LVS, LYFT-so-far) is flagged as an open question FOR THE SWEEP, with this document as input.
6. **Tracking is now a standing protocol.** `fetch_option_history.py` exists; raw histories archived in `Baxter/data/contract_history/`; wrap-up protocol now requires pulling and archiving the candle history of any contract within a week of expiry, and of every contract at position close. DKNG's history is gone because we didn't have this. That never happens again.

## 5. WHAT CHANGES ON THE BOOKS

- No trade today. LYFT holds (ladder governs). ABT still sells Wednesday into the ramp (its window at +150% came and went Jul 7, three days before the rule that would have caught it existed).
- The Jul 13 Calxter tier-proposal is withdrawn as tested-and-beaten; replaced by a sweep-counter input note.
- Contract-history archiving added to the wrap-up protocol (skill file updated).
- This document is the post-mortem data standard going forward: candles, not checkpoints.

## GLOSSARY

- **Candle (daily):** One day's open, high, low, and close for a contract. The high is the best price that printed that day -- an upper bound on what a resting sell order could have gotten.
- **In-window:** Between our entry date and our exit date (or today, for open positions). Peaks outside the window are someone else's trade.
- **Thin-print caveat:** On low-volume contracts a daily "high" can be one stray fill nobody could repeat (TRMB's Jun 18 $1.05 against a $0.38 close). Fills assumed at such prints are excluded or haircut; the phantom -98% lesson in Tab 5 is the same physics in reverse.
- **Flat harvest (Strategy A/B):** Sell the entire position at the first touch of a fixed gain (+10% or +20%). Tested and rejected: -$52 / +$33 vs reality's ~+$151.
- **Scale-out ladder (Strategy C):** The Jul 10 rule. Multi-contract: sell half at +100% pre-catalyst. Single contract: at +150% with >7 days to the catalyst, written EV, default sell. Mechanism expiry (BOTZ) overrides at any level. Backtested here at ~+$439 economic.
- **Mechanism override / BOTZ:** When the reason to hold expires (catalyst fired, theme window closed), sell regardless of price. What actually saved DKNG's +$251 in reality and in the backtest.
- **Sweep counter:** Standing decision -- every 5 closed positions, re-derive ladder thresholds from the actual winner distribution. The sanctioned place for threshold tuning; mid-cycle hand-tuning on 3 data points is curve-fitting.
- **Never-green loser:** A position whose contract never traded above entry (BSX confirmed; DSGX/CHWY presumed). The class that makes flat low-cap harvesting unprofitable: nothing offsets them.
- **Rule 6 (Reachability):** Required breakeven move ≤1.5x the stock's median earnings-day move. LYFT passes; ABT/TRMB/UBER/LVS as structured did not.
- **Economic total:** Realized P&L plus current open book value, used to compare strategies that close positions at different times.
