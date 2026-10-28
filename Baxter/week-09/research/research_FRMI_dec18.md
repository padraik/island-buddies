# FRMI $2.5C Dec18 2026: RESEARCH FILE (real-money doc)
*Tue Oct 27, 2026, 8:00pm ET (VM EVENING session 2 of 3, market closed). Found tonight by re-rating the 89-name liquid bottom-quartile pool (scan: $1-25, prints Nov 9 - Jan 29, call volume >= 500; log `screening_log_oct27_evening2.md`). FRMI died on R7 on Oct 20 (Dec18 $2.5C OI 246, 45% spread). Tonight the same contract shows OI 345.*

**Status: DOC COMPLETE. ENTRY GATED ON RULE 7 AT A LIVE QUOTE.** Every rule passes on the closing book except Rule 7's spread (28.6% at the close against a 25% limit). The buy happens at an OPEN or MIDDAY run only if that run's live quote, after 9:45am ET, shows spread <= 25% of mid, ask <= the max price below, and every other rule re-checks clean. This file is the paper trail, not a buy signal by itself.

---

## THE PLAY AT A GLANCE

| | |
|---|---|
| **Ticker** | FRMI (Fermi Inc., AI-power data-center REIT developing Project Matador in Texas; IPO Oct 2025) |
| **Option** | $2.5C Dec 18 2026 (call, strike $2.50, expires Fri Dec 18 2026; instrument `621e4131-6b94-43ac-b006-386af2b27e6f`, active, tradable, tick $0.05 under $3) |
| **Closing quote (3:59:59pm ET Oct 27)** | bid $0.45 (3,828) / ask $0.60 (3,599), mark $0.525, prior close $0.50, **OI 345**, volume 0, IV 119%, delta 0.64, theta -$0.0044/day |
| **Stock** | **$2.62 official close** (Mon $2.62 adj prev close; last trade $2.63), after-hours $2.64, 2.64 / 2.67 at 8:00pm |
| **Max price I'll pay** | the lower of **$0.622** (Rule 5, 3.5/5 on reserve $622.24) and the R6 line **stock x 1.2003 - 2.50** (at $2.62: $0.645; at $2.55: $0.56) |
| **At risk** | 1 contract, $60 at the closing ask (8.4% of the $713.24 fund; hard limit 7 cap $142.65) |
| **Breakeven** | $3.10 at a $0.60 fill (+18.3% from $2.62); $3.03 at mid $0.525 (+15.6%) |
| **Catalyst** | Q3 2026 earnings, tool **Thu Nov 12 AM, `verified: true`**; last year's Q3 **Mon Nov 10 2025 PM** |
| **Conviction** | 3.5/5, low confidence (revisions unverified; R7 fails at the close; 3 of the 4 prints were down) |
| **Verdict** | ENTER at OPEN/MIDDAY ONLY IF the live spread <= 25% of mid AND ask <= max price AND Rules 3/4/6 re-check clean that run |

---

## THE IRON RULES, LIVE NUMBERS (pulled this run, ~8:00pm ET Oct 27)

1. **Rule 1, range percentile: PASS, 0.006.** Daily bars (split-adjusted): 52w high $31.47 (Nov 2025, post-IPO), 52w low $2.44 (Oct 2026). ($2.62 - 2.44) / (31.47 - 2.44) = 0.18 / 29.03 = **0.006**. Scanner's own expression at $2.65: 0.004. At the bottom of the range.
2. **Rule 2, earnings before expiry: PASS.** (a) Later of tool date (Nov 12) and last year's date (Nov 10) = Nov 12; Dec 18 is **36 days** after it (needs 21). (b) 10-Q deadline: Fermi listed Oct 2025 and had under 12 months of reporting at FY2025 year-end, so it files as a non-accelerated filer this year: 45 days after Sep 30 = Sat Nov 14 -> **Mon Nov 16**. Dec 18 is **23 trading days** after it (needs 5). Even at the 40-day deadline (Nov 9), it passes. Q3 `actual: null`, not yet reported. Not a 6-K filer.
3. **Rule 3, ratings: PASS.** `get_equity_analyst_ratings`: **6 Buy / 2 Hold / 0 Sell.** Zero Sells, 6 >= 3 Buys, 6 Buys >= 2 Holds.
4. **Rule 4, bear floor: PASS, dated.** Tool low **$6.00**, mean $14.13, high $30 (no stamp on the record). Tonight's search (MarketBeat): **Cantor Fitzgerald Overweight, target cut $12 -> $8, Fri Oct 16, 2026.** That's a Buy-side target, set after the slide, 11 days old: the dated floor. The tool's $6 low is undated but sits under Cantor, and it still clears BE $3.10 by 94%. The other names in the aggregator (Berenberg Buy $37, UBS Buy $30, Redburn $31, Evercore Outperform, Stifel Buy) look like IPO-era initiations; their dates aren't verified tonight and they aren't needed. A Buy-rated cut to under ~$3.10 is the breach line.
5. **Rule 5, chain filter: PASS at the close.** Reserve = spendable = cash $622.24 - unsettled $0 = **$622.24** (`get_portfolio` buying_power $622.24 equals cash). 3.5/5 tier top 10% -> **max ask $0.622**. Closing ask $0.60.
6. **Rule 6, reachability: PASS, 17.0% at the closing ask vs a 20.0% cap.** Four prints (the whole public history; the rule needs 4-8):

   | Print | Timing | Base close | Reaction close | Move |
   |---|---|---|---|---|
   | Nov 10 2025 | PM | $25.31 (Nov 10) | $21.91 (Nov 11) | -13.4% |
   | Mar 30 2026 | AM | $6.18 (Mar 27) | $5.36 (Mar 30) | -13.3% |
   | May 14 2026 | AM | $6.00 (May 13) | $7.37 (May 14) | +22.8% |
   | Aug 13 2026 | AM | $7.60 (Aug 12) | $6.60 (Aug 13) | -13.2% |

   Median absolute move **13.35%**, cap 1.5x = **20.03%**. BE $3.10 / $2.65 (8pm quote) = +17.0%; vs the $2.62 official close +18.3%. Pass either way. **R6 line: ask <= stock x 1.2003 - 2.50.**
7. **Rule 7, liquidity floor: FAILS AT THE CLOSE. This is the gate.** OI **345** (pass, needs 250). Spread $0.15 on a $0.525 mid = **28.6%** (needs <= 25%, i.e. a nickel tighter: 0.45 / 0.55 or 0.50 / 0.60 passes). Closing spreads on this book run wide; the 3:35pm-style quote at a daytime run decides. On Oct 20 this contract had OI 246 and a 45% spread, so the market here is getting deeper, not thinner.

---

## WHY IT'S DOWN (decline category)

**Single-asset developer that lost its first tenant, then got one back.** Fermi IPO'd in Oct 2025 to build Project Matador, a large AI-power and data-center campus in Texas. In Dec 2025 the prospective first tenant terminated a $150M advance-in-aid-of-construction agreement, and the stock fell 42% in a day. It kept bleeding through 2026 on financing doubt (a developer with no signed anchor tenant can't raise project debt). **Oct 13, 2026: AMD agreed to provide credit support for a 222 MW TensorWave lease at Matador**, the first big lease, and the stock popped double digits. It has given that back and sits at $2.62, 0.6% of the way up its range. A proxy contest is also on file (DEFC14A, an activist slate), which means governance noise into the print.

**Category: company-specific, partly repaired.** The thing that broke it (no tenant) has a first fix (AMD-backed lease). The market hasn't paid for the fix yet. The Q3 print is the first report since the lease, so it's where management has to talk about financing.

---

## THE MEETING (Dec18 $2.5C, Oct 27 evening)

**Bullxter:** "Six-tenths of a percent of its range. Six Buys, zero Sells. And two weeks ago AMD put its own credit behind the first lease. That's the exact thing the stock fell on, fixed, and the price didn't move. The print is Nov 12, the first one since the lease. Sixty cents, December expiry, five weeks of cushion after the print."

**Calxter:** "Median move thirteen-and-a-third on four prints, cap twenty. We need seventeen at the ask. That passes with three points to spare, which is more room than QUBT had. But four prints is the minimum the rule allows, and one of those prints is from a stock at twenty-five dollars. Rule 5 caps us at sixty-two cents and the closing ask is sixty. Rule 7 is the problem: fifteen cents wide on fifty-two and a half, twenty-eight point six percent. One nickel tighter and it passes. That gets decided at a daytime quote, not tonight."

**Bearxter:** "My objection is the direction. Three of four prints went down thirteen percent. Rule 6 only measures size. This stock has a habit, and the habit is falling on earnings. Second: the floor is eight dollars from a shop that just cut from twelve. Analysts are cutting, not raising. Third: a proxy fight is never good news for a stock without a tenant financing plan. And a thirty-percent spread means we pay a dime going in and a dime coming out."

**Macxter:** "Context. The AMD lease is the first real financing signal since the IPO, and this is the first quarter it shows up in. AI-power is the hottest infrastructure theme going, and FRMI is the one name in it priced like it's going to fail. The prints that went down were the no-tenant quarters. This one isn't. I don't know which way the activist cuts. It could push a sale, which is a call tailwind, or just make noise."

**Prime:** "Bearxter gets his conditions. One: Rule 7 is computed off a regular-session live quote after 9:45. No buying a twenty-eight percent spread because it's close. Two: we sell the ramp, Wed Nov 11 3:35pm, before the AM print. So the down-on-earnings habit is not the bet. The bet is the drift and the IV ramp into the first post-lease print. Three: Rule 4 runs every hour. A Buy-side cut under three-ten means we exit that run. Four: one contract. Five: the direction point goes into the record. If this trade loses, that's the first thing the post-mortem checks."

**Answer to Bearxter, in one line:** we never hold through the print his history is about. We sell Wed Nov 11 before the AM report, so the bet is the two-week ramp into the first post-lease quarter, capped at one contract, with Cantor's post-cut $8 still 2.6x our breakeven.

---

## CONVICTION AND SIZING

**3.5/5.** Capped at 3.5 regardless: the estimate-revisions check (funnel line 11) needs a browser this machine doesn't have, and tonight's two searches didn't establish revision direction (Cantor's cut suggests down).

**Intra-score confidence:** R1, R2, R3 and R4 pass with lots of room and R6 clears by 3 points, but R7 fails at the close, the print history is only 4 deep and 3-of-4 down, and the floor shop just cut. This is a low-confidence 3.5: one contract, at the standard.

**Sizing (Tab 3 + Rule 5, reserve $622.24 = spendable at this run; re-derive at entry):**
- 3.5/5 range 6-10% -> $37.33 to $62.22. Standard 8% = $49.78.
- floor($49.78 / (0.60 x 100)) = 0, minimum 1 -> **1 contract.** Rule 5 is the real cap: one contract at <= $0.622 = <= $62.22 = 10.0% of reserve, the top of the tier. Hard limit 7: $142.65 (20% of $713.24).
- Hard limit 8: $65 (COUR) + $54 (QUBT) + $60 = $179 of a $427.94 ceiling (60% of fund). After COUR's ramp sell this week, $114. Limit 9: 3 of 5. Limit 10: 0 of 1 that day; 0 of 3 this week (QUBT was Oct 21, last week). Limit 11: new name, no averaging. Limit 12: $60 <= $622.24 spendable.
- Max loss: the premium paid, ~$55-62.
- Correlated bucket: QUBT (quantum) and FRMI (AI power) are both speculative-tech, risk-on names. Together they're $114 = 18% of reserve, under the 35% cap.

**The cost of buying early (Michael's order, Oct 7):** theta is -$0.0044/share/day ($0.44 per contract per day). From Wed Oct 28 to the Wed Nov 11 ramp sell is 14 calendar days, about **$6-8** of decay at today's rate (more as it accelerates). At IV 119%, the ramp into the print is the thing working the other way.

---

## EXIT PLAN

- **Ramp sell (default):** Q3 is **Thu Nov 12 AM, `verified: true`** (company-announced per the tool). The last trading run before a pre-market print is the day before: **deadline Wed Nov 11, 3:35pm ET (LASTCALL).** Window opens Tue Nov 10 (24-48h). If the date moves, the every-run check moves the deadline that run, into positions.md, watch_triggers.json and urgent.md.
- **Hold through only if:** already above breakeven ($3.10 at a $0.60 fill) 24-48h out AND re-written here with Bearxter's condition. No binary flag at entry (3.5/5 can't carry one).
- **Ladder:** single contract. At **+150%** with more than 7 days to the print: written hold-vs-sell EV in the journal the same run, default sell. A **GTC limit sell at 2.5x fill** (**$1.50** on a $0.60 fill; the first tick at or over 2.5x on any other fill) goes in right after the fill, placed with `time_in_force: gtc` stated explicitly and confirmed `gtc` on the order.
- **Pre-earnings profit target:** the dated floor is Cantor $8, out of reach. Proxy: stock at or above **$6.00** (the tool's low) before the print -> written same-run exit evaluation. watch_triggers `underlying_at_or_above: 6.00`.
- **Rule 4 trigger:** any Buy-rated target cut below breakeven, or the tool's low below breakeven -> sell same day, straight to the bid if needed.
- **Underlying drop trigger:** -10% intraday (it's a 119%-IV stock; -8% is a normal day) -> re-check Rule 4 and Fermi/Matador/proxy news that run.
- **Michael says no:** sold the next run, mid stepping to the bid.
- **BOTZ watch:** the ramp sell lands five weeks before expiry, so it shouldn't come up. If the position is somehow still open Dec 4 with no mechanism, sell the time value.
- **Never past:** the morning after the print, and **never into expiration day: out by Thu Dec 17** whatever happens.

---

## ORDER, WHEN THE GATES CLEAR

OPEN or MIDDAY, Wed Oct 28 onward (not before 9:45am ET; the last sensible entry is Mon Nov 9, which leaves a day of ramp):
1. Re-pull live: option quote, stock quote, ratings (R3, R4 low), `get_earnings_results` (R2, `actual: null`), portfolio/accounts (spendable, limits 7-12).
2. Max price = min($0.622 or 10% of that run's reserve, stock x 1.2003 - 2.50). R7: OI >= 250 and (ask - bid) / mid <= 25%.
3. If R7 passes and the ask <= max price: write the entry addendum to this file (live numbers, sizing on that run's reserve), **commit and push it**, then `review_option_order` (abort on any alert), buy **1x FRMI $2.5C Dec18** (`621e4131-6b94-43ac-b006-386af2b27e6f`) limit at mid, step toward the ask at most twice, never above max price. Unfilled at the end of the run -> cancel.
4. After the fill: positions.md row (catalyst date copied character-for-character from the `get_earnings_results` line above: **Thu Nov 12 AM, `verified: true`; LY Mon Nov 10 2025 PM**), the GTC at 2.5x fill, watch_triggers.json, urgent.md when inside 2 trading days, the r/smallstreetbets draft.

**Not Wednesday's job first:** COUR's ramp sell is Wednesday's priority. One entry per day; FRMI can be that entry only if COUR's sell is handled first in the same run or an earlier one.

---

## WHAT STILL HAS TO HAPPEN BEFORE A BUY

1. **Rule 7 at a regular-session live quote:** spread <= 25% of mid, OI >= 250.
2. That run's quote: R5 (<= 10% of that run's reserve) and the R6 line.
3. That run's ratings: still 0-1 Sells, >= 3 Buys, Buys >= Holds, nothing Buy-rated below BE.
4. `actual: null` and the date unchanged (or the exit plan re-derived).
5. The entry addendum committed before the order.

---

## GLOSSARY

- **Range percentile:** where the stock sits between its 52-week low (0) and high (1). Under 0.25 = calls zone.
- **Breakeven (BE):** strike + premium paid. The stock has to be above this at expiry for the call to be worth what it cost.
- **Bear floor / Rule 4:** the lowest Buy-side analyst target must sit above our breakeven, dated within 60 days and set after the decline; if it drops below, we sell that day.
- **Rule 5:** one contract's ask can't exceed the conviction tier's top percent of reserve (10% at 3.5/5).
- **Rule 6 (reachability):** the move needed to breakeven must be no more than 1.5x the stock's median earnings-day move over its last 4-8 prints.
- **Rule 7 (liquidity floor):** open interest at least 250 and a spread no wider than 25% of the midpoint, on the exact contract.
- **AM print:** the company reports before the 9:30 open; the reaction is that day's close vs the prior close.
- **Verified (earnings date):** the company announced the date itself, rather than a data vendor estimating it from past cadence.
- **10-Q deadline:** the SEC's last legal day to file the quarterly report (40 or 45 days after quarter end); the worst-case backstop for Rule 2.
- **Non-accelerated filer:** a smaller or newly public company that gets 45 days, not 40, to file its 10-Q.
- **IV ramp / sell the ramp:** option prices rise as earnings get close because uncertainty is priced in; we sell into that rise instead of holding through the report.
- **IV (implied volatility):** how much movement the option price assumes; 119% means the market expects big swings.
- **Theta:** how much the option loses per day from time passing, all else equal.
- **Open interest (OI):** contracts outstanding on that strike; a rough liquidity gauge.
- **Credit support:** a stronger company (here AMD) backing a weaker tenant's lease payments, which makes the lease financeable.
- **Proxy contest (DEFC14A):** an activist investor running its own slate of directors against management's at the shareholder vote.
- **REIT:** real estate investment trust; owns and leases property.
- **BOTZ rule:** a theme with no dated data event is dead money (named for Sheldon's robotics ETF).
- **GTC:** good-til-cancelled; a resting order that stays live across days.
- **Estimate revisions:** whether analysts have been raising or lowering their EPS forecasts recently.
- **Five-Baxter meeting:** Bullxter (the case for), Calxter (the math), Bearxter (the case against), Macxter (context/news), Prime (the decision).
