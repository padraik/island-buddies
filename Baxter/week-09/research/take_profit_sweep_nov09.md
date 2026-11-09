# THE TAKE-PROFIT SWEEP -- Round 4

*Baxter, Mon Nov 9, 2026, EVENING 1 (6pm ET, VM). Sweep counter hit 5 of 5 on the ACHR close at LASTCALL (3:36pm ET). LASTCALL does no analysis, so the sweep runs here, first thing in the next research session, before any entry. Entries were blocked from 3:36pm until this doc was committed. Same method as Jul 10, Aug 4 and Aug 12, plus the three standing agenda items in positions.md.*

---

## METHOD (unchanged)

Sell the ENTIRE position the first time it trades at entry plus X%. Positions that never reach X% follow their actual exits. Peaks come from archived daily bars (`data/contract_history/`), which are trade highs, not bids, so a bar high overstates what could have been sold. Where only a mark existed (TIGR), it's called out. YALA has no archive (pre-dates the Jul 13 archiving rule's enforcement on hand-closed trades); its session notes say the stock "ground down all session" and the position never went green.

## THE FIVE CLOSES SINCE AUG 12

| # | Ticker | Contracts | Entry | Exit | Realized | Peak seen | DTE at entry | Exit type |
|---|---|---|---|---|---|---|---|---|
| 1 | YALA $5C Aug21 | 2 | $0.50 (Aug 12) | $0.45 (Aug 17) | -$10 (-10%) | never green (notes) | 9 | ramp, called early |
| 2 | TIGR $4.5C Sep4 | 1 | $0.51 (Aug 19) | $0.50 (Aug 21) | -$1 (-2%) | mark +42% (0.725 on a 0.35 / 1.10 book, OI 6); real bid never above +0% | 16 | discretionary, 5 days pre-print |
| 3 | BILI $17.5C Aug28 | 2 | $0.64 (Aug 19) | $0.19 (Aug 26) | -$90 (-70%) | never green | 9 | ramp |
| 4 | COUR $5C Nov20 | 1 | $0.65 (Oct 8) | $0.35 (Oct 28) | -$30 (-46%) | 0.88 bar high Oct 16 (+35%) | 43 | ramp, OTM |
| 5 | ACHR $4C Dec18 | 1 | $0.53 (Nov 3) | $1.05 (Nov 9) | +$52 (+98%) | ~1.05 mid at exit (book 0.95 / 1.16); prior bar high 0.79 Nov 6 (+49%) | 45 | ramp, ITM |

**Total actual: -$79.** Three never-green losers (YALA, BILI, plus COUR, which peaked at +35%) = -$130 that no take-profit cap touches. TIGR's +42% was a mark on a six-lot book, never a real bid. One real winner: ACHR.

## THE SWEEP

| Hard take-profit at | ACHR result | Others | 5-trade total | vs actual -$79 |
|---|---|---|---|---|
| +50% ($0.795) | sold ~$0.80 on Nov 9 morning (Nov 6 bar high 0.79 fell a cent short), +$27 | actual | -$104 | **-$25** |
| +100% ($1.06) | the 3:35 mid was 1.055, a half-cent short; the bid never got there. Actual | actual | -$79 | $0 |
| +150% ($1.33, the resting GTC) | never reached. Actual | actual | -$79 | $0 |
| No cap (what we did) | +$52 | | **-$79** | baseline |

**No tested cap beats what actually happened, and the lowest one costs $25.** This is the same shape as Aug 12: the ramp sell, not a cap or the ladder, decided the only winner.

## WHAT HOLDING THROUGH THE PRINT WOULD HAVE DONE (the ramp rule's test, record only)

Both Monday sells reported after the close tonight. Both missed EPS:
- **ACHR** Q3 EPS -$0.35 vs -$0.27 est. Stock closed $4.815 (+8.4%) and traded **$4.56 after hours** (-5.3%, 6pm ET). The $4C would be ~$0.56 intrinsic plus whatever time value survives the IV crush. My estimate is $0.70-0.85, against the $1.05 we sold at. No after-hours option quote exists, so this is an estimate, not a number.
- **QUBT** Q3 EPS -$0.07 vs -$0.06 est. Closed $6.87 (+8.5%), **$6.62 after hours** (-3.6%). The $7C is OTM again. I'd guess $0.40-0.50 against the $0.62 we sold at (also an estimate). QUBT is close #1 of the next cycle, not part of this sweep's five.

Two for two, the ramp sell beat holding. That's the HITI lesson behaving the way the binder says it should.

## STANDING AGENDA ITEMS

**1. Brandt's DTE question (Aug 11, open since sweep #3).** Is the sell-the-ramp default capping winners before the ladder can fire? The new data:
- Era 1's three closes in this set (YALA, TIGR, BILI) had 9-16 days of life. Era 2's two (COUR, ACHR) had 43-45, because the Oct 8 Rule 2 text forces 21+ days past the print. The short-DTE squeeze Brandt described is gone structurally in Era 2.
- ACHR is the first Era 2 winner. It did its whole run in the four sessions before the print (+49% Nov 6 high, +98% at the ramp sell), and the stock gave back 5% after hours on a miss. QUBT did the same thing on a smaller scale.
- **Finding:** in Era 2 the ramp sell isn't capping winners. The run-up *is* the trade, and the print is where it gets taken back. Brandt's mechanism was real for 9-day contracts. With 40+ DTE it doesn't show up. **Not a rule change.** The item stays open one more sweep, because one winner isn't a distribution, but it now leans toward "the ramp default is right."

**2. Rule 5 counterfactual log (Jul 30).** For each Rule-6-era Era 2 close, what one step closer (lower strike, same expiry) would have done. Pulled tonight via `get_option_historicals` (daily trade bars) and Monday's 3:59pm closing quotes:

| Close | Held | Return | One strike closer | Entry | Exit | Return | R5 at entry (3.5/5 line = 10% of reserve) |
|---|---|---|---|---|---|---|---|
| COUR | $5C Nov20 | -46.2% | $4C Nov20 | 1.30 (Oct 8 close) | 0.85 (Oct 28 close) | **-34.6%** | fails ($130 vs ~$68 line) |
| QUBT | $7C Dec18 | +14.8% | $6C Dec18 | 1.22 (Oct 21 close; 1.00 open) | 1.13 mid (Nov 9 4pm; bid 0.91) | **-7.4%** (+13% off the open) | fails ($100-122 vs ~$54 line) |
| ACHR | $4C Dec18 | +98.1% | $3C Dec18 | 1.29 (Nov 3 close) | 1.87 mid (Nov 9 4pm; bid 1.61) | **+45.0%** | fails ($129 vs ~$54 line) |

The closer strike won on the loser (it lost less) and lost on both winners. It also would have cost 2-2.5x the premium per contract, and Rule 5 would have blocked all three at our reserve. Caveat: the closer-strike exits are 4pm closing marks, not the 3:35 books we actually sold into, so they slightly understate the closer strikes on ACHR and QUBT (both stocks were ~2% higher at 3:35). **The log now has 3 Era 2 Rule-6-era closes, so the first unlock condition is met. The second isn't: reserve is $539.11 against the $1,500 milestone. The unlock stays locked.** Nothing here argues for loosening anyway.

**3. Rule 3 "one Sell vs zero" (Oct 5).** Era 2 closes since the Oct 5 tightening: COUR 8/4/0, ACHR 8/2/0, and QUBT (next cycle) 5/2/0. Every one had zero Sells at entry. **No evidence either way yet.** Carried to the next sweep.

## OTHER FINDINGS

- **Every Era 2 position has been a single contract** (Rule 5 at a ~$540 reserve). The scale-out ladder needs 2+, so in Era 2 it has never been eligible to fire. The single-contract +150% hold-vs-sell line is the only take-profit mechanism live, and nothing has reached it (ACHR peaked at +98%). This isn't a threshold problem. It's what reserve size does, and Michael already said on Oct 9 that growth comes from deposits.
- The resting +150% GTCs (COUR 1.65, ACHR 1.33, QUBT 1.35, FRMI 1.65) never filled. They cost nothing and they guard against a gap-up, so they stay.

## VERDICT

**No threshold changes.** Ladder (+100% sell half for 2+ contracts), single-contract +150% hold-vs-sell line, ramp timing (last trading run before the print), and the daily/weekly entry ceilings all stay where they are. With no binder edit there's no `SWEEP #4: <change>` binder commit. This doc plus the counter reset in positions.md is the record.

**Sweep counter reset: 1 of 5** (QUBT, closed Nov 9 3:37pm ET, one minute after ACHR, carried in as close #1 of the next cycle). **Entries unblocked** as of this commit.

Carried to sweep #5: the Brandt DTE item (needs a second Era 2 winner), Rule 3 one-Sell (needs a one-Sell entry), Rule 5 unlock (needs $1,500 reserve).

---

## GLOSSARY

- **Take-profit sweep:** every 5 closed positions, re-test the exit thresholds against what actually happened. The binder says thresholds get re-derived from the data, not defended.
- **Sell the ramp:** sell before earnings, while the pre-print run-up and the high implied volatility are still in the price, instead of holding through the report.
- **Scale-out ladder:** with 2+ contracts at +100% before the catalyst, sell half. With one contract at +150% and more than 7 days to go, write down whether to hold or sell (the default is sell).
- **DTE:** days to expiration.
- **IV crush:** the drop in an option's implied volatility, and so its price, right after earnings, when the uncertainty is gone.
- **Mid / mark:** halfway between bid and ask. The bid is what you can actually sell at.
- **Bar high:** the highest trade in a day's price bar. On thin options it can be a single print that nobody could have sold into.
- **Rule 5:** one contract's ask can't exceed the conviction tier's percent of reserve (10% at 3.5/5).
- **Rule 5 counterfactual log:** compares each close with the next strike closer to the money, to test whether the affordability cap is pushing the fund into worse contracts.
- **Reserve:** spendable settled cash at entry.
- **Rule-6-era close:** a position entered after Rule 6 (reachability: the needed move fits the stock's typical earnings move) was in force.
- **EPS:** earnings per share. A "miss" is a reported EPS below the analyst estimate.
