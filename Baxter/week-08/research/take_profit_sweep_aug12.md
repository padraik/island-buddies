# THE TAKE-PROFIT SWEEP -- Round 3

*Baxter, Aug 12, 2026, evening. Sweep counter hit 5 of 5 on the BTBT close, same session it happened -- not deferred. Same method as Jul 10 and Aug 4, applied to the 5 closes since then.*

---

## METHOD (unchanged)

Sell the ENTIRE position the first time it marks at entry plus X%; positions that never reach X% follow their actual historical exits. Data source: real order-log fills (`get_option_orders`) plus recorded session-note marks for interim price color. `fetch_option_history.py` still not trusted (documented corrupted since Aug 4, not re-debugged -- a sweep doesn't clear the Fable-5 bar for fixing it).

## THE FIVE CLOSES SINCE AUG 4

| Ticker | Entry | Exit | Realized | Ever crossed a meaningful cap? |
|---|---|---|---|---|
| LYFT (remainder) | $0.90 (Jun 18) | $1.16 (Aug 6) | +$26 (+28.9%) | No -- highest recorded mark was $1.17 (Aug 3, +30%), never confirmed above that before the sale |
| KR | $0.50 x2 (Aug 7) | $0.30 x2 (Aug 10) | -$40 (-40.0%) | Never green -- calendar-trap close, not a price event |
| JMIA | $0.45 x2 (Aug 10) | $0.33 x2 (Aug 11) | -$24 (-26.7%) | Never green -- sell-the-ramp close while still OTM |
| UAMY | $0.50 x2 (Aug 10) | $0.33 x2 (Aug 11) | -$34 (-34.0%) | Never green -- sell-the-ramp close while still OTM |
| BTBT | $0.35 x4 (Aug 11) | $0.42-0.43 x4 (Aug 12) | +$30 (+21.4%) | No -- highest recorded mark today was $0.49 ask (+40%), sold at $0.42-0.43 under time pressure, ~10-15% below the session's own high but still never crossed +50% |

**Fixed baseline from the 3 never-green positions:** -$98 (KR -$40, JMIA -$24, UAMY -$34) -- unaffected by any take-profit cap, since there was never a profit to cap. Two real winners this round: LYFT remainder, BTBT.

## THE SWEEP

| Hard take-profit at | LYFT result | BTBT result | 2-trade total | vs actual +$56 |
|---|---|---|---|---|
| +50% | actual (never confirmed reaching 50%) | actual (peaked ~+40%, never reached 50%) | +$56 | $0 |
| +100% | actual | actual | +$56 | $0 |
| +150% | actual | actual | +$56 | $0 |
| No cap (what we actually did) | +$26 | +$30 | **+$56** | baseline |

**Every tested cap produces the identical result to what actually happened, because neither winner this round ever reached even the lowest cap tested.** This has never happened in any prior sweep -- Jul 10 and Aug 4 both had at least one position blow past +100%.

## FINDINGS

**1. Neither winner this round ever got close to the +100% scale-out ladder trigger.** LYFT topped out around +30%, BTBT around +40%, both sold by judgment (sell-the-ramp) well before any flat cap or the ladder itself would have mattered. This isn't evidence the ladder is miscalibrated -- it's evidence that in this particular window, the sell-the-ramp default did its job early enough that the ladder question never got exercised at all.

**2. Worth naming directly, since it's the second time this exact pattern has shown up this week: the sell-the-ramp default may be structurally capping upside below where the profit ladder would ever fire, for positions with tight pre-print timelines.** BTBT is a real data point for this -- entered with 10 total days of life, sold on a same-day AM-timing correction with the stock still climbing intraday. Brandt's unratified DTE question from Aug 11 (short total life meaning the ramp-sell decision arrives before a position has room to run) and this sweep's finding (winners this round never got the chance to reach +100%) are pointing at the same underlying mechanism from two different angles. Not a rule change tonight -- flagged as the same open item, now with a second, independent line of evidence behind it.

**3. The 3 losses this round are not informative for the take-profit question and shouldn't be read as one.** KR, JMIA, and UAMY all closed on Tab 4's sell-the-ramp discipline while still OTM -- correct process, real losses, nothing a take-profit cap could have changed since there was no profit at any point to cap. Two of the three (KR, UAMY) trace to date-verification failures already fully documented elsewhere (binder Tab 5, Aug 10-11 entries), not exit-mechanism failures.

**4. No threshold change indicated.** Same standing rule as the last two sweeps: thresholds get re-derived if the winner distribution changes shape, not defended from the old. This round's shape (small sample, both winners capped by the ramp rule rather than the ladder) doesn't argue for changing the ladder threshold itself -- it argues for finishing the Brandt DTE analysis, a different and still-open item.

## STANDING ITEM CARRIED FORWARD

**The Brandt DTE question (Aug 11, unratified) now has a second data point.** Next sweep, or sooner if Michael wants it prioritized: pull every closed play's DTE-at-entry against days-of-runway-to-actual-exit, and separately, whether the exit was ladder-triggered or ramp-triggered. If ramp-triggered exits are systematically capping gains below where the ladder would fire, that's worth a real rule, not just a running note.

## VERDICT

Sweep counter reset to 0 of 5. No standing rule changes to the ladder itself. The Rule 5 counterfactual log (Jul 30 standing addition) still isn't started -- still queued, still blocked on the same $101C pull that's been open since Aug 4, and the unlock milestone (3+ Rule-6-era closes, $1,500+ reserve) still isn't reachable regardless.
