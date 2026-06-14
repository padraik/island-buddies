# Fidelity National Information Services -- FIS
**Date:** June 13, 2026
**Conviction:** 3/5
**Expiry target:** Sep 18, 2026 (Aug21 not available in chain -- see below)

---

## THE SETUP

FIS is one of the largest banking technology companies in the world. It runs the software and processing infrastructure that powers thousands of banks. It also owns 45% of WorldPay, the merchant payment processor it sold a majority stake to private equity in 2023.

The stock peaked above $80 less than 12 months ago. It closed at $38.78 on June 10, 2026 -- a new 52-week low, down more than 53% from that high. The stock is now below where it was before the 2019 WorldPay merger that was supposed to be transformational.

Sixteen analysts rate FIS as Buy. Zero rate it Sell. Their average target is $80.

The market has concluded this restructuring will take forever and the stock is dead money. August 3 earnings is the moment that thesis gets tested.

---

## IRON RULES CHECK

| Rule | Requirement | FIS | Status |
|------|-------------|-----|--------|
| 1 | Bottom 20-25% of 52-wk range | $37.91 low, $82.74 high, current $39.23 = **2.9% from bottom** | PASS |
| 2 | Earnings catalyst before or within expiry | Aug 3, 2026 -- **46 days before Sep 18** | PASS |
| 3 | Zero or near-zero sell ratings | 16 Buy, 9 Hold, **1 Sell** out of 26 analysts | CONDITIONAL |
| 4 | Bear floor above option breakeven | Bear floor ~$65 (estimated lowest Buy analyst) vs $50.70 breakeven | CONDITIONAL |
| 5 | Option ask <= $1.00 | Sep 18 $50C at **$0.70** | PASS |

---

## AUGUST 21 CHAIN GAP -- HIGH PRIORITY FOR DOUBLE-CHECK

The chain script did not return Aug21 options for FIS. This is the same gap seen with ZTS, FLUT, STE, GEHC, and EQT -- the script appears to skip Aug21 for certain stocks, jumping from Jul31 to Sep18.

**If Aug21 exists for FIS (which is likely), the instrument picture changes dramatically:**

Aug21 (68d) with FIS earnings August 3 = 18 days before expiry. Options that likely exist but are not confirmed:
- If Aug21 $45C exists at ~$0.80-1.00, breakeven $45.80-46.00, needs +16.7-17.3%
- This would be a much stronger instrument than the Sep18 $50C

**Patrick must pull FIS Aug21 chain on Robinhood to check.** If Aug21 options exist at $45C or $50C within budget, this research doc should be re-evaluated at 4/5 conviction with the tighter instrument.

This doc proceeds with Sep18 as the available fallback.

---

## BEAR FLOOR NOTE

One Sell analyst out of 26. The 1 Sell analyst almost certainly holds a price target below current price (that is the nature of a Sell rating on a stock at 52-week lows). They are excluded from the bear floor calculation.

The bear floor uses only Buy-rated analysts. Sources show:
- Average Buy analyst target: $80.77
- One source shows low target overall: $50 (likely from a Hold analyst, not the Sell)
- Another source shows low target: $65 (more plausible as the lowest Buy analyst)

**Working assumption: Bear floor = $65 (estimated lowest Buy analyst target).**

Sep18 $50C breakeven: $50.70. $50.70 < $65 = Rule 4 PASSES.

If any Buy analyst has a target below $50.70, Rule 4 fails. Patrick should check the individual analyst breakdown to confirm. Given the average Buy target is $80.77, a bull at $50 would be a statistical outlier in a universe where the median is $80+.

---

## THE CHAIN

Chain pulled June 13, 2026. Current price $39.23.

**Aug 21, 2026:** Not available in chain script. **Manually verify on Robinhood.**

**Sep 18, 2026 (96 days):**

| Strike | Ask | At Risk | Breakeven | Needs | Status |
|--------|-----|---------|-----------|-------|--------|
| $45.00 | $1.50 | $150 | $46.50 | +18.5% | STRETCH |
| $47.50 | $1.05 | $105 | $48.55 | +23.8% | STRETCH |
| **$50.00** | **$0.70** | **$70** | **$50.70** | **+29.2%** | **OK** |
| $55.00 | $0.55 | $55 | $55.55 | +41.6% | OK |
| $60.00 | $1.00 | $100 | $61.00 | +55.5% | OK |

**Best instrument if entering (Sep18):** $50C at $0.70 ($70 at risk, breakeven $50.70).

The $55C at $0.55 ($55 at risk, breakeven $55.55) is also viable if bear floor confirms above $55.55.

---

## THE THESIS

FIS owns two things: a world-class banking software business and a 45% stake in WorldPay.

The banking software business (banking and capital markets technology) serves more than 20,000 clients globally. This business generates approximately $9B in annual revenue, has sticky enterprise contracts, and is the kind of infrastructure technology that banks cannot easily rip out. On this business alone, peer multiples suggest a valuation well above the current stock price.

The WorldPay stake is a complex liability in investor perception -- it creates noise, ongoing mark-to-market questions, and overhang about when FIS will monetize it. The market is pricing the WorldPay stake at zero or negative. Every quarter FIS management provides an update, and every quarter the market ignores it.

August 3 earnings will show:
1. Whether banking ARR growth is accelerating or stalling
2. Progress on deleveraging (FIS has prioritized debt repayment over buybacks)
3. Any update on WorldPay stake monetization
4. Whether Q2 guidance warning about "softness" was priced in or worse

If banking ARR growth is steady and management shows deleveraging progress, the stock re-rates from "distressed fintech" toward "infrastructure software." That re-rate runs directly through the $50C breakeven.

The risk: management warned Q2 would be soft. If the August 3 print is worse than already-lowered expectations, the stock at $39 could fall to $35 or lower. The 52-week low of $37.91 is not a floor -- it is a marker from three days ago.

---

## WHY THE INSTRUMENT IS SEP18, NOT AUG21

FIS earnings are August 3. The script returned no Aug21 options. The chain jumps from Jul31 to Sep18.

For Jul17/Jul24/Jul31 options: all expire BEFORE August 3 earnings. Rule 2 fails for any pre-earnings expiry.

Sep18 is the shortest available expiry that captures the August 3 catalyst. At 96 days (vs our preferred 68d), the option has more time decay risk but also more time for the post-earnings thesis to develop. FIS earnings on August 3 gives 46 days of post-earnings time within the Sep18 window.

If Aug21 exists on Robinhood (high probability), that is a better instrument: 18 days post-earnings, tighter premium, likely $45C range.

---

## RISK FACTORS

- Q2 may be genuinely worse than warned. Management telegraphed softness in Capital Markets. If softness turns into a miss, the stock continues lower.
- The 9 Hold ratings (vs 16 Buy) represent significant neutral skepticism. This is not a universally beloved setup.
- WorldPay stake creates ongoing complexity and potential additional negative marks.
- FIS has been hitting new 52-week lows sequentially: $82 → $65 → $46 → $43 → $38. Each "floor" broke. Nothing structurally prevents $35 or $30.
- Rule 4 is working off estimated data. Confirm bear floor before entering.
- Sep18 is a 96-day option. More time to be right, but also more premium decay if the thesis stalls.

---

## EXIT RULE

Sell at open August 4 (day after Q3 earnings). If the stock moves strongly pre-earnings on analyst upgrades or rumors, sell early. Do not hold through an earnings surprise in either direction past the position's original thesis window.

---

## GLOSSARY

**ARR (Annual Recurring Revenue):** The subscription and long-term contract revenue FIS collects from banks that license its software. More predictable than one-time implementation fees. ARR growth is the primary metric the market uses to value banking technology companies.

**WorldPay:** FIS's former merchant payments subsidiary. FIS sold 55% to private equity consortium GTCR in 2023 and retained a 45% stake. WorldPay processes card transactions for merchants globally. FIS's retained stake creates complexity in valuation because it is an illiquid minority interest in a separate company.

**Bear floor:** The lowest price target held by any analyst who still recommends buying the stock. For FIS, the estimated floor is $65 based on available data -- significantly above the Sep18 $50C breakeven of $50.70. Patrick should confirm this is accurate before entering.

**Deleveraging:** The process of paying down debt. FIS has significant debt from the 2019 WorldPay merger and has been directing free cash flow toward debt repayment rather than buybacks. The market has punished this prioritization. As debt falls, the thesis is that capital allocation shifts toward buybacks, supporting the stock.

**52-week range position:** How far the current price sits above the 52-week low, expressed as a percentage of the full range. FIS at 2.9% is essentially at its annual floor -- the stock set a new 52-week low just three trading days before this analysis.
