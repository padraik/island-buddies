# Exit Mechanism Audit -- Aug 12, 2026

*Baxter. Follow-through on the open item from tonight's sweep (`take_profit_sweep_aug12.md`) and Brandt's Aug 11 DTE question: across every closed trade the fund has, what actually decided the exit -- the +100% scale-out ladder, the Tab 4 sell-the-ramp default, or something else entirely?*

---

## METHOD

Every closed position, in order, classified by the real reason it closed (not by whether it happened to be profitable). Source: `positions.md` check-in narratives and `binder.md` Tab 5 lessons, both already-written contemporaneous records, not re-derived from price data. Six categories emerged from the data itself rather than being decided in advance:

- **LADDER** -- the +100% scale-out trigger fired (or the tick-constrained nearest equivalent)
- **RAMP-SELL** -- Tab 4's default: sold into the pre-earnings premium 24-48h out, OTM, no binary-hold exception
- **RULE 4 BREACH** -- bear floor broke, same-day exit per the standing rule
- **BOTZ / MECHANISM RESOLVED** -- the reason to hold expired (thesis window closed, catalyst date proved wrong, no remaining data event) independent of price level
- **DISCRETIONARY REDEPLOY** -- closed early to free capital for a better-ranked name, not because of any rule firing
- **PROCESS FAILURE** -- a standing order that should have executed never became a real order in the account

## THE FULL LEDGER

| Trade | Realized | Exit mechanism | Ladder-eligible? (2+ contracts, post-Jul10) |
|---|---|---|---|
| CCL | +$1 | Rule 4 breach | No -- pre-ladder era |
| DSGX | -$30 | Discretionary redeploy | No -- pre-ladder era |
| CHWY | -$23 | Discretionary redeploy | No -- pre-ladder era |
| NKE | -$70 | Rule 4 breach | No -- pre-ladder era |
| MDT | +$23 | BOTZ (mechanism expired, catalyst window closed) | No -- pre-ladder era |
| DKNG | +$251 | BOTZ (sentiment window closed, no data mechanism left) | No -- pre-ladder era |
| BSX | -$15 | Rule 4 breach | No -- pre-ladder era |
| HITI | -$12 | Old pre-audit default (hold through, sell at open) -- since retired | No -- pre-ladder era, and this is the exact trade that got the old default replaced |
| ABT | +$27 | Ramp-sell (proto-version, own standing order, pre-dates Tab 4's formal Jul 10 ratification) | No -- single contract, grandfathered explicitly |
| LYFT (ladder trigger) | +$90 | **LADDER** -- clean +100%/$1.80 automatic fire | Yes |
| TRMB (trim) | +$32 | **LADDER** -- tick-constrained nearest fill below the true +100% mark | Yes |
| LVS | -$67 | Process failure -- ramp-sell was the plan, the order never got placed, rode through earnings unprotected | Yes, but never got the chance |
| TRMB (close) | +$42 | BOTZ (the recorded catalyst date was found wrong; real print wasn't for another 1-2 weeks, sold rather than hold on a false premise) | Yes, but not what actually decided it |
| UBER | -$112 | Discretionary risk-cut -- Rule 6 math had become unreachable (+28.6% needed vs a 7.7% cap), sold ahead of the ramp window rather than wait for it | Yes, but Rule 6 deterioration decided it first |
| DIS | +$39 | **RAMP-SELL** -- clean Tab 4 default, sold within ~3-4% of its real peak | Yes, never reached |
| LYFT (close) | +$26 | **RAMP-SELL** | Yes, never reached (peaked ~+30%) |
| KR | -$40 | BOTZ (mechanism resolved -- real earnings date was 6 days past the contract's own expiry, catalyst could never happen) | Yes, never reached |
| JMIA | -$24 | **RAMP-SELL** | Yes, never reached |
| UAMY | -$34 | **RAMP-SELL** | Yes, never reached |
| BTBT | +$30 | **RAMP-SELL** (same-day, compressed by the AM/PM timing correction) | Yes, never reached (peaked ~+40%) |

## THE TALLY

**Ladder-eligible trades (post-Jul 10, 2+ contracts): 10.** Of those:
- **Fired the ladder: 2** (LYFT trigger, TRMB trim) -- both in the same 10-day window right after the ladder was ratified.
- **Closed by ramp-sell instead: 5** (DIS, LYFT close, JMIA, UAMY, BTBT) -- none of these five ever reached even a +50% mark before being sold.
- **Closed by BOTZ/mechanism-resolution before the ladder was ever relevant: 2** (TRMB close, KR).
- **Closed by process failure or discretionary risk-cut before the ladder got a chance: 2** (LVS, UBER).

**The ladder has fired exactly twice, ever, and never once since Jul 20 -- three and a half weeks and eight ladder-eligible closes ago.**

## FINDING

This confirms, with a real sample instead of two data points, what the Aug 12 sweep and Brandt's DTE question both pointed at separately. **The scale-out ladder was designed for a shape of trade the fund mostly isn't running anymore.** It fired twice in its first ten days and hasn't fired since, not because positions stopped winning -- five of the eight subsequent ladder-eligible closes were profitable or at least reached real conviction -- but because the sell-the-ramp default, BOTZ-style mechanism resolution, and process/risk-cut decisions are consistently resolving positions *before* price ever climbs high enough for +100% to matter.

Two real, distinct explanations, not mutually exclusive:

1. **Entries have gotten closer to their own catalysts with less total runway** (Brandt's framing) -- KR, JMIA, UAMY, and BTBT were all entered with single-digit total DTE, which compresses the window between "enter" and "the ramp-sell decision" to almost nothing. There's less time for a position to run before the exit rule fires regardless of price.
2. **The current sizing/conviction era (Rule 6, post-Jul 10) has produced tighter, more discipline-bound entries overall** -- Rule 4 live-breach and Rule 6 reachability checks are cutting positions on math (UBER) or catalyst validity (KR, TRMB) before a price-based mechanism ever gets a turn.

## WHAT THIS DOESN'T MEAN

Not a verdict that the ladder is broken or should be removed. It fired clean both times it got the chance, and both fires were profitable. It's a verdict that **the ladder is currently a rarely-used backstop, not the primary exit mechanism the binder's language implies it is** -- Tab 4 lists it first, but in practice the ramp-sell default is doing most of the real work.

## OPEN QUESTION FOR MICHAEL

Nothing here requires a rule change tonight. It does raise a real question worth his explicit call, not mine to decide alone: **should entries be sized/timed to give the ladder more room to actually matter** (longer DTE-at-entry where Rule 6 allows it), or **is the current shape -- ramp-sell doing most of the work, ladder as a rare bonus -- actually fine, since the fund's realized P&L (+$134) is positive either way?** This is the natural next step after Brandt's question and tonight's sweep, not a new thread -- same open item, now with the full ledger behind it instead of two trades.

## GLOSSARY

- **Ladder-eligible:** a position with 2+ contracts, entered on or after Jul 10, 2026 (when the scale-out ladder was ratified) -- the population this audit is scored against.
- **BOTZ:** the fund's standing rule that themes/mechanisms without a remaining data event are dead money, applied both to entries and to hold decisions (when the mechanism expires, so does the reason to hold).
- **Ramp-sell:** Tab 4's default exit -- selling an OTM position into elevated pre-earnings premium 24-48 hours out, rather than holding through the print.
- **Rule 4 breach:** the bear floor (lowest Buy-rated analyst target) drops below breakeven on a live position -- same-day exit, no exceptions.
