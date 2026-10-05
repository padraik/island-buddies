# Screening Log: Mon Oct 5, 2026, 1:35pm ET run (VM, MIDDAY slot)

**Source:** the research queue as left by the 12:35 run (COUR, PCT, CWH, MMYT, KGC on top), plus the next three Tier A names (GIL, ORN, NMRK). No fresh scanner pass.

**Rule 5 line this run:** reserve = spendable cash $450.78 ($290.54 still unsettled until Tue Oct 6). Screen line **$0.90/share**, 3.5/5 tier top **$0.45**, 4/5 tier top **$0.72**. **Tuesday preview** (reserve ~$741.32 if it settles): 3.5/5 line **$0.741**, 4/5 line $1.00 (transitional lock).

**Prices pulled 1:35-1:37pm ET.**

## Funnel

| Stage | Names | Tool |
|---|---|---|
| Queue in | 8 touched (COUR, PCT, CWH, MMYT, KGC, GIL, ORN, NMRK) | research_queue.md |
| Rule 2 date check | KGC **Nov 3 PM** (unverified; scanner said 10/28, wrong by 4 trading days), GIL Oct 28 AM (unverified; scanner 10/29), ORN Oct 27 PM (unverified; scanner 10/29), NMRK **Oct 29 AM (verified)** | get_earnings_results |
| Rule 3 / Rule 4 proxy refresh | 8, no changes from 12:35 or the sweep | get_equity_analyst_ratings |
| Rule 6 history (free) | KGC, GIL, ORN, NMRK | get_equity_historicals, daily, 6 prints each |
| Chain check (cap 5) | 5 (MMYT, ORN, NMRK, GIL, KGC) | get_option_instruments / get_option_quotes, Nov 20 calls |
| Requote (no chain pull) | COUR $5C | get_option_quotes |
| 8-K retry | CWH Oct 5 8-K: 404 (5th try) | get_sec_filing |
| Killed | 5 (MMYT, ORN, NMRK, GIL, KGC) | |
| Alive | COUR, PCT (both wait on Tuesday's settled reserve); CWH (still blocked) | |

## Rule 6 history

| Ticker | Price | R1 (sweep) | Print moves (oldest -> newest) | Median | Cap | Max BE at cap |
|---|---|---|---|---|---|---|
| KGC | $23.565 | 0.10 | +2.7, +3.8, +7.1, -3.2, +1.3, +1.8 (all PM) | 2.96% | 4.43% | $24.61 |
| GIL | $40.40 | 0.02 | +7.5 (PM), -2.2, -1.7, -3.1, +10.2, +2.4 (AM) | 2.76% | 4.13% | $42.07 |
| ORN | $9.22 | 0.13 | +1.0, -14.8, +17.8, -0.1, +3.9, -24.1 (all PM) | 9.34% | 14.01% | $10.51 |
| NMRK | $12.575 | 0.06 | -0.6, +3.2, -3.0, -0.5, +2.2, -8.1 (all AM) | 2.59% | 3.88% | $13.06 |

## Chain-checked (5 of 5)

| Ticker | Earnings (tool) | Ratings B/H/S | Low tgt | Contract | Bid/Ask | BE (ask) | Needs | R6 cap | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| MMYT | Oct 27 AM (unverified) | 10/0/0 | $60 | $45C / $50C Nov20 | 3.90/4.80, 2.05/3.60 | $49.80 / $53.60 | +10.8% / +19.3% | 12.15% | **KILL, R5 (+ R6 on the $50C, + liquidity).** Only 5-dollar strikes. The $45C passes R6 but asks $4.80, 6.5x Tuesday's line. OI 9 and 7. |
| ORN | Oct 27 PM (unverified) | 7/0/0 | $13 | $10C Nov20 | 0.10 / 1.60 | $11.60 | +25.8% | 14.01% | **KILL, R6 + R5 + liquidity.** Only 2.5-dollar strikes. $1.50 wide spread, OI 11. |
| NMRK | Oct 29 AM (verified) | 7/1/0 | $17.50 | $12.5C Nov20 | 0.30 / 1.45 | $13.95 | +10.9% | 3.88% | **KILL, R6 + liquidity.** Needs ~2.8x the cap. OI 1. |
| GIL | Oct 28 AM (unverified) | 14/1/0 | $54 | $40C / $42.5C Nov20 | 2.55/3.20, 1.75/2.00 | $43.20 / $44.50 | +6.9% / +10.1% | 4.13% | **KILL, R6 + R5.** A stock whose median print is 2.8% can't carry a 1.5-month ATM premium. |
| KGC | Nov 3 PM (unverified) | 18/2/1 | $30 | $24C / $25C Nov20 | 1.35/1.57, 0.98/1.18 | $25.57 / $26.18 | +8.5% / +11.1% | 4.43% | **KILL, R6 + R5.** Same shape as GIL: gold miner with small print reactions, priced on gold's volatility. Note the scanner's 10/28 date was wrong; the tool says Nov 3. |

## Pattern worth writing down

Four of today's five kills (KGC, GIL, NMRK, MMYT) are mid/large names with tight earnings reactions (median 2.6-3.0%, MMYT 8.1%). On names like that, any Nov 20 strike close enough to pass Rule 6 is near the money, and near-the-money premium on a $12-45 stock is far over a $0.74 line. Our Rule 5 cap effectively restricts us to sub-$10 stocks with big print moves (COUR, PCT, CWH). That's the system working as built, not a defect, but it means the Tier A list should be worked cheapest-stock-first: the free R6 math plus a back-of-envelope ATM premium kills the rest before a chain is spent. The queue has been reordered that way.

## Still alive

- **COUR** $5.19. $5C Nov20 0.60 / 0.75 (unchanged), BE $5.75, needs +10.8% vs cap 19.89%. R4 $6.50 holds (8/4/0). Tuesday: needs ask <= $0.74.
- **PCT** $4.02 (-8.4% vs Fri). 3/3/0, low $6. Not re-chained.
- **CWH** $4.505. 11/2/0, low $6. 8-K still unreadable.

## GLOSSARY

- **Rule 1 (range percentile):** where the price sits between its 52-week low (0) and high (1). Under 0.25 is the calls zone.
- **Rule 2:** a confirmed earnings date before the option expires. "Unverified" means the tool estimated it from the company's cadence.
- **Rule 3 (calls):** 0-1 Sell ratings, at least 3 Buys, and Buys at least equal to Holds.
- **Rule 4 (bear floor):** the lowest analyst target must sit above the call's breakeven (strike + premium).
- **Rule 5:** one contract's ask must fit the cap for its conviction tier, computed on spendable cash (the reserve).
- **Rule 6 (reachability):** the move to breakeven can't exceed 1.5x the stock's median earnings-day move over its last 4-8 prints. AM prints: prior close to print-day close. PM prints: print-day close to next-day close.
- **Breakeven (BE):** strike + premium; where the call neither makes nor loses money at expiry.
- **ATM / near the money:** a strike close to the current stock price. Those cost the most time premium.
- **Settled cash:** in a cash account, sale proceeds take one business day (T+1) to settle before they can be spent.
- **8-K:** a company's filing for a material event that can't wait for the quarterly report.
- **Open interest (OI):** contracts outstanding. Low OI plus a wide spread means there may be nobody to sell to.
- **Kill:** out for this cycle, with the rule that killed it.
