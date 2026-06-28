# BAXTER'S SYSTEM IMPROVEMENTS
*Running document. Baxters add one idea at a time, supporting evidence before recommendation.*
*Started June 28, 2026. Do not close or archive -- keep adding.*

---

## HOW THIS DOCUMENT WORKS

The binder is the law. This document is where the Baxters argue about whether the law needs amending.

For each idea: what we observed, what the data says, what the Baxters think, and what the recommendation is. A recommendation only becomes a standing decision (binder update) when Prime, Calxter, and Bearxter all agree. Bullxter is not a tie-breaker. Macxter's opinion counts when the idea involves macro triggers.

Each idea gets:
1. **The observation** -- what specific event or pattern prompted the idea
2. **The analysis** -- what the data actually shows
3. **The Baxters' debate** -- independent views, then the meeting
4. **The recommendation** -- what to change, or why not to

---

## IDEA 1: STOCK PRICE PRE-SCREEN (Rule 5 Structural Failures)

### The Observation

We have now encountered at least six names where the stock price itself -- before we ever look at the options chain -- made Rule 5 compliance economically impossible or meaningless:

- MELI ($1,624): puts would have cost $15+ at any remotely thesis-relevant strike. Screened out at chain.
- DUOL ($400): same structural issue. Calls at $1.00 forced 30%+ OTM, not matching thesis range.
- CAT ($1,000): flagged during batch 6 screen as structural Rule 5 risk before chain verification.
- GS ($1,021): flagged same batch.
- META ($551): flagged same batch. Called as likely MELI-category before chain was even pulled.
- INTC ($127.62): a different version -- the stock price didn't prevent a Rule-5-compliant instrument from existing, but forced puts 46% OTM when the thesis only targeted 25-30%. All five rules passed. EV was negative. The instrument existed but didn't match the thesis.

Each time, we identified the structural issue after advancing to full research -- sometimes after the chain was pulled. In the MELI case, we learned the hard way. By batch 6, we were anticipating it.

### The Analysis

**Why does this happen?**

Option pricing is roughly proportional to the underlying stock price. For a stock at $1,000, a $5 put premium buys you exposure to $995 downside per share. For a stock at $50, a $1 put premium buys you exposure to $49 downside. The absolute premium scales with the stock price, but our Iron Rules use fixed absolute caps ($1.50 for puts, $1.00 for calls) rather than percentage caps.

This creates a structural asymmetry: on higher-priced stocks, the fixed premium cap forces us into deeper OTM territory, requiring larger required moves, which typically generates negative EV.

**What does the data say about the thresholds?**

For PUTS (Rule 5: ask ≤ $1.50):
At $1.50 premium, a typical put at 54 DTE with 30% IV (reasonable for a stock near highs) would be approximately 30-35% OTM. On a $100 stock, that's a $65-70P -- stock needs to fall 30-35%. On a $300 stock, that's a $195-210P -- stock still needs to fall 30-35%. So the percentage required move is roughly similar. The structural problem isn't actually the premium vs stock price ratio -- it's whether the THESIS range aligns with the available OTM level.

What actually varies: on higher-priced stocks, the IV environment is different. A $1,000 stock (CAT) near its highs may have only 20-25% IV, meaning OTM puts are cheaper (fewer dollars) but the same percentage OTM. However, $1.50 on a $1,000 stock is only 0.15% of the stock price -- even a 1% daily move wipes out more than the entire put premium. The instrument is too small relative to normal daily variance.

Calxter's calculation:
- CAT at $1,000, daily range ±1.5% = ±$15/day
- A $1.50 put premium on a $1,000 stock is less than one typical day's volatility
- This means the put moves less than 1% with a normal daily move -- the position is too small to express the thesis meaningfully

The threshold where this becomes systematic:
- For PUTS: stocks above $300/share carry structural Rule 5 risk. Flag these before advancing.
- For CALLS: stocks above $200/share at $1.00 cap. Same math.

**Testing against the data:**
- LVS ($26.84): no structural issue. LVS below threshold.
- ZG ($28.67): no structural issue.
- DIS ($98.93): no structural issue. $115C at $0.85 is 16% OTM -- normal.
- MELI ($1,624): above threshold -- would have been flagged and avoided.
- DUOL ($400): above threshold (calls direction).
- CAT ($1,000): above threshold -- flagged in batch 6.
- META ($551): above calls threshold -- flagged correctly.
- INTC ($127.62): below threshold for puts ($300) but special case (discussed in Idea 2).

**The threshold would have correctly flagged: MELI, DUOL, CAT, META (4/4). No false flags on the plays we actually entered.**

### The Baxters' Debate

**Bearxter:** I want this formalized. Every batch, we waste analysis time on names that a single check would eliminate in 10 seconds. If the stock is at $1,000, I don't need to look at the chain to know it's likely a structural fail. The threshold rule is a pre-research efficiency gain. It doesn't require a chain pull. It doesn't require five Baxters. It's just math.

**Bullxter:** I'm worried about stocks that split. NVDA was at $1,000 and did a 10-for-1 split. After the split, it would have been at $100 and passed the threshold. But before the split, we'd flag it. What's the approach for imminent split situations?

**Prime:** If a stock announces a split (confirmed), the post-split price is the relevant figure. A confirmed split announcement is a catalyst that reprices the options chain simultaneously. Pre-split we flag it; post-announcement we reassess using the effective post-split price. The rule applies to the current chain, not a hypothetical future price.

**Calxter:** I want to add a second tier. For stocks in the $150-300 range (puts) or $100-200 range (calls): flag as "moderate structural risk, pull chain before advancing." Not automatic out -- just "proceed to chain earlier in the process." For stocks above $300 (puts) or $200 (calls): flag as "high structural risk, likely screen out." We still pull the chain, but the default assumption is screen-out until the chain proves otherwise.

**Macxter:** No additional input. The stock price threshold is a mechanical rule, not a macro judgment.

**The Five Baxters' Meeting:**
Prime: Mechanically sound. No objection.
Calxter: Two-tier approach adopted.
Bearxter: Agreed. The pre-screen flag saves research time.
Bullxter: Agreed with the split-announcement amendment.
Macxter: Pass.

### Recommendation

**RATIFIED: Add Stock Price Pre-Screen as Step 0.5 in the batch screen.**

Before calculating range percentile (Step 1), note each stock's price. Apply these flags:

| Stock Price | PUTS direction | CALLS direction |
|-------------|---------------|-----------------|
| Below $150 | No structural flag | No structural flag |
| $150-$300 | Moderate R5 risk -- pull chain before research | N/A at calls threshold |
| Above $300 | High R5 risk -- pull chain immediately; default assumption is screen-out | High R5 risk |
| $100-$200 | N/A | Moderate R5 risk -- pull chain before research |
| Above $200 | N/A | High R5 risk -- pull chain immediately; default assumption is screen-out |

The flag does not auto-eliminate the name -- it accelerates the chain check and sets the default expectation. A chain that shows valid instruments within the thesis range overrides the flag.

**Binder update needed:** Add Step 0.5 to THE UNIFIED SCREEN section.

---

## IDEA 2: EV FORMAL GATE (Instrument-Thesis Alignment)

### The Observation

INTC passed all five Iron Rules in batch 6:
- Rule 1: 89th pct (puts zone) ✓
- Rule 2: Earnings Jul 24 confirmed ✓
- Rule 3: 5 Sell/Underperform ratings ✓
- Rule 4: Highest Sell target (Rosenblatt $50) below any Aug 21 put breakeven ✓
- Rule 5: $65P Aug 21 at $1.16, ask ≤ $1.50 ✓

But EV analysis showed the trade was negative to breakeven:
- $65P breakeven: $63.84 (requires INTC to fall -50% from $127.62)
- Thesis: INTC at $127 vs avg analyst target $96 suggests 25-30% overvaluation, not 50%
- Bear scenario at thesis range ($85-96): stock is at $85-96 and $65P = $0 (still OTM)
- Break-even requires reaching $63 -- Rosenblatt's target, the most extreme bear
- EV = 0.07 × (payoff if reaching $63) - 0.93 × $116 = approximately -$19

This is the INTC problem: the available instrument (forced to deep OTM by Rule 5's $1.50 cap on a $128 stock) does not match the thesis range. The thesis is "stock falls 25-30%." The instrument needs "stock falls 50%." Those are different bets. All five Iron Rules can pass while the actual trade is economically wrong.

### The Analysis

**Why the Iron Rules don't catch this:**

Rule 4 is designed to ensure the most optimistic bear (highest Sell target) is still below the put breakeven. It checks that the BEAR case supports the instrument. But Rule 4 does NOT check whether the bear case is STRONG ENOUGH to reach the breakeven. Rosenblatt's $50 target (below any put breakeven) technically passes Rule 4, but the $50 target requires a -61% decline -- far more extreme than the 25-30% the general thesis targets.

The gap: Rule 4 checks that the highest Sell target is below breakeven (bear case supports the option). But it doesn't check that the OPTIONS range is within the THESIS range. Those are different questions.

**Formalizing the gap:**

Define "thesis range" as the expected price destination if the bear case materializes without being extreme. Practically: average Sell/Underperform target from the identified Rule 3 analysts.

For INTC:
- Rosenblatt Sell: $50
- JPMorgan Underweight: $45 (from April 2026; stock was $46 at the time)
- Average of known Sell targets: ~$47.50

"Thesis range" = $47.50 to $95 (avg analyst target as the midpoint)

Now: what's the put breakeven at Rule 5 limit?
- Best Rule-5-compliant put: $65P at $1.16, breakeven $63.84
- Is $63.84 within the thesis range ($47.50 to $95)? YES -- $63.84 is between the Sell targets and the midpoint.

But is the probability of reaching $63.84 meaningful? Only if the stock falls 50% in 54 days. The thesis targets $85-96 (25-30% move). The $63.84 breakeven is BELOW the thesis midpoint.

The distinction: the instrument is "inside the thesis range" (between $47.50 and $95), but it requires a more extreme move than the central thesis. There's a difference between "inside the range" and "centered on the most likely bear outcome."

**A cleaner metric: instrument breakeven vs. central bear scenario**

Central bear scenario for puts = average Sell/Underperform target OR the average analyst consensus if thesis is primarily "stock overvalued vs fundamentals."

For INTC:
- Central bear = avg analyst target $96 (if thesis is "stock returning to fair value")
- OR central bear = avg Sell target ~$47.50 (if thesis is "bears are right")

$65P breakeven = $63.84. 
- vs. fair value return thesis ($96): breakeven is $32 BELOW the central bear scenario. The option requires 2x the thesis move.
- vs. pure bear target ($47.50): breakeven is $16 above the average Sell target -- which passes.

The problem is that Rule 4 uses only the highest Sell target (checking that the MOST OPTIMISTIC bear supports the instrument). It doesn't check the CENTRAL bear scenario (the most likely bear outcome). When Rule 4's highest Sell target is extreme ($50 for INTC), it passes Rule 4 while the most likely bear scenario (stock to $90, not $50) leaves the instrument OTM.

**Proposed fix: EV gate**

After all five Iron Rules pass, calculate the base case EV using:
1. Central bear scenario = simple average of all identified Sell/Underperform targets (or consensus analyst target if the thesis is "overvalued vs fundamentals")
2. Probability = 20% (base rate for a bear earnings outcome; can be adjusted with specific catalyst conviction)
3. Payoff at central bear scenario = max(0, strike - central bear) × 100 - premium × 100
4. EV = 0.20 × payoff - 0.80 × premium × 100

If base case EV < 0 at 20% probability: the instrument doesn't match the thesis. The trade fails the EV gate regardless of Iron Rules.

**Testing INTC:**
- Central bear = $96 (avg analyst target is as the "return to fair value" thesis)
- $65P payoff at $96: max(0, 65-96) = $0 (still OTM at $96)
- EV at 20% bear probability: 0.20 × $0 - 0.80 × $116 = **-$92.80**
- Test: INTC FAILS EV gate.

**Testing DIS (calls, for comparison):**
- Central bull = avg analyst target $134
- $115C payoff at $134: max(0, 134-115.85) = $18.15/sh = $1,815 - $85 = $1,730
- EV at 20% bull probability: 0.20 × $1,730 - 0.80 × $85 = $346 - $68 = **+$278**
- Test: DIS PASSES EV gate.

**Testing ZG (from week-04):**
- Central bull = avg analyst target (from research_ZG.md -- approximately $36-40 range estimated)
- If $36C ZG at appropriate strike... (data not at hand, but ZG entered at 4/5 conviction suggests positive EV at central scenario)

The gate appears to work on the test cases.

### The Baxters' Debate

**Calxter:** This is the right fix. The EV gate doesn't replace the Iron Rules -- the Iron Rules are the pre-screening filters that ensure we're looking at the right kind of setup (range, catalyst, analyst consensus, floor). The EV gate is the economic filter that ensures the specific instrument available within Rule 5 actually captures the thesis. A setup that passes rules but fails EV is a mismatch between the framework and the instrument.

**Bearxter:** I want to know: is 20% the right base rate for "central bear probability"? Twenty percent feels arbitrary.

**Calxter:** Twenty percent is conservative for a thesis where we have 5+ Sell analysts and the stock is 30% above consensus. A well-supported puts thesis probably has a 25-35% bear probability. I'm using 20% as a floor -- if the trade fails at 20%, it's EV negative even if the probability is 15% higher. Any play that passes at 20% has positive EV across a wide probability range.

**Prime:** The gate should be documented as a step between Rule 5 verification and the full five Baxters meeting. If EV gate fails: screen out without full research. If EV gate passes: advance to five Baxters.

**Bullxter:** What if I believe the bear probability is 40% instead of 20%? Can I override the gate with a higher probability argument?

**Prime:** No. The EV gate uses the base rate. Your belief about probability is expressed in the conviction score (3.5 to 5/5), not in the EV gate calculation. The gate is a minimum threshold check, not a conviction optimization. If the gate passes at 20%, your 40% probability belief gives you stronger conviction -- but you can't use your conviction to bypass the gate. The gate exists specifically to prevent the "I believe in this trade more than the math supports" error.

**Macxter:** The EV gate should incorporate macro regime. In a risk-off macro environment (rising rates, tightening financial conditions), bear probabilities are structurally higher across the board. In risk-on, they're lower. The fixed 20% assumes an average regime. I'd suggest: in a clear risk-off macro regime (Warsh hold, VIX elevated, credit spreads widening), the base rate should be 25%. In a clear risk-on regime, 15%.

**Prime:** Noted but deferred. The macro overlay adds complexity. The initial implementation uses a flat 20% baseline. Macxter's adjustment can be added after the gate is field-tested.

### Recommendation

**RATIFIED: Add EV Gate as Step 4.5 between Rule 5 verification and full research.**

**EV Gate calculation:**

For PUTS:
- Identify central bear price: average Sell/Underperform analyst target. If all Sell targets are below current price by more than 40%, use the midpoint between the current price and the average Sell target as the central scenario (reflecting partial thesis realization rather than full bear case).
- Base probability: 20%
- Payoff at central bear price: max(0, strike - central bear price) × 100 - (ask × 100)
- EV = 0.20 × payoff - 0.80 × (ask × 100)
- If EV < 0: SCREEN OUT. Document reason: "EV gate fail -- instrument requires more extreme move than central bear scenario."

For CALLS:
- Identify central bull price: average BUY analyst target.
- Base probability: 20%
- Payoff at central bull price: max(0, central bull price - strike) × 100 - (ask × 100)
- EV = 0.20 × payoff - 0.80 × (ask × 100)
- If EV < 0: SCREEN OUT. Document reason: "EV gate fail -- instrument requires more extreme move than central bull scenario."

Note: This replaces the informal "Calxter EV estimate" in research docs with a required pre-research gate. The full EV analysis in research docs can still vary the probabilities -- the EV gate only sets the floor.

**Binder update needed:** Add EV Gate as Step 4.5 in both Iron Rules sections.

---

## IDEA 3: PRE-EARNINGS DIP ENTRY PROTOCOL

### The Observation

Micron (MU) provided a textbook example this week. On Tuesday June 23, MU fell 11.4% due to the South Korean KOSPI chip index cratering 10% and the broader AI demand skepticism narrative. None of the Tuesday news was Micron-specific. Micron had 16 long-term supply contracts representing $22B in committed revenue -- that doesn't change because Korean chipmakers fell. On Wednesday June 24 after hours, Micron reported EPS $25.11 vs $20.20 expected (+24%), revenue $41.46B vs $35.84B expected, and guided Q4 to $50B vs $43.58B consensus. The stock jumped 15%+ in after-hours.

If we had been tracking MU as a calls candidate and it dropped 11% the day before its own earnings on sector contagion, buying at Tuesday's $1,074 close would have captured the Wednesday jump. We were not tracking MU (it was near 52-week highs -- outside our calls zone). But the pattern applies to names we ARE tracking.

The specific case: imagine we're holding DIS as a pending pitch (research_DIS.md just written). DIS earnings are August 12. If DIS drops 8% on August 10 due to a macro event (rate spike, market selloff, sector contagion) with no DIS-specific news, what's the right action?

Our current protocol: we have an entry price and a pending entry decision. The drop on August 10 is not DIS-specific. The thesis hasn't changed. But the option is now cheaper (the stock moved down while the thesis didn't).

### The Analysis

**What is macro contamination?**

Macro contamination is when a stock's price moves due to broad market forces rather than company-specific news. Key characteristics:
- The news driving the move is NOT specific to the stock being tracked
- The stock's fundamental thesis (earnings setup, catalyst, analyst consensus) is unchanged
- Other stocks in the sector or broader market moved in the same direction for the same reason
- The stock recovers quickly when the macro fear recedes

MU on June 23 was classic macro contamination: Korean chip stocks fell (different companies, different supply chains), Nvidia fell (GPU, not memory), and Micron fell (DRAM). The DRAM supply/demand cycle, Micron's locked long-term contracts, and the Q3 earnings setup were all unchanged.

**How does contamination affect options pricing?**

When a stock drops on macro contamination before its own earnings:
1. The stock price falls, moving the option further OTM (the call is now deeper OTM)
2. The premium may drop as the option moves further from the money
3. But the fundamental catalyst (earnings) is unchanged and the timing is the same
4. If the stock bounces on earnings as thesis predicts, the call captures both the contamination bounce AND the earnings move

Effect: if we have a $100 stock with a $110C at $0.80 (breakeven $110.80, +10.8% required), and the stock drops to $92 on macro contamination, the $110C might reprice to $0.40. The required move from $92 is now $110.80 = +20.4%. But if the earnings beat takes the stock to $115 (a normal +15% move from $92... actually +25% from $92 to $115 is aggressive). Hmm. From $100, a 15% earnings move = $115. From $92, a 15% earnings move = $105.80. At $105.80, the $110C is still OTM.

Actually, macro contamination drops can HURT the trade if the required move now exceeds what the earnings catalyst delivers. If DIS needs to move +17.1% from $99 to reach $115.85 breakeven, and DIS falls to $88 due to macro contamination, the new required move from $88 to $115.85 = +31.6%. That's even less likely.

But if the DROP allows us to BUY a LOWER STRIKE that wasn't available before: if DIS drops to $88 and a $100C Aug 21 becomes available at $0.75 (which wouldn't have been available at $1.00 cap when DIS was at $99), the new breakeven is $100.75 -- only +14.4% required from $88. That's a better trade than the original $115C setup.

**When contamination helps vs. hurts:**

Contamination helps if: the drop creates a LOWER STRIKE opportunity within Rule 5 that improves the trade structure (lower breakeven, more thesis-aligned strike).

Contamination hurts if: the drop just makes the same option cheaper while pushing breakeven further from the current price, without opening new strike opportunities.

The key distinction: check the CHAIN after the contamination drop, not just the price.

**Protocol proposal:**

1. Active watch list includes all names with research docs written (pending entry decision).
2. If any watched name drops 5%+ in a single session on macro/sector news (not company news), note it as a "contamination alert."
3. Check the options chain the same day. Two questions: (a) Has a new lower strike opened that wasn't Rule-5-compliant before? (b) If entering the original strike at the new price, does the required move still work?
4. If a new viable strike opened: run fast Rule 4 check on the new strike. If passes, this is now an improved entry candidate.
5. If no new strike opened and the required move worsened: hold and wait for recovery.

### The Baxters' Debate

**Bullxter:** This is the single best improvement idea in this document. MU showed that macro contamination creates a buying window. We should be watching our pending names daily during the 2-week window before their earnings dates. Any drop on non-company news is an entry signal.

**Bearxter:** I want clarity on "macro/sector news" vs "company-specific news." Who decides if a drop is contamination vs. real information? If DIS drops 8% the day before earnings, it could be because: (a) broader market selloff (contamination), (b) a negative review of the latest Disney+ subscriber data from a research firm (company specific), or (c) a story about parks attendance declining from vacation-booking data (company specific). How do we distinguish?

**Prime:** The test is: did the news source specifically name the stock and cite a company-specific negative? If Bloomberg runs "Markets Selloff, Tech Weak" and DIS is down 8% in sympathy, that's contamination. If Bloomberg runs "Disney+ Subscriber Churn Accelerates in Q3 Per Third-Party Data," that's company-specific and the drop is the thesis changing, not contamination.

**Calxter:** The chain check is the key action regardless. If the drop opens a better strike, take it. If not, don't act. The "contamination alert" is a reminder to pull the chain and look for opportunities -- not a mandate to enter.

**Macxter:** I want to add: contamination drops in the 5-day window before earnings often reflect IV compression (the options become cheaper because the uncertainty event is imminent and the market "knows" when the resolution comes). This creates an additional pricing advantage for entry: not only is the stock cheaper, but IV may be compressing before the event, making the option cheaper even relative to the new lower stock price. The day before earnings is sometimes the cheapest entry point.

**Bullxter:** Exactly. The options market often prices "pre-earnings fear" on the underlying. Buy the fear.

**Bearxter:** One constraint: if the contamination drop takes the stock below the 25% percentile threshold (for calls), it's now MORE in the calls zone, not less. But if it drops below the 52-week low -- if a new all-time low is set -- that's a specific alert that the thesis may be broken (the "no fresh 52wk low in 5 days" Rule 1 addendum). If contamination pushes a stock to a new 52wk low, we don't buy -- we pause and verify the thesis is intact.

### Recommendation

**RATIFIED: Add Pre-Earnings Contamination Alert to active watch protocol.**

**Definition of contamination drop:** A drop of 5%+ in a single session where the news driving the market is broad market/sector, not stock-specific.

**Action protocol:**

1. When any pending research name drops 5%+ on contamination: pull the options chain same day.
2. Check for: (a) new viable strike not previously Rule-5-compliant, (b) improved required move on original strike.
3. If new viable strike found: run Rule 4 on the new strike. If passes, this is an improved entry opportunity.
4. Constraint: if contamination creates a fresh 52-week low, PAUSE -- do not enter. Verify thesis is intact before considering entry.
5. If nothing improves in the chain: wait for recovery. Do not enter on contamination alone -- only if the chain improves.

**Binder update needed:** Add to EXIT PROTOCOLS section as "Pre-Entry Watch Protocol" (or new TAB 4.5).

---

## IDEA 4: SHORT INTEREST ENHANCEMENT (Beyond the Squeeze Warning)

### The Observation

Wendy's (WEN) jumped 25-42% intraday on June 25 on a Reddit "Save Wendy's" campaign. The setup: 34% short interest + beaten-down stock near multi-year lows + new credible management (Steve Cirulis CFO + Bob Wright CEO from Potbelly, where they achieved a 500%+ turnaround). The combination of extreme short interest + fundamental catalyst created a short squeeze that briefly dwarfed any earnings play.

Our current binder handles short interest:
- PUTS: "Short interest >10% of float = SQUEEZE WARNING. Minimum 4/5 conviction required."
- CALLS: "Short interest is a tailwind. Note but do not penalize."

The calls short interest rule is correct in direction but too vague. "Note but do not penalize" doesn't capture the magnitude of the opportunity. WEN showed that extremely high short interest (>20%) with a fundamental catalyst (credible new management) creates a separate, higher-conviction calls category than our standard earnings plays.

### The Analysis

**How short squeezes work:**

Short sellers borrow shares and sell them, expecting to buy them back later at a lower price. They pay interest on the borrowed shares (borrow rate). If the stock rises instead of falls, short sellers face losses that compound with time. At some threshold (individual, not universal), they are forced to buy back shares to limit losses. That buying adds demand to existing buying, pushing the price higher, forcing more shorts to cover, creating a feedback loop.

The squeeze potential depends on three factors:
1. Short interest (% of float): how many shares are short. 34% is extreme. The typical equity has 2-5% short interest. 10%+ is notable. 20%+ is high. 34% is near-maximum for a liquid stock.
2. Borrow rate: how much shorts are paying to maintain positions. High borrow rates mean shorts are bleeding capital daily. They're more likely to close under pressure.
3. Days to cover: (short interest × average daily volume). How many trading days would it take for all shorts to close positions at average volume? Low days-to-cover = shorts can exit quickly without pushing the price too far. High days-to-cover = each day of covering creates visible price pressure.

**WEN had all three:** 34% short interest, elevated borrow rates (common when short interest this high), and retail concentrated enough to absorb daily volume.

**Can we predict meme events?**

No. We cannot predict when Reddit focuses on a stock. But we CAN identify stocks that are pre-positioned for a squeeze: they have the fuel (high short interest), need a spark (catalyst), and are near lows (giving calls direction).

**The pattern:**
1. Stock at or near 52-week lows (our CALLS zone already selects for this)
2. Short interest >20% of float
3. Credible management or operational catalyst (new CEO/CFO from a documented turnaround background, material partnership, etc.)

When all three align: the squeeze probability is elevated. Not just "note but do not penalize" -- this is a distinct and potentially higher-conviction setup than a standard earnings play.

**Difference from standard calls setup:**

Standard calls: we need earnings date with confirmed catalyst. The move comes from earnings beat resolving analyst consensus.

Squeeze calls: the catalyst can be ANY positive event -- management change, partnership, earnings beat, even major retail attention. The amplification comes from short covering, not just fundamental buyers. The timeline is potentially much shorter (days vs. weeks).

**Risk:**

Squeeze plays resolve faster and more violently in both directions. A stock that squeezes from $10 to $16 in two days can also drop back from $16 to $11 in two days as retail loses interest and longs take profits. The time window for the calls to be in the money is shorter.

**Can we fit squeeze calls into the Iron Rules?**

Rule 2 requires an earnings catalyst. WEN's move wasn't an earnings play. If we adapt Rule 2 for squeeze plays, we need to substitute "management catalyst confirmed" for "earnings date confirmed." The mechanism is different but the requirement for a specific catalyst date is the same.

### The Baxters' Debate

**Bullxter:** This is a separate playbook. The earnings plays are one system. Squeeze plays are a different animal. Don't try to force-fit squeeze plays into Iron Rules. Create a "Squeeze Play" protocol that runs alongside the Iron Rules for extreme short interest situations.

**Bearxter:** I'm skeptical. WEN is one data point. We've seen one meme squeeze this month. Building a protocol around one observation is premature. What if WEN is anomalous and the next 10 high-short-interest stocks we look at never squeeze?

**Prime:** Bearxter's right about the sample size. One observation. But the broader pattern (high short interest + beaten down + catalyst = squeeze potential) is well-documented in market history. GME, AMC, BBBY, WEN -- these follow the same structural pattern. The question is whether we should have a framework for evaluating them, not whether squeezes happen.

**Calxter:** The EV on squeeze plays is extremely high when they work, but the probability of timing correctly is low. A 34% short interest stock might squeeze next week, next month, or not at all. Our earnings plays have a specific date for resolution. Squeeze plays don't. That ambiguity makes position sizing and expiry selection much harder.

**Macxter:** The Reddit/retail investor market structure has evolved since 2021 GME. The institutional "short squeeze protection" mechanism (options market makers delta-hedging call purchases) is now well-established and documented. When retail buys calls on a high-short-interest stock, market makers buy the underlying to hedge, which itself adds buying pressure. This creates a structural amplification loop. WEN is not an anomaly -- it's the 2025-2026 version of the GME mechanism.

**Prime's synthesis:** Bullxter is right that squeeze plays are different. Bearxter is right that one data point isn't enough for a full protocol. Compromise: add a SHORT SQUEEZE WATCHLIST to passes.md. Any stock we encounter with:
- Short interest >20% of float
- Stock in bottom 25% of 52-week range (calls zone)
- Credible fundamental catalyst (not just "Reddit buzz")

Gets flagged for close monitoring. If a catalyzing event arrives (management change, partnership, beat-and-raise), we evaluate squeeze calls with a tighter time window (30 DTE max) and smaller position (3.5/5 conviction cap until we have more data). Rule 2 substitute: confirmed catalyst event (management announcement, contract, deal) with minimum 2 days of execution runway.

### Recommendation

**PROVISIONALLY RATIFIED: Add Squeeze Watchlist to passes.md. Full Squeeze Protocol deferred pending 3 data points.**

**For now:**
- When screening, flag any calls candidate with short interest >20% as "SQUEEZE AMPLIFICATION -- high priority for monitor."
- When screening, flag any puts candidate with short interest >20% as "SQUEEZE WARNING -- minimum 4/5 conviction required." (This was already in the binder.)
- For the calls direction: add to passes.md as "Squeeze Watchlist" -- names with short interest >20% at or near 52-week lows, with a specified catalyst trigger (what event would prompt squeeze calls evaluation).

**Full protocol pending:** After 3 squeeze watchlist names are observed (whether we enter or not), document what happened and formalize the protocol. Do not attempt to formalize squeeze play sizing, expiry selection, or exit protocol until we have observed examples.

**Binder update needed:** Expand the "CALLS: short interest is a tailwind" note to include: "Short interest >20% = SQUEEZE AMPLIFICATION. Add to squeeze watchlist in passes.md with specified catalyst trigger. Do not enter squeeze calls without a confirmed catalyst and a 30 DTE maximum."

---

## IDEA 5: EARNINGS DATE VERIFICATION PROTOCOL

### The Observation

During DIS research (June 28), two sources gave different earnings dates:
- One source (early search): "Q3 FY2026 earnings August 4, 2026"
- TipRanks (more recent): "August 12, 2026 after close"

The delta is 8 calendar days -- enough to determine whether the Aug 21 option expiry gives us 9 days of post-earnings runway (Aug 12) or 17 days (Aug 4). The wrong date could cause us to enter an option that expires before the catalyst (if the actual date is Aug 12 and we thought it was Aug 4, we'd correctly select Aug 21 -- but if we thought it was Aug 4, we might also consider Jul 31 as a viable expiry, which would actually expire 12 days BEFORE the real earnings).

Rule 2 depends entirely on the accuracy of the earnings date. One wrong date = entering an option that expires before the catalyst = Rule 2 violation we didn't know we made.

### The Analysis

**Sources hierarchy by reliability:**

1. **SEC 8-K filing:** Most accurate. Companies file an 8-K when they set the earnings date. Searchable via SEC EDGAR. But: not always filed far in advance, and the query requires navigating EDGAR.

2. **Investor Relations page (company website):** Second most accurate. Companies post their earnings calendars on their IR pages. Typically 2-4 weeks in advance. Subject to updates if the date changes.

3. **Earnings Whispers (earningswhispers.com):** Third party that aggregates from official sources. Known for accuracy and flagging tentative vs. confirmed dates. Shows "confirmed" or "tentative" status explicitly.

4. **TipRanks:** Aggregates from filings and financial databases. Generally reliable but occasionally shows preliminary dates that haven't been confirmed by company.

5. **News articles:** Least reliable. Journalists often pull unverified dates from other articles or financial databases without checking the original source. The August 4 DIS date likely came from an early projection that wasn't updated when Disney confirmed August 12.

**What "confirmed" means:**

A date is confirmed when: (a) the company has issued a press release or filed an 8-K stating the date, OR (b) the company's investor relations page shows the date with no "tentative" qualifier, OR (c) two independent aggregator sources (EarningsWhispers + TipRanks) agree on the same date.

A date is tentative when: (a) only one source shows it, (b) the source says "estimated" or "approx", or (c) the date is more than 6 weeks away (companies typically don't confirm that far ahead).

**The cost of getting it wrong:**

For DIS specifically: if we had entered a Jul 31 option believing earnings were Aug 4, we would have entered an option expiring 12 days BEFORE the actual catalyst. The option would expire worthless regardless of how well Disney performed. That's a 100% loss due to an administrative error, not a thesis failure.

The correction is cheap: one additional source check, 2 minutes.

### The Baxters' Debate

All five Baxters agreed this is purely a process rule. No debate. One additional verification source before writing any research doc.

**Calxter:** The cost of this check is approximately zero. The cost of Rule 2 violation from a bad date is 100% of premium. The expected loss from skipping the check even once exceeds the cumulative cost of all future checks. This is not a rule that requires debate.

**Prime:** Agreed. Add to research doc template. Not to binder -- this is an execution protocol, not a rule change.

### Recommendation

**RATIFIED: Add earnings date verification to research doc process.**

**Before writing any research doc:**
1. Identify the earnings date (Rule 2 gate)
2. Verify it with a SECOND source
3. Mark as "confirmed" only if two independent sources agree, or if the company's IR page shows it without "tentative" qualifier
4. If sources conflict: use the MORE RECENT source and flag the conflict in the research doc

**Hierarchy for verification:**
1. Company IR page
2. EarningsWhispers (shows confirmed/tentative status)
3. TipRanks
4. SEC EDGAR 8-K search

**Research doc template update needed:** Add "Earnings date: [DATE] -- confirmed via [SOURCE 1] and [SOURCE 2]" to the Prime's Review section.

---

*Document continues as more ideas are investigated.*
*Last updated: June 28, 2026*
