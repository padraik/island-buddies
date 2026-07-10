# THE TAKE-PROFIT SWEEP
*Calxter, Friday night, July 10, 2026. Michael asked: if we had sold every positive spike at some standard percentage, what should the percentage have been, and where would the total be?*

---

## METHOD AND DATA HONESTY

Universe: all 8 closed calls positions plus the 5 open ones. Price paths reconstructed from recorded session-note marks, not tick data. The sweep assumes a resting limit at each threshold fills exactly at threshold whenever the recorded path crossed it. This assumption is generous to the take-profit rule (real fills on thin chains would sometimes be worse, never better). The rule tested: sell the ENTIRE position the first time it marks at entry plus X%; positions that never reach X% follow their actual historical exits.

First structural fact, before any math: **6 of the 8 closed positions never traded meaningfully above entry.** CCL (peak ~$1.00 on a $0.99 entry), DSGX, CHWY, NKE, BSX, and HITI were never green. A take-profit rule at any percentage changes nothing about them. The entire question is a redistribution of exactly 2 trades: MDT and DKNG. Sample size 2. Every conclusion below inherits that caveat.

**The two paths:**
- **MDT $85C:** entry $0.54 (Jun 3), marked $1.82-2.00 on Jun 4 (peak +237%), faded, sold Jun 10 at $0.77 (+$23 realized).
- **DKNG $27.5C:** entry $0.49 (Jun 5), marked $2.40 by Jun 10 (+390%), $2.50-2.57 Jun 11, sold Jun 12 at $3.00 (+512%, +$251 realized).

---

## THE SWEEP

Fixed baseline from the 6 never-green positions: -$149. Actual realized total: +$125.

| Hard take-profit at | MDT result | DKNG result | Closed-trades total | vs actual +$125 |
|---|---|---|---|---|
| +50% | +$27 | +$25 | **-$97** | -$222 |
| +100% (Michael's question) | +$54 | +$49 | **-$46** | -$171 |
| +150% | +$81 | +$74 | **+$6** | -$119 |
| +200% | +$108 | +$98 | **+$57** | -$68 |
| +250% | +$23 (never hit; actual) | +$123 | **-$3** | -$128 |
| +300% | +$23 (actual) | +$147 | **+$21** | -$104 |
| +400% | +$23 (actual) | +$196 | **+$70** | -$55 |
| +500% | +$23 (actual) | +$245 | **+$119** | -$6 |
| No cap (what we did) | +$23 | +$251 | **+$125** | baseline |

Open-book footnote: among the 5 open positions, only ABT ever crossed +50% (peaked ~+86% on Jun 4). A +50% cap would have banked +$39 there instead of today's -$30 mark, worth about $69 to the +50% row. It does not change the ranking. No open position ever touched +100%.

---

## FINDINGS

**1. There is no percentage. Every hard take-profit level tested loses to what we actually did**, under fill assumptions rigged in the rule's favor. Bullxter's floor speech is confirmed arithmetically: a +100% cap puts the fund at -$46 lifetime on closed trades.

**2. The curve is not even monotonic.** +200% beats +250% because MDT's peak (+237%) sits between them. With 2 winners, every threshold is really a bet on where those 2 specific peaks happened to land. A "standard percentage" fit to this sample is numerology wearing a lab coat.

**3. Low caps are the worst caps.** Everything at or below +150% turns a profitable fund into a flat or losing one, because the entire P&L engine is one right-tail trade and low caps amputate it first.

**4. The reason no cap works is that both winners ended with mechanism exits, and the mechanisms outperformed every price level.** DKNG was sold at $3.00 because the sentiment window closed, which happened to be within 4% of the recorded peak. MDT was sold late, but late still beat every cap below +200%. Price rules know where the option has been. Mechanism rules ask whether the reason to hold still exists. The ledger says the second question is the profitable one.

**5. The ratified ladder beats the whole table, including our actual history.** Applied retroactively: MDT (1 contract, +150% crossed with the mechanism already spent) sells on the written EV check at ~$1.35 for +$81. DKNG (1 contract, +150% crossed with the World Cup mechanism still live and dated) holds per the same check and rides to $3.00 for the full +$251. Closed total: **+$183**, which is +$58 over actual and beats every row in the sweep. The ladder wins because it is asymmetric: it banks the winner whose reason to hold is dead and rides the winner whose reason to hold is alive. No fixed percentage can do both, because the percentage cannot see the mechanism.

---

## VERDICT

If forced at gunpoint to name a standard take-profit percentage from this history, the sweep says +500% or nothing, which is the data's way of saying the sample forbids a cap. The honest answer to "what should it have been" is: not a percentage. The scale-out ladder ratified tonight is the correct instrument, and this sweep is its independent confirmation: +$183 against +$125 actual against -$46 for the +100% cap.

Standing caveat for the record: n=2 winners. This conclusion gets re-run after every 5 closed positions under the new rules. If the winner distribution changes shape, the ladder thresholds get re-derived from the new data, not defended from the old.

---

## GLOSSARY

- **Take-profit cap:** A rule selling a position the moment it reaches a fixed percentage gain over entry.
- **Sweep:** Testing every candidate threshold across the same historical data to compare outcomes.
- **Mechanism exit:** Selling because the driver of the price move (catalyst window, sentiment wave, thesis) has expired, regardless of price. Contrast with price rules.
- **Right tail:** The rare, very large win in a positively skewed return distribution. Here, DKNG, which is 200% of lifetime realized profit.
- **Positive skew:** Many small losses, few large wins. Strategies with this shape live or die by protecting the large win from being capped.
- **Scale-out ladder:** Ratified Jul 10: multi-contract winners sell half at +100% pre-catalyst; single contracts get a written hold-vs-sell EV check at +150%, defaulting to sell unless a dated mechanism remains; mechanism expiry overrides all.
- **Mark:** The recorded price of an option at an observation point; on thin chains, an estimate of value, not a guaranteed fill.
- **GTC limit:** Good-til-canceled limit order; fills at the stated price or better, or not at all.
- **n=2:** The number of green trades this entire analysis rests on. Written here so nobody forgets it.
