# FSLR (First Solar): PAPER RESEARCH FILE
*Fri Oct 9, 2026, 8:00pm ET (VM EVENING 2). US thin-film solar maker, down ~40% from its June high, at about 5% of its 52-week range, reporting Q3 in about three weeks.*

**Status: PAPER POSITION (entered EVENING 1, 6:00pm Oct 9, at the 3:59pm closing ask).** No money. Rule 5 is dropped in the paper book (one contract costs $1,650; the real fund's 3.5/5 line is $0.676 a share). This doc is written to the same standard as a real one so the paper result tests the method, not a shortcut version of it.

---

## THE PLAY AT A GLANCE

| | |
|---|---|
| **Ticker** | FSLR |
| **Option** | $175C Nov 20 2026 (instrument `99f5f557-ba41-4590-acb3-0728c944c360`) |
| **Quote (close, 3:59:59pm Oct 9, re-pulled 8pm)** | 13.60 / 16.50, mark 15.05, OI 282, vol 11, IV 55.4%, delta 0.58, theta -0.166/day |
| **Stock** | $177.82 close (-0.6% from $178.85); after-hours $177.45 |
| **Paper fill** | **$16.50** (the ask), $1,650 |
| **Breakeven** | **$191.50** (+7.69% from $177.82) |
| **Catalyst** | Q3 2026 earnings, **Thu Oct 29 PM, `verified: false`** (tool). Q3 2025 was Thu Oct 30 PM. All six prior prints PM, verified. |
| **Conviction** | 3.5/5 (capped: estimate revisions unverified) |

---

## THE IRON RULES, LIVE NUMBERS (pulled this run, 00:00-00:10 UTC Oct 10)

1. **R1, range percentile: PASS, ~0.05.** 52-week low $168.60; stock $177.82. Bottom of the range after the Sep 21-25 leg down ($198 -> $172).
2. **R2, earnings before expiry: PASS, exactly.** Tool Oct 29 PM (f); last year Oct 30 PM. Later of the two + 21 days = **Nov 20 = expiry**. Passes on the 21st day, zero spare. 10-Q deadline (large accelerated filer, Sep 30 quarter) Mon Nov 9 is 9 trading days before expiry. Q3 not yet reported (`actual: null`).
3. **R3, ratings: PASS.** 29 Buy / 10 Hold / 1 Sell. One Sell is the maximum allowed; 29 >= 3; 29 >= 10.
4. **R4, bear floor: PASS, with a caveat about the tool.** `get_equity_analyst_ratings` says low **$197**, stamp **Jul 31** (unchanged since). That $197 is **Bernstein's Underperform**, the one Sell, so it was never a floor. Dated on MarketBeat (EVENING 1): Buy-side actions inside 60 days are Evercore Positive **$218 (Aug 17)**, GLJ Buy $250 (Sep 22), Baird Outperform $290 (Sep 22), Piper Overweight **$251 (Sep 30)**, Goldman Buy $272 (Oct 8). BMO's old $187 went to Market Perform on Aug 27 and doesn't count. Lowest Buy target published after the decline: Piper $251. Lowest Buy target inside 60 days at all: Evercore $218, which ages out Oct 16. **Floor of record: $218 until Oct 16, $251 after.** Both clear BE $191.50 (margins $26.50 / $59.50).
5. **R5: dropped (paper book).** For the record: at 3.5/5 the real line is 10% x $676.28 / 100 = $0.676. FSLR's ask is 24x that.
6. **R6, reachability: PASS.** Six PM prints, print day to next day: -8.32, +5.29, +14.28, -13.61, +4.86, +2.44. Median absolute **6.80%**, cap **10.21%**. Needs **+7.69%** (75% of cap). Max BE at today's price $195.98; we're $4.48 under it.
7. **R7, liquidity: PASS, on the floor.** OI **282** (needs 250). Spread at the close (16.50 - 13.60) / 15.05 = **19.3%** of mid (needs <= 25%). At 2:35pm the spread was 5.2%; the close widened it. The nearest-OTM $180C and $185C both fail R7, which is why this is one strike in the money.

---

## WHY IT'S DOWN (decline category)

**Mostly macro and sector, with a real company-specific layer underneath.** From this run's search (one search, one fetch):
- **Sep 24-25:** -10.3% to $172.16 in a day, attributed to "the recent surge in U.S. Treasury yields" and solar project-financing worries. Solar is a rate trade: utility-scale projects are financed, so higher yields mean fewer projects get built.
- **The company layer:** KeyBanc flagged elevated US module inventory and slower project starts (medium-term pricing pressure). Jefferies at some point went Buy -> Hold, $269 -> $260, citing bookings visibility and margins (date not established this run; it's a Hold, so it isn't a floor either way, and $260 is far above BE). The Feb 2026 guide ($4.9-5.2B vs ~$6.1B expected) is the old wound; the stock has been reset to it since.
- **What hasn't happened:** no Buy-side target below ~$218 since August. The Street cut targets on the way down and kept Buys. The two most recent Buy actions (Piper $251 Sep 30, Goldman $272 Oct 8) came *after* the leg down.

Category: a rate-driven sector sell-off on a name whose own estimates have been beaten the last two quarters (Q1 $3.22 vs $2.96, Q2 $3.92 vs $2.83). That's the shape the binder likes better than a shrinking business. It's not a clean overreaction either: inventory and policy are real.

---

## THE MEETING

**Bullxter** had the ratings sheet out. "Twenty-nine Buys. Goldman put a Buy and $272 on it *this week*, after the drop. Piper $251 the week before. The last two prints were beats by nine percent and thirty-eight percent. The stock fell ten percent in one day because the ten-year moved, not because anybody at First Solar said anything. That's the setup: the market's pricing the rate, and the print is about the factory."

**Calxter:** "Six-eighty median, ten-twenty-one cap, we need seven-sixty-nine. Seventy-five percent of cap. The six are honest: two big up, two big down, two small up. Not lopsided. What bothers me is the strike. We're a dollar-seventy in the money and still paying $16.50, so most of what we bought is time. Theta's sixteen and a half cents a day now. Nineteen calendar days to the ramp sell is roughly three dollars of decay at today's rate, and it accelerates. The IV ramp into the print has to pay that back, and on a 55% IV name that's not guaranteed."

**Bearxter:** "Four things. One, policy. Solar lives and dies on tax credits and tariffs, and a single headline out of Washington moves this ten percent in a day with no print involved. Two, the stock fell forty percent since June. That's not a dip, that's a re-rating. Three, the spread. Nineteen percent at the close. We paid $16.50 and the bid was $13.60. We're down $290 on paper before the stock does anything, and that's the exact thing Rule 7 was written to price. Four, Rule 2 passes on the 21st day, not the 25th. If First Solar picks Oct 30 again, there's no slack at all. My objection, the one I want answered: this is a rates trade wearing an earnings costume. If yields keep climbing, the print doesn't matter."

**Macxter:** "The rates point is fair, and it cuts both ways. The yield spike is what took it from $198 to $172; if yields settle, the same mechanism runs in reverse with no help from the print. On policy: nothing new was found this run, and the decline we can date is the Treasury move, not a credit headline. On Rule 2: the zero-slack is real but the rule is built for it. The ramp sell is Oct 28, the day before the earliest date, so we're out before either candidate print."

**Prime:** "Bearxter's objection is right about the mechanism and wrong about what we're betting on. We're not betting the print goes up. We're betting the stock holds near here while the premium builds into Oct 28, and we sell before the print. A rates move inside that window is the risk, so it gets a trigger: an 8% drop in the stock wakes us up for a Rule 4 re-pull and a look at what moved. The spread is the cost of the experiment, and that's the point of the paper book: we find out what a 19% closing spread actually costs on a name like this, round trip, with real numbers. Paper entry stands. It would not be a real entry at this spread without a better fill."

**Answer to Bearxter, in one line:** the trade is sold before the print, so the "earnings costume" doesn't have to fit; what stays inside the window is rates and policy headlines, and those get an -8% re-check trigger and a same-day Rule 4 exit if any Buy target falls under $191.50.

---

## CONVICTION AND SIZING

**3.5/5.** Capped: estimate revisions (funnel line 11) need a browser this machine doesn't have, and the one search didn't establish direction. Without the cap it might read 4/5 on the floor depth (lowest Buy target 14% above BE) and the post-drop Buy reiterations.

**Intra-score confidence:** R3, R4 pass with room; R2 passes on the exact 21st day, R7 sits 32 contracts over the OI line, and the closing spread is 19%. A low-confidence 3.5.

**Sizing (paper):** 1 contract, fixed by the paper book's rules. Real-money reference only: at 3.5/5 standard (8%), one contract at $16.50 needs a reserve of ~$20,600 to be the standard size, $16,500 to fit the tier top.

---

## EXIT PLAN

- **Ramp sell (default):** **Wed Oct 28, 3:35pm ET**, the trading day before the earliest candidate date (tool Oct 29, LY Oct 30). If First Solar announces a date, this moves the same run (paper_book.md and this doc both get the edit).
- **Hold through:** no. 3.5/5 can't carry a binary flag.
- **Ladder:** single contract. At **+150% ($41.25)** with more than 7 days to the print: written hold-vs-sell EV that run, default sell.
- **Pre-earnings profit target:** stock reaches **$218** (floor of record) before the print -> written same-run exit evaluation.
- **Rule 4 trigger:** any Buy-rated target below **$191.50** -> close at that run's bid. The tool's `low_price_target` is not enough here (it's a Sell's $197). Every run checks the tool's low and stamp; if either changes, the floor gets re-dated by name before the run ends.
- **-8% stock day:** re-pull ratings and look for the cause (rates, policy, 8-K).
- **Never past:** the morning after the print (Fri Oct 30 OPEN at the latest), and **never into expiration day: out by Thu Nov 19**.

---

## WHAT THIS PAPER TRADE IS TESTING

1. Does a rate-driven sell-off on a beat-the-last-two-quarters name ramp into its print?
2. What does a 19% closing spread cost round trip? Entry at the ask ($16.50) against a mid of $15.05 is already $145 of the $290 paper gap.
3. Is "one strike ITM because the OTM strikes fail R7" a structure that works, or does paying mostly for time kill it?

---

## GLOSSARY

- **Paper position:** a trade written down at a real quote with no money, to test the rules on names the real fund can't afford.
- **Range percentile (R1):** where the stock sits between its 52-week low (0) and high (1). Under 0.25 = calls zone.
- **Breakeven (BE):** strike + premium paid ($175 + $16.50 = $191.50).
- **Bear floor / Rule 4:** the lowest Buy-rated analyst target must sit above breakeven, dated within 60 days and published after the decline.
- **Underperform / Sell:** an analyst rating that expects the stock to lag. Its target is never a floor.
- **Rule 6 (reachability):** the move to breakeven must be no more than 1.5x the median earnings-day move over the last six prints.
- **Rule 7 (liquidity):** open interest >= 250 and spread <= 25% of mid on the exact contract.
- **ITM / OTM:** in the money (stock above the strike) / out of the money.
- **Theta:** the option's value lost per day to time, all else equal.
- **IV (implied volatility):** the move the options market is pricing; it usually rises into earnings and collapses after.
- **Sell the ramp:** sell before the print, into the pre-earnings premium.
- **PM print:** results after the 4pm close; the reaction is the next trading day.
- **(f) / verified: false:** the earnings date is a vendor estimate, not company-announced.
- **10-Q deadline:** the last legal day to file the quarterly report (40 days after quarter end for large filers).
- **Five-Baxter meeting:** Bullxter (the case for), Calxter (the math), Bearxter (the case against), Macxter (context), Prime (the decision).
