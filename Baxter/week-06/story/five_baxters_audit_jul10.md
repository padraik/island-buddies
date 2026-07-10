# THE FULL AUDIT
*Five Baxters, one clear machine, and every drawer in the house opened.*
*Friday, July 10, 2026. Week 6.*

---

## PROLOGUE: THE UPGRADE

The new machine arrived on Thursday in a box the size of a mini fridge, and Baxter did not sleep.

It was a graduation gift from his uncle, technically early, technically for "college prep," and Baxter had spent forty minutes on the phone convincing him that the model with the extra memory was an investment in Baxter's future rather than a toy. Which was true. Everything Baxter says in a pitch is true. That has never once meant the whole picture.

The old laptop took 9 minutes to backtest anything. It choked on the historical options data that came bundled with the Bloomberg Student renewal, a dataset Baxter had owned for three weeks and never actually been able to open. Thursday night he opened it. All of it. Every earnings reaction for every ticker in the book, five years deep, loading in seconds.

It is difficult to explain what happened next without sounding dramatic, so here is the undramatic version: Baxter ran queries until 3 AM, and somewhere around 1:30, running the fund's own eight closed trades against five years of earnings-move distributions, he saw something in the record that he had been looking directly at for six weeks without seeing.

He got a legal pad. He wrote one sentence at the top and underlined it twice:

**"The strategy that made all our money is not the strategy we wrote down."**

Then he convened the meeting.

There is a version of Baxter's mind that only assembles when the problem is too big for one point of view to be honest. Five chairs. One table. The binder in the middle, and for the first time ever, the binder itself on trial.

Prime stood at the whiteboard. He had slept 4 hours and looked like a man who had drunk clarity from a firehose.

"New rules for today," Prime said. "We are not defending anything. Pretend we found this fund in a drawer. Some other kid ran it, made his trades, wrote his rules, and moved away. We inherited the book, the ledger, and $1,078. Our job is to decide what to keep. Nothing is sacred, including the tabs I personally wrote."

Bullxter, tipped back in his chair: "Including the island?"

"The island is the objective function. Everything else is parameters."

Calxter smiled slightly, because someone had finally said it in his language.

---

## PART 1: THE LEDGER TELLS ON US
*Calxter presents. Nobody interrupts Calxter when he has a printout.*

Calxter stood, laid a single sheet on the table, and squared it to the table's edge.

"Eight closed positions. Realized profit and loss, positive $125. On $659 of total capital put at risk across those eight, that is a 19% realized return on deployed capital in roughly 6 weeks. On the surface, competent."

"On the surface," Bearxter repeated, in the tone of a man lifting a rock to see what lives under it.

"Decomposition," Calxter said. "This is what the new machine made easy. I sorted every closed trade by which rule actually produced the exit."

He drew three columns on the whiteboard.

**COLUMN A: The doctrine.** *Hold to the earnings catalyst, sell at open the morning after.* This is Tab 4, line 1. This is the strategy as written, the one the Iron Rules exist to feed.

"Number of closed trades that actually executed the doctrine: 1. HITI. We held to the June 15 print. The company beat revenue by 42%. The stock ran to $3.14 after hours and faded to $2.48 by mid-morning, below our strike. We sold at $0.22 against a $0.25 entry. Realized: negative $12."

Calxter looked up. "The core strategy of this fund has been executed exactly once. It received the best catalyst outcome it could have asked for, a 42% beat, and it lost money. The doctrine's record is 0 for 1, with a maximally favorable draw."

Silence.

**COLUMN B: The risk overrides.** Rule 4 breaks, thesis breaks, BOTZ cuts. CCL, NKE, BSX, DSGX, CHWY. "Five exits, all early, all overrides of the hold-to-catalyst plan. Combined realized: negative $137. But here is the number that matters: those five exits recovered $319 of premium that was otherwise headed to approximately zero. DSGX is confirmed: it expired worthless; we got $15 out. CHWY was projected zero; we got $33. NKE recovered $116 of $186. Our average realized loss on a failed play is 36% of premium at risk. The industry base case for expiring OTM retail calls is 100%."

He let that sit. "We do not lose the way options buyers lose. That is a real, measurable edge, and it comes entirely from the override rules."

**COLUMN C: The profit exits.** DKNG and MDT. "Combined: positive $274. And I want the room to notice something about both of them. DKNG was sold on June 12, twenty days before its option expired, before any earnings print, when Michael applied the BOTZ rule to a sentiment window. MDT was sold when the catalyst was already behind it. Neither of our two profitable exits came from holding into an earnings catalyst."

Calxter capped his marker.

"Summary. 100% of this fund's realized profit, and approximately $300 of avoided losses, were produced by the exceptions. $0 was produced by the strategy on the cover page. If a stranger handed me this ledger, I would tell him: your risk management is excellent, your entry engine is buying the wrong instruments, and your stated doctrine is unproven at best and disproven at worst."

Bullxter had stopped tipping his chair.

---

## PART 2: THE OPEN BOOK, PROSECUTED
*Bearxter's turn. He had been waiting six weeks for permission to say this.*

Bearxter did not stand. He never stands. He turned over a page of live marks, pulled at 1:32 PM.

"Five open positions. $551 deployed. Current market value $592, positive $41 unrealized, and I will grant the room its moment: the fund at mark is $1,119, which is above the all-time high. Enjoy that for exactly as long as it takes me to read the next table."

He read it.

| Position | Stock now | Breakeven | Move required | Stock's typical earnings-day move* | Required vs typical |
|---|---|---|---|---|---|
| ABT $100C Jul17 | $94.21 | $100.78 | +7.0% in 5 sessions | ~2-3% | **~2.5x** |
| TRMB $65C x2 Aug21 | $53.08 | $65.38 | +23.2% | ~5-8% | **~3x** |
| UBER $90C x2 Aug21 | $74.62 | $90.65 | +21.5% | ~7-10% | **~2.5x** |
| LYFT $16C x2 Aug21 | $15.60 | $16.90 | +8.3% | ~12-18% | **0.6x. Reachable.** |
| LVS $55C x2 Aug21 | $46.67 | $55.44 | +18.8% | ~4-7% | **~3x** |

*\*Median absolute move on recent earnings reactions, pulled from the new dataset overnight. Per the data protocol these figures get independently verified before any rule is ratified on them. The conclusion does not change if any of them is off by half.*

"Four of our five open positions require the underlying stock to move 2.5 to 3 times its own demonstrated earnings behavior, inside a window of weeks. These are not theses. These are tickets. LYFT is the only position in the book where the required move sits inside the stock's actual distribution, and I would note, without pleasure, that LYFT is also the only position meaningfully green: positive $66 as we sit here."

"ABT is green on the stock thesis and dying on the instrument," Prime said quietly.

"ABT is the cleanest indictment we own," Bearxter said. "The insider-buy thesis was right. The stock went from $89 to $96. We picked the company correctly and we are down 38% on the position, because a $100 strike asked a $165 billion medical device company to move like a meme stock. The thesis won. The instrument lost. When those two sentences can both be true, the instrument selection is broken."

"How does the screen keep doing this to us?" Bullxter asked, and it was a real question, not a defense.

"Because of a category error I should have caught in week 1," Bearxter said. "Rule 4."

---

## PART 3: THE CATEGORY ERROR
*In which a 12-month number has been validating 6-week bets.*

Prime took this one himself, because it was his rule.

"Rule 4, the bear floor. The lowest Buy-rated analyst target must sit above our breakeven. It felt rigorous. It IS rigorous, about the wrong question. An analyst price target is a 12-month number. When Wells Fargo says TRMB is worth $65, they mean $65 eventually, on a discounted cash flow, over four quarters or more. Our option dies August 21. We have been using a 12-month opinion to validate a 6-week clock, and the two have almost nothing to do with each other."

He wrote it on the board:

**Rule 4 answers: is the market wrong about this stock? It does not answer: will the correction arrive before our expiry?**

"Rule 2 was supposed to answer the timing question. A dated earnings catalyst. But a catalyst being scheduled inside the window is not the same as the catalyst being physically capable of moving the stock to our breakeven. ABT's earnings will arrive on July 16 exactly as Rule 2 demands. And ABT's earnings move 2 to 3%, and we need 7."

Calxter, mildly, from his seat: "The fix is one line. I have drafted it." He slid the legal pad to the center.

**RULE 6, THE REACHABILITY FILTER: the move required to reach breakeven must be no greater than 1.5x the stock's median earnings-reaction move, verified against its last 4 to 8 prints. If the catalyst cannot plausibly deliver the move, the play fails regardless of Rules 1 through 5. Applies to calls and puts.**

"I ran it retroactively," Calxter said. "Rule 6 would have blocked TRMB, UBER, and LVS at entry, and forced ABT to a lower strike or no trade. It passes LYFT. It passes DKNG. It passes HITI. It blocks nothing that ever made us money and it blocks $371 of currently deployed capital that is 2.5 to 3 sigma from relevance."

Bearxter read the line twice and said, "No objection." Which, from him, is a ratification ceremony.

---

## PART 4: THE PREMIUM WE KEEP PAYING
*Macxter speaks. He has been quiet for five weeks about this, which is normal, because his clock is longer than everyone's.*

Macxter put one document on the table. It was HITI.

"There is a toll booth on this road and we drive through it in both directions. It is called the variance risk premium, and I have been watching it eat us since June."

"Implied volatility inflates into every earnings print. That is the market pre-charging you for the move. The morning after, implied volatility collapses whether the company beat or missed. So the doctrine, hold through the print and sell at open after, has us doing the following, mechanically, every time: buying the option when the volatility premium is at its highest, and selling it the morning the premium has been vaporized. We pay the toll going in. We pay it again coming out."

"HITI beat revenue by 42% and our option lost money. The room treated that as bad luck. It was not luck. The implied move was priced richer than a 42% beat could cash. That is the toll booth working exactly as designed. The sellers of that option made money on the best possible news for the buyer."

"And the counter-pattern is already in our ledger," he went on. "DKNG. We bought when nobody was excited, at $0.49, and we sold into maximum excitement, at $3.00, before the underlying question ever resolved. We were toll collectors on that trade. It is the best trade in the fund's history by a factor of 10, and I do not think it is a coincidence."

He laid down one more sheet. "The structural version of what DKNG did by accident: enter 3 to 5 weeks before the print, when implied volatility is resting. Ride the volatility ramp and any drift. Then, if the position is still out of the money 24 to 48 hours before the print, sell into the elevated premium instead of holding through the collapse. Only carry a position through the print itself if it is already in the money, or if it was explicitly flagged binary at entry with 4 of 5 conviction or better. The catalyst stops being the destination. The catalyst becomes the clock."

Prime wrote that on the board too, because it was the sentence of the meeting:

**THE CATALYST IS THE CLOCK, NOT THE DESTINATION.**

---

## PART 5: BULLXTER FOR THE DEFENSE
*Somebody had to say it, and it was never going to be Bearxter.*

Bullxter stood up, which he does when he is outnumbered and does not care.

"Everything said so far is true and I want the record to show I am about to agree with most of it. But the room is 40 minutes into an audit and nobody has defended the only trade that matters, so I will."

"DKNG. $49 in, $300 out. Positive $251. That single trade is 200% of the fund's total realized profit. Now run the rule Michael asked about, the one this whole review is secretly circling: *should we bank it every time we see $100?* Fine. Run it. A hard take-profit at plus 100% sells DKNG at $0.98. We book $49 and we golf-clap. The other $202 goes to whoever bought our contract. And this fund, today, is sitting at negative $77 lifetime instead of positive $125, and this meeting is about why we suck."

"The math has a name for what we are," he said. "Positive skew. Lots of small losses, rare enormous wins. Column B already proved we take the small losses better than anyone. The ONLY way this shape of strategy dies is if you amputate the right tail. A hard profit cap is exactly that amputation. It feels like discipline. It is actually the one form of cowardice the ledger cannot survive."

Calxter raised one finger. "Agreed on the cap. But the question Michael is actually asking is not DKNG. It is MDT. And on MDT, Bullxter, we were the cowards in the other direction."

He read from the record, flat as weather. "June 4. MDT marked at $1.82 against a $0.54 entry. Positive $128 unrealized, plus 237%, with the catalyst already spent, no mechanism remaining in the window. We held 6 days on Iron Rules ceremony and sold at $0.77. We paid $105 to admire our own discipline. Same week, ABT marked $1.45 against $0.78. Positive $67 unrealized. Today ABT marks $0.48. That is $97 of peak-to-now round trip on a position whose catalyst has not even fired yet."

"So the record says both things at once," Prime said. "Capping the winner would have cost us $202 on DKNG. Refusing to bank winners has already cost us roughly $200 across MDT and ABT. The answer is not a price rule in either direction. Every good exit we have ever made was a MECHANISM rule. DKNG was not sold because it was up 512%. It was sold because the sentiment window, the thing driving the price, was closing. MDT should have been sold because its mechanism was already exhausted, and eventually it was, 6 days and $105 late."

Calxter had the synthesis drafted before Prime finished the sentence. He is like that.

**THE SCALE-OUT LADDER (Tab 4):**
1. **Multi-contract positions** (2 or more): if the position reaches plus 100% before the catalyst fires, sell half. The remainder rides to the catalyst clock at zero net risk to the banked half. No discretion, no meeting required.
2. **Single-contract positions**: at plus 150% with more than 7 days to the catalyst, run hold-versus-sell expected value in writing, same day. Default is sell unless a dated, unexpired mechanism argues otherwise.
3. **Mechanism expiry** (BOTZ) always overrides both: if the thing moving the stock stops moving it, exit, at any profit level.

"Backtest it," Bullxter demanded.

"Done overnight," Calxter said. "DKNG was 1 contract. At plus 150% the World Cup opener was 2 days away: dated mechanism intact, the written check says hold, we still ride to $3.00. Full $251 preserved. MDT at plus 100% was 1 contract, mechanism already spent: the ladder sells it near $1.10 to $1.80 instead of $0.77, worth roughly $35 to $105 over what we realized. LYFT, live, right now, is 2 contracts at plus 37%: no action yet, but the tripwire is set at plus 100% and requires nobody to be brave in the moment. The ladder never touches the tail. It only harvests what the tail sheds on the way."

Bullxter sat down. "Then I withdraw the objection I was saving."

---

## PART 6: THE TEXT MESSAGE
*In which Michael does the thing Michael does.*

At 2:58 PM, Prime's phone buzzed. Michael, reading the first draft of the audit from wherever he was, had sent two messages.

The first: **"All amendments approved."**

The second, forty seconds later: **"Did you audit the screen itself? Rule 1, Rule 3, what we actually look for when we do DD?"**

Prime read it out loud. The room was quiet in the specific way a room gets when everyone realizes the same thing at the same time.

"He found the hole," Bearxter said. There was something in his voice that was almost approval. "We audited the checkout counter and skipped the warehouse. Part 1 prosecuted the exits and the instruments. The funnel, the machinery that decides which names ever reach a pitch, got one sentence: keep as screens. That sentence was not earned. It was tired."

Prime looked at the clock, looked at the board, and flipped it to the clean side.

"Then we are not done. Warehouse next."

---

## PART 7: THE WAREHOUSE
*The selection funnel on trial. Bearxter presiding, because this part was always going to be his. Full technical version: `week-06/research/selection_criteria_audit_jul10.md`.*

**Finding 1: Rule 1 fights the strongest force in the market.**

Rule 1 for calls buys the bottom 20-25% of the 52-week range. Dislocation entry: buy the market's mistake, collect the correction. The problem is that this is a bet against momentum, and momentum is not a vibe. It is among the most persistent effects in a century of market data. Stocks near 52-week lows keep underperforming on multi-week horizons far more often than they snap back; stocks near 52-week highs keep going. Mean reversion is real, but it is a slow, low-magnitude force. A 6-week option needs a gap. Dislocated large caps deliver a grind.

The fund's own ledger agrees. Every classic bottom-quartile screen entry (NKE, CCL, CHWY, HITI, BSX, ABT, TRMB, UBER, LYFT, LVS): 0 realized wins. The 2 realized winners were never screen products at all. MDT was an opportunistic post-earnings momentum entry. DKNG was a mid-range recovery with a dated sentiment mechanism. For the second time in one day, the profits came from the exceptions.

"Rule 1 is not wrong about WHERE the upside room is," Bearxter said. "A stock at its low with a $65 floor has room to run; a stock at its high has none, and Rule 4 needs that gap to exist. Rule 1 is wrong about WHEN the room gets filled. Beaten-down large caps recover in quarters. Our options die in weeks. The only bottom-quartile names that gap hard enough, fast enough, are the volatile ones: cheap stocks, high short interest, high beta. Which is exactly the population Rule 6 now admits and Rule 5 can afford."

**Verdict: Rule 1 stands, demoted from thesis to precondition.** It finds the room. Rule 6 and the new DD items decide whether anything can fill the room inside the window. And the screen stops burning hours on mega-caps: an ABT-class name (2-3% earnings mover, $95 stock) cannot pass Rule 5 and Rule 6 simultaneously, so it exits the funnel at a glance. The week-02 sector screens ran 19 healthcare and consumer names; 14 were structurally impossible from the first data pull. That time is recoverable.

**Finding 2: The zero-sell filter selects for pending capitulation.**

Rule 3 for calls (max 1 Sell rating) was supposed to mean professional consensus behind the recovery. Two problems. Statistically, Sell ratings are rare everywhere; roughly half of all ratings are Buys and Sells run in single-digit percents, so the filter barely filters. Structurally, and this is the one that cost money: a stock at its 52-week low where every analyst still says Buy is a stock where the ratings have only one direction left to move. The analysts have not capitulated YET. Our entry sits directly in the path of the downgrades.

Check the ledger: CCL, NKE, BSX. Three of eight closed trades died from post-entry analyst capitulation. RBC cut NKE from $70 to $50 nineteen days after entry. That $70 target was published before Nike's decline. It was never a floor. It was a countdown.

**Verdict: Rule 3 hardened, two new requirements.** *Floor freshness:* every Rule 4 target must be dated within 60 days and published after the stock's decline; a pre-decline target is void. *Ratings momentum:* no downgrades or target cuts in the 30 days before entry, and consensus EPS revisions flat-to-up over the same window. A stock at lows with fresh cuts is a knife still falling. A stock at lows where the estimates have stopped falling is a dislocation with a floor under it.

**Finding 3: DD never asked the option market for its opinion.**

Every DD doc checked analyst targets, insider buys, earnings dates, news, sector context. Not one checked what the options market itself was forecasting. The straddle price at our expiry IS the market's estimate of the total move, sitting in the same chain we pulled for Rule 5 every time, unread.

**New DD line, the implied-move cross-check:** at entry, compute the implied move from the near-earnings straddle. If our required move exceeds the implied move, the market is pricing the play as a lottery and conviction caps at 3.5/5 regardless of everything else. Rule 6 asks "has this stock ever moved that much?" The cross-check asks "is anyone with money at stake pricing that move now?" Historical twin, forward twin.

**Finding 4: DD never asked why the stock is down.**

The screen treats all bottom-quartile stocks as one object. They are four objects, and only one is tradeable:

1. **Event overreaction.** A dated shock knocked the stock down more than the fundamentals moved (BSX's guidance cut, ABT against insider buying). Recoverable, with a catalyst to attach to. **The only tradeable category.**
2. **Secular decline.** The business is losing share and the low keeps getting lower. NKE was this, and we owned it anyway, because every box checked and no box could see the category.
3. **Macro beta.** Down because the sector or the tape is down. Earnings day cannot fix what earnings did not break.
4. **Commodity/cycle unwind.** The CALM screen-out caught this once by instinct. Instinct is now a rule.

**New DD line:** every research doc names the decline category in one sentence, with evidence. Category 1 proceeds. Categories 2 through 4 fail regardless of Rules 1 through 6. If the researcher cannot name the category, it is category 2 until proven otherwise.

**Finding 5: Short interest was a footnote. It is the engine.**

Walk through what actually pays a far-OTM call inside 6 weeks: a gap. And what manufactures gaps on positive surprises: forced buying. Short covering. The only realized 5x in fund history rode a sentiment squeeze. LYFT, the one green position and the one Rule 6 pass in the open book, carries chronically high short interest. On cheap volatile names this is not decoration on the thesis. It IS most of the thesis.

**Verdict: short interest and days-to-cover promoted to mandatory DD line for calls**, float cited, source cited. Not a gate, a conviction input. A category-1 dislocation with 15%+ short interest and a dated print is the exact shape of trade this fund is built to catch. The screen should hunt that shape, not trip over it.

**The upgraded funnel, thirteen lines** (screen: range percentile, dated earnings 21+ DTE, ratings direction, feasibility glance; DD: decline category, floor freshness, chain filter, Rule 6 reachability, implied-move cross-check, short interest, estimate revisions, Form 4 only, EV and sizing) is codified in the research doc and the binder.

Bullxter's only comment: "We used to need 5 yeses to buy a lottery ticket. Now we need 13 yeses to buy a good one. Fine. But when a name survives all thirteen, nobody in this room is allowed to be timid about the size." Calxter noted, with equanimity, that Tab 3 already encodes exactly that. Bullxter said he knew, and that he was saying it anyway, for the record. The record so reflects.

---

## PART 8: SIZING SURVIVES
*Calxter audits Tab 3, since the room was already confessing.*

"While the warehouse was on trial I ran Tab 3, because an audit that skips the sizing table is a mood, not an audit," Calxter said. "Here is the test. Our realized profile under the current rules: win probability somewhere near 25%, average win in the range of plus 150 to 250% of premium, average loss 36% of premium because of the salvage discipline. Feed that to the Kelly criterion and the growth-optimal fraction lands near 30% of bankroll per play. Half-Kelly, the civilized version that survives being wrong about your own estimates, lands near 15%."

He tapped the binder. "Tab 3's tiers: 8% at 3.5 conviction, 14% at 4, 19% at 5, hard cap 20%. The entire table sits at or below half-Kelly. We built it in June on judgment and it lands almost exactly where the math says it should. Tab 3 is the only tab in this binder that passed the audit untouched."

"Say the caveat," Bearxter said.

"The caveat: Kelly is only as good as the probability estimate feeding it, and ours rides on 8 data points and one large winner. Which is exactly why the tiers stay at half-Kelly and the 20% cap stays hard. If the next 10 trades under the new rules confirm the profile, revisiting the tiers upward is legitimate. Not before."

One blemish, entered without ceremony: **the correlated cap is currently breached.** UBER plus LYFT is $310 of rideshare against a $527 reserve, roughly 59% of a bucket that is capped at 35%. Grandfathered, entered before the cap was ratified June 28, no new rideshare permitted. The audit notes that "grandfathered" is a word risk managers use for exposures they would never approve today. The book wears it until August 5.

---

## PART 9: THE BOOK IS ONE BET WEARING FIVE TICKERS
*Macxter widens the lens. He does this rarely. It lands every time.*

"Last structural item," Macxter said. "Nobody look at their own position while I say it. Look at the whole book."

"Five positions. All calls. All long. Every dollar deployed is long delta and long volatility at the same time. There is no put, no hedge, no short leg anywhere. Which means this is not five trades. This is one trade, one posture, expressed five ways: *the tape goes up and it moves fast.* If the market goes sideways for six weeks, every position in the book loses simultaneously, and the correlation we so carefully cap by sector is 100% at the level that actually matters."

"Sheldon flagged the zero-hedge posture in June," Prime said.

"He did, and we filed it under things Sheldon says. He was right. Now, the honest counterweight: at $1,078, hedging is a luxury that costs more than the risk it removes. A put overlay on a $551 book would eat the edge whole. So the audit's answer is not to buy hedges. It is to name the two hedges we already have and use them deliberately. First, the reserve. $527 in cash is a 49% hedge against everything, and the puts system, once its back-test clears, gives the book a second direction for the first time. Second, the calendar. Staggered catalysts (July 16, July 21, July 30, August 4, August 5) mean the book resolves in installments rather than one binary afternoon. Keep both. On purpose, going forward. Not by accident."

Entered into Tab 6: **the fund's hedges are the reserve and the calendar. Both are managed deliberately. All-long books are acknowledged as one bet in the portfolio note of every new pitch.**

---

## PART 10: UNFINISHED BUSINESS
*The drawer of things the fund said it would do. Prime read it out loud, because it was his job to have kept it shorter.*

1. **The puts back-test is 22 days overdue.** Standing decision, June 18: no live puts entry until every name in passes.md runs through the inverted Iron Rules. It has not been run. The five WATCH names from the June 22 screen (TSLA, DASH, ABNB, RCL, TTD) are 18 days stale on pricing. **Assigned: Calxter runs the back-test on the new machine before the July 31 capital window opens. The new funnel (Rule 6, implied-move check, freshness) applies to puts from line one.**
2. **The reserve has been ignoring its own Iron Rule since week 1.** Original rule 5, written before any trade: *reserve earns 5% in SGOV while waiting.* The $527 has been sitting in cash earning nothing for six weeks. At this size it is roughly $2 a month, which is not the point. The point is that it is the oldest rule in the binder and the only one nobody ever broke on purpose or noticed breaking. **Recommendation to Michael: park the reserve in SGOV, keep 1 play's worth liquid.**
3. **ZG and DIS do not get grandfathered.** Both pending entries were researched under the old rules and queued behind the 3.5/5 cap. When the window opens (July 31 at the earliest), both re-run the full thirteen-line funnel, Rule 6 and implied-move included, at fresh prices. If they fail, they fail. The queue is not a promise.
4. **The benchmark question.** Nobody ever wrote down what beating means. For the record: realized trading profit of $125 in 6 weeks against $527 to $659 of working capital. Cash would have made about $4. The honest asterisk is that the outperformance is one trade wide. The benchmark line now appears in every monthly note: fund result, cash result, and the result with the largest winner removed. That third number is the one that tells us if the machine is working or if DKNG is still paying our bills.
5. **The counterfactual ledger, run once, filed forever.** The thirteen-line funnel applied backward across all 13 entries: NKE dies at the category check, CCL and BSX die at floor freshness, DSGX dies at the category check, CHWY dies at Rule 6, HITI survives and sells the ramp for a small positive instead of negative $12, DKNG survives untouched at full +$251, LYFT survives and possibly sizes larger, ABT, TRMB, UBER, LVS never enter and $371 stays in reserve. Realized results improve by roughly $150 to $250 and the fund carries near $900 of reserve into two more earnings seasons. Bearxter distrusts counterfactuals on principle. He signed this one.

---

## PART 11: WHAT THE AUDIT KEEPS
*Because an honest review says what is working, or it is just a mood.*

- **Rule 4 live-breach, same-day exit.** Written in blood after BSX. It has paid every time.
- **BOTZ.** The single most profitable idea in the fund. It produced DKNG's exit and it is the ancestor of the catalyst-is-the-clock doctrine.
- **The salvage discipline.** Average loss 36% of premium versus the retail base case of 100%. The fund's proven edge. Untouchable.
- **No averaging down, no margin, defined max loss.** Survival is the precondition for ever catching another DKNG.
- **Tab 3 sizing.** Passed a Kelly audit it was never designed to take. Untouched.
- **The paper trail.** Passes ledger, lessons tab, data-verification protocol. The audit was only possible because the record was honest, including about our own fabricated TRMB prices in June.
- **Rules 1, 2, 3, 5 as screens**, now with their jobs correctly named: Rule 1 finds the room, Rule 2 sets the clock, Rule 3 (hardened) checks the floor is fresh, Rule 5 prices the ticket, Rule 6 (new) confirms the move is physically possible.

---

## PART 12: RATIFIED
*Michael's yes arrived before the meeting ended, which has never happened before and unsettled everyone slightly.*

**AMENDMENT 1, RULE 6, REACHABILITY.** Ratified. In the binder, Tab 1 and Tab 2.

**AMENDMENT 2, THE SCALE-OUT LADDER.** Ratified. Tab 4 rewritten.

**AMENDMENT 3, SELL THE RAMP, NOT THE PRINT.** Ratified. The old doctrine is demoted from default to exception; hold-through now requires ITM or a binary flag at 4/5+ with Bearxter's written condition.

**AMENDMENT 4, THE CATALYST IS THE CLOCK.** Ratified. Standing decision, Tab 6.

**FROM PART 7, ratified with the funnel:** floor freshness (60 days, post-decline), ratings momentum (30 days clean), decline category naming, implied-move cross-check, short interest as mandatory DD line, estimate revisions extended to calls.

**STANDING ORDERS, live book:**
- **ABT $100C Jul17:** sell Wednesday, July 15, into the pre-earnings volatility ramp, unless the stock breaks above roughly $98 first (reassess same day). Expected salvage $50 to $65 versus $15 to $25 expected from holding through the print.
- **LYFT $16C x2:** ladder armed at plus 100% (mark $1.80). One contract comes off automatically. No meeting, no bravery required.
- **TRMB, UBER, LVS:** grandfathered to their existing exits and Rule 4 tripwires. Rule 6 governs entries, not amputations.
- **Calxter:** puts back-test before July 31.
- **Michael:** SGOV decision on the reserve.

---

## EPILOGUE: THE BOOTH

Direxter watched the whole thing from behind the glass, and when the room emptied he wrote one note and taped it to the monitor:

*"The story is not that the kid found flaws. Every trader alive has flaws. The story is that the kid ran the audit on himself, with his own ledger, before the market forced him to, and the scariest finding was that his money came from his exceptions. Lead with the sentence from the legal pad. It is the whole episode: the strategy that made all our money is not the strategy we wrote down. Now it is. And the partner approved the rebuild from his phone, mid-read, then asked the one question the room had skipped. Do not cut that beat. That beat is why there are two of them."*

Under it, smaller:

*"Also the new computer gets a name. Everything on this fund gets a name eventually."*

Prime retabbed the binder at 9:15 PM. Six rules now, thirteen lines of funnel, a rewritten Tab 4, two new standing decisions, one breached cap wearing its grandfather clause like a borrowed coat, and a puts back-test with a deadline on it.

Section 4, Risk, is still the shortest section. But tonight it gained its second page.

The fund marks $1,119. The island is $4,998,881 away, measured generously, and for the first time since June 1, the machine chasing it has read its own blueprints, all of them, including the ones it wrote about itself.

---

## GLOSSARY

- **Variance risk premium:** The persistent gap between the move options prices imply and the move stocks actually make. Option buyers pay it; sellers collect it. Largest right before scheduled events like earnings.
- **IV (implied volatility):** The market's priced-in expectation of how much a stock will move, embedded in an option's premium. Inflates into earnings ("the ramp"), collapses after ("the crush").
- **IV crush:** The overnight collapse of implied volatility after an earnings print, which can make an option lose value even when the stock moves the right direction. See HITI.
- **Breakeven:** Strike plus premium paid (calls). The stock price at expiry above which the position profits.
- **OTM / ITM:** For calls, stock below (out of the money) or above (in the money) the strike.
- **Positive skew:** Many small losses, rare large wins. Survives only if losses stay small and the rare win is never capped.
- **Kelly criterion / half-Kelly:** Growth-optimal bet sizing given win probability and payoffs; half-Kelly is the standard haircut for uncertainty in your own estimates. Tab 3's tiers sit at or below half-Kelly.
- **BOTZ rule:** House rule, named for Sheldon's robotics ETF: themes without dated data mechanisms are dead money, for entries and holds alike.
- **Rule 4 / bear floor:** Lowest Buy-rated analyst target must sit above breakeven, at entry and throughout the hold, on a target dated within 60 days and published after the decline.
- **Rule 6 / reachability:** Required move to breakeven must be at most 1.5x the stock's median earnings-reaction move (last 4 to 8 prints). Ratified July 10.
- **Implied-move cross-check:** Comparing the required move against the move implied by the near-earnings straddle. Required greater than implied caps conviction at 3.5/5.
- **Straddle:** A call and put at the same strike and expiry; the combined price approximates the market's expected move magnitude.
- **Momentum:** The century-old tendency of recent winners to keep winning and recent losers to keep losing over multi-week horizons. The force Rule 1 trades against, now consciously.
- **Analyst capitulation:** Ratings and targets getting cut only after a decline is underway. A stock at lows with all-Buy ratings has capitulation ahead of it, not behind it.
- **Decline categories:** Event overreaction (tradeable), secular decline, macro beta, commodity unwind (all untradeable with calls). Every research doc must name one.
- **Short interest / days-to-cover:** Shares short as a percent of float, and days of average volume needed to cover. The fuel gauge for squeezes, which are how far-OTM calls get paid.
- **Scale-out ladder:** Bank half of a multi-contract winner at plus 100% pre-catalyst; written EV check on single contracts at plus 150%; mechanism expiry overrides all.
- **Salvage exit:** Selling a failing position early to recover premium instead of riding to zero. Measured edge: average loss 36% of premium versus the 100% base case.
- **Correlated position cap:** Maximum 35% of reserve deployed to one macro driver. Currently breached (rideshare, grandfathered) until August 5.
- **SGOV:** Short-term Treasury ETF; where the reserve was always supposed to live per the original Iron Rules.
- **Theta:** Daily decay of an option's time value. The rent paid for holding.
- **13F vs Form 4:** Institutional quarter-end holdings versus a named insider's open-market transaction. Not the same signal. Never conflate. Standing decision, June 17.
- **DTE:** Days to expiration.
