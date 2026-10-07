# ONDS (Ondas Inc.) — RESEARCH FILE
*Wed Oct 7, 2026, 12:35pm ET (VM MIDDAY run). Counter-drone and defense-autonomy roll-up, down 54% from its January high, revenue up about 13x in a year, buying companies as fast as it can sign the paperwork. Reports Q3 in about five weeks.*

**Status: DOC COMPLETE, ENTRY BLOCKED ON RULE 2 VERIFICATION.** Every number rule passes at the live ask this run (R6 at 93% of cap), and the floor is dated and fresh. The one gate left: the Nov 12 AM date is `verified: false`. With an AM print the ramp-sell deadline is the trading day before, so the date has to be the company's before money goes in (KR rule, Aug 7). This file is the paper trail, not a buy signal by itself.

**Per Michael's Oct 7 standing order ("I like buying early... time matters"),** there is no calendar entry window on this doc. The cost of buying early is written out under CONVICTION AND SIZING.

---

## THE PLAY AT A GLANCE

| | |
|---|---|
| **Ticker** | ONDS |
| **Option** | $8C Nov 20 2026 (call, strike $8.00, expires Nov 20, 2026; instrument `9d6ece20-12bf-487e-a664-04b851d1665a`) |
| **Live quote (12:35pm ET Oct 7)** | bid $0.41 / ask $0.42, mark $0.415, prior close $0.57, OI 10,604, volume 1,703, IV 76.8%, delta 0.37, theta -$0.0083/day |
| **Stock** | $7.045 (prior close $7.41, -4.9% today) |
| **Max price I'll pay** | **$0.51** (Rule 6 ceiling at a $7.045 stock: 7.045 x 1.2089 - 8.00 = $0.517; tighter than the Rule 5 line of $0.741). Recompute off the live stock price at entry. |
| **At risk** | 1 contract, $42 at the current ask (5.7% of the $741.32 fund; hard limit 7 cap is $148.26) |
| **Breakeven** | $8.42 at a $0.42 fill (+19.5% from $7.045) |
| **Catalyst** | Q3 2026 earnings, **Nov 12 AM, `verified: false`** (tool). Last year's Q3: Nov 13 2025 AM. All six of the last six prints were AM. |
| **Conviction** | 3.5/5, low confidence (revisions unverified; R6 at 93% of cap; operating losses widening) |
| **Verdict** | ENTER ONLY IF the company confirms the date, AND that run's live ask keeps BE inside the R6 cap, AND Rules 3/4 still pass |

---

## THE IRON RULES, LIVE NUMBERS (pulled this run, 12:35pm ET Oct 7)

1. **Rule 1, range percentile: PASS, 0.203.** `get_equity_fundamentals`: 52w low $4.95 (Nov 7, 2025), 52w high $15.28 (Jan 12, 2026). ($7.045 - 4.95) / 10.33 = 0.203. The $4.95 low rolls off after Nov 7; the percentile will rise then, but Rule 1 is an entry test.
2. **Rule 2, earnings before expiry: PASS on timing, verification pending.** Tool: Q3 Nov 12 AM, `verified: false`. Prior prints: May 15 2025, Aug 12 2025, Nov 13 2025, Mar 23 2026, May 14 2026, Aug 13 2026, all AM, all verified. 8 calendar days of buffer to the Nov 20 expiry. No date in the Sep 14 or Sep 23 press releases (read via EDGAR this run). **Gate:** company press release or `verified: true`.
3. **Rule 3, ratings: PASS, with room.** 11 Buy / 0 Hold / 0 Sell. The cleanest consensus in the queue.
4. **Rule 4, bear floor: PASS, dated, several shops.** Tool low $13 (undated, older). Lowest **dated** Buy target: **Citizens JMP Market Outperform $14, Oct 5, 2026** (initiation, 2 days old). Others: Needham Buy $19 (Sep 14), Ladenburg Buy $22.75 (Aug 17), Oppenheimer Outperform $18 (Aug 14); Citigroup Market Outperform (Oct 5, no target shown), Roth Buy (Aug 18, no target). Dating source: MarketBeat forecast page, pulled at 10:35am today (`screening_log_oct07_midday.md`). $14 vs BE $8.42 = 66% above. The floor stays fresh through the whole hold (Citizens JMP ages out Dec 4). Weiss "Sell (D+)" (Aug 4) is a quant grade, not a covering analyst; the tool counts 0 Sells.
5. **Rule 5, chain filter: PASS.** Reserve (= spendable, `cash - unsettled_funds` = $741.32 - $0.00) $741.32. 3.5/5 tier top 10% -> max ask $0.741. Live ask $0.42.
6. **Rule 6, reachability: PASS, 93% of cap.** Four prints, all AM, prior close to print-day close (from `screening_log_oct07_open.md`): **+19.1, +8.4, +26.5, -8.8**. Median absolute 13.93%, cap **20.89%**. Needs +19.5% at the $0.42 ask. Max BE $7.045 x 1.2089 = $8.517 -> **max price $0.51**. Today's -4.9% took the ceiling from $0.63 (OPEN) to $0.51; the ask fell with it. Requote at entry.

**Liquidity:** OI 10,604, spread one cent (0.41 / 0.42), 1,703 contracts traded by 12:35. The best market in the queue.

---

## WHY IT'S DOWN (decline category)

**Roll-up re-rate plus dilution.** ONDS ran from $4.95 (Nov 2025) to $15.28 (Jan 12, 2026) on counter-UAS and Israel/Europe defense demand, and has given back more than half. Nothing broke in the revenue line. The pressure is supply and burn:

- **Acquisitions paid partly in stock.** Sep 14 8-K (EX-99.2, read via EDGAR; `get_sec_filing` 404'd): "Ondas Acquires GATE Technologies and Bron Technologies," "$205 million upfront, comprised of $105 million in cash and $100 million in Ondas common stock," plus "$22.5 million of such stock consideration" within nine months and "earn-outs of up to $185 million through 2028" payable in cash or stock. Company expects "$65 million of revenue in full year 2026, increasing to $180 million revenue in 2028." Sep 23 8-K (EX-99.1): three more defense businesses (Insignito, Ottopia Defense, Caribou Labs), "purchase price represents less than three times the businesses' expected 2027 revenue," plus inducement awards of "2,979,063 shares... at $7.72 per share" to 37 new hires. Two 424B7 resale prospectuses (Sep 14, Sep 23) register shares for sellers to dump. Item 3.02 (unregistered equity) on Aug 10, Aug 28, Sep 14, Sep 23.
- **Burn.** Operating loss: -$10.3M (Q1 2025), -$9.3M (Q2 2025), **-$42.7M (Q1 2026), -$162.9M (Q2 2026)** on revenue of $50.1M and $83.8M. Cash: $550.7M (Dec 31) -> $1,026.0M (Mar 31, after raises) -> **$657.9M (Jun 30)**. Some of Q2's operating loss is likely acquisition-related (stock comp, amortization), but I didn't break it out this run.
- **Market cap $4.10B** (582M shares), P/B 2.5. This is not a cash-floor story like QUBT.

**The income-statement anomaly (passes.md flag since Jun 1): ANSWERED.** Q1 2026 10-Q (filed May 15, `get_sec_filing_facts`): net income +$362.8M came from **nonoperating income of +$404.2M**, almost all of it the **change in fair value of the warrant liability, $389.5M** (Level 3; the cash-flow line `FairValueAdjustmentOfWarrants` is -$389.5M, the non-cash gain backed out). The stock fell from $15.28 to the ~$7-9 range during Q1, so the warrants the company owes got cheaper and the drop booked as a gain. Operating loss that quarter was -$42.7M. Nothing dishonest, just the standard mark-to-market on liability-classified warrants. Corollary: if the stock rallies, Q3 books a warrant *loss*, so the headline EPS line can look ugly on a good quarter. The EPS estimate (-$0.10) may or may not model that; the reaction should follow revenue and guidance.

**What the print can deliver:** revenue went $6.3M (Q2 2025) -> $83.8M (Q2 2026). The GATE deal alone adds a guided $65M for 2026. With 11 Buys and a fresh $14 initiation, a revenue print that confirms the roll-up is consolidating cleanly is what the call is betting on. Two of the last four prints moved the stock more than +19%.

---

## THE MEETING

**Bullxter** had the chain open before anyone sat down. "Eleven Buys. Zero Holds. Zero Sells. A brand-new initiation at fourteen dollars two days ago. Ten thousand contracts open on our strike and a one-cent spread. Revenue up thirteen times in a year. The stock's down five percent today on nothing, and it's at twenty percent of its range. We're paying forty-two cents."

**Calxter:** "Median thirteen-ninety-three, cap twenty-point-eight-nine, we need nineteen and a half. Ninety-three percent of cap. Same neighborhood as QUBT. The difference is ONDS's prints actually move: plus nineteen, plus twenty-six. QUBT's last one moved two-tenths of a percent. And the ceiling moves with the stock: fifty-one cents today, sixty-three this morning. One more down day and the ask has to fall with it or we're out."

**Bearxter:** "Read the 10-Q, not the press releases. They lost a hundred sixty-three million dollars from operations last quarter on eighty-four million of revenue. Cash went from a billion to six-fifty-eight in three months. They're paying for acquisitions in stock and then filing prospectuses so the sellers can unload it. That's why it's down, and none of that stops on November twelfth. And the EPS line has a warrant mark in it that flips to a loss if the stock goes up. My objection: we're buying a call on a company that's diluting into every rally, and the print might be the moment the sellers get their exit."

**Macxter:** "The dilution is real and it's already in the price: that's what fifty-four percent off the high is. The analysts have all of it too. Citizens initiated *after* the September deals, at fourteen. Needham's nineteen is from September fourteenth, the same day as GATE. The floor isn't stale; it's fresh and it saw the dilution. Defense budgets in Israel and Europe aren't slowing down. And the AM print means the ramp sell is the afternoon before, so we never sit through the call."

**Prime:** "Bearxter's right about the burn, and it goes in the confidence line. Three answers. One: size. One contract, forty-two dollars, under six percent of the fund. Two: the exit. AM print, so the ramp sell is three-thirty-five the trading day before. We sell the anticipation, not the 10-Q. Three: the floor. Every Buy target on the Street is dated after the deals Bearxter's worried about, and the lowest is sixty-six percent above our breakeven. What Bearxter gets: no order without the company's date; the ceiling is fifty-one cents off today's stock, recomputed every run; a new 424B or a 3.02 filing while we hold gets read the same run; and an underlying drop of eight percent in a day triggers a Rule 4 re-check."

**Answer to Bearxter, in one line:** the dilution and burn explain the price, and every dated Buy target was set after them; we hold five weeks into the run-up and sell the day before the print, so the 10-Q's burn number never lands on us, and one contract caps what being wrong costs.

---

## CONVICTION AND SIZING

**3.5/5.** Capped at 3.5 regardless: the estimate-revisions check (funnel line 11) needs a browser this machine doesn't have, and no search established revision direction.

**Intra-score confidence:** R1, R3, R4 and R5 pass with room (11/0/0, floor 66% above BE, fresh dated targets), but R6 is at 93% of cap, operating losses quadrupled last quarter, and the date is unconfirmed, so this is a low-confidence 3.5 sized at one contract.

**Sizing (Tab 3 + Rule 5, reserve $741.32 = spendable at this run):**
- 3.5/5 range 6-10% -> $44.48 to $74.13. Standard 8% = $59.31.
- floor($59.31 / (0.42 x 100)) = 1 contract. Two contracts ($84) would be 11.3%, over the tier top. One contract at <= $0.51 = <= $51 = 6.9% of fund, inside hard limit 7 ($148.26).
- Hard limit 8: <= $51 deployed of a $444.79 ceiling (60%); with QUBT also entered, <= $111. Limit 9: 1 of 5. Limit 10: 0 entries today, 0 this week (if QUBT, COUR and ONDS all clear the same day, only one can go per day).
- Correlated cap (Tab 3, 35%): ONDS is defense; QUBT is quantum/tech theme; COUR is edtech. Different drivers.
- Max loss: the premium paid, $42-51.

**The cost of buying early (Michael's order, Oct 7):** theta is -$0.0083/share/day now ($0.83 per contract per day). Entering this week versus three weeks before the print costs roughly two extra weeks of decay at today's rate, about $0.12/share ($12 per contract), more as expiry nears. The IV ramp into an AM print works the other way. Written down so it's a known cost.

---

## EXIT PLAN

- **Ramp sell (default):** AM print, so the deadline is **3:35pm ET (LASTCALL) on the trading day before the print.** On the tool's Nov 12 AM date that's **Wed Nov 11, 3:35pm ET** (NYSE is open on Veterans Day). The company's confirmed date sets this, the same run it's announced.
- **Hold through only if:** already above breakeven 24-48h out AND re-written here with Bearxter's condition. No binary flag at entry (3.5/5 can't carry one).
- **Ladder:** single contract. At +150% (2.5x fill: $1.05 on a $0.42 fill) with more than 7 days to the print, a written hold-vs-sell EV in the journal the same run, default sell. A GTC limit sell at 2.5x fill gets placed right after the fill, `time_in_force: gtc` confirmed.
- **Pre-earnings profit target:** the lowest dated Buy target ($14) is out of reach in five weeks. Proxy: stock at or above **$10.00** (+42%) before the print -> written same-run exit evaluation. watch_triggers `underlying_at_or_above: 10.00`.
- **Rule 4 trigger:** any Buy-rated target cut below the real breakeven, or the tool's low below breakeven -> sell same day, straight to the bid if needed.
- **Underlying drop trigger:** -8% intraday -> re-check Rule 4 and read any new 8-K / 424B that run.
- **Michael says no:** sold the next run, mid stepping to the bid.
- **Never past:** the morning after the print, and **never into expiration day: out by Thu Nov 19** whatever happens.

---

## ORDER, WHEN THE GATES CLEAR

`review_option_order` first; buy 1x ONDS $8C Nov20 (`9d6ece20-12bf-487e-a664-04b851d1665a`), limit at mid, step toward the ask at most twice, **never above the R6 max price computed off that run's stock price** (max price = stock x 1.2089 - 8.00; today $0.51) or $0.741, whichever is lower. Unfilled at the end of the run -> cancel.

---

## WHAT STILL HAS TO HAPPEN BEFORE A BUY

1. **The company confirms the Q3 date** (press release or tool `verified: true`). Nov 12 AM is an estimate from cadence.
2. That run's quote: BE inside the R6 cap at the live stock price.
3. That run's ratings: still 0 Sells, >= 3 Buys, Buys >= Holds, nothing Buy-rated below BE.
4. One entry per day: if QUBT or COUR also clears the same run, the docs get compared on that run's numbers and only one goes.

---

## GLOSSARY

- **Range percentile:** where the stock sits between its 52-week low (0) and high (1). Under 0.25 = calls zone.
- **Breakeven (BE):** strike + premium paid. The stock has to be above this at expiry for the call to be worth what it cost.
- **Bear floor / Rule 4:** the lowest Buy-side analyst target must sit above our breakeven, dated within 60 days and set after the decline; if it drops below, we sell that day.
- **Rule 5:** one contract's ask can't exceed the conviction tier's top percent of reserve (10% at 3.5/5), capped at $1.00 for now.
- **Rule 6 (reachability):** the move needed to breakeven must be no more than 1.5x the stock's median earnings-day move over its last 4-8 prints.
- **AM print:** the company reports before the 9:30 open; the reaction is that day's trading. The ramp sell has to happen the afternoon before.
- **Verified (earnings date):** the company announced the date itself, rather than a data vendor estimating it from past cadence.
- **IV ramp / sell the ramp:** option prices rise as earnings get close because uncertainty is priced in; we sell into that rise instead of holding through the report.
- **Theta:** how much the option loses per day from time passing, all else equal.
- **Open interest (OI):** contracts outstanding on that strike; a rough liquidity gauge.
- **Warrant liability / fair-value gain:** warrants the company issued are carried as a debt-like liability at market value; when the stock falls, the liability shrinks and the drop is booked as non-cash income (and the reverse when it rises).
- **Item 3.02 / 424B7:** an 8-K item reporting shares issued without registration (here, acquisition consideration); a 424B7 is a prospectus that registers those shares so the holders can sell them. Both mean more supply of stock.
- **Roll-up:** a company growing mainly by buying other companies.
- **BOTZ rule:** a theme with no dated data event is dead money (named for Sheldon's robotics ETF).
- **GTC:** good-til-cancelled; a resting order that stays live across days.
- **Estimate revisions:** whether analysts have been raising or lowering their EPS forecasts recently.
- **Five-Baxter meeting:** Bullxter (the case for), Calxter (the math), Bearxter (the case against), Macxter (context/news), Prime (the decision).
