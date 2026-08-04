# THE TAKE-PROFIT SWEEP -- Round 2
*Baxter, Aug 4, 2026, mid-afternoon. Sweep counter hit 5 of 5 on the DIS close. Same method as Jul 10, applied to the 5 closes since then.*

---

## METHOD (unchanged from Jul 10)

Same rule tested: sell the ENTIRE position the first time it marks at entry plus X%; positions that never reach X% follow their actual historical exits. Data source this round is real order-log fills (robin_stocks/MCP get_option_orders) plus recorded session-note marks for interim price color -- **not** `fetch_option_history.py`'s raw historicals endpoint, which returned corrupted data for both DIS and UBER when checked today (see Tab 5 lesson, logged separately). This is a genuine gap from the Jul 10 method, which had clean archived candles for its two winners; this round's peak estimates for TRMB and DIS lean on discrete order-log price points and session-note marks rather than continuous daily data. Flagged, not hidden.

## THE FIVE CLOSES SINCE JUL 10

| Ticker | Entry | Exit | Realized | Ever crossed a meaningful cap? |
|---|---|---|---|---|
| ABT | $0.78 (Jun 1, pre-ladder, grandfathered) | $1.05 (Jul 16) | +$27 (+34.6%) | Yes -- real peak $1.95 (Jul 7, +150%), confirmed via archived candles |
| LVS | $0.435 avg x2 (Jun 29) | $0.10 x2 (Jul 29) | -$67 | Never green at any recorded mark |
| TRMB | $0.38 x2 (Jun 17, pre-ladder, ladder applied anyway) | $0.70 + $0.80 (Jul 28/29) | +$74 (+97.4%) | Touched ~+97% (chain ask $0.75) repeatedly Jul 7/16/20; never cleanly confirmed above +100% until the exit itself |
| UBER | $0.65 x2 (Jun 18) | $0.09 x2 (Jul 29) | -$112 | Never green at any recorded mark |
| DIS | $0.87 (Jul 30, post-audit, fresh 13-line funnel) | $1.26 (Aug 4) | +$39 (+44.8%) | Real peak ~$1.28-1.30 (Aug 3-4 session marks), sold within ~3-4% of it |

**Fixed baseline from the 2 never-green positions:** -$179 (LVS -$67, UBER -$112). This round's whole question is again a redistribution of a small number of trades, not a broad sample -- same caveat as Jul 10, now n=3 (ABT, TRMB, DIS) instead of n=2.

## THE SWEEP

| Hard take-profit at | ABT result | TRMB result | DIS result | 3-trade total | vs actual +$140 |
|---|---|---|---|---|---|
| +50% | +$39 | ~+$74 (never confirms an earlier fill; cap ≈ actual) | ~+$35 (near peak, cap slightly under actual) | ~+$148 | +$8 |
| +100% | +$78 | ~+$76 (first clean touch above +100%, close to actual) | actual (+44.8%, never confirmed above +100%) | ~+$193 | +$53 |
| +150% | +$117 (right at the confirmed peak) | actual | actual | ~+$230 | +$90 |
| No cap (what we actually did) | +$27 | +$74 | +$39 | **+$140** | baseline |

*(TRMB and DIS rows above are less precise than ABT's, which has clean archived candles -- see method note. Where a cap's trigger price wasn't clearly confirmed above or below by the discrete data points available, the actual result is carried forward rather than guessed.)*

## FINDINGS

**1. ABT is still the fund's one clear, repeated counterexample -- and it's the same lesson as Jul 10, not a new one.** Every cap from +50% to +150% beats ABT's actual +$27, for the same reason flagged twice before (Jul 13 profit-taking consult, Jul 16 close): a GTC limit sell was live through the peak and never filled because the peak decayed before the limit price was reached, and the eventual exit came from an earnings gap that only partially recovered the lost ground. This is grandfathered, single-contract, pre-ladder -- the scale-out ladder that exists specifically to prevent this can't apply to a 1-contract position by construction. Nothing about this round changes the standing conclusion; it just adds a third confirmed data point to a pattern that was already well-documented.

**2. Unlike Jul 10's round (where DKNG and MDT both blew past every cap tested), this round's other two real trades (TRMB, DIS) show caps and actual performance landing close together.** TRMB's mechanism exit (scale-out trim + earnings-date-correction sale) captured value within a few points of where a +100% flat cap likely would have, because the contract spent weeks oscillating just under +100% before a real move finally cleared it near the very end -- there wasn't a big uncaptured peak sitting further out, unlike DKNG's or MDT's paths in the original sweep. DIS is too young (5 days) to have developed a large peak-vs-exit gap either way.

**3. The gap between "the ladder wins" (Jul 10's clean verdict) and "this round is closer to a toss-up" is explained by which mechanism did the work.** Jul 10's two winners (DKNG, MDT) were saved by mechanism *timing* (BOTZ: the reason to hold expired well before a price cap would have fired). This round's two winners (ABT excluded as the counterexample; TRMB) were governed more by *chain mechanics* (the $0.05 tick size meant the "ladder trigger" and "sell at the best real price" ended up being nearly the same action) than by a mechanism genuinely riding past where a flat cap would have sold. The lesson isn't that mechanism-based exits stopped working -- it's that this batch of trades didn't happen to produce a large, sustained right-tail move the way DKNG did, so there was less for any exit philosophy to capture or miss.

**4. No threshold change is indicated by this round.** The winner distribution didn't change shape enough to justify re-deriving anything -- three winners (n up from 2 to 3, ABT/TRMB/DIS), still a small sample, still dominated by one recurring, already-understood counterexample. Per the Jul 10 sweep's own standing caveat, thresholds get re-derived "if the winner distribution changes shape, not defended from the old" -- it hasn't changed shape here, so the ladder and Tab 4 rules as written stand unchanged.

## OPEN ITEM: THE RULE 5 COUNTERFACTUAL LOG

The Jul 30 standing sweep-agenda addition asks for the Rule 5 counterfactual specifically: what the blocked $101C would have returned against the filled $105C, at equal sizing budget, now that DIS has closed. **Not completed in this pass** -- it requires pulling the $101C's actual price history from Jul 30 through today, which wasn't done as part of today's live trading session (Michael was mid-session on the DIS/LYFT exit decisions when this sweep became due). The Rule 5 unlock milestone (Tab 6) still requires 3+ Rule-6-era closes and $1,500+ reserve regardless -- DIS is only the first Rule-6-era close, so the milestone isn't reachable yet either way. Queued for the next research session rather than rushed here.

## VERDICT

Sweep counter reset to 0 of 5. No standing rule changes. ABT's grandfathered pre-ladder status remains the fund's one open scar tissue -- worth remembering the next time a single-contract position threatens to repeat the same decay-then-partial-recovery shape, since the current rules still can't scale-out a position that only has one contract to scale.

## TAB 5 LESSON (new, this session)

**`fetch_option_history.py`'s raw historicals endpoint returned corrupted data for both DIS and UBER when checked Aug 4, 2026** -- both showed price data starting August 2025 (over a year before either position existed) with implausible peak values (DIS supposedly hit $11.63, a 1236% move that live quotes minutes earlier contradicted directly). The ABT and LYFT archives already in the repo are clean because they were built from real order-log fills and manually-verified session marks, not this script's raw output -- this round's DIS/LVS/TRMB/UBER archives follow that same order-log method. **The historicals script itself needs debugging before it's trusted again** -- likely an instrument-matching bug on strike/expiry collisions (multiple listings sharing a strike across different real expirations). Until fixed, contract-history archiving should use order logs (`get_option_orders` by chain_id) plus session-note marks, the same method that's always worked for ABT.
