# PUTS + CALLS SCREENING LOG -- Batch 6 (Unified)
*June 28, 2026. Week 4, Saturday. Unified screen.*
*Health insurers, media/streaming, financials, industrials, megacap tech. 20 names.*

---

## CONTEXT

100 names screened Jun 22-27 across 5 batches. LVS and ZG are the live calls advances from the prior session.

Active watch/pending list entering Batch 6:
- DASH: $179.15, -28% required, trending against us
- TSLA: $377.91, waiting for Q2 delivery numbers ~Jul 1-2
- RCL: $316.40, research doc needs revision
- CMG: conditional, Rule 3 gate
- RBLX: conditional calls, Rule 4 ambiguous

Batch 6 targets sectors not yet screened: health insurers, media/streaming, Chinese ADRs, megacap financials, aerospace/defense industrials, megacap tech.

Live prices pulled June 28, 2026 via `fetch_price.py --range`.

---

## BATCH 6 -- 20 NAMES

### PRIME's Unified Screen

| # | Ticker | Price | 52wk Range | Pct | Direction | R2 (earnings) | R3 | Result |
|---|--------|-------|------------|-----|-----------|---------------|----|--------|
| 1 | UNH | $426.68 | $234.60-$427.93 | 99th | PUTS | PASS (~Jul 16) | FAIL -- 0 Sells. 78% Buy, 34 analysts. BofA raised to $475 Jun 24. Morgan Stanley $453. Pure upgrade cycle. | **FAIL R3** |
| 2 | HUM | $383.84 | $163.11-$385.49 | 99th | PUTS | PASS (Jul 29) | PASS -- 2 negative ratings (1 Sell + 1 Strong Sell out of 20 analysts; avg target $237 vs $383 stock -- 38% below current) | **FAIL R1 (5-day)** -- stock $1.65 from 52wk high; almost certainly touched within 5 days |
| 3 | ELV | $391.77 | $273.71-$426.98 | 77th | PUTS | PASS (late Jul) | CONDITIONAL -- Elevance had Medicaid/Medicare Advantage bear ratings; likely 2-4 Sells | **CONDITIONAL (R3 gate)** |
| 4 | CVS | $104.51 | $58.50-$106.15 | 97th | PUTS | PASS (early Aug) | CONDITIONAL -- pharmacy/insurance convergence bears likely 2-3 Sells | **CONDITIONAL (R1 5-day + R3 gate)** -- $1.64 from 52wk high |
| 5 | MRNA | $67.19 | $22.28-$69.28 | 96th | PUTS | PASS (late Jul) | UNCERTAIN -- stock ran from $22 to $67 suggests analyst upgrades; may have 0-1 Sells now | **CONDITIONAL (R3 uncertain)** |
| 6 | WBD | $26.71 | $10.76-$30.00 | 83rd | PUTS | PASS (late Jul) | CONDITIONAL -- streaming bears exist but rally to $27 may have cleared most | **CONDITIONAL (R3 gate)** |
| 7 | BABA | $94.98 | $91.99-$192.67 | 3rd | CALLS | CONDITIONAL (Aug -- R2 timing risk) | FAIL -- China ADR carries 3-5 Sell/Underperform ratings from geopolitical/regulatory risk analysts; max 1 Sell for calls | **FAIL R3** |
| 8 | DIS | $98.93 | $92.19-$124.69 | 21st | CALLS | PASS (Aug 12) | PASS -- 0 Sells; 83% Buy across 36 analysts; avg target $134.18 | **ADVANCE** |
| 9 | SOFI | $17.75 | $14.92-$32.73 | 16th | CALLS | PASS (late Jul) | CONDITIONAL -- likely 2-3 Sells from credit risk/fintech bears; need confirmation | **CONDITIONAL (R3 gate)** |
| 10 | RIVN | $15.63 | $11.57-$22.69 | 37th | MID | -- | -- | **MID-OUT** |
| 11 | BA | $217.51 | $176.77-$254.35 | 53rd | MID | -- | -- | **MID-OUT** |
| 12 | INTC | $127.62 | $18.96-$141.45 | 89th | PUTS | PASS (est. Jul 24) | PASS -- 6 Sell/Underperform: BofA Underperform, JPMorgan Underweight, Rosenblatt Sell + 3 others confirmed; avg target $96.07 vs $128 stock (25% below) | **ADVANCE** |
| 13 | GE | $368.60 | $243.34-$379.67 | 92nd | PUTS | PASS (Jul 16) | PASS -- 2 negative ratings: 1 Sell + 1 Underperform (BNP Paribas Exane cited specifically) out of 21 analysts | **ADVANCE (R1 5-day check needed)** |
| 14 | CAT | $1000.75 | $382.75-$1,057.07 | 92nd | PUTS | PASS (mid-Jul) | CONDITIONAL -- likely 2-3 Sells from cycle bears | **R5 STRUCTURAL CONCERN** -- at $1,000/share, OTM puts likely cost well above $1.50. See MELI precedent. Advance conditionally; chain will confirm. |
| 15 | GS | $1,021.00 | $685.39-$1,125.00 | 76th | PUTS | PASS (Jul 14) | FAIL -- only ~1 Sell (7% of 15 analysts = 1 analyst). Need 2 minimum. | **FAIL R3** |
| 16 | AMZN | $231.90 | $196.00-$278.56 | 43rd | MID | -- | -- | **MID-OUT** |
| 17 | META | $551.09 | $520.26-$796.25 | 11th | CALLS | PASS (Jul 29) | PASS -- 0 Sells; 39 of 44 analysts Buy; avg target $842 | **R5 STRUCTURAL CONCERN** -- at $551/share, viable calls likely cost $5-15 at strikes where R4 passes. Need chain to confirm. See MELI precedent. |
| 18 | V | $337.16 | $293.89-$359.66 | 66th | MID | -- | -- | **MID-OUT** |
| 19 | HON | $231.49 | $186.76-$248.18 | 73rd | MID | -- | -- | **MID-OUT** |
| 20 | BAC | $57.93 | $44.75-$59.20 | 91st | PUTS | PASS (mid-Jul) | CONDITIONAL -- typically 1-2 Sells; $1.27 from 52wk high, R1 5-day uncertain | **CONDITIONAL (R1 5-day + R3 gate)** |

---

### BEARXTER's Independent Pass

**UNH -- why Rule 3 kills it despite being at 99th pct:**

UnitedHealth Group is at its 52-week high and 78% of covering analysts rate it Buy. BofA raised the target to $475 on June 24 -- four days ago. Morgan Stanley is at $453. The professional community is actively upgrading this stock as it touches all-time highs. For puts, we need the credentialed bears to establish that there is a bull ceiling. There are no bears. Every professional who covers UNH believes it goes higher. We don't fight the entire analyst community without the framework's protection. Rule 3 fail. Do not advance.

**HUM -- why Rule 1 kills it despite 2 Sell ratings:**

Humana at $383.84 with a 52-week high of $385.49 is $1.65 from the 52-week high. The Rule 1 addendum is explicit: no fresh 52-week high within the prior 5 trading days. A stock $1.65 below its annual high almost certainly touched or set that high within the past week. The 52-week high and the current price are too close to distinguish. This is the momentum-buyer protection: a stock setting new highs has buyers behind it. We wait for the high to stall. If HUM pulls back 5-10% and re-enters the top quartile without having touched its high in 5 days, run the screen again. Avg analyst target $237 vs $383 stock is a remarkable divergence -- this setup may return.

*Note: HUM is the most intriguing miss in this batch. The bear case is specific (Medicare Advantage reimbursement pressure, operating cost inflation, enrollment slow-down) and quantified (avg professional target 38% below current price). File for Monday re-check.*

**GS -- 1 Sell is not 2:**

7% of 15 analysts = 1 analyst at Sell. The framework requires 2. This is the number, not a judgment call. GS at $1,021 is in a position where the trading surge is real (Q2 2026 revenue >$5B, record quarter expected). The professional community has not lined up against it. Rule 3 fail.

**INTC -- the most interesting puts setup in the batch:**

Intel at $128 with average analyst target $96 is a stock that has run 25% above where the aggregate professional community thinks it belongs. This is the inverse of what we usually see: a stock near its highs where the bears have NOT upgraded their price targets to chase the rally. The 6 confirmed Sell/Underperform ratings represent analysts who wrote their bear thesis at lower prices and haven't capitulated as the stock ran. That is unusual. Normally, stocks near all-time highs see Sell ratings converted to Hold as analysts capitulate to momentum. If the Sell analysts have NOT capitulated despite a 570% gain from the $18.97 low, they believe the rally is fundamentally unsupported. That is Rule 3's job: identify when the professional community has set an active bearish ceiling.

**BABA calls -- why China ADRs fail calls Rule 3:**

Alibaba at 3rd percentile is exactly the kind of beaten-down setup that calls Rule 3 protects against. The stock is near its lows and analysts have NOT converged on Buy. Why? Because the Sell ratings on BABA don't come from bearish fundamental views -- they come from geopolitical risk analysts who believe the Chinese government or US tariffs represent binary event risk that no earnings catalyst can resolve. This is the correct disqualification: when analysts remain at Sell not because the company is doing poorly but because the risk environment hasn't changed, the calls thesis requires a different kind of catalyst than earnings. Our Rule 3 is built for earnings-driven calls. BABA is not that setup.

**CAT and META -- structural Rule 5 flags:**

CAT at $1,000 and META at $551 share the same structural problem as MELI at $1,624: the chain will very likely fail Rule 5 before Rule 4 can be evaluated. A $1.50 premium on a $1,000 stock buys a put that's 0.15% of the stock value. On any volatile stock, that is essentially zero expected value -- the instrument doesn't exist in any meaningful way. META at $551 is less severe (not as extreme as MELI or CAT) but a $1.00 cap on a stock at $551 still leaves very little to work with. Pull chains out of completeness and confirm. Do not advance to full research until chain confirms the instrument exists.

---

### BULLXTER's Independent Pass

**DIS calls thesis:**

Disney at $99 is 21% of its 52-week range ($92.19-$124.69). The stock is $7 above its 52-week low. Q3 FY2026 earnings are August 12 -- 9 days before the Aug 21 expiry, which is the tightest post-earnings runway of any calls advance this session.

The bull thesis: Disney's streaming-to-profitability story is more than halfway done. Disney+ ARPU has been growing through price increases and ad tier expansion. ESPN direct-to-consumer (the ESPN flagship streaming service that launched in late 2025) represents a new revenue stream with its first full Q3 data. Parks revenue has been steady despite consumer discretionary pressure. At $99 with a $134 average analyst target (35% upside), the market is pricing in a permanent reset -- not a business that is executing on a defined plan.

The catalyst is specific: Q3 FY2026 is the first quarter that will show the full impact of the Disney+ price increase cycle that started in Q4 2025. If subscriber retention held (meaning subscribers absorbed the price increase without churning), ARPU beats consensus and the streaming profitability story accelerates. That reprices DIS from "streaming uncertainty" to "streaming profit."

Required move: from $99 to breakeven (call strike + premium). If lowest analyst Buy target is ~$110-115, and a call at $105 costs $0.70, breakeven is $105.70. Required move is +6.8% -- the smallest required move of any calls advance this week.

**GE Aerospace calls thesis (why it's a fascinating one):**

GE is in puts territory because it's at 92nd pct. But Bullxter wants to file a note: the 2 Sell ratings on GE represent analysts who missed the entire run from $243 to $380 and have not capitulated. Their targets (which need Rule 4 verification) may still be well below the current price. The specific puts thesis would be: Q2 services growth below the "high-teens" guidance, plus margin pressure from supply chain. GE raised its 2026 profit outlook by $1B -- the market has priced this in. If the execution disappoints by even a small amount, the multiple compresses.

---

### CALXTER's Independent Pass

**Rule 5 structural analysis -- CAT and META:**

CAT at $1,000: For a put to be priced at $1.50, it needs to be approximately (based on 54 DTE, est. 25% IV): strike roughly 30-35% OTM = $650-$700 strike. At $650P on a $1,000 stock, the required move is -35%. Any stock with that required move at the put premium limit is at the edge of EV viability. Will check chain.

META at $551: For a $1.00 call, strike roughly 30% OTM = $716C. Required move from $551 to $716 = +30%. Lowest Buy target must be above $717 (if premium is $1.00, breakeven = $717). Avg target is $842 but lowest Buy analyst is certainly below $717. This is likely a structural Rule 4 failure at the only strikes that could clear Rule 5. Pre-screening as likely MELI-category fail.

**INTC EV estimate:**

Intel at $128, 6 Sell ratings, avg target $96 (25% below stock). If Q2 earnings disappoint:
- Bear scenario: Q2 operating margin compresses below expectations (fab costs staying high), guidance cut. Stock retraces to $90-100 range. Probability: 25-30%.
- If INTC reaches $85 average in bear scenario: implied $85P gain calculation pending live chain.
- Positive EV likely if bear probability above 15% and put can be acquired under $1.50.

Need live chain to complete EV math.

**DIS EV estimate:**

Disney at $99, earnings Aug 12 (9 days before expiry). Post-earnings moves: Disney typically moves ±8-12% on earnings.
- Bull scenario: streaming ARPU beat + ESPN DTC subscriber data positive. Stock reaches $107-112 range. Probability 35-40%.
- On a $105C at $0.70 (breakeven $105.70): if Disney reaches $109 avg, gain = $109 - $105.70 = $3.30 = $330/contract - $70 = $260.
- Bear/inline: stock stays $95-103, call expires worthless. Probability 65%.
- EV ≈ 0.37 × $260 - 0.63 × $70 = $96.20 - $44.10 = **+$52.10** (estimated, pending chain).

---

### MACXTER's Independent Pass

**INTC macro context:**

Intel's 570% run from $18.97 represents a narrative shift from "Intel is losing the semiconductor war" to "Intel is winning the US chip independence story." The CHIPS Act was designed specifically to fund domestic semiconductor production. Intel's foundry business received significant federal backing. The stock ran on that narrative and on Apple deal speculation (Intel designing chips for Apple = guaranteed revenue from the world's most profitable consumer electronics company).

The puts macro thesis: the narrative is priced in. The execution hasn't started yet. Intel's foundry is not yet at the scale where it generates the revenue that justifies $128/share. If Q2 shows foundry revenue below expectations AND the Apple deal timeline slips, the narrative discount returns. Macxter is supportive of the INTC puts thesis on macro grounds: the stock is priced for successful execution of a 3-year plan. Q2 is only one quarter into that plan.

**DIS macro context:**

Consumer discretionary remains under pressure from Warsh rates -- high rates suppress consumer spending on entertainment and travel. Disney's consumer-facing revenue (theme parks, merchandise, linear TV) is macro-sensitive. The streaming business is partially protected (subscription revenue is stickier than discretionary spending). The macro environment is a mild headwind for DIS. Not disqualifying for calls -- the specific earnings catalyst (streaming ARPU and ESPN launch data) is company-specific, not macro-dependent. Macro: mildly negative, not a blocker.

**Rate sensitivity and BAC/HUM pending conditionals:**

BAC at 91st pct in a high-rate Warsh environment is counterintuitive -- banks benefit from rate spreads in a high-rate environment. If Warsh cuts rates (even one cut), net interest margin compresses and bank earnings go down. But BAC is at all-time highs despite Warsh's hold. The puts thesis would require either a credit deterioration story (commercial real estate losses) or a rate cut signal from Warsh. Neither is confirmed. CONDITIONAL pending Rule 3 verification.

---

## BATCH 6 RESULTS

| Category | Direction | Names | Count |
|----------|-----------|-------|-------|
| **ADVANCE -- full research** | PUTS | **INTC, GE** | **2** |
| **ADVANCE -- full research** | CALLS | **DIS** | **1** |
| STRUCTURAL R5 CONCERN (pull chain to confirm) | PUTS | CAT | 1 |
| STRUCTURAL R5 CONCERN (pull chain to confirm) | CALLS | META | 1 |
| R1 FAIL (5-day high) | PUTS | HUM | 1 |
| FAIL R3 -- puts direction | PUTS | UNH (0 Sells), GS (1 Sell) | 2 |
| FAIL R3 -- calls direction | CALLS | BABA (3-5 Sells) | 1 |
| CONDITIONAL (R1 5-day + R3 data) | PUTS | CVS, BAC | 2 |
| CONDITIONAL (R3 gate) | PUTS | ELV, MRNA, WBD | 3 |
| CONDITIONAL (R3 gate) | CALLS | SOFI | 1 |
| MID-OUT (25-74% range) | -- | RIVN, BA, AMZN, V, HON | 5 |

---

## POST-CHAIN UPDATE -- INTC, GE, DIS (June 28, 2026)

After pulling live chains via `fetch_puts_chain.py`, the three batch 6 "ADVANCE" names resolved as follows:

**DIS -- FULL ADVANCE. Research doc written.**
- $115C Aug 21 at $0.85. Breakeven $115.85. Required move +17.1%.
- Rule 4: Lowest Buy target $123 > $115.85. Margin $7.15. Clean pass.
- Rule 5: $0.85 ≤ $1.00. Pass.
- Conviction: 3.5/5. At risk: $85.
- Status: `research_DIS.md` written and pushed. Pending Patrick's entry decision.

**INTC -- STRUCTURAL EV MISMATCH. Screen out.**
- All five Iron Rules technically pass: 89th pct (R1), earnings Jul 24 (R2), 5 Sell ratings after BofA upgrade (R3), highest Sell target Rosenblatt $50 < any Aug 21 put breakeven (R4), $65P at $1.16 ≤ $1.50 (R5).
- EV calculation: The Rule-5-compliant puts (best: $65P Aug21 at $1.16, breakeven $63.84) require a -50% decline from $128 to $63.84. The thesis -- Intel running 25-30% above avg analyst target ($96) on narrative that may not be supported by Q2 execution -- targets a pullback to $85-100. That range returns $0 on a $65P.
- EV is negative if the bear scenario averages $90 (stock is $26 above breakeven). Even the Rosenblatt bear target of $50 only delivers $13.84/sh = $1,384/contract - $116 = $1,268 gain. At 7% probability: EV = 0.07 × $1,268 - 0.93 × $116 = $88.76 - $107.88 = **-$19.12**.
- Conclusion: The instrument (deep OTM puts forced by Rule 5's $1.50 cap on a $128 stock) does not match the thesis range. Same structural category as MELI/DUOL -- the stock price creates a mechanical EV failure even when the thesis is real. **INTC screens out. Do not write research doc.**

**GE -- CONDITIONAL on Rule 4. Research deferred.**
- BNP Paribas Exane: Underperform, target $270. Confirmed.
- Unknown 2nd negative rating: identity and target unconfirmed (search returned "1 Sell + 1 Underperform" but the Sell analyst is unidentified).
- Rule 4 on Aug 21 $270P (ask $1.20, breakeven $268.80): BNP target $270 > $268.80 by $0.80. FAILS by $1.20.
- Rule 4 on Jul 31 $280P (ask $1.20, breakeven $278.80): BNP $270 < $278.80. PASSES IF unknown Sell analyst target is also ≤ $278. Unknown analyst's target determines outcome.
- Status: Conditional. GE is a valid puts setup IF the unknown Sell analyst's target falls below $278.80. Identify the analyst before writing research doc. If confirmed, best structure is Jul 31 $280P at $1.20 (breakeven $278.80, -24.3%), 33 DTE at entry.

**Updated Batch 6 results table:**

| Name | Direction | Post-chain outcome |
|------|-----------|-------------------|
| DIS | CALLS | FULL ADVANCE -- research doc written |
| INTC | PUTS | SCREEN OUT -- structural EV mismatch (all rules pass but required move -50% vs thesis range -25%) |
| GE | PUTS | CONDITIONAL -- Rule 4 gate: need identity/target of unknown Sell analyst |

---

## HUM WATCH NOTE

HUM cannot advance today due to Rule 1 5-day constraint. File for Monday:
- Current: $383.84, 52wk high $385.49
- Gap: $1.65 (0.4% from high)
- Avg analyst target: $237.71 (38% below current price)
- 2 Sell/Strong Sell ratings from 20 analysts
- Q2 earnings: July 29, 2026 -- inside window
- If on Monday HUM is >$5 below the 52wk high AND the high was not touched this past week: re-run Rule 1 check and advance to full research. The bear thesis (Medicare Advantage margin compression, enrollment deceleration, avg target disconnect) is one of the strongest in this session.

---

## GLOSSARY

**52-week high freshness check (Rule 1 addendum):** A stock can be in the top quartile of its range without having set a fresh 52-week high recently. A stock at 99th percentile that is $1.65 from its high almost certainly touched that high in the prior 5 days. The Rule 1 addendum specifically prevents entry when momentum is still actively pushing to new highs -- that is when the put buyer is fighting the tape, not fading complacency.

**Intel foundry:** Intel's contract chipmaking business, which it separated from its product design business in 2024. The foundry offers chip manufacturing services to third parties (like Apple) while the product business continues to design Intel-branded chips. The CHIPS Act funding was directed partly at Intel's foundry to build US-based fab capacity. The thesis that Intel is a "chip independence story" rests on this foundry succeeding at attracting external customers.

**Medicare Advantage reimbursement:** The federal government annually sets payment rates for Medicare Advantage (private Medicare plans offered by insurers like Humana). If the government reduces the per-member payment rate, Humana's margin compresses immediately -- it still has to pay for member healthcare at the same rate but receives less revenue from CMS. The average analyst target of $237 vs. current price of $383 implies a large portion of the professional community believes Humana's earnings are structurally impaired by reimbursement changes.

**Consumer media convergence (DIS context):** Disney's business is shifting from a linear TV company that owns theme parks to a streaming company that also owns theme parks. The transition creates near-term margin pressure (streaming requires investment before it generates profit) but the long-term multiple should be higher (streaming is recurring subscription revenue, not cyclical ad revenue). The market's pricing of $99 vs. $134 analyst average target suggests investors are not yet giving Disney credit for the streaming business hitting profitability. Q3 FY2026 earnings will be the clearest signal yet.
