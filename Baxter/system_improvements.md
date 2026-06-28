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

## IDEA 6: RULE 4 RATING DIRECTION CLARIFICATION

### The Observation

During GE research (June 28), we encountered ambiguity about what ratings count for Rule 4. GE had two negative ratings: BNP Paribas Exane "Underperform" and one unknown "Sell." Both are negative. The question arose: does an Underperform count the same as a Sell for Rule 4 purposes? And separately: if there's a "Hold" analyst with a low target, does their target count for Rule 4?

The rule as currently written in the binder:
- PUTS Rule 4: "Highest Sell target must be BELOW put breakeven."
- CALLS Rule 4: "Lowest Buy target must be ABOVE call breakeven."

The words "Sell" and "Buy" create ambiguity at the boundaries. What counts as a Sell? What counts as a Buy? Does Underperform = Sell? Does Neutral = Hold? Does Buy = Outperform?

### The Analysis

**Standard analyst rating scales:**

Most investment banks use a 5-point scale (or a variant):
1. Strong Buy / Overweight / Outperform (top tier bullish)
2. Buy / Accumulate / Positive
3. Hold / Neutral / Market Perform / Equal Weight
4. Underperform / Reduce / Underweight
5. Sell / Strong Sell

Some use 3-point: Buy / Hold / Sell. Some use 4-point (no "Strong Buy"). The key boundaries:

**For PUTS Rule 4:**
The rule requires "highest Sell target." Should this include Underperform/Underweight?

Yes. Underperform = Sell in every meaningful sense. An analyst who rates a stock Underperform is saying "this stock will do worse than the market" -- functionally a bearish call. Underweight means the same thing in portfolio context. These ratings carry downside price targets. The Underperform/Underweight rating is what enables Rule 3 puts to pass (we allow "Sell/Underperform" in Rule 3). Consistency requires that Rule 4 also uses Underperform/Underweight targets when identifying the highest Sell-direction target.

**What about Hold/Neutral for Rule 4?**

This is the critical clarification. A Hold analyst with a price target of $15 on a stock at $20 is bearish by implication -- they're saying the stock is worth $15 but they're not calling it a Sell. Do their $15 targets count for puts Rule 4?

NO. Here's why.

Rule 4 for puts checks: "Is the most optimistic bear still expecting the stock to fall below our breakeven?" The "most optimistic bear" is the highest-target analyst who is actively calling the stock a sell/underperform. A Hold analyst saying "target $15" is not an active bear -- they're saying "don't buy more, don't sell." Their target represents what they think the stock is worth, not a bearish call. A Hold rating is not a directional bet.

If Hold targets counted for Rule 4, we could game the system: any stock with one Hold analyst who has a low target would "pass Rule 4" even with zero Sell ratings. That would essentially eliminate Rule 4's protective function.

**The clean rule:**
- PUTS Rule 4: only targets from analysts with Sell, Strong Sell, Underperform, or Underweight ratings count.
- CALLS Rule 4: only targets from analysts with Buy, Strong Buy, Outperform, or Overweight ratings count.
- Hold/Neutral/Market Perform/Equal Weight ratings are IRRELEVANT to Rule 4 in both directions.

**The same logic for CALLS:**

A Hold analyst who has a target of $150 on a stock at $100 is bullish by implication. Does their $150 count for calls Rule 4 (lowest Buy target above breakeven)?

NO. Same logic inverted. A Hold analyst saying "target $150" is not an active bull. They're saying the stock could get to $150 but they don't want to call it a Buy. The Calls Rule 4 lowest Buy target needs to come from an active bull (Buy/Outperform/Overweight). If the lowest BUY (active bull) target is $120 and the breakeven is $115, that means even the most conservative active bull thinks it's worth more than our breakeven. That is what Rule 4 is checking.

**Practical implications for past research:**

- ZG: Rule 4 for calls checked against Buy analyst targets only. Hold targets with lower numbers were excluded. This was correct.
- DIS: Same. The "$123 low forecast" was confirmed as the current floor of BUY analyst targets. Hold analysts with lower estimates were excluded. Also correct.
- GE: Rule 4 for puts checked BNP Exane Underperform ($270). The unknown "Sell" analyst also counts. Any Hold analyst's target is irrelevant. This was handled correctly but not explicitly stated.
- INTC: Rosenblatt Sell ($50) and JPMorgan Underweight ($45) both counted. Any Hold analyst with a $70 target was correctly excluded.

The rule was applied correctly in practice but never explicitly written. Writing it down prevents future confusion.

### The Baxters' Debate

**Prime:** This requires no debate. It's a clarification of existing intent, not a rule change. Write it in the binder. Done.

**Bearxter:** I want one additional clarification: "Buy-to-Hold downgrade." If an analyst was previously Buy and downgrades to Hold, they no longer count for CALLS Rule 4. Their prior Buy target is now stale. For PUTS Rule 3, the binder already says "Buy-to-Hold downgrades do NOT satisfy Rule 3 -- a Hold analyst cannot contribute a bull ceiling." The same logic means that a downgraded-to-Hold analyst's target no longer counts for Rule 4. Their new Hold rating supersedes their prior Buy.

**Calxter:** Agreed. Rating is always the CURRENT rating, not historical. Targets are only relevant when paired with the current active rating.

### Recommendation

**RATIFIED: Add Rule 4 rating direction clarification to binder.**

**For PUTS Rule 4:** Only count targets from analysts with CURRENT ratings of: Sell, Strong Sell, Underperform, Underweight, or equivalent active bear ratings. Exclude Hold/Neutral/Market Perform/Equal Weight even if they have low price targets.

**For CALLS Rule 4:** Only count targets from analysts with CURRENT ratings of: Buy, Strong Buy, Outperform, Overweight, or equivalent active bull ratings. Exclude Hold/Neutral/Market Perform/Equal Weight even if they have high price targets.

**The rule in one sentence:** Rule 4 cares about what direction-aligned analysts think, not what fence-sitters think.

**Binder update needed:** Add a "Rating definitions for Rules 3 and 4" paragraph to both Iron Rules sections.

---

## IDEA 7: PUTS EXIT PROTOCOL (Formalizing the Calls-Side Equivalent)

### The Observation

The binder has detailed exit protocols, built primarily from experience with calls plays. The calls exit architecture:
- Standard exit: sell at market open the morning after earnings
- Rule 4 breach: same-day exit
- Pre-earnings profit (bear floor reached early): evaluate same-day exit
- BOTZ (no mechanism remaining): sell into time value

But puts plays have structural differences that calls exit protocols don't address:

1. **Timing around earnings:** For calls, we're buying recovery into an earnings beat. For puts, we're buying deterioration into an earnings miss. The pre-earnings and post-earnings behavior is different.

2. **IV dynamics:** When a stock is falling (puts gaining), IV often rises simultaneously (market fear increases). This creates a "double benefit" dynamic: intrinsic value gained AND extrinsic (vega) value gained. The reverse: when the stock doesn't fall as expected, IV can collapse post-earnings, wiping out both premium components simultaneously.

3. **Catalyst-resolved puts:** After a bad earnings report, the stock typically opens 10-20% lower. The put is deep ITM. But should we hold for further deterioration, or exit at the open? If guidance is bad, the stock may continue falling over days. Unlike calls (where earnings were the specific catalyst), puts can have post-earnings continuation.

4. **Rule 4 equivalent for puts:** The binder defines Rule 4 as "Highest Sell target must be below put breakeven." During the hold, if a previously Sell-rated analyst UPGRADES to Hold, the effective "highest Sell target" could change if the upgrading analyst had the highest target. This is the puts equivalent of the calls Rule 4 breach -- except it's an upgrade rather than a downgrade.

### The Analysis

**When to sell a winning puts position:**

Scenario A: Stock opens down 15% after earnings miss. Put is deep ITM. Should we sell at open?

The calls analogy: sell at open the morning after earnings. The catalyst fired. But for puts, a company reporting bad guidance often continues to sell off over days as analysts cut price targets, funds rebalance, and retail investors process the news. The post-earnings puts opportunity can extend 2-5 sessions.

However, holding a deep ITM put through multiple days also introduces "gap reversal" risk: the company or a competitor says something positive after the first down day, and the stock bounces 8%. If the put loses all intrinsic value in a single bounce day, the gain from an extended hold was erased.

**The resolution:**

Sell at open the morning after earnings. Same as calls. Reason: the catalyst (earnings) resolved. The thesis was "stock falls on earnings." It did. What happens on day 2, 3, 4 is a new thesis (continued deterioration), and we have no mechanism to evaluate day 2 probability with the same rigor we used to evaluate the catalyst. The earnings-catalyst logic closed. The position close is the right action.

Exception: if the guidance provided a specific data point that confirms a multi-week deterioration (e.g., company says "we expect operating margin to compress for the next 4 quarters"), hold to a day-2 close to capture the opening reversal gap if the stock gaps down further on the open. No longer than day 2.

**Rule 4 equivalent for puts during hold:**

For puts, Rule 4 says highest Sell target must be below put breakeven at entry. During the hold, what's the puts equivalent of a Rule 4 breach?

Two situations:
1. An analyst upgrades from Sell to Hold (or Buy): the "highest Sell target" may now change. If the only Sell analyst upgrades to Hold, Rule 3 now fails (fewer than 2 Sells) AND Rule 4 may change (their previous Sell target was the benchmark). Exit same day. Same logic as the calls Rule 4 breach.

2. A Sell analyst RAISES their target above the put breakeven: the highest Sell target is now above breakeven. Rule 4 is breached. Exit same day.

**Pre-earnings profit target for puts:**

For calls: "If the stock reaches the bear floor price before the earnings date, evaluate same-day exit." The puts equivalent: "If the stock reaches the bull ceiling price (the highest Sell analyst target) before the earnings date, evaluate same-day exit."

Wait -- the puts direction: if a stock falls to the Sell analyst's target price, the put is now well in the money (breakeven is below the analyst target by design). Should we take profits? Yes, if the stock has reached the price the most optimistic bear expected -- the thesis has fully played out.

**The BOTZ equivalent for puts:**

If the stock is NOT falling and earnings are within 10 days, the puts thesis has not materialized. The time value is decaying against us. Apply BOTZ: if the stock hasn't moved toward breakeven with 10 days remaining and no remaining mechanism, sell into time value.

### The Baxters' Debate

**Prime:** The exit protocol for puts should mirror calls as closely as possible:
- Standard: sell at market open morning after earnings
- Rule 4 breach (analyst upgrade or target increase above breakeven): same-day exit
- Pre-earnings: if stock reaches highest Sell target before earnings, evaluate same-day exit
- BOTZ: if no movement toward breakeven within 10 days of expiry, sell time value

**Bearxter:** I want to add: if the stock falls sharply BEFORE earnings (not due to earnings, but due to a pre-announcement, negative data release, or bad news event), evaluate same-day exit. The thesis was an earnings-specific catalyst. If the thesis played out early (like the calls pre-earnings profit protocol), the same principle applies.

**Bullxter:** What if the stock falls 15% pre-earnings and then has a disastrous earnings call that drops it another 15%? We could make more money holding through earnings. Why cut early?

**Prime:** Because holding through earnings with a thesis that already resolved is speculation without a mechanism. The pre-earnings fall may have been the catalyst playing out. The earnings call introduces binary uncertainty -- they could actually beat on the operating line while guidance is bad. The safe exit is when the thesis resolves, not when maximum profit is hypothetically achievable.

**Calxter:** Bullxter's concern has a specific answer in Kelly terms: a put that is 30% in the money has already returned 3x+ on the initial premium (the option gained much more than the premium at risk). Holding for more profit when the instrument is deep ITM extends the hold duration without reducing the denominator (at-risk amount is now larger on the books, even though it's "in the money"). The risk-adjusted incremental return of holding deeper vs. taking profit and redeploying to a fresh position is almost always negative.

### Recommendation

**RATIFIED: Puts exit protocol added as parallel to calls protocols in binder.**

**PUTS EXIT RULES:**
1. **Standard exit:** Sell at market open the morning after earnings. Same as calls. The catalyst resolved. The thesis is closed.
2. **Upgrade breach:** If any identified Sell/Underperform analyst upgrades to Hold or Buy during the hold period, AND this reduces active Sell ratings below 2 (Rule 3 failure) OR raises the highest Sell target above put breakeven (Rule 4 failure): exit same day. Do not wait for earnings.
3. **Pre-earnings profit:** If the stock falls to the highest Sell analyst's target price before earnings: evaluate same-day exit. The thesis (bears are right about the price target) has been confirmed. Hold only if there is a specific additional catalyst expected at earnings that the bear thesis would amplify.
4. **BOTZ for puts:** If the stock has NOT declined toward breakeven within 10 days of expiry AND no specific negative catalyst is pending: sell remaining time value. The thesis did not materialize within the window.
5. **M&A announcement:** Exit at open the next trading day. The thesis is structurally destroyed.

**Binder update needed:** Add PUTS EXIT RULES as a sub-section of TAB 4 (EXIT PROTOCOLS).

---

## IDEA 8: POST-IPO PUTS FRAMEWORK (The SPCX Pattern)

### The Observation

SpaceX (SPCX) IPO'd on June 12 at approximately $31/share. Within 10 days, the stock had rallied to approximately $190 (a ~510% gain), making Elon Musk the world's first trillionaire on paper. Then the stock began a decline: -5% one day, -3.6% another, then -16.4% in a single session on June 22-23, erasing $600B in market value and taking the stock back to $154.60 -- 23% below the all-time high.

The specific trigger was a bond issuance announcement ($20B in investment-grade bonds for AI infrastructure). The structural setup was: post-IPO euphoria had compressed any natural seller (lockup prevented most early investors from selling). The bond announcement signaled "the company needs capital beyond what the IPO raised" and broke the euphoria narrative.

Our current Iron Rules cannot evaluate SPCX. There is no 52-week range (SPCX IPO'd 11 days ago). Rule 1 requires a 52-week range percentile. The entire framework assumes a price history we don't have.

### The Analysis

**What makes post-IPO stocks structurally different:**

1. No price history: can't calculate a 52-week range
2. No earnings data: company may have disclosed financials in S-1 but no quarterly earnings pattern exists
3. No analyst coverage yet (typically 25-day quiet period after IPO before analysts can publish)
4. All-time highs are also the recent all-time highs: every price above IPO is new territory with no resistance
5. Lockup prevents natural sellers: float is artificially small (only IPO shares + pre-lockup secondary), concentrating any selling pressure

**The post-IPO pattern:**

1. IPO at $X
2. First-day pop (often 20-50% for high-sentiment IPOs)
3. First-week rally (retail momentum buying, limited analyst coverage)
4. First negative catalyst (anything: lock-up unlock rumor, secondary offering, bond issuance, first analyst initiates with Hold not Buy, etc.)
5. Selloff from peak (typically 20-40% from post-IPO high in the first 30-90 days)

SPCX executed this pattern in compressed form: IPO June 12, all-time high ~$190 by June 19, bond announcement June 22, $154 by June 23 = -19% from high in days.

**Is the puts framework applicable?**

Partial answer only. The challenge: without analyst coverage, there is no Rule 3 (no Sell ratings -- analysts haven't published yet). Without a 52-week range, there is no Rule 1. Without a quarterly earnings history, there is no Rule 2.

What IS predictable:
- Post-IPO rallies >100% above IPO price create structural vulnerability (no floor below IPO price from fundamental buyers who got in the IPO)
- Any capital raise (bonds, secondary) is bearish signal (company needs more capital than IPO provided)
- Lockup expiry dates are known in advance (typically 90-180 days post-IPO) -- that date creates a scheduled supply event

What COULD be a substitute framework:
- Rule 1 substitute: stock at 100%+ above IPO price (equivalent to "near all-time high")
- Rule 2 substitute: known negative catalyst (lockup expiry, expected secondary announcement, first earnings)
- Rule 3 substitute: no analyst with a Sell rating exists yet (opposite problem -- but if one initiates with Underperform, that's the Rule 3 trigger)
- Rule 4 substitute: IPO price as natural floor? First analyst consensus target?
- Rule 5: same

The problem with a substitute framework: it requires assuming the IPO price is the "fair value floor" -- which is not reliable. SPCX at $31 IPO price may be undervalued, fairly valued, or overvalued. The IPO price is a market-clearing price at one point in time, not a fundamental floor.

**Calxter's assessment:**

Without Rule 3 (analyst coverage to establish professional bearish consensus), we cannot distinguish "this stock is 23% below its post-IPO high for good reason" from "this stock is 23% below its post-IPO high because retail took profits." Rule 3 is load-bearing: it establishes that the decline has credentialed professional support. Without it, we're guessing about fundamentals in a name with limited public disclosure.

**The path to a valid post-IPO puts trade:**

Wait for analyst coverage to initiate. The 25-day quiet period post-IPO ends, analysts publish initiations. If 2+ analysts initiate with Underperform/Sell and targets below current price: Rule 3 is now satisfied from the initial coverage universe. Then apply the rest of the framework.

For SPCX specifically: the first analyst initiations will come in mid-July (June 12 + 25 days = July 7). Watch the initiation ratings. If 2+ Underperform initiations with targets below $150: evaluate puts using the post-IPO price history (even 6 weeks of data) as a proxy for Rule 1.

### The Baxters' Debate

**Macxter:** The SPCX pattern will repeat. High-sentiment IPOs that go public in a risk-on market will rally aggressively and then face the same structural pullback. The bond-issuance-as-negative-catalyst is a recurring pattern: every AI company that IPOs in 2025-2026 will eventually need to tap debt markets. That announcement will always read as "we need more money than equity alone." The framework should account for this.

**Bearxter:** Macxter is right that the pattern is recurring, but Calxter is right that we need analyst coverage before applying Rule 3. The hard minimum: no post-IPO puts until at least 2 analyst initiations are published. No exceptions. Without credentialed bears establishing a professional bearish case, we're not using the Iron Rules -- we're gambling on a pullback.

**Prime:** Recommendation: add a "Post-IPO Watch Protocol" separate from the standard screen. Any high-profile IPO (first-day pop >50% or market cap >$10B at close of first day) gets flagged for monitoring. Track: (a) % gain from IPO price (flag when >100%); (b) scheduled analyst initiation window (IPO date + 25 days); (c) expected capital raise events (bonds, secondary); (d) lockup expiry date.

At the 25-day initiation window: check if any analyst initiates with Underperform/Sell. If yes, run the modified screen. If no: keep watching.

**Bullxter:** The returns on SPCX puts -- if entered at $190 and the stock falls to $154 -- are enormous. A put struck at $150 (before the gap down) with $1.50 premium, if SPCX falls from $190 to $120: that's a $29 payoff on a $1.50 bet. 19x. We should have tools for this.

**Calxter:** The options pricing on a fresh IPO will also reflect the enormous uncertainty. IV will be extreme -- puts on SPCX at $190 would cost 5x more than puts on a stable company with the same % OTM. Our $1.50 Rule 5 cap would eliminate most viable instruments on a 500% post-IPO spike. The structural Rule 5 issue from Idea 1 applies here too.

**Prime's synthesis:** The full Post-IPO framework is deferred. Too many unknowns. Action for now: add SPCX to a "Post-IPO Watch" list. Track analyst initiations starting July 7. If Underperform/Sell initiations emerge AND the stock is still elevated AND Rule 5 allows a viable instrument: run the standard puts framework with the following substitution: use the IPO price as a preliminary Rule 1 anchor (if stock is >75% above IPO price, treat as "near highs").

### Recommendation

**PROVISIONALLY RATIFIED: Post-IPO Watch Protocol added to passes.md structure. Full framework deferred pending observation.**

**For now:**
- Any high-profile IPO (>50% first-day gain or >$10B market cap) gets added to a "Post-IPO Watch" list in passes.md.
- Track: % above IPO price, analyst initiation window, capital raise events, lockup expiry.
- Do not attempt puts until: (a) 2+ analyst initiations with Sell/Underperform published, AND (b) stock still >50% above IPO price, AND (c) Rule 5 allows a viable instrument.
- Apply standard Iron Rules with substitution: Rule 1 anchor = IPO price (stock at 75%+ above IPO price = "near highs" equivalent).

**SPCX immediate action:** Monitor from July 7 for analyst initiations. If 2+ Underperform/Sell, run modified screen.

**Binder update needed:** Add Post-IPO Watch category to STANDING DECISIONS with specific conditions for activation.

---

## IDEA 9: CONVICTION CALIBRATION -- 3.5/5 VS 4/5 IN PRACTICE

### The Observation

Looking at the Island Fund's actual trades versus the conviction scores:

- DSGX: entered, lost. The entry was identified as wrong at entry (post-earnings OTM spike entry). This was not a conviction calibration issue -- it was a rule violation.
- CHWY: entered, wrong strike, exited to redeploy. Conviction was likely overcalibrated (should not have entered).
- NKE: entered 4/5, exited on Rule 4 breach. The Rule 4 breach was legitimate. No calibration issue.
- MDT: entered, exited on BOTZ correctly. No calibration issue.
- DKNG: 4/5, exited on BOTZ (World Cup Day 2), excellent timing, $251 profit. Conviction calibration likely correct.
- HITI: entered, exited correctly at open after earnings. Small loss. Conviction was possibly too high (Rule 5 was STRETCH).
- BSX: Rule 4 breach on entry day. 3.5/5 conviction was possibly too high given the ambiguity at entry.
- TRMB: 3.5/5. Calxter flagged it as "frontier of confidence." Open position.
- UBER: 4/5. Entered at $91.34 (vs $90 strike), the specific thesis (autonomous vehicle doubt meets near-term quarterly headwind) is specific. Open.
- LYFT: 3.5/5. Specific catalyst. Open.
- ABT: 3.5/5 with upgrade rationale. Open.
- ZG: 4/5. All rules clean. Strong setup. Open.
- LVS: 3.5/5. Largest required move (+30%). Open.
- DIS (today): 3.5/5. Required move +17.1%, above typical earnings range.

**The pattern:** Our 3.5/5 plays have higher required moves and more uncertainty. Our 4/5 plays have cleaner rule alignment and more specific catalysts. This seems correct directionally.

**But the calibration question:** Is our 4/5 score truly corresponding to 4/5 performance? We don't have enough closed 4/5 plays to know for sure (DKNG was the clearest 4/5 success). The 4/5 minimum is supposed to filter out marginal trades. Has it?

### The Analysis

**What 3.5/5 and 4/5 are supposed to mean:**

- 3.5/5: All five Iron Rules pass. At least one rule passed with minimal margin (barely cleared the gate). Required move is elevated. Thesis has a specific risk that cannot be fully quantified.
- 4/5: All five Iron Rules pass with clear margin. The specific rule that tends to be tight (Rule 4) passes with >$5 gap (calls) or >$5 gap (puts). Thesis catalyst is specific and high-conviction. No single rule was borderline.
- 5/5: Reserved for situations where Rule 4 has extraordinary margin, the analyst consensus is near-unanimous, the earnings catalyst is very specific and imminent, and historical patterns strongly support the setup.

**Current 5/5 constraint:** Puts system requires 3 closed plays before 5/5 is available. We've never used 5/5 on calls either (it was available from the start but we've consistently scored below it).

**The 4/5 question:**

Our 4/5 plays have been:
- NKE: Rule 3 was solid (2 Sell ratings), Rule 4 had a $6 margin, specific catalyst (recovery from Chinese exposure). Rule 4 breached in-period. **4/5 but Rule 4 breach = loss.**
- DKNG: Cleanest 4/5 we had. Every rule passed with margin. Exited correctly on BOTZ. **4/5 = correct execution, excellent outcome.**
- UBER: 4/5. Still open. Thesis intact as of last check.
- ZG: 4/5. Still open.

The NKE case is instructive: 4/5 score but Rule 4 breach. The breach was legitimate (RBC downgrade, new target below breakeven). The Rule 4 exit was executed correctly. The lesson is not that 4/5 should have been 3.5/5 -- the lesson is that Rule 4 breaches can happen even on solid setups.

**Is 5/5 being systematically underused?**

Looking at our plays, we've consistently scored at 3.5 or 4/5. No play has achieved 5/5 even when all rules passed with large margin. Why?

Possible reasons:
1. Genuine humility (the scores reflect real uncertainty)
2. Anchoring (we anchor to 4/5 as the "good" score and don't push to 5/5)
3. 5/5 threshold is too high (requires conditions we may never see)

The 5/5 definition in the binder: not formally defined. The position sizing table stops at 5/5 (17-20% of reserve). The calls rules say 5/5 is available but not when or what qualifies.

**The gap:** We have detailed definitions for 3.5/5 and 4/5 (intra-score confidence notes in the binder). But 5/5 is defined only by inference: "better than 4/5." Without explicit 5/5 criteria, we can't know if we're underusing it or correctly avoiding it.

### The Baxters' Debate

**Calxter:** I want to define 5/5 explicitly. It should require: (1) Rule 4 margin >10% above breakeven (not just >$5, but >10% for calls or puts); (2) Average analyst consensus MORE than 20% from breakeven in the right direction; (3) Historical earnings: for calls, the company has beaten EPS estimates 3+ consecutive quarters (showing the market systematically underprices it); (4) All five rules pass without ANY borderline interpretation.

**Bearxter:** I'd add a catalyst specificity requirement. A 5/5 calls play should have a specific, documentable catalyst that is not "earnings beat in general" but "THIS specific metric will beat because of THIS specific reason." For NKE, we identified the Chinese revenue recovery story specifically. That was 4/5 quality. A 5/5 play would be, for example, "DKNG Q2 will beat because World Cup has 104 games in 31 days vs Q2 2025's 0 major events -- the revenue increase is structural and countable." That level of specificity is 5/5.

**Bullxter:** DKNG was 4/5 but Bearxter's description fits it. Maybe we should retroactively score DKNG at 5/5? The outcome was consistent with 5/5 quality.

**Prime:** We don't retroactively adjust scores. The score was set at entry with the information available at entry. DKNG was 4/5 at entry. That's the record. The outcome validates that 4/5 plays can have excellent results -- it doesn't make DKNG a 5/5.

**Macxter:** I want to add a 5/5 macro qualification: a 5/5 play should not have material macro risk that could override the thesis regardless of the specific earnings outcome. For calls, if the macro environment is significantly adverse (rates rising fast, sector in broad retreat), even a good earnings beat may not move the stock enough. A 5/5 play should be in a macro-neutral or macro-tailwind environment.

### Recommendation

**RATIFIED: 5/5 Conviction Criteria formally defined.**

**5/5 Conviction criteria (calls -- all must be met):**

1. Rule 4 margin: Lowest BUY analyst target is at least 10% above call breakeven (not just $5 -- 10% of current stock price above breakeven).
2. Analyst consensus gap: Average analyst target at least 20% above call breakeven (stock has significant upside to consensus, not just barely above our exit point).
3. Catalyst specificity: The earnings beat thesis is based on a specific, countable metric that can be verified ahead of the report (not just "they usually beat"). Examples: World Cup games = countable, park attendance in data sets = partially verifiable, subscriber data from third-party sources = countable. Generic "management is good at beating estimates" = NOT 5/5.
4. Clean rules: All five rules pass without ANY borderline interpretation (no "barely cleared Rule 3 with exactly 2 Sells," no "Rule 4 margin is positive but thin").
5. Macro alignment: No meaningful macro headwind specific to the stock's sector. Sector is either neutral or supported by current macro regime.

**5/5 Conviction criteria (puts -- same structure inverted, plus):**

Puts 5/5 is not available until three puts plays close with documented outcomes. This standing decision is unchanged.

**Binder update needed:** Add 5/5 criteria definition to TAB 3 (POSITION SIZING) immediately after the conviction table.

---

## IDEA 10: BATCH SCREEN NAMING AND DOCUMENTATION STANDARD

### The Observation

We are now in Week 4 of the Island Fund, with 6 batches screened (Batches 1-3 in weeks prior, Batch 4 Jun 22, Batch 5 Jun 27, Batch 6 Jun 28). The batch logs are stored in week folders by date. The naming convention has been somewhat ad-hoc:

- `screening_log_batch4_jun22.md`
- `screening_log_batch5_jun27.md`
- `screening_log_batch6_jun28.md`

The passes.md file references batch logs but doesn't have a master index of what was screened in each batch.

The problem: after 20+ batches, finding a specific stock that was screened (and when) will require searching through multiple files. Currently, there's no master index of "which stocks have been screened" across all batches.

### The Analysis

**Current retrieval problem:**

To answer "has TSLA been screened?", you need to know it's in the TSLA research doc (batch 4 per passes.md). To answer "has IBM been screened?", it doesn't appear in any batch log or passes entry. To answer "what batches covered the financial sector?", you'd need to read through batch log context sections.

The batch log system creates information that lives in the week folders but isn't easily queryable.

**What a master screen index would provide:**

A single file: `Baxter/screen_index.md`

Format:
```
| Ticker | Date | Batch | Direction | Result | Notes |
|--------|------|-------|-----------|--------|-------|
| UNH | Jun 28 | B6 | PUTS | FAIL R3 | 0 Sells, pure upgrade cycle |
| DIS | Jun 28 | B6 | CALLS | ADVANCE | research_DIS.md |
| INTC | Jun 28 | B6 | PUTS | SCREEN OUT | EV mismatch -- research cancelled |
...
```

Benefits:
1. Instant lookup: "has X been screened?" = search the ticker column
2. Batch history: "what was in Batch 4?" = filter by batch
3. Result distribution: "how many ADVANCE vs FAIL?" = count the result column
4. No duplicate screening: prevents re-doing work on names already evaluated
5. Pass tracker integration: instead of scanning passes.md for every ticker, filter screen_index for "ADVANCE" and see which ones are still pending

**Implementation:**

The screen_index would be updated after each batch, adding one row per ticker. The index file is append-only (old rows never removed). It's a reference document, not a decision document.

**Volume estimate:**

Batch 1-6: approximately 100+ tickers already screened. At ~20 names per batch and ~3 batches per week, by week 12 that's ~720 names in the index. Still manageable in a single markdown table.

### The Baxters' Debate

**Prime:** Process improvement. No complexity. Add the file, add a row per screening. Two minutes of work per batch.

**Bearxter:** The index should also flag "re-screen eligible" conditions. When a stock was screened out for FAIL R1 (wrong range) three months ago but the stock has moved, it might now be in the correct range. The index should note when a "FAIL R1" result should be re-evaluated (stock moved into the zone). How? Note the price at screen time. If current price differs by >20% from screen price: flag for re-screen.

**Calxter:** That requires active monitoring. Start with the simple index. Add re-screen flags in a v2.

**Bullxter:** Yes, don't over-engineer. Simple index first.

**Prime:** Done. Simple index. Append-only. One row per screened ticker.

### Recommendation

**RATIFIED: Create Baxter/screen_index.md as running master ticker log.**

**Format:**
```
| Ticker | Screen Date | Batch | Direction | Result | Detail | Research Doc |
```

Result values:
- ADVANCE -- full research doc written
- SCREEN OUT -- passed 1-4 but failed at chain/EV gate
- FAIL R1 -- wrong range
- FAIL R2 -- no earnings catalyst in window
- FAIL R3 -- analyst ratings wrong direction/count
- MID-OUT -- 25-74% range, no direction
- CONDITIONAL -- pending specific data to resolve
- WATCH -- re-screen eligible if price changes

**Action needed:** Backfill all 6 batches into screen_index.md (approximately 120 names). Then maintain going forward.

---

## IDEA 11: OPTION LIQUIDITY GATE (Beyond Rule 5)

### The Observation

Rule 5 filters by ask price (≤$1.50 for puts, ≤$1.00 for calls). But the STZ entry from Week 1 was abandoned despite the ask being in range because the bid-ask spread was 56% ($0.70 on a $1.25 option). We called this "instrument is too illiquid to enter cleanly" and walked away. This was correct -- but the decision was ad-hoc, not systematic.

A $1.25 ask with a $0.55 bid means: to enter, we pay $1.25. To exit immediately, we receive $0.55. We're down 56% the moment we enter. The fill price risk alone exceeds our maximum tolerance for any 3.5/5 play.

The binder has no formal liquidity rule. Rule 5 only checks the ask. It doesn't check the bid-ask spread, open interest, or daily volume. These are the three components of option liquidity.

### The Analysis

**Three liquidity metrics:**

1. **Bid-ask spread as % of ask:** (ask - bid) / ask. STZ was 56% ($0.70 spread on $1.25 ask). This is extreme. A normal liquid option has 5-15% spread. A moderately liquid option has 15-30%. Above 30%, the friction of entry/exit materially erodes the return.

At 56% spread: if we pay $1.25 to enter and need to exit at bid immediately (emergency exit), we receive $0.55 = 56% loss at entry. Even if the thesis plays out and the option gains 50% to $1.875 ask, our bid might be ~$1.20. We'd make ~$0.20/sh total = 16% gain on the entry. The spread consumes most of the profit.

**The threshold:** No option with bid-ask spread >25% of ask should be entered. The friction is too high.

2. **Open interest:** How many contracts exist in the current market for this specific option (strike + expiry). Low open interest = few parties have traded this instrument. A thin market means our order could move the price significantly, and there may not be a buyer when we want to exit. Threshold: minimum 100 open interest at the target strike.

3. **Daily volume:** How many contracts traded today. Low volume is fine if open interest is high (existing contracts just aren't trading today). Low volume + low open interest = illiquid instrument. We should not enter an option that hasn't traded today unless open interest is substantial (>500). Threshold: minimum 10 contracts traded today, OR open interest >500.

**When does illiquidity matter most?**

At exit (morning after earnings). We need to sell a contract at market open. If the contract has 10 open interest, the market maker may not have a bid ready at open, and we could face a 50%+ spread at the exact moment we need liquidity. This is particularly dangerous for puts, where the earnings event may be disastrous for the company and the put is deep ITM -- the irony is that being deeply right can still generate a bad outcome if liquidity is absent.

**Current chain script -- does it show liquidity?**

Looking at the fetch_puts_chain.py script: it shows strike, ask, at-risk, breakeven, % needed, Rule 5 status. It does NOT show bid, open interest, or volume. These are available in the Robinhood API (the `get_option_market_data` call includes bid, ask, volume, open_interest).

**Required: update fetch_puts_chain.py to show bid-ask spread and open interest.**

The output should include:
- Bid price (to calculate spread)
- Spread % = (ask - bid) / ask
- Open interest
- Volume (today's contracts traded)

And apply a liquidity gate in the output: mark any strike with spread >25% or open interest <100 as "ILLIQUID -- do not enter."

### The Baxters' Debate

**Prime:** This should have been in the binder from the start. STZ in Week 1 exposed it. We've been lucky that our subsequent trades (ZG, LVS, TRMB, UBER, LYFT, DIS) appear to be liquid enough. But we've been checking bid-ask by hand (when Robinhood shows the chain) and deciding informally. Formalizing the rule prevents the next STZ.

**Calxter:** The spread threshold matters for EV calculation too. If spread is 25%: we're paying a 25% tax on the at-risk amount. A $0.85 put with 25% spread: effective cost is $0.85 + $0.21 slippage at entry + $0.21 slippage at exit = $1.27 total friction on a $0.85 bet. That's 150% of the original ask price just in friction. The EV gate (Idea 2) should incorporate the spread: use the midpoint price (bid + ask)/2 as the effective price in EV calculations, not the ask alone.

**Bearxter:** Agree. Update the chain script. Add the liquidity gate to Rule 5 (or add it as Rule 5.5). The script should flag "ILLIQUID" and we should treat ILLIQUID as an automatic fail regardless of how well Rules 1-5 pass.

**Bullxter:** What about STZ -- we said we'd revisit when the fund grows? If STZ had good liquidity at a different expiry or strike, we wouldn't have known without checking. The liquidity check should be per-strike, not per-stock.

**Prime:** Yes. Per-strike liquidity. The chain script already shows per-strike data. Just add bid, spread, OI, volume per strike.

### Recommendation

**RATIFIED: Add Liquidity Gate as companion to Rule 5.**

**Liquidity Gate (applies at same stage as Rule 5 -- live chain required):**

| Metric | Threshold | Result if below |
|--------|-----------|-----------------|
| Bid-ask spread | <25% of ask | ILLIQUID -- fail |
| Open interest | ≥100 contracts | ILLIQUID -- fail |
| Volume today | ≥10 contracts OR OI ≥500 | ILLIQUID -- fail |

Any strike marked ILLIQUID fails regardless of Rules 1-5.

**Script update needed:** `fetch_puts_chain.py` and the equivalent calls variant must show: bid price, spread %, open interest, today's volume. Add ILLIQUID flag to output. Also: update EV calculation guidance to use midpoint price, not ask.

**Binder update needed:** Add Liquidity Gate to both Iron Rules sections alongside Rule 5.

---

## IDEA 12: ANALYST TARGET FRESHNESS RULE

### The Observation

During INTC research (June 28), we found that JPMorgan had raised their Underweight target from $35 to $45 in April 2026 when INTC was at $45.95. INTC has since run to $127.62. We had to acknowledge that JPMorgan's current target is "certainly higher" than $45 but we didn't know what it was.

This creates an asymmetric risk: the published $45 target is stale. JPMorgan may have raised it to $75 or $80 by now, which would completely change the Rule 4 calculation. We used stale target data.

During DIS research, we also encountered a Piper Sandler target of $95 from October 2024 -- 8 months old. The current context showed a floor of $123 among current analysts, making the $95 target clearly stale. We correctly identified and excluded it.

The question: how old can an analyst target be before we stop relying on it?

### The Analysis

**What makes a target stale?**

Analyst targets are set with a 12-month forward view. They're updated when:
- The company reports earnings (quarterly updates are common)
- A material event occurs (M&A announcement, major product release, regulatory decision, macro shift)
- The analyst changes their rating

If none of these events have occurred, a target can remain valid for up to 12 months. But if significant events have occurred and the analyst hasn't updated:
- Either they're not following the stock actively (low engagement = low target reliability)
- Or they plan to update at the next opportunity (usually earnings)

**Practical staleness thresholds:**

For most active analysts: quarterly earnings = opportunity to update. Targets more than 2 quarters (6 months) without update are potentially stale.

For stocks that have moved >30% from where the target was set: targets set at a materially different price require reconsideration. If INTC was at $46 when JPMorgan set $45, and INTC is now at $128, JPMorgan's $45 target was set with the assumption that $46 was the starting point. Their model has not been updated to reflect a $128 starting point.

**The rule:**

A target is "fresh" if:
- It was set or confirmed (analyst reaffirmed the rating and target) within 3 months, OR
- The stock price has not moved more than 25% since the target was set

A target is "stale" if:
- It was set more than 6 months ago AND the stock has moved >20% since then

**Stale target handling for Rule 4:**

- If the only targets available are stale: flag as "STALE DATA -- Rule 4 requires fresh verification"
- If some targets are fresh and some stale: use fresh targets only for the Rule 4 calculation
- If a stale target would fail Rule 4 but fresh targets pass: advance, noting the stale exclusion
- If a stale target would pass Rule 4 but no fresh targets exist: defer research until fresh data obtained

**The INTC case:**
JPMorgan's $45 target (from April 2026) is stale by both criteria: more than 3 months old (set April 2026, now June 2026 = 2.5 months -- borderline), and the stock has moved from $46 to $128 = +178% (well above the 25% threshold). The target is stale. Rule 4 calculation for INTC using a $45 stale target is unreliable.

**The Piper Sandler DIS $95 case:**
Set October 2024 -- 8 months old. DIS has moved from ~$90 (Oct 2024) to $98.93 = +10%. Time-based staleness: yes (>6 months). Price-based: no (DIS only moved +10%). The target is stale by time but not by price. We correctly excluded it because the current analyst universe shows a floor of $123. The $95 target was an outlier that no current analyst supports.

### The Baxters' Debate

**Bearxter:** I want this rule to be strict. Any target more than 90 days old is required to have a "last reaffirmed" date if we're using it. If we can't find evidence the analyst updated their target in the last 90 days, tag it as "UNVERIFIED -- needs freshness check."

**Prime:** 90 days is roughly one quarter. That's a reasonable boundary. Analysts update at earnings. If the last earnings was 90+ days ago, the next earnings (where they'll update) is also coming up -- meaning the target will be refreshed soon. This suggests: if a target is >90 days old, it's acceptable only if the NEXT earnings is within 30 days (the target will update soon enough that it's worth a brief wait before research).

**Calxter:** The price movement threshold matters more than the time threshold for Rule 4. A target set when a stock was at $200 and is now at $260 (+30%) could be either higher OR lower than the breakeven -- we don't know without a fresh check. Staleness is only a problem if the price has moved significantly. A target set 6 months ago on a stable stock (±5%) is still relevant.

**Bullxter:** INTC is the only case where this has actually mattered. One data point. Don't over-engineer.

**Prime:** Bullxter is right that one case isn't a crisis, but the framework should be explicit about what we do when targets are stale. The question will come up again.

### Recommendation

**RATIFIED: Add Target Freshness Check to Rule 4 verification process.**

**Freshness criteria:**

A target is considered FRESH if ANY of the following:
- Set or reaffirmed within 90 days of research date, AND
- Stock price has not moved >30% since the target was set

A target is STALE if BOTH:
- Set more than 90 days ago, AND
- Stock price has moved >20% since the target was set

**Stale target protocol:**
1. Flag the stale target in the research doc
2. If fresh targets are available from other analysts: use fresh targets for Rule 4
3. If all targets are stale: defer research and note "Rule 4 requires fresh target verification"
4. Exception: if the stale target would FAIL Rule 4 (disqualify the trade), we do not need to update it -- a failing target that is stale means the rule fails conservatively, which is acceptable

**Key exception:** A stale FAILING target is acceptable (conservative). A stale PASSING target requires freshness verification before research advances.

**Binder update needed:** Add "Target freshness: required for passing Rule 4 verification. See [[system_improvements.md]] Idea 12" to Rule 4 language.

---

## IDEA 13: OPTION VOLUME TIMING -- WHEN TO ENTER

### The Observation

We've been entering options based on when the research is done and the thesis is confirmed. But options pricing is not constant. Specific time patterns affect option pricing:

1. **Pre-earnings IV crush:** Implied volatility typically rises in the 1-2 weeks before earnings (more uncertainty, more demand for options) and then collapses after earnings resolve. If we enter calls too early (4+ weeks before earnings), we pay elevated IV that hasn't peaked yet and face theta decay while waiting. If we enter too late (1-2 days before earnings), we're buying at peak IV and paying maximum premium.

2. **Day of week effects:** Options lose theta (time decay) over weekends. Friday close - Monday open = 3 days of theta decay for 2 days of holding. Monday open calls are slightly cheaper than Friday close calls (because 3 days of decay has already happened). We've been implicitly aware of this but haven't formalized it.

3. **Morning vs. afternoon entry:** Option prices are often wider (larger spread) at market open due to dealer recalibration. Prices typically stabilize mid-morning after the first hour of trading. Entering in the first 30 minutes often means paying wider spreads.

### The Analysis

**IV crush timing:**

The typical pattern for a stock with 45 DTE options:
- 45 DTE: IV at baseline
- 30-35 DTE: IV starts rising (analysts begin previewing earnings)
- 20-25 DTE: IV rises faster (earnings closer, more uncertainty demand)
- 7-14 DTE: IV at peak (pre-earnings speculation)
- Post-earnings: IV collapses to baseline (the uncertainty event resolved)

If we enter at 45 DTE (6 weeks before earnings): we pay baseline IV but wait a long time, paying theta.
If we enter at 30 DTE (4 weeks before earnings): we pay slightly elevated IV and pay less theta.
If we enter at 21 DTE (3 weeks before earnings): we're at Rule 2 minimum for puts. IV is elevated. We pay more premium but less theta.

**Optimal entry window:**

The binder currently says "minimum 21 DTE at entry" for puts. This is a floor, not an optimum. The optimal entry is typically 28-35 DTE for puts and 28-42 DTE for calls.

Reasoning:
- Too early (>45 DTE): too much theta decay while waiting for the catalyst
- Too late (<21 DTE for puts, any DTE for calls that's pre-earnings): insufficient runway
- Sweet spot: 28-35 DTE gives 2-3 weeks of holding time with manageable theta, and enters when IV is moderately elevated but not at peak

**Day-of-week effect:**

Weekend theta decay is a real cost but not large enough to materially change entry decisions. The effect is approximately 3/252 days × (annual premium value), which for a $0.85 option over a weekend is roughly $0.01-0.03 of lost time value. Not material.

However, if given a choice between entering Thursday (theta for Friday-Sunday already priced in most scenarios) or Monday (theta has decayed over the weekend, option may be slightly cheaper), prefer Monday entry on a new position where timing is flexible.

**Morning entry timing:**

First 30 minutes of trading (9:30-10:00 AM ET): spreads are widest. Market makers are recalibrating after overnight news. Avoid entering options in the first 30 minutes unless the research is complete and the thesis is specific.

Preferred entry window: 10:30 AM - 2:00 PM ET. Liquidity is typically highest mid-morning to mid-afternoon. Avoid the last hour (3:00-4:00 PM ET) on Thursday or Friday (theta decay concerns).

**Current practice:**

We've been entering based on when research is done, not on timing optimization. For ZG and LVS (entered Jun 27), we don't know what time of day they were entered or what the IV environment was relative to earnings. This needs to be tracked going forward.

### The Baxters' Debate

**Calxter:** The IV timing effect is real but small for individual retail investors. The options market is efficient enough that the "optimal entry window" is mostly a theoretical concept. For plays where we're buying $85-130 in premium, the difference between entering at 35 DTE vs 42 DTE is less than $10 in price impact. This is not worth over-engineering.

**Prime:** Agreed that it's not worth over-engineering. But adding the 28-35 DTE sweet spot as a guideline (not a rule) to the entry process makes sense. It's free information once you know the earnings date.

**Bearxter:** The first-30-minutes avoidance is worth formalizing. We know spreads are wider at open. Avoiding the first 30 minutes is a free improvement with no cost.

**Bullxter:** What if there's a big price move at open that creates an entry opportunity? If DIS gaps down 5% at open due to overnight news, we want to enter immediately to capture the improved price -- not wait 30 minutes.

**Prime:** Special case: if the stock moves materially at open (>3% change) creating an improved thesis setup, enter immediately. The 30-minute rule applies to routine entries, not opportunity-driven entries.

### Recommendation

**RATIFIED: Add entry timing guidelines (soft rules, not iron rules).**

**Entry timing guidelines:**

1. **DTE preference:** Target 28-35 DTE for new entries where flexibility exists. 21 DTE is the hard floor (puts). Do not avoid a valid setup because it's outside the 28-35 window -- this is a preference, not a gate.

2. **Day of week:** No strong preference. Monday is slightly preferable for premium efficiency (weekend decay has already happened). This is a $0.01-0.03 benefit, not material.

3. **Time of day:** Avoid the first 30 minutes (9:30-10:00 AM ET) for routine entries. Spreads are widest at open. Exception: enter immediately if the stock has moved >3% at open and the move improves the trade setup (lower call entry, higher put entry opportunity).

4. **IV calendar awareness:** Note the IV environment at entry in the research doc. If entering in the final 2 weeks before earnings, flag "ENTERING HIGH-IV ENVIRONMENT -- premium includes elevated IV that will collapse post-earnings." This is a reminder, not a gate.

**Binder update needed:** Add entry timing as a footnote in TAB 4 (EXIT PROTOCOLS) or a new subsection of the Iron Rules application guidance.

---

## IDEA 14: SECTOR CONCENTRATION TRACKING

### The Observation

DIS at 3.5/5 produces 1 contract at $85 at risk. When we go to enter, we note in the research doc: "Correlated cap note: UBER $90C Aug 21 ($130 at risk) + DIS $115C Aug 21 ($85 at risk) = $215 = 35.0% of reserve. At the correlated cap ceiling."

The correlated cap (35% in any single primary macro driver) is defined in the binder. But we don't have a systematic way to evaluate it at entry time. Currently:
- We calculate the correlated cap check manually in the research doc
- We don't have a central place that tracks current deployment by sector/macro driver
- If we enter LYFT, UBER, and a hypothetical third ride-share play, we'd need to manually sum across positions.md to check the cap

### The Analysis

**The correlated cap is load-bearing:**

The purpose: if three correlated plays all fail simultaneously (because the macro event that would make them fail is the same event), we don't want to be overloaded in that bucket. Rate-sensitive plays, consumer discretionary plays, and commodity-sensitive plays all carry correlated risk.

Current open positions and their primary macro drivers:
- ABT $100C Jul17: healthcare. Relatively macro-independent (dividends, stable healthcare demand). Low rate sensitivity.
- TRMB $65C Aug21: construction tech / precision instrumentation. Mild rate sensitivity (affects construction volumes). Medium.
- UBER $90C Aug21 × 2: consumer/tech/rideshare. Rate-sensitive (consumer spending), macro-sensitive (employment). High.
- LYFT $16C Aug21 × 2: consumer/tech/rideshare (SAME bucket as UBER). High correlation with UBER.
- DIS (pending): consumer entertainment/streaming. Mild rate sensitivity (parks spending is discretionary). Medium.

**Calculating current exposure:**

Total reserve: $614.
- UBER (2 contracts): $130 × 2 = $260? Wait -- from positions.md, UBER is 2 contracts. Each $90C at some premium. Let me recall: UBER $90C at $0.65 × 2 = $130 at risk.
- LYFT $16C × 2: at some premium. Let me recall: LYFT entered at $0.90 × 2 = $180 at risk.

Consumer/rideshare bucket: UBER ($130) + LYFT ($180) = $310. $310/$614 = 50.5%. Already ABOVE the 35% correlated cap.

Wait -- if UBER and LYFT are in the same consumer/rideshare bucket and total $310, that's already 50.5% of reserve in the same bucket. This is a problem. Or did we already account for this?

Looking at positions.md from memory: the system ratified the LYFT entry noting that UBER and LYFT together don't necessarily have the same macro driver. UBER is larger (35 cities, autonomous vehicle program) and LYFT is smaller (pure rideshare). But their primary Q2 catalysts are both "rideshare summer travel demand" -- the same macro driver.

If we were tracking this systematically, we'd have caught the UBER+LYFT combined exposure before entering LYFT.

**The tracking solution:**

`positions.md` should include a sector/macro driver column. Something like:

```
| Ticker | Entry Date | Strike | Expiry | Premium | At Risk | Macro Driver |
| UBER | Jun 18 | $90C | Aug 21 | $0.65 | $130 | Consumer/Rideshare |
| LYFT | Jun 18 | $16C | Aug 21 | $0.90 | $180 | Consumer/Rideshare |
```

Then: at each new entry, calculate the sum of at-risk by macro driver to check the 35% cap.

Current consumer/rideshare: $310 / $614 = 50.5% (OVER). This means we cannot add DIS (even though DIS is consumer entertainment, not rideshare) without checking if DIS counts in the same bucket.

DIS is not a rideshare play -- it's consumer entertainment (streaming + parks). Different driver. DIS would go in "Consumer Entertainment" bucket, not "Rideshare." So:
- Consumer/Rideshare: UBER ($130) + LYFT ($180) = $310 = 50.5% -- OVER
- Consumer Entertainment: DIS ($85) = $85 = 13.8%

The total consumer exposure (combining rideshare + entertainment) is $395 = 64% of reserve. That's a lot in consumer-facing plays. If Warsh cuts rates tomorrow and consumer discretionary tanks, ALL of these could lose simultaneously. But they're not the exact same driver.

**The resolution: define the driver more specifically.**

The correlated cap applies to plays with THE SAME PRIMARY CATALYST, not all plays in a broad sector. "Consumer" is too broad. "Consumer rideshare earnings" is specific. "Consumer entertainment streaming earnings" is different. UBER and LYFT both require "Q2 rideshare demand exceeded expectations" as their primary catalyst. DIS requires "Q3 streaming profitability accelerated" as its primary catalyst.

These are different catalysts that happen to be in the same broad sector. If rideshare demand was weak in Q2, that doesn't necessarily mean Disney's streaming subscriptions were weak. They can diverge.

But: if a MACRO event causes all consumer spending to fall (recession announcement, major layoff report, consumer confidence crash), ALL consumer-facing plays move together regardless of specific catalyst. That's the correlated risk we're managing.

**Revised correlated cap protocol:**

Tier 1 (same specific catalyst): UBER and LYFT share the exact same Q2 rideshare thesis. Their catalysts are essentially identical. These fully count against each other in the cap.

Tier 2 (same broad macro driver, different specific catalysts): UBER/LYFT (rideshare demand) and DIS (streaming profitability) both depend on consumer health but have independent specific catalysts. These count at 50% weight against each other.

Effective exposure: Consumer/Rideshare ($310) + 50% × Consumer Entertainment ($85) = $310 + $42.50 = $352.50 = 57.4% of reserve.

Still over 35% if we include the 50% cross-tier correlation. The issue is that UBER+LYFT alone blew past the 35% cap at $310 = 50.5%.

This means LYFT should not have been entered given UBER was already at $130/$614 = 21.2% of reserve in the consumer/rideshare bucket. Adding LYFT pushed it to 50.5%.

**The lesson:** The correlated cap must be checked BEFORE entry, not after. If UBER was already in the system at 21.2% of reserve, LYFT could only be added up to 35% - 21.2% = 13.8% remaining in the rideshare bucket. At $180 at risk, LYFT was $180 = 29.3% alone -- already over the remaining 13.8% budget.

This suggests LYFT either should not have been entered, or should have been sized much smaller (1 contract at $0.90 = $90, representing 14.7% -- still over, but closer).

### The Baxters' Debate

**Bearxter:** The correlated cap violation is serious if it's real. But looking at positions.md, both UBER and LYFT are open. The question is whether the system identified the cap issue at entry. I don't have the June 18 entry notes here.

**Prime:** We need to verify in positions.md what was noted at LYFT entry. If the correlated cap was checked and documented as acceptable, there was a reason. If it wasn't checked, that's the gap we're fixing now.

**Calxter:** The corrective action going forward is mechanical: positions.md should include a "cap check" row that shows the cumulative at-risk by macro driver, updated at each entry. Before entering any position, check: (total at risk in this bucket + proposed at risk) / current reserve ≤ 35%.

**Bullxter:** What's the penalty for being over the cap? Nothing happened retroactively. Is this a hard rule or a guideline?

**Prime:** It's supposed to be a hard rule ("may not exceed 35%"). If we're over it now, we need to document why and what the corrective action is. We don't force-exit positions to cure a cap violation (that would mean selling LYFT at a loss just to fix a sizing error), but we note it and do not add more correlated exposure until we're back under the cap.

### Recommendation

**RATIFIED: Add Correlated Cap Tracker to positions.md and enforce at each entry.**

**positions.md update needed:**
Add a "Correlated Cap Summary" section at the bottom of the open positions table:

```
| Macro Driver | Open Positions | Total At Risk | % of Reserve | Cap Status |
|---|---|---|---|---|
| Consumer/Rideshare | UBER, LYFT | $310 | 50.5% | OVER -- no new entries |
| Healthcare | ABT | $76 | 12.4% | OK |
| Construction Tech | TRMB | $152 | 24.8% | OK |
| Consumer Entertainment | DIS (pending) | $85 | 13.8% | OK |
```

**At each new entry:**
1. Identify the macro driver for the proposed play
2. Sum existing at-risk in that driver bucket
3. Add proposed at-risk
4. If total > 35% of current reserve: cap violation. Must size smaller or pass.
5. Update the cap summary table after each entry.

**Action needed on current over-cap:** Document in positions.md. No forced exits. Note that no additional Consumer/Rideshare plays may be entered until UBER or LYFT closes.

**Binder update needed:** Add enforcement language to correlated position cap: "Check the Correlated Cap Summary in positions.md before any entry. If adding the proposed position puts any bucket over 35%, the position cannot be entered at the proposed size. Either size smaller to stay within the bucket, or pass."

---

## IDEA 15: LIMIT ORDER EXECUTION PROTOCOL

### The Observation

When we enter options, we "buy at the ask." The ask is the price at which the market maker is willing to sell. The bid is what they'll pay to buy from us. We always pay the ask on entry and receive the bid on exit. This is standard for retail options traders.

But there's an intermediate option: a limit order at the midpoint (bid + ask)/2. If the market maker is willing to fill at mid, we save approximately half the spread. For a $0.85 ask with a $0.65 bid, the mid is $0.75. If we get filled at $0.75 instead of $0.85, we save $10 per contract.

How often do limit orders at mid fill? In liquid options (OI > 500, narrow spread), mid fills happen frequently -- market makers have enough volume to work around the spread. In illiquid options (OI < 100, wide spread), mid fills are rare -- the market maker needs the spread to manage their hedging costs.

### The Analysis

**The midpoint fill strategy:**

For liquid options:
- Set a limit order at the midpoint ((bid + ask)/2)
- Give it 5-10 minutes to fill
- If unfilled, move to (mid + 0.05) -- split the difference slightly toward ask
- If still unfilled after 15 minutes: reassess. If the thesis is time-sensitive (stock is moving away from the entry price), buy at ask. If not time-sensitive, wait.

For illiquid options (or if the spread is <10%):
- Buy at ask immediately. The spread is small enough that the difference doesn't matter materially. Don't risk missing the fill on a tight-spread option.

**What we save:**

At $0.10 spread, saving $0.05 per share = $5 per contract. Marginal.
At $0.20 spread (for example, $0.85 ask, $0.65 bid = $0.20 spread), saving $0.10 per share = $10 per contract. Meaningful.
At $0.40 spread (wide, illiquid), saving $0.20 per share = $20 per contract. Significant.

Over 20 trades at an average $10 savings each = $200 saved. At our fund size, $200 is significant.

**Exit execution:**

On exit (morning after earnings), we're selling into an open market. The bid-ask spread at the open may be very wide (market makers are recalibrating after overnight news). Setting a limit sell at mid or 10% below mid is reasonable. If unfilled within 30 minutes, sell at bid to ensure the position closes before the option decays further.

Exception: if the put is deep ITM after a large post-earnings stock decline, there may be no bid at all on a very illiquid option. In this case, convert to shares (exercise the put to sell the stock) if the option market is non-functional. However, this requires actually holding shares, which may not be allowed in the Island Fund (options-only). This is an edge case to flag but not solve today.

**Robinhood-specific:**

Robinhood supports limit orders on options. The interface shows the natural limit order entry. Set limit at mid, submit, let it work. Robinhood does not support "working orders" that auto-adjust -- you'd need to manually update the limit price if not filled.

### The Baxters' Debate

**Calxter:** The savings are real but small per trade. Over time they compound. Worth formalizing the 5-10 minute midpoint attempt.

**Bearxter:** I want to add a caveat: if the thesis is time-sensitive (e.g., we just saw a news event that confirms the thesis and the stock is moving), buy at ask immediately. Don't lose the entry price chasing $5 in savings.

**Prime:** Agreed. The midpoint order is for routine entries where we have time. Opportunistic entries get filled at ask.

**Bullxter:** And on exit, we're selling the morning after earnings. The stock has either moved significantly or it hasn't. If it moved significantly (the option is deeply ITM), there WILL be a bid -- just maybe not a great one. The limit at mid should work within 30 minutes in most cases.

### Recommendation

**RATIFIED: Limit Order Execution Protocol.**

**Entry:**
1. Calculate midpoint: (bid + ask) / 2
2. Place limit buy at midpoint
3. Wait 5-10 minutes
4. If unfilled: raise limit by $0.05 increments, wait 3-5 minutes each
5. If unfilled at (mid + $0.10): buy at ask. Do not let limit order chase consume more than 20 minutes on a routine entry.
6. Exception: if the thesis is time-sensitive (stock moving away from target entry price), skip midpoint and buy at ask immediately.

**Exit:**
1. Set limit sell at midpoint
2. Wait 30 minutes post-open
3. If unfilled: lower limit to bid and fill

**Binder update needed:** Add to TAB 4 (EXIT PROTOCOLS) as "Entry/Exit Execution."

---

## IDEA 16: THE HOLD/NEUTRAL ANALYST PROBLEM IN RULE 3

### The Observation

In batch 6, WBD (Warner Bros. Discovery) at 83rd pct was screened as CONDITIONAL (Rule 3 gate) with the note "streaming bears exist but rally to $27 may have cleared most." This required actually looking up WBD's current analyst ratings to determine how many Sell/Underperform ratings exist.

For calls candidates with MULTIPLE Hold/Neutral ratings, there's a different problem: calls Rule 3 says "maximum 1 Sell/Underperform." But what if a stock has 0 Sells and 15 Holds out of 20 analysts? Zero Sells passes Rule 3 for calls. But 15 Holds means the professional community is far from convinced about the recovery. A stock with 75% of analysts saying "Hold" is NOT the same as a stock with 83% saying "Buy."

DIS had 0 Sells and 83% Buy. WBD might have 0 Sells and 70% Hold. Both pass calls Rule 3. But the quality of the analyst consensus is very different.

### The Analysis

**What does a Hold-heavy consensus mean for calls?**

When 70%+ of analysts are at Hold:
- The professional community is not convinced the stock will outperform
- They're not adding it to client portfolios
- Their price targets (even if above current price) reflect limited conviction
- A Hold-rated analyst's target is their best estimate of fair value, but they don't believe buying it at fair value generates alpha

For a calls thesis to work (stock beats at earnings and re-rates toward analyst targets), we need analysts who WANT to own the stock to be proven right. A Hold analyst who says "target $150" will not change their rating to Buy if the stock reaches $150 -- they'll change their target to $175 and remain at Hold. The re-rating mechanism requires BUY-rated analysts, not Hold-rated ones.

**The Hold ratio as a conviction modifier:**

Proposed: when >50% of covering analysts are at Hold/Neutral, cap calls conviction at 3.5/5 maximum (cannot achieve 4/5). The Hold majority indicates the professional community lacks the conviction that fuels a post-earnings re-rating.

**Testing against our calls plays:**

- ZG: Specific Buy % not confirmed, but strong consensus apparent (we found it as a calls advance with confidence). Likely >60% Buy. Appropriate for 4/5.
- LVS: Similar -- strong Buy consensus for a casino recovery play.
- DIS: 83% Buy, 0 Hold (only Hold/Sell would be the non-Buy). Clear 4/5 candidate without the Hold cap.
- TRMB: The Buy consensus was sufficient for 3.5/5. If >50% were Hold, the 3.5/5 cap was already in place by coincidence.

**The current Rule 3 for calls:** "Max 1 Sell/Underperform." This only screens on the negative end. It doesn't incorporate the positive concentration (% Buy).

**Proposed Rule 3 enhancement for calls:**
- Current minimum: max 1 Sell/Underperform (kept as is)
- New addition: if % Buy (explicitly rated Buy/Outperform/Overweight, NOT including Hold) is < 50% of covering analysts: cap conviction at 3.5/5 maximum.

Note: this is a CONVICTION CAP modifier, not an additional gate that screens out the name. The name still advances if max 1 Sell passes. But if the Buy concentration is low (Hold-heavy), 4/5 or 5/5 conviction is not available.

### The Baxters' Debate

**Prime:** This is a quality-of-consensus metric that belongs in the conviction scoring, not in the binary pass/fail rules. I support adding it as a conviction modifier.

**Bullxter:** What if analysts are stubbornly at Hold but the stock is clearly cheap? Sometimes the market misprices something and analysts are late to upgrade. The Hold-heavy consensus might mean "analysts haven't gotten to the upgrade yet" rather than "analysts don't believe the thesis." DIS at $92 with 70% Hold would still be a strong calls candidate.

**Bearxter:** Bullxter's concern is valid but is exactly what Rule 3 protects against. If analysts are at Hold, they're saying "I don't see enough upside to recommend a Buy." Until they upgrade to Buy, there's no professional buying pressure to support the re-rating post-earnings. The re-rating mechanism requires BUY upgrades after earnings -- which means we need analysts who are close to Buy, not stuck at Hold.

**Calxter:** The EV gate (Idea 2) uses the average BUY analyst target for the central bull scenario. If there are only a few Buy analysts (< 50% of coverage), the "average BUY analyst target" is based on a small minority. This makes the EV estimate less reliable. The conviction cap and the EV calculation are consistent: low Buy concentration → lower EV reliability → lower conviction ceiling.

**Macxter:** No additional input. Consensus quality is an internal framework judgment, not a macro variable.

### Recommendation

**RATIFIED: Add Buy Concentration Conviction Modifier to calls research protocol.**

**Buy Concentration Rule (calls only):**
- After Rule 3 passes (max 1 Sell/Underperform), calculate: % of analysts at Buy/Strong Buy/Outperform/Overweight (explicitly positive ratings).
- If Buy concentration < 50%: Conviction cap is 3.5/5. Document "HOLD-HEAVY CONSENSUS -- conviction capped at 3.5/5."
- If Buy concentration ≥ 50% and ≤ 70%: Standard conviction scoring applies. 4/5 is available.
- If Buy concentration > 70%: No additional cap from this rule. Strong consensus is a positive for conviction scoring.

**DIS check:** 83% Buy. >70%. No cap from this rule. Conviction of 3.5/5 from other constraints (required move, DTE) -- not from the hold concentration.

**Binder update needed:** Add Buy Concentration Rule to TAB 1 (IRON RULES -- CALLS) after Rule 3.

---

## IDEA 17: RESEARCH DOC PEER REVIEW PROTOCOL

### The Observation

We've had several data quality issues in research documents:

1. TRMB June 18 failure: wrote $66.91 price, actual was $49.15. The error was not caught until after the document was shared.
2. DIS August date conflict: two sources showed different dates. We caught this during research but could have missed it.
3. INTC JPMorgan target: we used a stale April 2026 target without fully knowing it was stale until mid-research.

The five-Baxter structure is designed to provide independent analysis before a consensus meeting. But all five Baxters are analyzing the same data. If the data is wrong, all five Baxters have wrong inputs. There's no independent data verification step.

### The Analysis

**The gap:**

The current process:
1. Screen identifies advance
2. Chain pulled
3. Five Baxters run independently (but from same data)
4. Five Baxters meet
5. Verdict

The gap: "same data" means a single data point error propagates through all five Baxters unchecked.

The TRMB error: Baxter had the wrong price ($66.91 vs $49.15). Prime checked the price against the screen estimate. But the screen estimate was also wrong. Five independent analyses of a wrong starting price won't catch the error.

**Proposed: Data Verification Layer**

Before the five Baxters analyze, verify key data points from a SECOND source:

| Data point | Primary source | Verification source |
|---|---|---|
| Current stock price | Robinhood (fetch_price.py) | TipRanks or Yahoo Finance |
| 52-week high/low | Robinhood | Yahoo Finance |
| Earnings date | TipRanks | Company IR page or EarningsWhispers |
| Analyst ratings count | TipRanks | Stockanalysis.com or Wall Street Horizon |
| Highest/lowest analyst target | TipRanks | Marketbeat or consensus estimate source |
| Option chain (ask prices) | Robinhood | None (Robinhood is the execution platform, no substitute needed) |

If primary and verification sources agree: proceed.
If they conflict: use the more conservative for Rule purposes, flag the conflict in the research doc.

**The cost:**

2-3 additional lookups per research doc. Each lookup takes 1-2 minutes. For a research doc that takes 30-60 minutes to write, 5 minutes of data verification is a 10% overhead cost. Very acceptable given the alternative (sending a corrupted research doc to correspondence or acting on wrong data).

**Calxter's note:**

The option chain (Rule 5 and chain section) doesn't need cross-verification because the Robinhood chain IS the execution platform. Checking another source for option prices would show different data (different broker's market). The chain data from Robinhood is authoritative for our execution.

### The Baxters' Debate

**Prime:** This is a process addition, not a rule change. Straightforward.

**Bearxter:** I want to add: if a data conflict is found between sources (like DIS's Aug 4 vs Aug 12), the research doc must explicitly note the conflict. "Earnings date confirmed: Aug 12, 2026 per TipRanks (primary) -- note: one source showed Aug 4, TipRanks overridden as more recent/specific confirmation." Future readers need to know the verification was performed and what was found.

**Calxter:** Document the verification sources in the Prime's Review section of each research doc. Makes the doc auditable.

**Bullxter:** Isn't this already what TipRanks is for? We use TipRanks for analyst ratings.

**Prime:** Yes, for analyst ratings. The enhancement is adding the CROSS-VERIFICATION step for price data (which we get from Robinhood) and earnings dates (which we get from news sources). We haven't been systematically verifying price data from Robinhood against another source.

### Recommendation

**RATIFIED: Add Data Verification Layer to research doc process.**

**Verification checklist (run before starting the five Baxters analysis):**

1. Stock price: confirm Robinhood price within 2% of a second source (Yahoo Finance or TipRanks)
2. 52-week range: confirm high/low within 5% of a second source
3. Earnings date: two independent sources agree (see Idea 5 protocol)
4. Analyst ratings: TipRanks count vs Stockanalysis.com count within 2 analysts
5. Key analyst targets: highest Sell target (puts) or lowest Buy target (calls) confirmed from at least one source

If any check fails: flag the conflict, use the conservative value, note in research doc.

**Research doc template update:** Add "DATA VERIFICATION" section to Prime's Review, immediately after the data section header, with one line per verified data point.

**Binder update needed:** Add Data Verification as a mandatory pre-step to research doc writing. "All data points used in Rule 4 and the chain section must be verified from a second source before the five Baxters begin independent analysis."

---

## IDEA 18: WHEN TO EXPAND THE FUND

### The Observation

The Island Fund started at $500. Michael's birthday money plus the profits from early plays. The fund has grown to $1,078 total ($614 in reserve, $464 in open positions at cost).

The question: at what point do we move to 2 contracts as the "minimum"? Or increase position sizes? Or start taking plays that previously were too expensive for the fund?

Currently:
- 1 contract minimum is enforced (can't buy 0.5 contracts)
- Sizing is percentage of reserve (6-10% for 3.5/5, 12-16% for 4/5)
- The 1-contract minimum often overruns the sizing budget for 3.5/5 plays

At $614 reserve: 3.5/5 sizing = 6-10% = $37-$61. But 1 contract of most options costs $70-130. We're systematically oversizing relative to conviction.

At what reserve level does 1 contract of a 3.5/5 play fit within the 6-10% budget?
- If 1 contract costs $85 (DIS): $85 / 6% = $1,417 reserve needed to be at the bottom of 3.5/5 range
- If 1 contract costs $100: $100 / 6% = $1,667 reserve needed

**The math is stark:** We need approximately $1,400-1,700 in reserve for 1 contract at the BOTTOM of the 3.5/5 range to be correct sizing. Currently at $614, we're oversizing on almost every trade.

### The Analysis

**Why we accept the sizing override:**

The minimum 1 contract exception was explicit in the binder. We acknowledged that at $500-$1,000 fund size, the minimum contract constraint will systematically produce position sizes above the correct percentage. The exception reads: "Accept as structural minimum contract constraint" -- same as how we rationalized the DIS $85 at 13.8% vs the 3.5/5 ceiling of 10%.

**The compound problem:**

If every 3.5/5 trade is 13-15% of reserve (instead of 6-8%), we're running each trade at nearly double the intended risk. The 3.5/5 sizing is designed to protect against moderate uncertainty -- we're betting twice as much as intended on plays with meaningful uncertainty.

**Two paths to resolution:**

Path 1: Accept the current sizing and update the binder to reflect that at sub-$2,000 reserve levels, 1 contract is always the de-facto minimum and the percentage cap is aspirational, not binding.

Path 2: Only enter 3.5/5 plays when the fund reaches the level where 1 contract fits within the 10% ceiling. At $1,000 in reserve, a $100 option = 10% = bottom of 4/5 range. At $1,500, a $100 option = 6.7% = middle of 3.5/5 range. So the "correct sizing" threshold is approximately $1,500 in reserve before taking 3.5/5 plays.

**Path 3 (hybrid):** Allow 3.5/5 plays at the minimum 1 contract regardless of fund size, but document the sizing override and limit the NUMBER of simultaneous 3.5/5 plays. If we can't size them correctly individually, we can at least limit how many we have open simultaneously. Cap at 2 open 3.5/5 positions until reserve exceeds $1,500.

### The Baxters' Debate

**Calxter:** Path 2 is mathematically clean. Path 3 is pragmatic. Path 1 is accepting an error as a feature.

**Bullxter:** Path 2 means we don't trade for months while waiting for the reserve to reach $1,500. We're at $614 reserve now. If we compound the existing positions at the current rate, we'll cross $1,500 in roughly 4-6 months assuming continued success. That's 4-6 months with no 3.5/5 plays.

**Bearxter:** The closed plays (DKNG +$251 is the biggest) have already shown the fund can grow quickly on 4/5+ plays. Maybe the answer is to hold 3.5/5 plays to a hard maximum of 2 simultaneously and only pursue 4/5+ plays as the primary engine.

**Prime:** Path 3 hybrid, with the additional constraint that 3.5/5 plays should only be entered when their specific catalyst is particularly high-quality (clear earnings setup, confirmed date, clean Rule 4). Not "borderline 3.5/5 barely cleared" -- but "solid setup that happens to have one elevated-risk element keeping it below 4/5."

**Macxter:** The reserve growth depends on the macro environment. In a sustained bull market for consumer tech (our main plays), the fund compounds faster. In a risk-off environment where all our consumer plays stall, it compounds slower. The $1,500 threshold is 2.4x the current reserve -- achievable in 3-6 months if current plays resolve positively.

### Recommendation

**RATIFIED: Fund sizing thresholds defined.**

**Sizing protocol by reserve level:**

| Reserve Level | 3.5/5 sizing | 4/5 sizing | Notes |
|---|---|---|---|
| < $1,000 | 1 contract (accept override) | 1-2 contracts (accept override) | Minimum contract exception in effect. Cap at 2 open 3.5/5 positions. |
| $1,000-$2,000 | 1-2 contracts (checking against 6-10% budget) | 1-2 contracts (12-16% budget often requires 1) | Getting closer to correct sizing. |
| $2,000-$5,000 | Standard sizing (% of reserve, not contract count) | Standard sizing | First tier where percentage sizing is mechanically achievable. |
| > $5,000 | Standard sizing | Standard sizing | Full framework applies cleanly. |

**Immediate action:**
- Current reserve $614: in "< $1,000" tier
- Apply 2-open-3.5/5-positions cap immediately
- Current 3.5/5 positions: DIS (pending, if entered) + LYFT + possibly TRMB if scored 3.5
- Count before entering DIS: LYFT (3.5/5), TRMB (3.5/5) = 2 already open. DIS would be the 3rd.
- Per the 2-open cap: DIS would exceed the limit. This is a new constraint.

However: this rule wasn't in place when LYFT and TRMB were entered. Retroactive application would create the constraint immediately. Prime's judgment: apply the cap to NEW entries from this point forward. LYFT and TRMB were entered under the prior system. DIS, if entered, would be the 3rd 3.5/5 -- evaluate against the new cap.

**Binder update needed:** Add Sizing Protocol by Reserve Level to TAB 3 (POSITION SIZING).

---

## IDEA 19: FORMALIZING SEE-THROUGH RISK

### The Observation

The binder has a standing decision: "See-Through Risk: The market may price past a good earnings quarter because it is already discounting the forward environment the quarter does not capture." This is in TAB 6 (STANDING DECISIONS) but is stated as a principle without a formal protocol.

During the NKE analysis (and in the BSX situation), see-through risk was relevant: NKE could report a good Q4 but the market might already be pricing in the Q1 recovery and looking at Q2 guidance. If Q2 guidance is weak (because the China recovery story is "already in the stock"), the Q4 beat doesn't move the price in our direction.

See-through risk is also relevant to INTC: Intel could beat Q2 estimates but the market is already pricing in the 3-year foundry success narrative. A Q2 beat that doesn't meaningfully advance the 3-year story might not move the stock.

The question: when does see-through risk raise enough to downgrade conviction?

### The Analysis

**When does the market see through a quarter?**

The market "sees through" a quarter when:
1. The specific quarter's result is already priced in (consensus estimates incorporate the beat because multiple data signals have already shown the outcome)
2. The market is focused on the NEXT quarter or next year, not the current report
3. The catalyst (the earnings print) doesn't change the NARRATIVE, only confirms what was expected

**Examples:**

- DKNG: the World Cup bookings would be visible in real-time data (betting exchanges, daily GGR reports). By earnings day, the market might already have priced in the World Cup upside. See-through risk was low for DKNG because the exact Q2 bookings number wasn't visible before earnings -- it required the company to report.

- NKE: the China recovery was visible in channel checks and import data. Some analysts were already incorporating the recovery. See-through risk was real -- if the recovery was "known" before earnings, the earnings print just confirmed consensus and didn't move the stock.

- INTC: the AI narrative and foundry story are long-term. Q2 results are one quarter of a 3-year thesis. See-through risk is HIGH -- even a strong Q2 beat might not move the stock if the market is pricing in years 2 and 3 of the foundry plan.

**How to evaluate see-through risk:**

1. **Analyst estimate revision direction:** If estimates have been rising in the 30 days before earnings, the "beat" is already being anticipated. The upward revision is the market saying "we think they'll beat." A stock with rising estimates heading into earnings has higher see-through risk than one with flat estimates.

2. **Stock performance into earnings:** If the stock is already up 15% in the 30 days before earnings, the market is pricing in a beat. A beat that takes the stock from -5% to +10% of month-ago price is different from a beat that takes it from +15% to +18%. The former moves the narrative; the latter is already embedded.

3. **Guidance specificity:** Stocks with highly visible guidance metrics (subscriber counts in real-time, booking volumes, transaction data) have higher see-through risk because the market can estimate the quarter before the report. Stocks with opaque guidance (specialty manufacturing, project-based revenue) have lower see-through risk because the actual result is genuinely unknown.

**Scoring see-through risk:**

Low (0): Guidance is opaque, estimates have been flat or declining, stock has underperformed in 30 days before earnings.
Medium (1): Guidance has some visible metrics, estimates slightly rising, stock flat to up 5-10%.
High (2): Guidance widely tracked in real-time, estimates rising 15%+, stock up >15% into earnings.

**Conviction impact:**
- Low see-through: no impact on conviction
- Medium see-through: note in research doc, no automatic cap
- High see-through: cap conviction at 3.5/5 (market may already see past the quarter)

### The Baxters' Debate

**Prime:** This is Bearxter's domain -- identifying risks that make the thesis fail even when the rules are satisfied.

**Bearxter:** See-through risk is the most underrated risk in our framework. The Iron Rules check the SETUP correctly but don't check whether the market has already PRICED the catalyst. A stock with perfect setup (bottom 25% of range, 0 Sells, strong earnings) can still fail to move if the catalyst is anticipated. The conviction cap is the right tool.

**Bullxter:** Most of our calls plays are on beaten-down stocks where the recovery HASN'T been priced in yet (by definition -- if the stock is at 52-week lows, the market has given up on it). See-through risk is more relevant for puts (where a stock at 52-week highs might already be pricing in perfection). I'd argue see-through risk is a more important constraint for puts than for calls.

**Calxter:** Bullxter makes a good point. A stock at the bottom of its range with falling estimates and underperformance heading into earnings is a LOW see-through setup -- which is exactly what the calls framework selects for. See-through risk is more likely to appear on puts setups, where the stock has been rallying into the quarter.

**Prime:** Add see-through scoring to BOTH directions, but note that calls setups naturally tend toward low see-through and puts setups naturally tend toward medium/high.

### Recommendation

**RATIFIED: See-Through Risk formally scored in research docs.**

**See-Through Risk Score (add to each research doc, in Calxter's section):**

| Factor | Low (0 pts) | Medium (1 pt) | High (2 pts) |
|--------|-------------|---------------|--------------|
| Estimate revision (30d pre-earnings) | Flat or down | Up 0-10% | Up >10% |
| Stock performance (30d pre-earnings) | Down or flat | Up 5-15% | Up >15% |
| Guidance visibility | Opaque (no real-time proxies) | Some visible metrics | Highly visible in real-time data |

**Total score and conviction impact:**
- 0-1 pts: Low see-through. No conviction cap from this factor.
- 2-3 pts: Medium see-through. Note in research doc. No automatic cap.
- 4-6 pts: High see-through. Conviction cap: 3.5/5 maximum.

**For calls specifically:** Low see-through is structurally built into the framework (bottom-of-range stocks rarely have rising estimates heading into earnings). Scoring should still be performed -- a calls candidate with unexpected see-through (stock has quietly risen 15% while still in bottom 25% of range) should be flagged.

**Binder update needed:** Upgrade see-through risk from a "standing decision" to a formal scoring metric in the research doc template.

---

## IDEA 20: THE PUTS BACK-TEST PROTOCOL

### The Observation

The binder contains this standing decision: "Puts system requires back-test before first live entry. Run every name in passes.md through the inverted Iron Rules. Document what would have been entered and what happened. The purpose is calibration, not cherry-picking."

As of June 28, 2026: no back-test has been run. The puts system was ratified June 18. We've been screening puts candidates (Batches 4-6) and finding plays (INTC, GE as conditional, DASH, TSLA, ABNB) but have not entered any puts plays.

The back-test is a prerequisite. But we have no formal protocol for how to run it.

### The Analysis

**What the back-test needs to accomplish:**

1. For each name in passes.md that would have qualified as a puts advance (top quartile range, 2+ Sells, earnings catalyst), identify the specific put that would have been entered.

2. Determine the entry date (what date would we have entered, assuming we saw the play at the time of the original screen).

3. Determine the actual outcome: what price did the underlying reach at or before the option expiry? Did the put expire in the money?

4. Calculate P&L: did the trade win or lose? By how much?

5. Check if the Iron Rules would have correctly flagged or advanced the play.

**What the back-test is NOT:**
- Cherry-picking the winners. The back-test must include every qualifying name, including ones that failed.
- Retroactive rule-fitting. If a play fails in the back-test, we don't add a new rule specifically to exclude that play pattern.

**Historical puts candidates to back-test (from passes.md and batch logs):**

Looking at names that have been screened as puts candidates since the puts system was ratified June 18:

From batch 4 (Jun 22) and batch 5 (Jun 27):
- TSLA: $405.04, 97th pct, earnings pending, 5-10+ Sells. Would have been advanced. Q2 delivery data due Jul 1.
- DASH: ~$172, 83rd pct, 2-4 Sells suspected.
- ABNB: ~$139, 87th pct, pending.
- RCL: ~$316.40, 94th pct, pending.

From batch 6 (Jun 28):
- INTC: 89th pct, 5 Sells. EV gate failed -- screened out.
- GE: 92nd pct, 2 negative ratings. Rule 4 conditional.

The back-test protocol should focus on names that are already CLOSED (meaning the earnings catalyst has already fired, so we can see what actually happened). As of June 28, the candidates above mostly haven't had earnings yet.

**Historical names from BEFORE the puts system was ratified (Jun 18):**

Were there names screened before June 18 that would have qualified under the puts rules? Looking at batch 1-3 (run in weeks 1-3): those batches focused on calls candidates. The unified screen (which evaluates both directions) wasn't implemented until batch 5. So back-testing puts plays from batches 1-3 would require retroactively applying the puts rules to names that were in the top quartile of their range.

**Names from weeks 1-3 that were near 52-week highs:** These would have been flagged as "not our setup" for calls, but could now be evaluated as puts candidates retroactively. Examples: PENN was 89th pct (screened out Jun 1 as "wrong position for calls"). Under puts rules, PENN at 89th pct would advance if Rule 3 passed. PENN's earnings were August 6, 2026 -- still upcoming. Not historical yet.

**The back-test problem:** Most of our potential puts candidates haven't had their earnings catalysts yet. We're in mid-summer 2026. Q2 earnings season is July-August. The puts plays (all targeting Q2 earnings) won't have resolvable outcomes until July-August.

**Resolution:** The back-test as specified (testing historical outcomes) cannot be run on Q2 plays until Q2 earnings occur. The correct action:

1. For TSLA, DASH, ABNB, RCL: track what happens at their Q2 earnings (Jul-Aug 2026). Record the hypothetical trade outcome.
2. For pre-June 18 names: there are very few puts candidates in the batch 1-4 logs because the unified screen wasn't implemented. The back-test data is thin.
3. Proposed: run the back-test AFTER Q2 earnings season (late August 2026). At that point, we'll have 5-8 hypothetical puts plays with known outcomes.

### The Baxters' Debate

**Prime:** The back-test cannot be meaningfully run until after Q2 earnings. This is a timing constraint, not a process failure. The standing decision ("back-test required before first live entry") means we cannot enter puts until we have back-test data. All current puts candidates (TSLA, DASH, ABNB, RCL) cannot be entered until the back-test runs.

**Bearxter:** This is exactly the protection I specified when we ratified the puts system. We don't have enough history to trust the rules yet. The back-test is how we earn that trust.

**Bullxter:** If TSLA has Q2 delivery numbers out July 1-2, and the delivery miss is significant, and the puts thesis is clear -- we're going to watch a great trade pass because we can't do the back-test? That's painful.

**Prime:** Yes. That's the standing decision. Three closed puts plays required before full conviction is available. The back-test is how we get there efficiently. Alternative: we can watch TSLA without entering, record the hypothetical trade (entry price, exit price, P&L), and count that as a data point toward the back-test. If TSLA, DASH, ABNB all have clean hypothetical back-test outcomes by August, we'd have 3 data points and could enter the next clean puts setup.

**Calxter:** The hypothetical tracking is the right compromise. We track the plays as if we had entered, record the outcomes, and use those outcomes to validate (or invalidate) the Iron Rules for puts. The back-test requirement doesn't require us to ENTER the plays -- just to OBSERVE and RECORD them.

### Recommendation

**RATIFIED: Puts Back-Test Protocol defined.**

**Back-test mechanism:**

1. For each name identified as a puts advance through the Iron Rules (and EV gate), document:
   - Entry date and stock price
   - The specific put that would have been entered (strike, expiry, ask, at-risk)
   - Breakeven price
   - The reasoning (which specific element of the thesis)

2. At earnings resolution, record:
   - Stock price at earnings close
   - Stock price at morning-after-earnings open
   - P&L on the hypothetical entry
   - Whether Rule 4 was breached during the hold period

3. After 3 resolved back-test observations: evaluate. If 2+ of 3 back-tests show positive outcomes: enables first live puts entry (subject to the standing conviction cap of 4/5 maximum until 3 LIVE plays close).

**Current back-test queue:**
- TSLA: hypothetical entry tracked in `research_TSLA.md`. Resolution: Q2 delivery numbers Jul 1-2, earnings ~late July.
- DASH: hypothetical tracked, pending Rule 3/4 confirmation. Resolution: Q2 earnings Jul-Aug.
- ABNB: hypothetical tracked, pending Rule 3 confirmation. Resolution: Aug 4.

**Binder update needed:** Add Back-Test Protocol to STANDING DECISIONS, replacing the current vague instruction with the specific mechanism above.

---

## IDEA 21: THE FIELD BRIEF FORMAT -- STANDARDIZATION

### The Observation

The field brief (`field_brief_2026-06-22.md`) is a weekly document that orients the Baxters before a screening session. Looking at the existing brief, it contains:
- Fund state (reserve, positions)
- Open thesis updates
- Macro context for the week
- What to screen next

The brief is created manually. Its format varies (it was written once and hasn't been updated since June 22 -- now 6 days old). As we enter more weeks, the field brief needs a standard format that's consistently updated.

### The Analysis

**What should every field brief contain:**

1. **Fund state (always current):**
   - Reserve balance
   - Open positions with current value (mark-to-market, not just cost basis)
   - Total fund value (reserve + open positions at current prices)
   - Week-to-date performance

2. **Open positions summary:**
   - Each position: entry date, strike, expiry, current value, P&L to date, thesis status
   - "Thesis intact" or "thesis shifting" flag for each

3. **Pending actions:**
   - Research docs written but not yet pitched (DIS, for example)
   - Conditional advances needing data (GE Rule 4, TSLA delivery numbers)
   - Watch items with known trigger dates (HUM re-check Monday, TSLA July 1)

4. **Upcoming catalyst calendar:**
   - All earnings dates for open positions in the next 30 days
   - Macro events (Fed meetings, economic data) that affect open positions
   - Option expiry dates

5. **Screening direction for the week:**
   - Which sectors haven't been screened yet
   - Which ranges to focus on (has the market moved such that previously MID-OUT names are now in puts/calls zones?)

6. **Macro context:**
   - Rate environment
   - Sector rotation in effect
   - Any macro risk that cuts across multiple positions

**Update schedule:**

Field brief updated every Saturday for the coming week. The brief is valid for one week and replaced the following Saturday.

**Format improvement:**

Current field brief is narrative-heavy. The standard format should be table-heavy with a brief narrative summary at the top. Tables are faster to scan, easier to update, and less subject to information being buried in paragraphs.

### The Baxters' Debate

**Prime:** Format standardization is a maintenance task. Prioritize it but don't block screening on it. The field brief is a convenience tool, not a prerequisite.

**Direxter:** (The narrative director -- the one who manages the story and public presence.) This is my domain. The field brief is the document Baxter reads before walking into the room. If it's not updated weekly, Michael doesn't get a current picture. I want the Saturday update to be mandatory. Not optional.

**Bearxter:** Agreed. If the brief is 6 days old, the fund state section is wrong. Reserve moves, positions mark-to-market differently. The brief should never be more than 7 days old.

**Calxter:** Add a mark-to-market calculation note: the positions in the brief should show current option value (using fetch_puts_chain.py or fetch_price.py to get the current option ask), not cost basis. That's what actually matters for decision-making.

### Recommendation

**RATIFIED: Field Brief standardized and weekly update schedule established.**

**Standard field brief sections (in order):**

1. FUND STATE: Reserve, open position current values, total fund value
2. OPEN POSITION SUMMARY: Table with cost basis, current value, P&L, thesis flag, days to expiry
3. PENDING ACTIONS: Undecided pitches, conditional advances, watch items
4. CATALYST CALENDAR: Next 30 days of earnings + macro events
5. SCREENING PLAN: What to screen this week and why
6. MACRO CONTEXT: Rate environment, sector rotation, cross-position risks

**Update schedule:** Every Saturday. Brief is valid for one week.

**Action needed:** Update `field_brief_2026-06-22.md` to current state (June 28) and rename to `field_brief_2026-06-28.md`. Create a template file at `Baxter/field_brief_template.md`.

**Binder update needed:** Add "Field Brief" as a new standing document referenced in STANDING DECISIONS.

---

## SUMMARY: IMPROVEMENT ROADMAP

*21 ideas analyzed as of June 28, 2026. Status summary:*

| # | Idea | Status | Binder Update? | Script Update? | File Update? |
|---|------|--------|---------------|----------------|--------------|
| 1 | Stock Price Pre-Screen (R5 structural flag) | RATIFIED | Yes (Step 0.5) | No | No |
| 2 | EV Formal Gate (Step 4.5) | RATIFIED | Yes (both Rules) | No | research_template.md |
| 3 | Pre-Earnings Dip Entry Protocol | RATIFIED | Yes (TAB 4.5) | No | No |
| 4 | Short Interest Enhancement | PROVISIONAL | Yes (calls SI note) | No | passes.md |
| 5 | Earnings Date Verification | RATIFIED | No (execution) | No | research_template.md |
| 6 | Rule 4 Rating Direction Clarification | RATIFIED | Yes (both Rules) | No | No |
| 7 | Puts Exit Protocol | RATIFIED | Yes (TAB 4) | No | No |
| 8 | Post-IPO Puts Framework | PROVISIONAL | Yes (Standing Dec.) | No | passes.md |
| 9 | 5/5 Conviction Criteria | RATIFIED | Yes (TAB 3) | No | No |
| 10 | Screen Index (screen_index.md) | RATIFIED | No | No | screen_index.md |
| 11 | Option Liquidity Gate | RATIFIED | Yes (both Rules) | Yes (chain script) | No |
| 12 | Analyst Target Freshness Rule | RATIFIED | Yes (Rule 4) | No | No |
| 13 | Option Entry Timing Guidelines | RATIFIED | Yes (TAB 4) | No | No |
| 14 | Sector Correlated Cap Tracker | RATIFIED | Yes (TAB 3) | No | positions.md |
| 15 | Limit Order Execution Protocol | RATIFIED | Yes (TAB 4) | No | No |
| 16 | Hold-Heavy Consensus Cap (calls) | RATIFIED | Yes (TAB 1) | No | No |
| 17 | Research Doc Peer Review / Verification | RATIFIED | Yes (both Rules) | No | research_template.md |
| 18 | Fund Sizing Thresholds by Reserve Level | RATIFIED | Yes (TAB 3) | No | No |
| 19 | See-Through Risk Formal Scoring | RATIFIED | Yes (both Rules) | No | research_template.md |
| 20 | Puts Back-Test Protocol | RATIFIED | Yes (Standing Dec.) | No | No |
| 21 | Field Brief Standardization | RATIFIED | Yes (Standing Dec.) | No | field_brief_template.md |

**Priority implementation order (by leverage per effort):**
1. EV Gate (Idea 2) -- prevents INTC-category errors; research_template.md update
2. Rule 4 Rating Clarification (Idea 6) -- prevents data errors on research
3. Liquidity Gate + chain script update (Idea 11) -- prevents STZ-category entry failures
4. Correlated Cap Tracker in positions.md (Idea 14) -- prevents UBER+LYFT-category overconcentration
5. Screen Index creation (Idea 10) -- prevents rescreening already-evaluated names

---

## IDEA 22: SIMULTANEOUS ENTRY DISCIPLINE

### The Observation

On June 18-19, multiple entries were made in a compressed window: UBER, LYFT, and possibly others (CELH, MCD were listed as "pending entries Jun 19"). The correlated cap analysis (Idea 14) showed that UBER + LYFT alone exceeded the 35% consumer/rideshare cap. This likely happened because the entries were processed in sequence without checking the cap between entries.

The question: should we ever enter two new positions in the same session?

### The Analysis

**When simultaneous entries make sense:**

- Two uncorrelated positions that both independently meet all five rules
- The correlated cap is not violated when both are added together
- Each has its own specific catalyst date (different earnings dates, different sectors)
- The reserve comfortably supports both without overweighting

**When simultaneous entries are problematic:**

- Same sector or macro driver (UBER + LYFT = same rideshare driver)
- Both positions use the same option expiry (both at risk simultaneously)
- Entering multiple 3.5/5 plays pushes past the 2-open cap
- Reserve is thin enough that the combined entry constitutes >35% of reserve

**The discipline:**

Enter one position. Update positions.md. Calculate reserve. Calculate correlated cap. Then evaluate the second position with the updated numbers.

Never pre-approve two entries and execute them back-to-back without the update step in between.

This is primarily a process discipline, not a rule change. The rules (correlated cap, sizing) already prevent the problem if applied sequentially.

**Exception:** If both positions are targeting the SAME earnings event (e.g., entering both a calls and a puts position on the same stock as an earnings strangle), they should be evaluated together because they're truly a single compound trade.

### The Baxters' Debate

**Prime:** Process discipline. No new rules needed. Just: after each entry, update positions.md and check the cap before the next.

**Calxter:** The math check is the key. If reserve is $614 and we enter UBER at $130 (reserve: $484), then evaluate LYFT with $484 as the denominator. $180/$484 = 37.2% -- still over the 35% cap even on the reduced reserve. But the point is: the check would have caught it.

**Bearxter:** This is the difference between "we know the rules" and "we apply the rules." The system_improvements doc should note this as a process failure, not a rule gap. The rules existed. They weren't applied correctly.

### Recommendation

**RATIFIED: Sequential entry protocol -- update and check between each entry.**

**Entry checklist (sequential, not batch):**
1. Write research doc for Position A
2. Confirm entry with Patrick
3. Enter Position A in Robinhood
4. Update positions.md with Position A
5. Recalculate reserve and correlated cap
6. Only then evaluate Position B, using updated numbers

**If two positions will exceed the correlated cap together:** Choose one. Do not enter both. Apply the higher-conviction position first and defer the lower-conviction one until room in the cap opens.

---

## IDEA 23: OPTION EXPIRY SELECTION FRAMEWORK

### The Observation

When we have a valid calls or puts setup, we select an option expiry. The binder says "confirmed earnings before expiry" (Rule 2) but doesn't specify HOW FAR before expiry the earnings should be. We've had:

- DKNG: earnings Aug 5, expiry Jul 2 (pre-earnings -- the catalyst was World Cup, not earnings, per BOTZ lesson)
- TRMB: earnings Jul 30, expiry Aug 21 (22 days post-earnings runway)
- UBER: earnings Aug 4, expiry Aug 21 (17 days post-earnings runway)
- LYFT: earnings Aug 12, expiry Aug 21 (9 days post-earnings runway)
- DIS: earnings Aug 12, expiry Aug 21 (9 days post-earnings runway)

The pattern: the minimum viable post-earnings runway is 7-9 days (LYFT, DIS). The preferred runway is 14-22 days (UBER, TRMB). The July weekly expirations are available but most expire before August earnings.

Is 9 days of post-earnings runway enough? Is 22 days too much (paying for time we don't need)?

### The Analysis

**Post-earnings runway considerations:**

After earnings, the stock moves on the catalyst. If the move is in our direction, the option gains intrinsic value. If we sell at the open the morning after earnings (standard exit protocol), we need exactly 1 day of post-earnings runway.

So why does runway matter?

1. **The option must STILL EXIST the morning after earnings.** If earnings are Aug 12 and expiry is Aug 14, we have 2 days. The option exists. We sell at the Aug 13 open. Fine.

2. **Extrinsic value retention.** An option with 20 days remaining has more extrinsic value than an option with 9 days remaining (theta curve). If the stock moves slightly in our direction but not past breakeven, we can still recover some premium from remaining extrinsic value. With 9 days remaining at expiry, almost all extrinsic value is gone.

3. **Maximum hold flexibility.** If the earnings beat is exceptional and we want to hold for a secondary re-rating (which Bearxter warns against, but which Bullxter advocates), longer post-earnings runway allows it. This is NOT our standard exit protocol, but longer runway gives us the option.

4. **The cost of longer runway:** More theta decay during the hold period (before earnings). If we enter at 45 DTE and earnings are at 9 days before expiry (36 DTE), we're holding for 27 days of theta decay before the catalyst. At $0.85 premium, daily theta might be $0.008/day × 27 days = $0.22 in time decay before the catalyst fires. That's 26% of the premium lost to theta before we even need the option.

**Optimal structure:**

- Minimum post-earnings runway: 7 days (enough to sell at the open morning after)
- Preferred post-earnings runway: 10-21 days (allows for the stock to settle post-catalyst, gives some flexibility for extrinsic value recovery if near the money)
- Maximum preferred: 28 days (any longer and you're holding unnecessarily past when the thesis resolves)

- Minimum DTE at entry: 21 days for puts (Rule 2). For calls, no minimum specified -- but practically, the earnings need to be before expiry, so minimum is: days from today to earnings + 7 days.
- Preferred DTE at entry: 30-45 days

**The LYFT/DIS 9-day problem:**

LYFT and DIS both have Aug 12 earnings and Aug 21 expiry = 9 days of post-earnings runway. This is technically viable (7-day minimum is met), but:
- 9 days means we sell at the Aug 13 open
- If we don't sell at Aug 13 open (miss the bell), we have 8 more days until expiry -- still time to sell, but theta is decaying fast
- No flexibility for secondary thesis

9-day runway is acceptable for clean setups (Rule 4 has good margin, the thesis is specific). It's less comfortable for marginal setups.

**What's the next available expiry after Aug 21?**

For August 2026: the next standard expiry would be Sep 18 (the monthly). That's the next monthly after Aug 21. A Sep 18 expiry for LYFT/DIS would give 37 days of post-earnings runway. But Sep 18 options may not have been available when the plays were structured, or they may be priced differently.

### The Baxters' Debate

**Calxter:** The 9-day minimum vs 21-day preferred is a theta tradeoff. If we enter at 45 DTE on a stock with Aug 12 earnings and Aug 21 expiry:
- We hold for 36 days before the catalyst
- We hold for 9 days after
- Theta decays most aggressively in the final 30 days
- Most of the time we hold, theta is accelerating

The Sep 18 option would:
- Hold 77 days to earnings, 37 days after
- Pay more in absolute premium (longer duration = more expensive)
- But theta decay before earnings is SLOWER (less time pressure before the catalyst)
- The Sep 18 option is likely more expensive per day of hold due to premium

Net effect: the Aug 21 option is often more efficient when the earnings are in mid-August. You pay less in absolute terms and the post-earnings window is acceptable.

**Bearxter:** 9 days is fine if we commit to the standard exit (sell at open morning after). It only becomes a problem if we start treating the post-earnings runway as "time to recover" from a bad trade. The standard exit eliminates the runway-flexibility problem.

**Prime:** Add the minimum and preferred runway guidelines to the research template. No new rules -- just documentation of the framework.

### Recommendation

**RATIFIED: Option expiry selection guidelines formalized.**

**Expiry selection criteria:**

1. **Earnings must be CONFIRMED before expiry** (Rule 2 -- existing rule)
2. **Minimum post-earnings runway:** 7 calendar days after earnings date to option expiry
3. **Preferred post-earnings runway:** 10-21 calendar days
4. **Preferred DTE at entry:** 30-45 days
5. **When multiple expiries qualify:** select the nearest expiry that meets the 7-day minimum runway AND the preferred DTE at entry. Shorter duration = less theta decay = better for the fund.
6. **Exception for Sept 18 monthly:** If the next available expiry after Aug 21 is Sep 18 (far out), evaluate whether the theta cost of the longer hold justifies the additional runway. Usually, the closer expiry is preferred unless the earnings catalyst is very close to the near-term expiry.

**Add to research doc Prime's Review:** "Option expiry: [EXPIRY DATE]. Post-earnings runway: [DAYS] calendar days. DTE at entry: [DAYS]."

---

## IDEA 24: RULE EXCEPTION DOCUMENTATION

### The Observation

The binder has hard rules. But we've been making exceptions. The major documented exceptions:
- 1 contract minimum when sizing budget is too small (multiple research docs)
- STRETCH options flagged as "one tier above OK but acceptable for high-conviction setups"
- Puts conviction cap at 4/5 until three plays close (standing decision)
- 2-open-3.5/5 cap when reserve < $1,000 (new from Idea 18 today)

These exceptions are documented in various places: the binder, individual research docs, this improvements document. But there's no master exception log.

**Why exceptions matter:**

Each exception is a bet that the exception won't cause harm in this instance. If the same exception causes harm repeatedly, it needs to become a rule change, not a standing exception. If a recurring exception never causes harm, it might become a rule relaxation.

Without a master exception log, exceptions accumulate implicitly. Six months from now, we won't be able to look back and determine: "did STRETCH options cause more losses than OK options? Were the 1-contract oversize exceptions worth it?"

### The Analysis

**Proposed: Exception Log**

Not a separate file -- add a "KNOWN EXCEPTIONS" section to positions.md. Each entry records:
- Which rule was modified
- What the modification was
- The trade it applied to
- The outcome

This creates a data set for future calibration: if STRETCH options consistently underperform OK options, the exception gets tightened. If 1-contract oversizes consistently win at the same rate as properly-sized positions, the minimum contract exception is validated.

**Format:**

```
## KNOWN EXCEPTIONS

| Trade | Rule | Exception | Outcome |
|---|---|---|---|
| TRMB $65C Aug21 | R5: OK threshold | STRETCH ($0.38 ask) | Open |
| DIS $115C Aug21 | Sizing: 3.5/5 budget | 1 contract oversize ($85 vs $61 ceiling) | Open |
| UBER+LYFT | Correlated cap | 50.5% in rideshare vs 35% cap | Open |
```

### The Baxters' Debate

**Prime:** Simple and correct. Track exceptions. Review quarterly.

**Calxter:** Quarterly review should ask: for closed exceptions, what was the win rate and average return vs. the baseline (non-exception plays)? If exceptions underperform the baseline, tighten the exception conditions. If they match, the exception is validated.

**Bearxter:** The correlated cap exception (UBER+LYFT) is the most important one to track. If both close at a loss, the lesson is "correlated cap exists for a reason." If both close at a profit, the lesson is "the cap may be too conservative for our fund size."

### Recommendation

**RATIFIED: Add Known Exceptions section to positions.md.**

Format: as above. Each exception noted at entry, outcome noted at close.

**Quarterly exception review:** After each calendar quarter (or after 10+ closed plays), review the exception log. Calculate:
- Win rate for exception plays vs. non-exception plays
- Average return for exception plays vs. non-exception plays
- Use the data to decide if the exception should become a rule modification

---

*Document last updated: June 28, 2026. Continue adding ideas below as they are identified.*
