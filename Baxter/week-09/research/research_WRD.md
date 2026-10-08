# WRD (WeRide Inc.) — RESEARCH FILE
*Wed Oct 7, 2026, 8:00pm ET (VM EVENING 2). Guangzhou robotaxi and robobus company, ADR on Nasdaq, at a fresh 52-week low the same day its 52-week high rolls off. Beat Q2 revenue by ~30% and fell 9.6% anyway. Reports Q3 around Nov 23, before the open.*

**Status: DOC COMPLETE, ENTRY BLOCKED.** Three gates, all named:
1. **Rule 2 verification:** Nov 23 AM is `verified: false` (tool). AM print, so the ramp sell is the trading day before; the date has to be the company's before money goes in (KR rule, Aug 7).
2. **Rule 4 freshness at entry:** the floor is dated and post-decline tonight (BofA Buy $10.70, Aug 14; Morgan Stanley Overweight $12, Aug 19), but it **ages out Oct 13 (BofA) and Oct 18 (MS)**. WeRide likely confirms its date in early-to-mid November, by which time both are stale unless Q3 previews refresh them. On the day the date confirms, there has to be a Buy-side target dated inside 60 days.
3. **Price:** passes at mid only. Max price $0.659 at a $4.965 stock; the ask is $0.75 (fails Rule 5's $0.741 line and Rule 6). A fill at or under the max price is required.

**Per Michael's Oct 7 standing order ("I like buying early... time matters"),** no calendar entry window. The cost of buying early is written out under CONVICTION AND SIZING.

---

## THE PLAY AT A GLANCE

| | |
|---|---|
| **Ticker** | WRD |
| **Option** | $5C **Jan 15 2027** (call, strike $5.00; instrument `a952b2ab-f6b2-4f87-a097-676a4c35b72a`). WRD lists no Dec 18 expiry: Nov 20 expires before the print, Jan 15 is the first contract that covers it. |
| **Live quote (Oct 7 close, pulled 8:00pm ET)** | bid $0.55 (size 5) / ask $0.75 (size 1,446), mark $0.65, prior close $0.73, OI 2,263, volume 13, IV 62.1%, delta 0.57, theta -$0.0034/day |
| **Stock** | $4.965 last regular trade (official close $4.96; after hours $4.96) |
| **Max price I'll pay** | **$0.659** (Rule 6 ceiling: 4.965 x 1.1397 - 5.00). Tighter than the Rule 5 line of $0.741. Recompute off the live stock price at entry. |
| **At risk** | 1 contract, $65 at mid (8.8% of the $741.32 fund; hard limit 7 cap $148.26) |
| **Breakeven** | $5.65 at a $0.65 fill (+13.8% from $4.965) |
| **Catalyst** | Q3 2026 earnings, **Nov 23 AM (Mon), `verified: false`** (tool). Last year's Q3: Nov 24 2025 AM. All six reported prints were AM. |
| **Conviction** | 3.5/5, low confidence (revisions unverified; R6 at 99% of cap at mid; floor expires before the likely entry date) |
| **Verdict** | ENTER ONLY IF the company confirms the date AND a Buy target dated inside 60 days sits above BE AND that run's fill keeps BE inside the R6 cap |

---

## THE IRON RULES, LIVE NUMBERS (pulled this run, 8:00pm ET Oct 7)

1. **Rule 1, range percentile: PASS, 0.009.** `get_equity_fundamentals`: 52w low $4.90 (Oct 7, 2026, today), 52w high $12.405 (Oct 8, 2025). ($4.965 - 4.90) / 7.505 = 0.009. The high rolls off tomorrow; the next-highest weekly high in the window will be lower, but at a fresh 52-week low the percentile stays near zero.
2. **Rule 2, earnings before expiry: PASS on timing, verification pending.** Tool: Q3 Nov 23 AM, `verified: false`. History: May 21 2025, Jul 31 2025, Nov 24 2025, Mar 23 2026, May 13 2026, Aug 12 2026, all AM, all verified. 53 calendar days of buffer to the Jan 15 expiry. **Gate:** company announcement or `verified: true`.
3. **Rule 3, ratings: PASS, with room.** 13 Buy / 0 Hold / 0 Sell (tool). MarketBeat shows Weiss Ratings "Sell (D-)" (Sep 25 upgrade from E+); that's a quant grade, not a covering analyst, and the tool counts 0 Sells, same treatment as ONDS.
4. **Rule 4, bear floor: PASS tonight, dated, post-decline; ages out Oct 13 / Oct 18.** Tool low $10.51 (13 Buys, so it's a Buy-side number; likely BofA's $10.70 after an FX or ADR conversion). Dated targets (MarketBeat forecast page, pulled this run): **Bank of America Buy $10.70, Aug 14, 2026**; **Morgan Stanley Overweight $12.00, Aug 19, 2026**; HSBC Buy $11.40 (Mar 31), BNP Paribas Exane Outperform $11 (Mar 26), CLSA Outperform $13 (Jan 5), UBS Buy $12 (Aug 2025), Goldman Buy (Apr 16, no target), Citi Buy (Jan 19, no target). **Post-decline test:** on Aug 14-19 the stock traded $5.64-6.49 (weekly bars), against a 52-week high of $12.405; it was already at about the 10th percentile of its range. Both August targets were set after the slide, not before it. $10.70 vs BE $5.65 = 89% above. **Freshness:** BofA turns 60 days on Oct 13, Morgan Stanley on Oct 18. After that, no dated floor until someone publishes again (Q3 previews usually land in the two weeks before the print).
5. **Rule 5, chain filter: PASS AT MID, FAILS AT THE ASK.** Reserve (= spendable, `cash - unsettled_funds` = $741.32 - $0.00) $741.32. 3.5/5 tier top 10% -> max ask $0.741. Ask $0.75 fails by a penny; mid $0.65 passes.
6. **Rule 6, reachability: PASS AT MID, 99% of cap.** Four AM prints, prior close to print-day close (from `screening_log_oct07_evening1.md`, `get_equity_historicals`): **Nov 24 2025 +14.72, Mar 23 2026 +8.98, May 13 2026 -0.78, Aug 12 2026 -9.64.** Median absolute 9.31%, cap **13.97%**. Max BE = 4.965 x 1.1397 = $5.659 -> **max price $0.659.** Mid $0.65 -> BE $5.65, +13.8%. At the ask, BE $5.75 (+15.8%) fails. Only four prints are in the tool's history window with reliable bars; the median is thin.

**Liquidity:** OI 2,263, but the bid side is 5 contracts and the spread is 20 cents (27% of mid). Volume 13 today. A fill at mid is not guaranteed; the ask size (1,446) says the sellers are there at $0.75.

---

## WHY IT'S DOWN (decline category)

**Sector de-rating plus persistent losses, not a broken business.** WRD peaked at $12.405 on Oct 8, 2025 in the robotaxi run (Uber partnership, Middle East launches) and has bled down since: ~$7.66 at the start of June, $5.3-6.5 through July-September, a fresh low of $4.90 today.

- **Q2 2026 (Aug 12, AM):** revenue RMB 230M, +82% y/y and +103% q/q, about 30% above expectations; gross margin 37.5% (+9.4 pts); L4 operations revenue RMB 130M (+47% y/y); overseas revenue +164% y/y, 13 countries; fleet ~3,400 L4 vehicles incl. 1,800+ robotaxis (Jul 31). **Net loss RMB 401M**, narrowed only 1% y/y; EBITDA loss RMB 335M. **Cash and liquid resources RMB 5.4B (~$750M at ~7.2 RMB/USD)** against a $1.68B market cap; P/B 1.79. Sources: WeRide 6-K exhibit 99.1 (SEC), Gasgoo summary of the release.
- **The tape's verdict:** the stock fell 9.64% on that beat. The market isn't paying for revenue growth while the loss line doesn't move. That is the main thing the call is fighting.
- **No dilution event found this run.** I didn't read the 6-K list for an offering; that's a PREMARKET check before any entry (EDGAR fallback if `get_sec_filing` 404s).

**What the print can deliver:** a quarter where the loss line finally narrows meaningfully alongside revenue growth. The Nov 2025 print (+14.72%) is the template: that quarter's beat came with narrowing losses. The thesis is that 13 Buys with targets 2x the stock describe a mispricing a clean Q3 can start closing.

---

## THE MEETING

**Bullxter:** "Thirteen Buys, zero Holds, zero Sells. Every target is more than double the stock. The lowest dated one, Bank of America at ten-seventy, was set in August with the stock already at six. Revenue doubled quarter on quarter, gross margin up nine points, and half the market cap is cash. It's at a fifty-two-week low tonight, the actual low, today."

**Calxter:** "Median nine-thirty-one, cap thirteen-ninety-seven. At sixty-five cents we need thirteen-point-eight. Ninety-nine percent of cap. That's the thinnest pass in the book. At the ask it fails, at seventy-five. The max price is sixty-six cents and moves with the stock: every ten cents the stock drops takes eleven cents off the ceiling. Theta is a third of a penny a day, so the Jan contract is cheap to hold. That's the one good thing about having no December."

**Bearxter:** "They beat revenue by thirty percent and the stock fell almost ten. That's the whole story. The market doesn't care about revenue here, it cares that they lose four hundred million yuan a quarter and that loss didn't shrink. Two of the last four prints went down. And your floor expires in six days. By the time WeRide tells us the date, Bank of America and Morgan Stanley are both stale, and you'll be standing there with a confirmed date and no floor. My objection: the print has shown it can't rescue this stock, and the paper that says otherwise is about to go out of date."

**Macxter:** "The ten-percent drop in August wasn't the beat getting ignored in a vacuum; China AV names were all getting sold, and PONY's on the kill list tonight for the same reason. Half the market cap in cash means the floor under the company isn't the analysts, it's the balance sheet. And the stale-floor point is a reason to wait, not a reason the thesis is wrong. Q3 previews come out the two weeks before the print; if the Street still believes, it'll say so in writing."

**Prime:** "Bearxter wins the timing. This doc doesn't authorize a buy on tonight's floor, because tonight's floor won't be the floor on entry day. Three conditions. One: the company's date. Two: a Buy target dated inside sixty days on that day, above breakeven, set after the decline; Bank of America and Morgan Stanley don't count past the eighteenth. Three: a fill at or under the R6 max price off that run's stock. One contract. AM print, so the ramp sell is Friday the twentieth at three-thirty-five. And Bearxter's point about the August reaction goes in the confidence line: this is a low-confidence 3.5."

**Answer to Bearxter, in one line:** the stale floor is a gate, not a footnote (no order without a Buy target dated inside 60 days on entry day), and the August reaction is why this sizes at one contract and sells the ramp the Friday before instead of betting on the print itself.

---

## CONVICTION AND SIZING

**3.5/5.** Capped at 3.5 regardless: the estimate-revisions check (funnel line 11) needs a browser this machine doesn't have; the tool carries no EPS estimates for WRD at all (`estimate: null` every quarter), so revisions are unverifiable here.

**Intra-score confidence:** R1, R3 and R4 pass with room (0.009, 13/0/0, floor 89% above BE), but R6 is at 99% of cap at mid and fails at the ask, the floor goes stale Oct 18, and the last print fell 9.6% on a beat, so this is a low-confidence 3.5 sized at one contract.

**Sizing (Tab 3 + Rule 5, reserve $741.32 = spendable at this run):**
- 3.5/5 range 6-10% -> $44.48 to $74.13. Standard 8% = $59.31.
- floor($59.31 / (0.65 x 100)) = 0, minimum 1 -> **1 contract**. One at <= $0.659 = <= $65.90 = 8.9% of fund, inside the tier and hard limit 7 ($148.26).
- Hard limit 8: <= $66 deployed of $444.79 (60%). Limit 9: 1 of 5. Limit 10: one entry per day, three per week; if COUR, QUBT, ONDS or BRSL clear the same run, compare on that run's numbers and only one goes.
- Correlated cap (Tab 3, 35%): WRD is China autonomous driving. Nothing else held or queued shares that driver (TME and FINV are China ADRs on different drivers; if TME and WRD are both live, China-ADR exposure gets watched against 35%).
- Max loss: the premium paid, about $65.

**The cost of buying early (Michael's order, Oct 7):** theta is -$0.0034/share/day ($0.34 per contract per day). Entering on Oct 8 vs. three weeks before the print (Nov 2) is ~25 days, about $0.09/share ($9 per contract) at today's rate. Low because the Jan 15 contract has ~100 days left. The bigger cost of waiting is the floor: in practice, entry waits on a fresh dated target anyway.

---

## EXIT PLAN

- **Ramp sell (default):** AM print, so the deadline is **3:35pm ET (LASTCALL) on the trading day before.** On the tool's Mon Nov 23 AM date that's **Fri Nov 20, 3:35pm ET**. Reset from the company's date the run it's announced.
- **Hold through only if:** already above breakeven 24-48h out AND re-written here with Bearxter's condition. No binary flag at entry.
- **Ladder:** single contract. At +150% (2.5x fill: $1.63 on a $0.65 fill) with more than 7 days to the print, a written hold-vs-sell EV in the journal the same run, default sell. A GTC limit sell at 2.5x fill placed right after the fill, `time_in_force: gtc` confirmed.
- **Pre-earnings profit target:** the lowest dated Buy target ($10.70) is out of reach in six weeks. Proxy: stock at or above **$6.50** (+31%, the August highs) before the print -> written same-run exit evaluation. watch_triggers `underlying_at_or_above: 6.50`.
- **Rule 4 trigger:** any Buy-rated target cut below the real breakeven, or the tool's low below breakeven -> sell same day, straight to the bid if needed. A floor that goes stale during the hold gets a same-run re-date search; no fresh Buy target above BE within the hold = treat as a Rule 4 question in writing that run.
- **Underlying drop trigger:** -8% intraday -> re-check Rule 4, read any new 6-K.
- **Michael says no:** sold the next run, mid stepping to the bid.
- **Never past:** the morning after the print (Tue Nov 24 open at the latest on the tool date). Expiry is Jan 15 2027, so "never into expiration day" is out by Thu Jan 14 at the very latest; in practice the position is closed by Nov 24.

---

## ORDER, WHEN THE GATES CLEAR

`review_option_order` first; buy 1x WRD $5C Jan15 2027 (`a952b2ab-f6b2-4f87-a097-676a4c35b72a`), limit at mid, step toward the ask at most twice, **never above the R6 max price off that run's stock** (stock x 1.1397 - 5.00; tonight $0.659) or $0.741, whichever is lower. Unfilled at the end of the run -> cancel.

---

## WHAT STILL HAS TO HAPPEN BEFORE A BUY

1. **WeRide confirms the Q3 date** (press release / 6-K, or tool `verified: true`).
2. **A Buy-side target dated inside 60 days, set after the decline, above breakeven,** on the entry day. BofA $10.70 (Aug 14) counts through Oct 13; Morgan Stanley $12 (Aug 19) through Oct 18.
3. That run's quote: a fill at or under max price (stock x 1.1397 - 5.00).
4. That run's ratings: still 0 Sells, >= 3 Buys, Buys >= Holds.
5. PREMARKET before entry: read the 6-K list since Aug 12 for an offering.

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
- **ADR:** American Depositary Receipt; a US-listed share representing stock of a foreign company.
- **6-K:** the report a foreign issuer files with the SEC (the foreign version of an 8-K), used for earnings releases and offerings.
- **RMB / yuan:** China's currency; about 7.2 to the dollar.
- **L4:** "Level 4" autonomy: the vehicle drives itself without a safety driver within a defined area.
- **Quant grade (Weiss):** a formula-driven rating, not a covering analyst with a model and management access; not counted under Rule 3.
- **GTC:** good-til-cancelled; a resting order that stays live across days.
- **Estimate revisions:** whether analysts have been raising or lowering their EPS forecasts recently.
- **Five-Baxter meeting:** Bullxter (the case for), Calxter (the math), Bearxter (the case against), Macxter (context/news), Prime (the decision).
