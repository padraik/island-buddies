# BRSL (Brightstar Lottery) — RESEARCH FILE
*Tue Oct 6, 2026, ~8:05pm ET (VM EVENING session 2). The old IGT lottery business, pure-play lottery since the gaming sale, down 44% from its 52-week high and sitting at 7% of its range, reporting Q3 in about four weeks.*

**Oct 7 EVENING 1 update: gate (2) closed, gate (3) dropped per Michael's Oct 7 order; only the company date is left, plus a max price now $0.16 on the lower stock price. See ADDENDUM at the end.**

**Status: DOC COMPLETE, ENTRY BLOCKED.** Three gates are open: (1) the Q3 date is `verified: false`, and the web disagrees with itself (Nov 3 / Nov 4 / Nov 5); (2) Stifel's rating on its Sep 25 $19 target isn't confirmed as a Buy, and the firm behind the $11.90 low isn't identified; (3) **entry window: not before Thu Oct 22** (Prime's call in the meeting below, on theta math). Every later run re-checks with live numbers before any order. This file is the paper trail, not a buy signal.

---

## THE PLAY AT A GLANCE

| | |
|---|---|
| **Ticker** | BRSL |
| **Option** | $11C Nov 20 2026 (strike $11.00; instrument `8de8b482-b4c8-4226-8088-ab41fba3fd05`) |
| **Live quote (4:00pm ET Oct 6 close, pulled 8pm)** | bid $0.20 / ask $0.30, OI 53, vol 8, IV 36.3%, delta 0.32, theta -$0.0055/day, vega $0.0128. Prior close $0.01 is a phantom print, ignore. |
| **Alternative** | $10C Nov20 (`dae4b4f1-3679-4b56-81c4-f63b0007e6a5`) 0.20 / 0.80, OI 87. Better breakeven ($10.50 at mid) but the ask fails R5. If its ask ever comes in to <= $0.741, it's the preferred instrument. |
| **Stock** | $10.22 (Oct 6 close $10.21) |
| **Max price I'll pay** | **$0.30** for the $11C (R6 line, see below; R5 alone would allow $0.741) |
| **At risk** | 1 contract, $30 (4.0% of the $741.32 fund) |
| **Breakeven** | $11.30 at the ask (+10.57%) |
| **Catalyst** | Q3 2026 earnings, **Nov 3 AM, `verified: false`** (tool). Web: one source says the call is Nov 4 8:00am, another says Nov 5. All six prior prints were AM and verified; Q3 2025 was Tue Nov 4. |
| **Conviction** | 3.5/5, low confidence (cap: estimate revisions unverified; R6 at 96% of cap) |
| **Verdict** | ENTER ONLY IF date confirmed AND Stifel/low-target check done AND on/after Oct 22 AND ask <= $0.30 AND R3/R4 pass on that run's pull |

---

## THE IRON RULES, LIVE NUMBERS (pulled this run)

1. **Rule 1, range percentile: PASS, 0.068.** 52w range $9.625 to $18.406 (daily bars Oct 6 2025 - Oct 6 2026). ($10.22 - 9.625) / 8.781 = 0.068.
2. **Rule 2, earnings before expiry: PASS on timing, verification pending.** Tool: Nov 3 AM `verified: false`. Expiry Nov 20 leaves 2+ weeks of buffer for any of Nov 3/4/5. Last year Brightstar put out a "to host Q3 results call on Tuesday Nov 4" release ahead of the print, so a company date is expected in the next two to three weeks. Per the Aug 7 rule (KR), real money waits for the company's date, because the ramp-sell deadline hangs on it.
3. **Rule 3, ratings: PASS.** 7 Buy / 3 Hold / 0 Sell (tool). 7 >= 3 Buys, 7 >= 3 Holds. Note: MarketBeat lists a Weiss quant grade "Sell (D+)" (reiterated Jul 10). Weiss is a quant grade, not a credentialed analyst with management access, and the tool doesn't count it; same treatment as COUR's Weiss grade. Zacks went Strong Sell -> Hold Jul 13 (also quant).
4. **Rule 4, bear floor: PASS on the number, one identification gap.** Tool low **$11.90** (all ratings), mean $16.61, high $21. $11.90 > $11.30 BE by $0.60 (5.3%). Dated actions (MarketBeat, this run): **Stifel, $19 target, Sep 25, 2026** (12 days old, set with the stock ~$10.5; rating not shown on the page: Stifel has been a Buy on the name, confirm it), **Jefferies, upgrade Hold -> Buy, $12 -> $16, Aug 13** (55 days, ages out of the 60-day window Oct 12; set at ~$11.5, before the last leg down), Truist Hold $13 (Jul 20), Deutsche Buy $15 (Jul 1, stale), Susquehanna Positive $15 (May 14, stale). **Who holds $11.90 isn't on any page I can read**; one search turned up a "low $11.00 / $12.60" from other aggregators, which don't match the tool. Since the tool's $11.90 is the lowest target of any rating, the lowest Buy target is at least $11.90 either way. Gate (2) is naming it, or at least confirming Stifel is a Buy so there's a dated, post-decline Buy target on file. **Exit trigger: tool low < breakeven -> sell same day.**
5. **Rule 5, chain filter: PASS.** Reserve (spendable, `cash - unsettled_funds` = $741.32 - $0.00) $741.32. 3.5/5 tier top 10% -> max ask $0.7413. Ask $0.30.
6. **Rule 6, reachability: PASS, barely.** Four prints (all AM, so prior close -> print-day close): Nov 4 2025 +0.42, Feb 24 2026 +5.13, May 12 2026 -9.55, Aug 4 2026 +11.77. Median absolute 7.34%, cap 11.01%, max BE $11.35. Needs +10.57% at a $0.30 fill: **96% of cap.** At $0.25, +10.08% (92%). Anything over $0.35 fails. This is why the max price is $0.30, not the R5 line.

**Liquidity:** OI 53, 8 contracts traded Oct 6, ask size 209, bid size 46. Thin but a real two-sided market; one contract is all we'd ever trade here.

---

## WHY IT'S DOWN (decline category)

**Mixed: a reported-revenue optics problem plus drift, not a broken business.** Q2 2026 (Aug 4): revenue $584M, -7% y/y, on higher service-revenue amortization from the $1.67B Italy Lotto licence (final payment April) and a U.K. contract transition. Italy revenue -15% ($259M -> $221M). But adjusted EBITDA +4% to $286M, margin 48.9% vs 43.5%, operating income swung to +$56M from -$60M, FY26 guidance reaffirmed ($2.50-2.55B revenue, $1.16-1.19B adj. EBITDA, >5% organic growth), and the OPtiMa savings target was raised from $80M to $100M. The stock jumped +11.8% on that print, peaked $11.57 (Aug 17), and has drifted to $10.22 since with no single event I could find. Down 44% from the $18.41 high a year ago (that high was right after the gaming sale and special-dividend period).

**The honest weak spot:** I couldn't find a reason for the Sep slide. Drift with no news is either a mispricing or something I haven't read yet. Two prints out of four went the wrong way or nowhere.

---

## THE MEETING

**Bullxter:** "Seven Buys, zero Sells, stock at seven percent of its range. Margin up five points on the last print, savings target raised, guidance held. The market sold the reported revenue line and the business underneath it got better. Stifel put a nineteen on it twelve days ago at ten and a half. The ask is thirty cents. Thirty dollars, four percent of the fund."

**Calxter:** "And it needs ten-and-a-half percent to break even, against an eleven percent cap. Ninety-six percent of cap. That's the thinnest R6 pass on the board. The biggest move this stock made on a print in a year was eleven-seven. So the 'expected' print, the median, doesn't get us there; we need roughly the best print of the year. Now the real math, because we sell the ramp: theta is half a cent a day. Buy tomorrow and hold to Nov 2, that's 26 days, about fifteen cents of decay on a thirty-cent option with the stock flat. Vega is 1.3 cents a vol point; IV is 36. If it ramps to 50 into the print, that's plus eighteen cents. Buy tomorrow and flat stock roughly breaks even. Buy Oct 22, eight trading days out, decay is maybe six cents and the ramp is the same. The entry date matters more than the entry price."

**Bearxter:** "Here's my objection. This is a thirty-cent lottery ticket on a lottery company. Literally. You need the stock's best day of the year to get paid at expiry, and you're telling me the plan is to sell before the day that's supposed to deliver it. So what pays us? Volatility going from 36 to 50 on a stock that moves seven percent on prints? Maybe. And nobody can tell me who has the eleven-ninety, or why it fell ten percent in September."

**Macxter:** "Two specifics. The Jefferies upgrade in August came off a Hold, and Stifel's nineteen in late September came after the slide, so the most recent Street actions point up. And Q3 is the first quarter where the raised OPtiMa savings show up against the Italy amortization, so there's a dated reason for this print to read better than the reported-revenue headline. The September slide: no news I could find. That's a hole, and it's on the PREMARKET list."

**Prime:** "Bearxter's objection is mostly right, and the answer is the structure, not the story. One: thirty dollars, one contract, bottom of the tier. The intra-score confidence is low because R6 barely clears. Two: Calxter's theta math sets the entry window: **no entry before Thu Oct 22**, so we're paying for the ramp and not a month of decay. Three: no binary hold, ever, on a 3.5. We sell by the last run before the print. Four: max price thirty cents; at thirty-five cents R6 fails and the play is dead. Five: nothing gets bought until Brightstar puts its own date out and someone names the eleven-ninety or Stifel shows as a Buy."

**Answer to Bearxter, in one line:** what pays us is the ramp plus any pre-print drift back toward the $11.57 August level, bought late enough that theta can't eat it, at a size where being wrong costs $30; the print itself, which is where you're right, is outside the hold window by design.

---

## CONVICTION AND SIZING

**3.5/5.** Capped at 3.5 regardless: estimate revisions can't be checked on this machine (no browser), and no search this run established their direction.

**Intra-score confidence:** R1, R3 and R5 pass with room, R4 passes by 5.3% with the low target unidentified, and R6 clears at 96% of cap, so this is a low-confidence 3.5, sized at the bottom of the tier.

**Sizing (Tab 3 + Rule 5, reserve $741.32 = spendable at this run):**
- 3.5/5 range 6-10% -> $44.48 to $74.13. Low confidence -> bottom, 6% = $44.48.
- floor($44.48 / (0.30 x 100)) = 1 contract. $30 = 4.0% of fund. Hard limit 7 cap $148.26: inside.
- Hard limit 8: $30 of a $444.79 ceiling. Limit 9: 1 of 5. Limit 10: checked on the entry day.
- Max loss: $30 (premium paid).
- Single contract, so the Tab 4 half-sell ladder doesn't exist; the +150% single-contract leg does.

---

## EXIT PLAN

- **Ramp sell (default):** sell by **the last trading run before the pre-market print.** If Nov 3 AM: **Mon Nov 2, 3:35pm ET (LASTCALL)**. If Nov 4 AM: Tue Nov 3, 3:35pm. If Nov 5 AM: Wed Nov 4, 3:35pm. Re-derived the run the company confirms.
- **Hold through only if:** never at 3.5/5 (binary flag needs 4/5+ and Bearxter's written condition).
- **Ladder:** single contract. GTC limit sell at **$0.75** (+150% on a $0.30 fill) placed right after the fill, `time_in_force: gtc` confirmed. If it fires with >7 days to the print, the written hold-vs-sell EV is moot: it's sold, default.
- **Pre-earnings profit target:** stock reaches **$11.90** (the bear floor) before the print -> written same-run exit evaluation, default sell.
- **Rule 4 trigger:** tool low target below the real breakeven (strike + fill, $11.30 at $0.30) on any run -> sell same day, straight to the bid if needed.
- **Michael says no:** sold the next run, at mid stepping to the bid.
- **Never past** the morning of the print (it's pre-market, so the ramp sell the day before is the real deadline), and **never into expiration day: out by Thu Nov 19** whatever happens.

## WATCH TRIGGERS (for `watch_triggers.json` on fill)
gain_pct_trigger +150, loss_pct_trigger -50, underlying_at_or_above $11.90, underlying_drop_pct_trigger -6 (re-check Rule 4), resting_order_ids = the $0.75 GTC.

---

## ORDER, WHEN THE GATES CLEAR

`review_option_order` first; buy 1x BRSL $11C Nov20 (`8de8b482-b4c8-4226-8088-ab41fba3fd05`), limit at mid ($0.25 on today's quote), step toward the ask at most twice, **never above $0.30**. Unfilled at the end of the run -> cancel.

---

## WHAT STILL HAS TO HAPPEN BEFORE A BUY

1. Q3 date confirmed by Brightstar (tool `verified: true` or a company release). Expected mid-to-late October.
2. Stifel's Sep 25 rating confirmed as a Buy, or the $11.90 holder named and dated within 60 days, after the decline.
3. Calendar: on or after Thu Oct 22.
4. That run's quote: ask <= $0.30 (R6 at the ask), and R3 still 0 Sells with Buys >= Holds, tool low > breakeven.
5. Open question for PREMARKET: why the stock slid ~10% in September.

---

## ADDENDUM, Oct 7 6:00pm ET (EVENING 1)

**Gate 3 dropped (Michael's standing order, Oct 7):** "You know I like buying early. I know they're more expensive, but I also feel like time matters a lot." The not-before-Oct-22 window was my own theta call, not a binder rule, so it is no longer an entry gate. Calxter's math above stays as the record of what entering early costs: about half a cent a day of decay on the $11C, roughly 13 cents from Oct 8 to Nov 2 with the stock flat.

**Gate 2 closed:** Stifel set $19 on Sep 25 (MarketBeat, no rating shown). Stifel has kept a Buy on Brightstar without a break: reaffirmed Buy May 13 (cut $20 -> $19), maintained Buy $19 Jun 4, and no downgrade appears on any page I could read. So the Sep 25 note is read as **Buy $19, 12 days old, set with the stock near $10.5, after the slide.** This is an inference from that unbroken record, not a quote of the Sep 25 note. Jefferies' Aug 13 upgrade to Buy $16 is also on file until Oct 12. The tool's $11.90 low is still unnamed, but as the lowest target of any rating it bounds the lowest Buy from below either way.

**R6 moved against us on price.** Stock $10.055 at the Oct 7 close (was $10.22 when this doc was written). Max BE = 10.055 x 1.1101 = **$11.16**. Close quote on the $11C: 0.10 / 0.20, OI 61. Ask BE $11.20 **fails** by 4 cents; mid BE $11.15 passes (99.9% of cap). **New max price: stock x 1.1101 - 11.00, which is $0.16 at $10.055.** The $0.30 cap above is replaced by that formula, recomputed on the live stock price at entry.

**What's left before a buy:** (1) Brightstar confirms the Q3 date (tool still Nov 3 AM, `verified: false`; last year Nov 4 AM); (4) that run's quote fits the max-price formula and R3/R4 still hold. Gate 5 (the September slide) is still an open question, not a gate.

---

## GLOSSARY

- **Range percentile (R1):** where the stock sits between its 52-week low (0) and high (1). Under 0.25 = calls zone.
- **Breakeven (BE):** strike + premium paid.
- **Bear floor / Rule 4:** the lowest analyst price target must sit above our breakeven; if it drops below, we sell that day. It has to be dated within 60 days and set after the decline (binder Tab 6).
- **Rule 5:** one contract's ask can't exceed the tier's top percent of reserve (10% at 3.5/5), capped at $1.00 for now.
- **Rule 6 (reachability):** the move to breakeven must be no more than 1.5x the median earnings-day move over the last 4-8 prints.
- **AM print:** results come out before the 9:30 open; the reaction is that same day, so the last chance to sell before it is the prior afternoon.
- **Verified (earnings date):** the company announced the date itself.
- **Theta:** how much the option loses per day from time passing alone.
- **Vega:** how much the option gains per one-point rise in implied volatility.
- **IV ramp / sell the ramp:** option prices rise into earnings as uncertainty gets priced in; we sell into that rise, before the print.
- **Weiss / Zacks grades:** quantitative model scores, not analyst ratings with management access; not counted in Rule 3.
- **OPtiMa:** Brightstar's cost-savings program.
- **Licence amortization:** the Italy Lotto licence fee gets expensed against revenue over its life, which shrinks reported revenue without touching cash generation the same way.
- **GTC:** good-til-cancelled resting order.
- **Five-Baxter meeting:** Bullxter (for), Calxter (math), Bearxter (against), Macxter (context), Prime (decision).
