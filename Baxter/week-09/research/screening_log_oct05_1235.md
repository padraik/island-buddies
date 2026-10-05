# Screening Log: Mon Oct 5, 2026, 12:35pm ET run (VM, MIDDAY slot)

**Source:** the research queue as left by the 11:35 run (COUR, PCT, CWH, PRG, LVS on top), plus the next two Tier A names (METC, MMYT). No fresh scanner pass.

**Rule 5 line this run:** reserve = spendable cash $450.78 ($290.54 still unsettled until Tue Oct 6). Screen line **$0.90/share**, 3.5/5 tier top **$0.45**, 4/5 tier top **$0.72**. **Tuesday preview** (reserve ~$741.32 if it settles): 3.5/5 line 0.10 x 741.32 / 100 = **$0.741**, 4/5 line $1.00 (transitional lock).

**Prices pulled 12:35-12:37pm ET.**

## Funnel

| Stage | Names | Tool |
|---|---|---|
| Queue in | 7 worked (COUR, PCT, CWH, PRG, LVS, METC, MMYT) | research_queue.md |
| Rule 2 date check | COUR (Oct 22 PM, still unverified), METC (Oct 26 PM, unverified; scanner said 10/27), MMYT (Oct 27 AM, unverified; scanner said 10/28) | get_earnings_results |
| Rule 3 / Rule 4 proxy refresh | 7, no changes from 11:35 | get_equity_analyst_ratings |
| Rule 6 history (free) | METC, MMYT | get_equity_historicals, daily, 6 prints each |
| Web search (1) | COUR merger status | WebSearch |
| Chain check (cap 5) | 5 (PRG, LVS, COUR, CWH, METC) | get_option_instruments / get_option_quotes, Nov 20 calls |
| Killed | 3 (PRG, LVS, METC) | |
| Alive | **COUR** (merger question answered; R5 on Tuesday's line is a penny short at the ask); PCT; CWH (still blocked); MMYT (R6 done, chain next) | |

## Chain-checked (5 of 5)

| Ticker | Price | Earnings (tool) | Ratings B/H/S | Low tgt | Contract | Bid/Ask | BE (ask) | Needs | R6 cap | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| COUR | $5.22 | Oct 22 PM (unverified) | 8/4/0 | $6.50 | $5C Nov20 | 0.60 / 0.75 | $5.75 | +10.2% | 19.89% | **ALIVE, still the best name.** Spread widened from 0.60/0.70 to 0.60/0.75. R4 $6.50 > $5.75. R6 at 51% of cap. OI 3,135. R5: $0.75 is **one cent over** Tuesday's ~$0.741 3.5/5 line at the ask; mid $0.675 fits. Needs an ask at or under $0.74 on Tuesday's quote. |
| CWH | $4.43 (-11.9% vs Fri $5.03, recovered from $4.145) | Oct 27 PM (unverified) | 11/2/0 | $6.00 | $4C Nov20 | 0.60 / 0.80 | $4.80 | +8.4% | 23.90% | **HOLD, BLOCKED.** R6 and R4 pass. R5: $0.80 over today's and Tuesday's 3.5/5 line. OI 15. Oct 5 8-K still 404 (4th try). Cause of the drop still unknown. |
| PRG | $31.02 | Oct 21 AM (unverified) | 6/1/0 | $45.00 | $30C / $35C Nov20 | 2.50/4.90, 0.70/2.15 | $34.90 / $37.15 | +12.5% / +19.8% | 10.23% | **KILL, R5 + R6 + liquidity.** Only 5-dollar strikes near the money ($30, $35; no $32.5/$33). $30C ask $4.90, OI 0. $35C BE over the $34.25 max. Oct 16 expiry is before the print. |
| LVS | $36.79 | Oct 21 PM (unverified) | 17/7/0 | $47.00 | $37.5C / $40C / $42.5C Nov20 | 1.55/1.93, 0.81/0.94, 0.35/0.46 | $39.43 / $40.94 / $42.96 | +7.2% / +11.3% / +16.8% | 11.33% | **KILL, R5 + R6.** $37.5C ask $1.93 over every line. $40C needs +11.3% vs an 11.33% cap (99.7% of cap, no margin) and $0.94 is over the 3.5/5 line today and Tuesday. $42.5C fails R6. Conviction can't reach 4/5 on this machine (revisions unverifiable), so there's no tier where the $40C fits. |
| METC | $8.125 | Oct 26 PM (unverified) | 6/3/0 | $11.00 | $8C / $9C Nov20 | 1.00/1.30, 0.60/0.80 | $9.30 / $9.80 | +14.5% / +20.6% | 11.75% | **KILL, R6 (+ R5 on the $8C).** Both strikes need more than the cap. $8C ask $1.30 also over the screen line. |

## Rule 6 history only (no chain spent)

| Ticker | R1 pct | Print moves (oldest -> newest) | Median | Cap | Max BE at cap | Low tgt | Verdict |
|---|---|---|---|---|---|---|---|
| METC | ~0.00 (52w closing range $8.105-$54.55) | +0.1, -6.8, -16.9, -15.5, +8.8, -4.1 (1 AM, 5 PM) | 7.83% | 11.75% | $9.08 | $11.00 | Killed on the chain above. |
| MMYT | 0.19 | -1.4, +2.8, -10.2, -12.1, -7.7, +8.5 (AM) | 8.10% | 12.15% | $50.37 at $44.915 | $60.00 | **ALIVE.** 10/0/0. Next: chain $45 / $47.5 / $50 Nov20, need ask <= $0.74 (Tuesday 3.5/5) and BE <= $50.37. A $47.5C needs ask <= $2.87 for R6, so R5 is the binding rule. |

## COUR: what changed

- **The merger is done, not pending.** Coursera and Udemy signed Dec 17, 2025, stockholders approved Apr 9, 2026, and it closed May 11, 2026 (all-stock; Udemy is a wholly owned subsidiary). No live deal, so the calls M&A flag doesn't apply and no deal price caps Rule 4. Q2 2026 revenue $299M (+60% y/y, Udemy included from May 11). Q3 guide $364-372M revenue, $52-56M adj. EBITDA.
- **New Bearxter point:** of the 6 prints in the Rule 6 history, only one (Jul 29, 2026) is from the combined company. The other five were a smaller, different business. The doc has to say whether a pre-merger median still describes how this stock reacts. The post-merger print was -14.7%, which is inside the cap either way.
- **Still open:** Oct 22 PM isn't company-confirmed (the search didn't turn up a date announcement; Q3 2025 was Oct 23 PM). The $6.50 low target still has no date. Why it's near the low is still unwritten (integration cost, guidance, or the four straight down prints).

Sources: [Coursera 10-Q, Q2 2026](https://www.sec.gov/Archives/edgar/data/0001651562/000165156226000063/cour-20260630.htm), [Coursera 8-K Ex. 99.1, Q2 2026](https://www.sec.gov/Archives/edgar/data/0001651562/000165156226000059/cour-20260630xexx991.htm), [RBC on the merger (Tiger)](https://www.itiger.com/news/2592188620).

## GLOSSARY

- **Rule 1 (range percentile):** where the price sits between its 52-week low (0) and high (1). Under 0.25 is the calls zone.
- **Rule 2:** a confirmed earnings date before the option expires. "Unverified" means the tool estimated it from the company's cadence.
- **Rule 3 (calls):** 0-1 Sell ratings, at least 3 Buys, and Buys at least equal to Holds.
- **Rule 4 (bear floor):** the lowest analyst target must sit above the call's breakeven (strike + premium).
- **Rule 5:** one contract's ask must fit the cap for its conviction tier, computed on spendable cash (the reserve).
- **Rule 6 (reachability):** the move to breakeven can't exceed 1.5x the stock's median earnings-day move over its last 4-8 prints. AM prints: prior close to print-day close. PM prints: print-day close to next-day close.
- **Breakeven (BE):** strike + premium; where the call neither makes nor loses money at expiry.
- **Mid:** halfway between bid and ask. Rule 5 is checked on the ask, not the mid.
- **Settled cash:** in a cash account, sale proceeds take one business day (T+1) to settle before they can be spent.
- **8-K:** a company's filing for a material event that can't wait for the quarterly report.
- **Open interest (OI):** contracts outstanding. Low OI plus a wide spread means there may be nobody to sell to.
- **All-stock merger:** one company buys another by paying in its own shares instead of cash.
- **Kill:** out for this cycle, with the rule that killed it.
