# OBDC (Blue Owl Capital Corp, BDC) — RESEARCH FILE
*Tue Oct 6, 2026, ~8:35pm ET (VM EVENING session 2). A $5B business development company (private-credit lender to middle-market firms), trading at a fresh 52-week low and 0.71x book, with the only company-confirmed print date on the live list.*

**Status: DOC COMPLETE, ENTRY BLOCKED ON RULE 4 DATING** (same block as PCT, MLCO, ENVX). The tool's $11.00 low is a Wells Fargo **Equal Weight (Hold)** from May 8. The Buy-side targets I could find (Truist Buy $13, May 19; Capital One $13, Jul 24; RBC Outperform $13, Feb 20) are all older than 60 days and were all set with the stock at $11-11.8, before the Sep-Oct slide to $10.04. Under binder Tab 6 (Jul 10), a floor that old and that far above today's price isn't a floor. Unblocks on a fresh dated Buy target above breakeven. The rest of the doc is written so that the day that happens, it's ready.

---

## THE PLAY AT A GLANCE

| | |
|---|---|
| **Ticker** | OBDC |
| **Option** | $10C Nov 20 2026 (strike $10.00; instrument `6197e090-d0c2-4f73-bb2b-62dc8e6f9d09`) |
| **Live quote (4:00pm ET Oct 6 close, pulled 8pm)** | bid $0.30 / ask $0.45, OI 1,632, vol 73, IV 23.8%, delta 0.56, theta -$0.0043/day, vega $0.0139 |
| **Stock** | $10.04 (Oct 6 close $10.03; intraday low $9.98 = new 52-week low) |
| **Max price I'll pay** | **$0.47** (R6 line: max BE $10.51); R5 alone would allow $0.741 |
| **At risk** | 1 contract, $45 at today's ask (6.1% of the $741.32 fund) |
| **Breakeven** | $10.45 at the ask (+4.08%) |
| **Catalyst** | Q3 2026 earnings, **Wed Nov 4 PM, `verified: true`** |
| **Conviction (if unblocked)** | 3.5/5, low confidence |
| **Verdict** | BLOCKED (R4 dating). ENTER ONLY IF a Buy target above BE, dated within 60 days and set at or near the current price, appears; plus ask <= $0.47 on that run |

---

## THE IRON RULES, LIVE NUMBERS (pulled this run)

1. **Rule 1, range percentile: PASS, ~0.02.** 52w range $9.98 (today, Oct 6) to $13.575 (Dec 5, 2025) per `get_equity_fundamentals`. ($10.04 - 9.98) / 3.595 = 0.017.
2. **Rule 2, earnings before expiry: PASS, confirmed.** `get_earnings_results`: Q3 2026 **Nov 4 PM, `verified: true`**. Expiry Nov 20. All six prior prints PM and verified.
3. **Rule 3, ratings: PASS.** 11 Buy / 2 Hold / 0 Sell.
4. **Rule 4, bear floor: FAIL ON DATING.** Tool low $11.00, mean $13.17, high $15.00. $11.00 is **Wells Fargo Equal Weight, $12 -> $11, May 8, 2026** (a Hold, 151 days old). Buy-side: Truist Buy $15 -> $13 (May 19, 140 days), Capital One $13 (Jul 24, 74 days, rating not shown), RBC Outperform $14 -> $13 (Feb 20), Citizens JMP Market Outperform $15 (Nov 2025), Lucid upgrade to Strong Buy (Jul 24, no target). On the number, every Buy target ($13+) clears BE $10.45 easily. On dating, none is within 60 days, and all were set at $11+ before the September/October slide (Sep 17 close $11.35 -> $10.04). Tab 6: "A stale target from before the drop is not a floor, it is a countdown to a downgrade." **Blocked.**
5. **Rule 5, chain filter: PASS.** Reserve $741.32 (spendable). 3.5/5 line $0.7413. Ask $0.45.
6. **Rule 6, reachability: PASS, thin.** Four prints, PM (print-day close -> next-day close): Nov 5 2025 -5.32, Feb 18 2026 -1.04, May 6 2026 -3.15, Aug 5 2026 +3.10. Median absolute 3.13%, cap 4.69%, max BE $10.51. Needs +4.08% at $0.45: **87% of cap**; six cents of room.

**Dividend check:** $0.31 quarterly, ex-dividend **Sep 30** (paid Oct 15). The next ex-date should land around the end of December, after the Nov 20 expiry, so no ex-dividend price drop inside the hold. Confirm when Q3 results declare the Q4 dividend.

**M&A check:** Blue Owl merged OBDC III into OBDC by stock merger in January 2025; a proposed combination with Blue Owl Capital Corp II was **terminated in November 2025.** No pending deal found. Under THE UNIFIED SCREEN, a revived OBDC II merger would be a flag (stock-for-stock BDC mergers carry no takeover premium, and the last one was pulled on NAV-dilution complaints), not a tailwind.

---

## WHY IT'S DOWN (decline category)

**Sector, plus a dividend cut.** Private credit has been under pressure all year (valuation questions on illiquid loans, lending to highly leveraged borrowers), and Blue Owl's platform has been in those headlines: one report says Blue Owl restricted OBDC II redemptions and sold ~$1.4B of loans across three funds, sending shares to a 2.5-year low. **I could not pin that report's date;** it may be the cause of the Sep-Oct slide or an earlier episode. OBDC itself cut its base quarterly dividend from $0.37 to $0.31 in Q2 2026 (plus a $0.02 supplemental), bringing the payout inside adjusted NII of $0.34. NAV was ~$14.26 at Jun 30; the stock is at 0.71x book.

**The case it's mispriced:** a 29% discount to NAV on a senior-secured book, a dividend now covered by earnings, 11 Buys and no Sells. **The case it isn't:** the market is saying it doesn't believe the NAV marks. A BDC at 0.7x book is a bet on the marks.

---

## THE MEETING

**Bullxter:** "The only confirmed date on the board. Eleven Buys, zero Sells. Seventy-one cents on the dollar of book. Dividend just reset to something it can pay. Deepest chain we've seen besides COUR, sixteen hundred open interest, and the option costs forty-five cents to buy at the money."

**Calxter:** "And the stock moves three percent on a print. Cap four-seven, we need four-one. Six cents. Theta is four-tenths of a cent a day; IV is 24, and it doesn't ramp much on a BDC. Plus ten vol points is fourteen cents. Buy Oct 21, two weeks out, decay ~six cents, ramp maybe ten. It's roughly a wash with a flat stock, which means the whole trade is delta: the stock has to rise four percent into a print that has fallen three times out of four."

**Bearxter:** "A coin with a fee. I said it at six o'clock and the numbers say it again. And the floor isn't a floor: the lowest number is a Hold from May, the Buys are from spring at eleven-and-change, and the stock is at ten. Every one of those analysts is going to update after Nov 4, and the direction of the sector says down. My objection is Rule 4 itself: this fails it today, and buying it would be buying CCL, NKE and BSX over again, a stale floor waiting for the downgrade."

**Macxter:** "The one real thing here is the confirmed date, and that's worth keeping the doc for. Q3 is the first quarter on the reset dividend, so coverage is the number everyone's watching. If a post-slide note comes out with a Buy target, it'll probably be in the next three weeks."

**Prime:** "Bearxter wins today. It's blocked on Rule 4 dating, and the binder says why in three closed trades. The doc stays ready: if a dated Buy target above ten-forty-five lands at or near the current price, the play is a one-contract, low-confidence 3.5 with a max price of forty-seven cents, entry no earlier than Oct 21. If the first new note is a cut, it dies."

**Answer to Bearxter, in one line:** agreed, no entry on a stale floor; the doc exists so a fresh, dated Buy target is the only thing standing between this and an order, and the max price ($0.47) keeps the thin R6 edge honest if that day comes.

---

## CONVICTION AND SIZING (if unblocked)

**3.5/5.** Capped: estimate revisions unverified; thin R6.

**Intra-score confidence:** R2, R3, R5 pass cleanly, but R6 clears at 87% of cap on a 3% mover and R4 depends on a target that doesn't exist yet, so low confidence, bottom of the tier.

**Sizing (reserve $741.32 = spendable at this run):** 6% = $44.48; floor($44.48 / 45) = 0 -> minimum 1 contract, $45 (6.1%). Hard limits 7/8 inside. Max loss $45.

---

## EXIT PLAN (if entered)

- **Ramp sell (default):** **Wed Nov 4, 3:35pm ET (LASTCALL)**, the last run before the after-close print (confirmed date).
- **Hold through:** never at 3.5/5.
- **Ladder:** single contract; GTC limit sell at **$1.13** (+150% on $0.45; recomputed on the real fill), `time_in_force: gtc` confirmed.
- **Pre-earnings profit target:** stock reaches the floor in force on the entry day (today's tool low $11.00) -> written same-run exit evaluation, default sell.
- **Rule 4 trigger:** tool low below the real breakeven on any run -> sell same day.
- **Drop trigger:** underlying -5% intraday -> same-run Rule 4 re-check.
- **Michael says no:** sold the next run.
- **Never past** the morning after the print (Thu Nov 5 OPEN at the latest); **never into expiration day: out by Thu Nov 19.**

---

## WHAT STILL HAS TO HAPPEN BEFORE A BUY

1. A Buy-rated target above breakeven, dated within 60 days and set at or near the current price. (Check `get_equity_analyst_ratings` every run; MarketBeat forecast page when the tool's low or count changes.)
2. Calendar: on or after Wed Oct 21.
3. That run's quote: ask <= $0.47.
4. No revived OBDC II merger.

---

## GLOSSARY

- **BDC (business development company):** a listed fund that lends to and invests in mid-sized private companies, paying out most of its income as dividends.
- **NAV / P/B:** net asset value per share (the fund's own valuation of its loans); 0.71x means the stock trades at 71% of it.
- **NII:** net investment income, a BDC's earnings from interest minus expenses; dividends are judged against it.
- **Ex-dividend date:** buyers on or after this date don't get the dividend; the stock usually drops by about the dividend that morning.
- **Range percentile (R1), Breakeven, Rule 4/5/6:** as in the binder Tab 1; Rule 4 floors must be dated within 60 days and set after the decline (Tab 6).
- **PM print:** results after the close; the reaction is the next day.
- **Verified (earnings date):** company-announced.
- **Theta / vega / delta:** daily time decay / gain per IV point / move per $1 in the stock.
- **Stale floor:** an analyst target set before the stock's latest drop; the binder doesn't count it.
- **Five-Baxter meeting:** Bullxter (for), Calxter (math), Bearxter (against), Macxter (context), Prime (decision).
