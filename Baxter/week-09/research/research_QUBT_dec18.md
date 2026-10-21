# QUBT $7C Dec18 2026 — RESEARCH FILE (real-money doc)
*Tue Oct 20, 2026, 8:00pm ET (VM EVENING session 2 of 3, market closed). Successor to `research_QUBT.md` (the Oct 7 Nov20 $8C doc, superseded by Rule 2's Oct 8 clarification and by the stock's slide). Parked by EVENING 1 tonight as the one real-money near-miss (`screening_log_oct20_evening1.md`).*

**Status: DOC COMPLETE. ENTRY GATED ON RULE 6 AT THE LIVE QUOTE and on the floor's date.** Every rule passes on tonight's numbers except Rule 6, which fails at the official $6.50 close and passes at the $6.63 after-hours print. The buy happens at an OPEN or MIDDAY run only if that run's live ask is at or under the R6 line below, every other rule re-checks clean, and the run is **on or before Fri Oct 23** (the dated floor ages out Sun Oct 25) unless a fresh dated Buy target turns up. This file is the paper trail, not a buy signal by itself.

---

## THE PLAY AT A GLANCE

| | |
|---|---|
| **Ticker** | QUBT (Quantum Computing Inc., Hoboken NJ, 77 employees) |
| **Option** | $7C Dec 18 2026 (call, strike $7.00, expires Fri Dec 18 2026; instrument `d92fe604-2aca-4cb3-a0b8-4779b06b511d`, active, tradable, tick $0.01 under $3) |
| **Closing quote (3:59:59pm ET Oct 20)** | bid $0.47 (35) / ask $0.52 (101), mark $0.495, prior close $0.46, OI 1,091, volume 47, IV 65.9%, delta 0.45, theta -$0.0061/day |
| **Stock** | **$6.50 official close** (+0.0% vs Mon $6.50; range $6.32-$6.77); after-hours $6.63 last, 6.60 / 6.64 at 8:00pm |
| **R6 line (max price)** | **ask <= stock x 1.13875 - 7.00.** At $6.50: $0.40. At $6.63: $0.55. At $6.57: $0.48. |
| **Max price I'll pay** | the lower of the R6 line at that run's live stock price and **$0.676** (Rule 5, 3.5/5 on reserve $676.28) |
| **At risk** | 1 contract, $52 at the closing ask (7.1% of the $729.28 fund; hard limit 7 cap $145.86) |
| **Breakeven** | $7.52 at a $0.52 fill (+15.7% from $6.50; +13.4% from $6.63) |
| **Catalyst** | Q3 2026 earnings, tool **Fri Nov 13 PM, `verified: false`**; last year's Q3 **Fri Nov 14 2025 PM**. All six prints in the tool are PM. |
| **Conviction** | 3.5/5, low confidence (revisions unverified; R6 lives or dies on a few cents of stock price; one dated floor that ages out Oct 25) |
| **Verdict** | ENTER at OPEN/MIDDAY Oct 21-23 ONLY IF the live ask <= the R6 line AND Rules 3/4/5/7 re-check clean that run |

---

## THE IRON RULES, LIVE NUMBERS (pulled this run, ~8:00pm ET Oct 20)

1. **Rule 1, range percentile: PASS, 0.033.** `get_equity_fundamentals`: 52w low **$6.08 (Oct 15, 2026, five days ago)**, 52w high $18.88 (Oct 20, 2025, rolls off tomorrow). ($6.50 - 6.08) / (18.88 - 6.08) = 0.42 / 12.80 = **0.033**. When the Oct 2025 high rolls off, the next high is lower (the May 2026 spike, ~$14.45), and the percentile is still ~0.05. Bottom quartile either way.
2. **Rule 2, earnings before expiry: PASS.** (a) Later of tool date (Nov 13) and last year's date (Nov 14) = Nov 14; Dec 18 is **34 days** after it (needs 21). (b) 10-Q deadline for the Sep 30 quarter: Nov 9 (accelerated, 40 days) or Mon Nov 16 (45 days, Nov 14 falls on a Saturday) at the latest; Dec 18 is **23 trading days** after Nov 16 (needs 5). Q3 `actual: null`: not yet reported. Not a 6-K filer.
3. **Rule 3, ratings: PASS.** `get_equity_analyst_ratings`: **5 Buy / 2 Hold / 0 Sell.** Zero Sells, 5 >= 3 Buys, 5 Buys >= 2 Holds.
4. **Rule 4, bear floor: PASS, dated, one shop, ages out Sun Oct 25.** Tool low **$10** is Cantor Fitzgerald **Hold** (Jun 24 per tonight's search; the Oct 7 doc had it as Aug 11), so it is not the floor, but it still clears BE $7.52 by 33%. Lowest **dated** Buy inside 60 days: **Ascendiant Buy $32, Aug 26, 2026** (55 days old tonight; turns 60 on **Sun Oct 25**, so the last trading day it counts is **Fri Oct 23**). Undated or stale Buys, all far above BE: Lake Street Buy $16 (Jul 6), Rosenblatt Buy $22 (Jun 29), Northland Outperform $20 (Apr 20). Tool high $32, mean $18.86. **Tonight's one search** ("QUBT analyst price target buy October 2026") found no new rating or target after Aug 26. The decline-dating check: Ascendiant's Aug 26 target came after the main slide ($24 -> ~$9 by August); the stock has fallen another ~25% since, so the floor is old in feel even inside 60 days. Bearxter's point, below.
5. **Rule 5, chain filter: PASS.** Reserve = spendable = cash $676.28 - unsettled $0 = **$676.28** (`get_portfolio` buying_power $676.28 equals cash; `get_accounts` returned 502 four times this run, see the journal). 3.5/5 tier top 10% -> **max ask $0.676**. Closing ask $0.52.
6. **Rule 6, reachability: FAIL at the close, PASS after hours. This is the gate.** Six prints, close on print day -> next close (all PM; table from `screening_log_oct20_evening1.md`):

   | Print | Close | Next close | Move |
   |---|---|---|---|
   | May 15 2025 | $9.24 | $12.87 | +39.3% |
   | Aug 14 2025 | $15.38 | $15.32 | -0.4% |
   | Nov 14 2025 | $10.60 | $11.50 | +8.5% |
   | Mar 2 2026 | $8.59 | $7.73 | -10.0% |
   | May 11 2026 | $10.18 | $11.78 | +15.7% |
   | Aug 10 2026 | $8.93 | $8.95 | +0.2% |

   Median absolute **9.25%**, cap **13.875%**. At the 0.52 ask, BE $7.52 needs **+15.69% from the $6.50 close: FAILS by 1.8pt.** (EVENING 1 measured off $6.57, an intraday print, and called it 0.58pt; the official close is $6.50.) From the $6.63 after-hours print it needs **+13.42%: passes by 0.45pt.** Line: **max ask = stock x 1.13875 - 7.00.**
7. **Rule 7, liquidity: PASS.** OI **1,091** (>= 250). Spread 0.05 on a 0.495 mid = **10.1%** (<= 25%). Volume 47 today. Re-measure at entry, after 9:45 (opening spreads).

**Correlation (Tab 3):** the only other holding is COUR (edtech, $65). Quantum/photonics is a different driver. No bucket issue.

---

## WHY IT'S DOWN (decline category)

**Theme unwind, now trading under book.** QUBT ran with the quantum group into October 2025 ($18.88 close a year ago today) and has bled since, to a fresh 52-week low of $6.08 last Thursday. Nothing company-specific broke that the record shows; the group re-rated and QUBT kept going. Market cap **$1.47B** (tool tonight), P/B **0.91** (was 1.12 on Oct 7): the market now values the company below its book, which is mostly cash from last year's raises. Revenue is still tiny (Q1 2026 $3.7M per the Oct 7 doc). Short of a print surprise, the stock follows RGTI / QBTS / IONQ, not its own news.

**What changed since the Oct 7 doc:** the stock went $7.555 -> $6.50 (-14%), P/B 1.12 -> 0.91, the Nov20 $8C is no longer the contract (Rule 2's Oct 8 reading plus last year's Nov 14 puts Nov20 at 6 days of cushion, fail), and the Dec18 $7C is the strike that sits just over the money with real open interest. The Rule 6 math is the same median; what moved is the stock.

---

## THE MEETING (Dec18 $7C, Oct 20 evening)

**Bullxter** had the quote up before anyone sat down. "Fifty-two cents, ten-ninety-one open interest, a nickel wide. Three percent of the range. Under book value. Five Buys, zero Sells. And it's December, so we're not sweating whether the print lands before expiry; it lands with five weeks to spare. Michael wants time. This is time."

**Calxter:** "Then here's the number that decides it. Median move nine-and-a-quarter on six prints, cap thirteen-eighty-eight. At the official close we need fifteen-seven. That's a fail. At the after-hours print we need thirteen-four. That's a pass. The line is stock times one-point-one-three-eight-seven-five minus seven. I don't want anyone arguing about it at the open, I want it computed off the live bid/ask and then the order goes in or it doesn't. And remember the median has a +39% and a -0.4% in it. The distribution is fat on both ends. We're selling before the print anyway, so what we're really buying is five weeks of the stock drifting plus the IV ramp."

**Bearxter:** "My objection is the floor and the trend, together. The floor that makes Rule 4 pass is one shop's thirty-two-dollar target from August, when the stock was nine. It's gone stale in five days, and nobody has put out a new Buy since. Meanwhile the stock printed a new 52-week low last Thursday. When a name keeps making lows and the bulls go quiet, the next analyst note is the cut, not the raise. That's the CCL, NKE, BSX pattern the dating rule was written for. And the after-hours print that makes Rule 6 pass is six cents on a thin evening book. If we buy because of an after-hours tick, we're buying a rounding error."

**Macxter:** "Two context points. One: quantum names trade as a group, and the group's been weak for a year; there's no group catalyst I can date inside our window. Two: under-book is real support. A company trading at ninety-one percent of book with most of the book in cash has a floor that isn't an analyst's opinion. That doesn't make it go up. It makes the downside slower."

**Prime:** "Bearxter gets the conditions, all of them. One: no order off an after-hours print. Rule 6 is computed off the regular-session live quote at an OPEN or MIDDAY run, after 9:45, and the ask has to be at or under the line. Two: the buy window closes Friday Oct 23 at 3:35, the last trading run Ascendiant's target still counts, unless a fresh dated Buy above breakeven turns up. Three: if any analyst cuts to a Buy target under breakeven, or the tool's low drops under breakeven, it's a Rule 4 exit that run. Four: one contract, under the 8% standard. Five: we sell the ramp, so the -10% and -0.4% prints aren't our problem; the drift between now and Nov 12 is."

**Answer to Bearxter, in one line:** the trade only exists if the regular-session market hands us the Rule 6 price before the floor ages out on Friday; if it does, the stale-floor risk is capped at one contract, checked every run with a same-day exit, and the stock's under-book cash cushion is the thing slowing the slide he's worried about.

---

## CONVICTION AND SIZING

**3.5/5.** Capped at 3.5 regardless: the estimate-revisions check (funnel line 11) needs a browser this machine doesn't have, and tonight's one search did not establish revision direction.

**Intra-score confidence:** R1, R2, R3, R5 and R7 pass with room, but R6 passes or fails on a few cents of stock price and the only dated floor ages out in five days, so this is a low-confidence 3.5: one contract, under the 8% standard.

**Sizing (Tab 3 + Rule 5, reserve $676.28 = spendable at this run; re-derive at entry):**
- 3.5/5 range 6-10% -> $40.58 to $67.63. Standard 8% = $54.10.
- floor($54.10 / (0.52 x 100)) = **1 contract.** One contract at <= $0.55 = <= $55 = 8.1% of reserve, inside the tier, inside hard limit 7 ($145.86 = 20% of $729.28).
- Hard limit 8: $65 (COUR) + $52 = $117 of a $437.57 ceiling (60% of fund). Limit 9: 2 of 5. Limit 10: 0 of 1 today, 0 of 3 this week. Limit 11: new name, no averaging. Limit 12: $52 <= $676.28 spendable.
- Max loss: the premium paid, ~$52-55.

**The cost of buying early (Michael's order, Oct 7):** theta is -$0.0061/share/day ($0.61 per contract per day). From Oct 21 to the Nov 12 ramp sell is 16 trading days, about **$10-12** of decay at today's rate (more as it accelerates), against an IV ramp into a print that has moved the stock a median 9%. Written down so it's a known cost.

---

## EXIT PLAN

- **Ramp sell (default):** until the company announces, the deadline is the trading day before the earliest of (tool Nov 13, LY Nov 14): **Thu Nov 12, 3:35pm ET (LASTCALL).** If the company announces a date, the every-run check moves it that run: for a PM print, the last trading run before the print (that day's 3:35pm LASTCALL). If it announces an earlier date (the Oct 7 aggregators guessed Mon Nov 9 PM), the deadline moves earlier the same run, into positions.md, watch_triggers.json and urgent.md.
- **Hold through only if:** already above breakeven 24-48h out AND re-written here with Bearxter's condition. No binary flag at entry (3.5/5 can't carry one).
- **Ladder:** single contract. At **+150%** with more than 7 days to the print: written hold-vs-sell EV in the journal the same run, default sell. A **GTC limit sell at 2.5x fill** (e.g. **$1.30** on a $0.52 fill; first nickel at or over 2.5x on any other fill) goes in right after the fill, placed with `time_in_force: gtc` stated explicitly and confirmed `gtc` on the order.
- **Pre-earnings profit target:** the lowest dated Buy ($32) is out of reach. Proxy: stock at or above **$10.00** (the tool's overall low) before the print -> written same-run exit evaluation. watch_triggers `underlying_at_or_above: 10.00`.
- **Rule 4 trigger:** any Buy-rated target cut below breakeven, or the tool's low below breakeven -> sell same day, straight to the bid if needed. Ascendiant aging out (Oct 25) on a held position is not a breach by itself; that run writes it up and searches once for a fresh dated Buy. A fresh Buy target below BE is a breach.
- **Underlying drop trigger:** -8% intraday -> re-check Rule 4 and quantum-group news that run.
- **Michael says no:** sold the next run, mid stepping to the bid.
- **BOTZ watch:** the ramp sell lands five weeks before expiry, so it shouldn't come up; if the position is somehow still open Dec 4 with no mechanism, sell the time value.
- **Never past:** the morning after the print, and **never into expiration day: out by Thu Dec 17** whatever happens.

---

## ORDER, WHEN THE GATES CLEAR

OPEN or MIDDAY, Wed Oct 21 to Fri Oct 23 (not before 9:45am ET):
1. Re-pull live: option quote, stock quote, ratings (R3, R4 low), `get_earnings_results` (R2, `actual: null`), portfolio/accounts (spendable, limits 7-12).
2. R6 line = live stock (regular-session last, or the bid if last is stale) x 1.13875 - 7.00. Max price = min(R6 line, $0.676). R7: OI >= 250, spread <= 25% of mid.
3. If the live ask <= max price: write the entry addendum to this file (live numbers, sizing on that run's reserve), **commit and push it**, then `review_option_order` (abort on any alert), buy **1x QUBT $7C Dec18** (`d92fe604-2aca-4cb3-a0b8-4779b06b511d`) limit at mid, step toward the ask at most twice, never above max price. Unfilled at the end of the run -> cancel.
4. After the fill: positions.md row (catalyst date copied character-for-character from the `get_earnings_results` line above: **Nov 13 PM, `verified: false`; LY Nov 14 PM**), the GTC at 2.5x fill, watch_triggers.json, the r/smallstreetbets draft.

---

## WHAT STILL HAS TO HAPPEN BEFORE A BUY

1. **Rule 6 at a regular-session live quote:** ask <= stock x 1.13875 - 7.00. Not after hours, not off the mark.
2. **Date window:** a run on or before **Fri Oct 23 3:35pm**, or a fresh dated Buy target above BE.
3. That run's ratings: still 0-1 Sells, >= 3 Buys, Buys >= Holds, nothing Buy-rated below BE.
4. That run's quote: R5 (<= $0.676 on that run's reserve) and R7.
5. The entry addendum committed before the order.

---

## GLOSSARY

- **Range percentile:** where the stock sits between its 52-week low (0) and high (1). Under 0.25 = calls zone.
- **Breakeven (BE):** strike + premium paid. The stock has to be above this at expiry for the call to be worth what it cost.
- **Bear floor / Rule 4:** the lowest Buy-side analyst target must sit above our breakeven, dated within 60 days and set after the decline; if it drops below, we sell that day.
- **Rule 5:** one contract's ask can't exceed the conviction tier's top percent of reserve (10% at 3.5/5).
- **Rule 6 (reachability):** the move needed to breakeven must be no more than 1.5x the stock's median earnings-day move over its last 4-8 prints.
- **Rule 7 (liquidity floor):** open interest at least 250 and a spread no wider than 25% of the midpoint, on the exact contract.
- **PM print:** the company reports after the 4pm close; the reaction shows up the next trading day.
- **Verified (earnings date):** the company announced the date itself, rather than a data vendor estimating it from past cadence.
- **10-Q deadline:** the SEC's last legal day to file the quarterly report (40 or 45 days after quarter end); the worst-case backstop for Rule 2.
- **IV ramp / sell the ramp:** option prices rise as earnings get close because uncertainty is priced in; we sell into that rise instead of holding through the report.
- **Theta:** how much the option loses per day from time passing, all else equal.
- **Open interest (OI):** contracts outstanding on that strike; a rough liquidity gauge.
- **P/B (price to book):** market value divided by the company's net assets; under 1 means the market values it below what's on the balance sheet.
- **After-hours print:** a trade outside the 9:30-4:00 session; thin and not used for entry math.
- **BOTZ rule:** a theme with no dated data event is dead money (named for Sheldon's robotics ETF).
- **GTC:** good-til-cancelled; a resting order that stays live across days.
- **Estimate revisions:** whether analysts have been raising or lowering their EPS forecasts recently.
- **Five-Baxter meeting:** Bullxter (the case for), Calxter (the math), Bearxter (the case against), Macxter (context/news), Prime (the decision).
