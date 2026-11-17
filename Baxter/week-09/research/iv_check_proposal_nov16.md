# Proposal: measuring implied volatility instead of only pricing around it

*Mon Nov 16, EVENING 2. Written because Michael asked whether we consider implied volatility when picking options. **This is a proposal only.** No rule changes here. Under the Nov 11 rule-change order, any rule or process change needs Patrick's yes (and a hard_limits change would need a local session). Nothing below applies to any run until that happens.*

## Where IV already shows up

1. **No rule names it.** We write IV down on most quotes (COUR ran 75-94%, QUBT 62-78%, FRMI 121-165%). No rule gates on that number.
2. **It hits us through price.** High IV makes the premium expensive, which pushes breakeven out. Rule 6 (the breakeven move has to fit inside 1.5x the stock's median earnings reaction) and Rule 5 (the price cap) then reject the contract. That's a crude version of the question "is this option overpriced for how the stock really moves?" I haven't counted how many Rule 6 kills were really IV kills. That count would be the first job if option A below goes ahead.
3. **The exit is an IV trade.** Sell-the-ramp sells into the pre-print IV build-up and gets out before the post-print crush. Era 2 so far: COUR, ACHR, QUBT and FRMI all sold the ramp. ACHR and QUBT both traded lower after hours the night of their prints.

## What we don't measure

- **IV rank:** is today's IV high or low compared with this stock's own last year?
- **Implied move vs realized move:** what earnings move is the market pricing (roughly, the at-the-money straddle for the first expiry after the print, divided by the stock price), compared with the move the stock actually makes on prints (our Rule 6 median)?

The second one matters most for us. Rule 6 asks whether the *stock* can plausibly get to breakeven. It doesn't ask whether we're *overpaying* for that chance compared with the market's own estimate. When the implied move is well above the realized median, we pay for a move the stock rarely makes. Rule 6 catches the worst of those cases only indirectly.

## What the tools can and can't do

- `get_option_quotes` returns IV per contract, live. So **implied move vs realized median** can be computed in any run: one straddle quote plus the Rule 6 median we already compute.
- There's **no IV-history tool**. IV rank would need a year of daily IV per name. We could build that slowly by logging it, but we can't pull it today. So IV rank is out for now.

## The proposal (three options, smallest first)

**A. Log only, no gate (recommended).** Every research doc and paper entry gets one more line in its Rule 6 section: `implied move X% vs realized median Y% (ratio Z)`. At the next sweep, compare the ratio against outcomes across closes. That sweep needs at least 5 entries carrying the line. If high-ratio entries do measurably worse, *then* propose a gate with real data behind it. Cost: one extra quote per doc. It changes no decision.

**B. Soft cap on conviction.** An entry whose implied move is more than 1.5x its realized median caps at 3.5/5. That would be a sizing-rule change. It would need Patrick, and I'd rather have option A's data first.

**C. Hard gate.** No entry when implied is more than 2x realized. It would be a new Iron Rule and would need a ratified back-test. Not recommended now: we have no data, and the paper book is where something like this should be tested first.

**What I'd ask for:** a yes or no on option A. If it's yes, it starts on the next doc, and the line goes into the research template.

## GLOSSARY

- **IV (implied volatility):** the yearly volatility the option's price implies. Higher IV means a more expensive option for the same strike and date.
- **IV rank:** where today's IV sits within the stock's own range over the past year (0 = lowest, 100 = highest).
- **Implied move:** the earnings-day move the options market is pricing, roughly the at-the-money straddle price divided by the stock price, for the first expiry after the print.
- **Realized median:** the median absolute stock move on the last 4-8 earnings prints (what Rule 6 already uses).
- **IV crush:** the drop in IV right after earnings, when the uncertainty resolves.
- **Straddle:** a call plus a put at the same strike and expiry. We only quote it here to read the implied move. We never buy one (calls only, hard limit 3).
- **Sweep:** the every-5-closes review that re-derives the tunable thresholds from real results.
