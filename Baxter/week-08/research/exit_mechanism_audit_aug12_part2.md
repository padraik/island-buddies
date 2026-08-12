# Exit Mechanism Audit, Part 2 -- The Pre-Ladder Counterfactual

*Baxter, Aug 12, 2026, same night as Part 1. Michael's question: for the single-contract, pre-ladder trades, would the +100% scale-out ladder have fired if it had existed? Do we even have the data?*

---

## METHOD AND A REAL DATA-AVAILABILITY ANSWER

Checked `Baxter/data/contract_history/raw_pull_jul13_*.txt` first -- two bulk historical pulls done the day the archiving rule became binding (Jul 13, 2026), before some of these contracts' data aged out of Robinhood's system. **Three of the eight have no recoverable data: DKNG, DSGX, CHWY all show `NO HISTORICAL DATA (expired or bad contract)` in the raw pull itself** -- they'd already expired and Robinhood had purged the option chain before this pull happened, and archiving wasn't a standing rule yet when they closed (Jun 5-12) to catch it earlier. That data is genuinely gone, not just inconvenient to find.

The other five (CCL, NKE, MDT, HITI, BSX, ABT -- six, not five) have real daily bars, though the same known corruption bug (flat pre-entry stub, first flagged Aug 4) sits in front of each block. The real portion, starting at each contract's actual entry date, is intact and usable. HIGH-vs-entry is computed inline in the file for every real row.

## THE RESULTS

| Ticker | Entry | Real peak (HIGH vs entry) | Date of peak | Actual exit | Would the ladder have fired? |
|---|---|---|---|---|---|
| NKE | $1.86 | +9.7% | Jun 1 (entry day) | -$70, Rule 4 breach | **No.** Never got meaningfully above entry. Declined almost the entire life of the position. |
| CCL | $0.99 | **+116.2%** | Jun 17 | +$1, Rule 4 breach | **Yes.** Crossed 100% four separate sessions (Jun 15-18), then gave essentially all of it back before the eventual flat exit. |
| MDT | $0.54 | **+307.4%** | Jul 7 | +$23 (+52% at BOTZ exit) | **Yes, overwhelmingly.** Crossed 100% on literally its first trading day and stayed above it most of its life, peaking at over 4x cost. |
| HITI | $0.25 | **+460.0%** | Jun 9 | -$12 | **Yes, the most extreme case in the book.** Crossed 100% at least five separate times across its life, including the day it closed. |
| BSX | $0.70 | **+118.6%** | Jun 4 | -$15, Rule 4 breach | **Yes.** Crossed 100% twice in its first week, then declined the rest of the way to the eventual breach. |
| ABT | $0.78 | **+150.0%** (confirmed, matches the Aug 4 sweep's own number) | Jul 7 | +$27 (grandfathered exit) | **Yes** -- already the fund's known counterexample, now with five siblings instead of standing alone. |
| DKNG | -- | No data | -- | +$251 | Unknown -- but given the +512% final exit, almost certainly yes, likely well before the final gap-up. |
| DSGX | -- | No data | -- | -$30 | Unknown |
| CHWY | -- | No data | -- | -$23 | Unknown |

**Of the six trades with real data: five would have fired the ladder. Only NKE would not.**

## WHAT THIS ACTUALLY MEANS, READ TOGETHER WITH PART 1

This flips the framing from Part 1's audit, and the two halves together tell a complete story instead of a partial one.

**Pre-ladder era (June, single contracts): positions routinely blew far past +100% and gave almost all of it back.** MDT ran to +307% and got cut at +52%. HITI ran to +460% and closed at a loss. This isn't ABT being an unlucky outlier -- ABT is the *median* case in this sample, not the exception. The ladder wasn't created to fix a hypothetical problem; it was created to fix a problem that had already happened five separate times by the time anyone wrote the rule down.

**Post-ladder era (Jul 10 onward, Part 1's finding): the ladder has only fired twice, because positions mostly aren't reaching +100% anymore in the first place.** Five of the eight ladder-eligible closes since Jul 20 never even reached +50%.

**Put together, this reads as a success story, not a lingering question.** The combination of tighter Rule 6 reachability screening, the sell-the-ramp default, and generally more disciplined entries has done something the pre-ladder era's positions never had: prevented the kind of runaway unrealized peak that MDT and HITI show. The ladder sits underused not because it failed, but because the rest of the system got good enough that it's rarely needed. That's a real answer to the open question Part 1 left for Michael -- not "should we change the ladder," but "the system got tighter, and the ladder became a backstop instead of a workhorse, which is what you'd want to see if the tightening actually worked."

## OPEN ITEM, NARROWED

DKNG's real peak is still unknown and would be worth confirming if the data ever surfaces (it won't -- Robinhood has long since purged it and no archive exists). Not worth chasing further; the five-of-six sample is large enough to trust the conclusion without it.

## GLOSSARY

- **Ladder-eligible (counterfactual sense, this document):** for Part 2, a trade is scored as "would the ladder have fired" based on whether its real HIGH price ever crossed 2x its entry price, regardless of how many contracts it actually held.
- **HIGH vs ENTRY:** the archived data's own computed column -- that day's intraday high divided by the entry price, minus one.
