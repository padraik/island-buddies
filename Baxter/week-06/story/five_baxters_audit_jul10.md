# THE AUDIT
*Five Baxters, one clear machine, and the question nobody wanted to ask.*
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

**PROPOSED RULE 6, THE REACHABILITY FILTER: the move required to reach breakeven must be no greater than 1.5x the stock's median earnings-reaction move, verified against its last 4 to 8 prints. If the catalyst cannot plausibly deliver the move, the play fails regardless of Rules 1 through 5.**

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

**PROPOSED AMENDMENT, THE SCALE-OUT LADDER (Tab 4):**
1. **Multi-contract positions** (2 or more): if the position reaches plus 100% before the catalyst fires, sell half. The remainder rides to the catalyst clock at zero net risk to the banked half. No discretion, no meeting required.
2. **Single-contract positions**: at plus 150% with more than 7 days to the catalyst, run hold-versus-sell expected value in writing, same day. Default is sell unless a dated, unexpired mechanism argues otherwise.
3. **Mechanism expiry** (BOTZ) always overrides both: if the thing moving the stock stops moving it, exit, at any profit level.

"Backtest it," Bullxter demanded.

"Done overnight," Calxter said. "DKNG was 1 contract. At plus 150% the World Cup opener was 2 days away: dated mechanism intact, the written check says hold, we still ride to $3.00. Full $251 preserved. MDT at plus 100% was 1 contract, mechanism already spent: the ladder sells it near $1.10 to $1.80 instead of $0.77, worth roughly $35 to $105 over what we realized. LYFT, live, right now, is 2 contracts at plus 37%: no action yet, but the tripwire is set at plus 100% and requires nobody to be brave in the moment. The ladder never touches the tail. It only harvests what the tail sheds on the way."

Bullxter sat down. "Then I withdraw the objection I was saving."

---

## PART 6: THE STING
*Calxter says the quiet part, because he is the only one who can say it without flinching.*

"One more number, and I present it without agenda," Calxter said, which is what he says when the number has the biggest agenda in the room.

"Trading, 6 weeks, best efforts of five of us: positive $125. Contributions in the same window, Michael and his dad emptying pockets: $734. The savings rate is outperforming the hedge fund by a factor of 6."

Bullxter groaned. "You cannot island-math a paper route."

"I am not proposing we replace trading with allowance," Calxter said. "I am stating what the fund's actual product is at this size. At $1,078, no strategy on Earth trades us to $5 million; the arithmetic requires roughly twelve consecutive doublings. What CAN be built at $1,078 is the machine: rules that are calibrated on real money, real fills, real mistakes, at a tuition of tens of dollars per lesson. NKE cost $70 and bought us the same-day Rule 4 exit. HITI cost $12 and bought us the entire volatility argument Macxter just made. The system we are ratifying today is the asset. The balance is the byproduct. When the balance is $20,000 someday, these rules will be why it survives being $20,000."

Nobody argued. It had the specific silence of a true thing.

---

## PART 7: WHAT THE AUDIT KEEPS
*Because an honest review says what is working, or it is just a mood.*

Prime read the keep-list into the record:

- **Rule 4 live-breach, same-day exit.** Written in blood after BSX. It has paid every time.
- **BOTZ.** The single most profitable idea in the fund. It produced DKNG's exit and it is the ancestor of today's "catalyst is the clock" doctrine.
- **The salvage discipline.** Average loss of 36% of premium versus the retail base case of 100%. This is the fund's proven edge. Untouchable.
- **No averaging down, no margin, defined max loss.** Survival is the precondition for ever catching another DKNG.
- **The paper trail.** Passes ledger, lessons tab, data-verification protocol. The audit itself was only possible because the record was honest, including about our own fabricated TRMB prices in June.
- **Rules 1, 2, 3, and 5 as screens.** They find dislocated stocks with professional support and cheap chains. The failure was never the screen. It was asking a 12-month opinion (Rule 4) to do a 6-week job, with no reachability check behind it.

---

## PART 8: THE AMENDMENTS
*Drafted by the five, for Michael. He controls the yes or no. That one he keeps.*

**AMENDMENT 1, RULE 6, REACHABILITY.** Required move to breakeven must be at most 1.5x the stock's median earnings-reaction move (verified, last 4 to 8 prints). Applies to every future entry, calls and puts. *Retroactive audit: blocks TRMB, UBER, LVS, and ABT-as-structured; passes LYFT, DKNG, HITI.*

**AMENDMENT 2, THE SCALE-OUT LADDER.** Multi-contract: bank half at plus 100% pre-catalyst. Single-contract: written hold-versus-sell EV at plus 150% with more than 7 days to catalyst, default sell. BOTZ overrides everything at any profit level. *Retroactive audit: preserves all of DKNG, recovers $35 to $105 of MDT, arms a live tripwire on LYFT.*

**AMENDMENT 3, SELL THE RAMP, NOT THE PRINT.** A position still out of the money 24 to 48 hours before earnings is sold into the elevated pre-print premium, not held through the collapse. Holding through the print requires the position to be already in the money, or a binary flag set at entry with 4 of 5 conviction and Bearxter's written condition. *The doctrine of hold-through-and-sell-at-open is demoted from default to exception. Its record is 0 for 1 on a 42% beat.*

**AMENDMENT 4, DOCTRINE RESTATEMENT.** The catalyst is the clock, not the destination. Rule 2 still requires a dated catalyst before expiry; the catalyst now defines when the thesis must have resolved, not an obligation to sit through the toll booth.

**IMMEDIATE APPLICATION, ABT, decision required before Wednesday.** ABT marks $0.48 against $0.78, stock $94.21, breakeven $100.78, print Thursday July 16 before open. Under Amendment 3 the play is: hold through Tuesday to let the pre-earnings volatility ramp inflate the premium, then sell Wednesday July 15 unless the stock has broken above roughly $98 and put the strike in play. Calxter's numbers: probability of clearing breakeven by Friday expiry on a stock with a 2 to 3% typical print move, on the order of 5 to 10%. Expected value of holding through, roughly $15 to $25. Expected salvage selling into Wednesday's ramp, roughly $50 to $65. The ramp sell dominates under every assumption we tested. *This is a rule change applied to a live position, so it goes to Michael as a recommendation, not an action.*

**NO ACTION: TRMB, UBER, LVS.** Entered under the old rules; grandfathered to their existing exit protocols. Rule 6 governs entries, not amputations. Their exit dates and Rule 4 tripwires stand.

**LYFT: ladder armed.** 2 contracts, plus 37%. At plus 100%, half comes off without a meeting.

---

## EPILOGUE: THE BOOTH

Direxter watched the whole thing from behind the glass, and when the room emptied he wrote one note and taped it to the monitor:

*"The story is not that the kid found flaws. Every trader alive has flaws. The story is that the kid ran the audit on himself, with his own ledger, before the market forced him to, and the scariest finding was that his money came from his exceptions. Lead with the sentence from the legal pad. It is the whole episode: the strategy that made all our money is not the strategy we wrote down. Now it is."*

Under it, smaller:

*"Also the new computer gets a name. Everything on this fund gets a name eventually."*

Prime retabbed the binder at 6:40 PM. Section 2, Current Thesis, now opens with the four amendments awaiting Michael's yes or no. Section 4, Risk, is still the shortest section. But tonight it gained its second page.

The fund marks $1,119. The island is $4,998,881 away, measured generously, and for the first time since June 1, the machine chasing it has read its own blueprints.

---

## GLOSSARY

- **Variance risk premium**: The persistent gap between the move options prices imply and the move stocks actually make. Option buyers pay it; sellers collect it. It is largest right before scheduled events like earnings.
- **IV (implied volatility)**: The market's priced-in expectation of how much a stock will move, embedded in an option's premium. Inflates into earnings ("the ramp"), collapses after ("the crush").
- **IV crush**: The overnight collapse of implied volatility after an earnings print, which can make an option lose value even when the stock moves in the right direction. See HITI.
- **Breakeven**: Strike price plus premium paid (for calls). The stock price at expiry above which the position makes money.
- **OTM / ITM (out of / in the money)**: For calls, whether the stock is below (OTM) or above (ITM) the strike.
- **Positive skew**: A return profile of many small losses and rare large wins. Its survival depends on cutting losses small and never capping the rare large win.
- **Kelly criterion**: A formula for bet sizing that maximizes long-run growth given win probability and payoff. Referenced by Calxter as the ceiling sizing should never exceed.
- **BOTZ rule**: House rule, named for Sheldon's robotics ETF: themes without dated data mechanisms are dead money, for entries and for holds. When the mechanism expires, so does the reason to hold.
- **Rule 4 / bear floor**: House rule requiring the lowest Buy-rated analyst target to sit above breakeven at entry and throughout the hold.
- **Reachability (proposed Rule 6)**: New filter requiring the move to breakeven to be at most 1.5x the stock's demonstrated median earnings-reaction move.
- **Scale-out ladder**: Proposed exit amendment: bank half of a multi-contract winner at plus 100% pre-catalyst; written EV check on single contracts at plus 150%; mechanism expiry overrides all.
- **Theta**: The daily decay of an option's time value. The rent paid for holding.
- **Salvage exit**: Selling a failing position early to recover remaining premium instead of riding it to zero. The fund's measured edge: average loss 36% of premium versus the 100% base case.
- **13F vs Form 4**: Institutional quarter-end holdings filing versus a named insider's transaction report. Not the same signal. Never conflate. (Standing decision, June 17.)
