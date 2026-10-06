# Screening Log: Tue Oct 6, 2026, 10:35am ET run (VM, MIDDAY slot)

**Source:** the research queue's "Tuesday Oct 6 MIDDAY" block left by the 9:37am OPEN. DO run: 3 chains (QBTS, AORT, COLL), 3 requotes (COUR $5C, REZI $22.5C, ADTN $7C), 1 web search (COUR Q3 date).

**Rule 5 line:** spendable = cash $741.32 - unsettled $0.00 = **$741.32**. 3.5/5 line **$0.741**; 4/5 line $1.00 (lock); screen line $1.00.

**Quotes are 10:35-10:36am ET**, an hour into the session, so spreads are the normal daytime ones.

## Funnel

| Stage | Names | Tool |
|---|---|---|
| Queue in | 8 touched (COUR, REZI, ADTN, QBTS, AORT, COLL; ratings also on PCT, CWH) | research_queue.md |
| Ratings refresh | 8, all unchanged from OPEN (COUR low still $6.00; CWH still 11/2/0, low $6) | get_equity_analyst_ratings |
| Earnings date | COUR still Oct 22 PM, `verified: false`. Web search: an aggregator says Oct 26 PM (also an estimate). No company announcement. | get_earnings_results, WebSearch |
| Chains (new) | 3: QBTS, AORT, COLL | get_option_instruments + get_option_quotes |
| Requotes | 3: COUR $5C, REZI $22.5C, ADTN $7C | get_option_quotes |
| Killed | 4: QBTS, AORT, COLL, REZI | |
| Alive | COUR (doc written, R5 now passes, date gate shut), ADTN, PCT, CWH | |

## Chains

| Ticker | Stock | Strike Nov20 | Live bid/ask | Prior close | BE at ask | Max BE (R6) | Verdict |
|---|---|---|---|---|---|---|---|
| QBTS | $15.85 | $15C | 2.05 / 2.45 | 1.93 | $17.45 | $17.27 | Fails R5 and R6. |
| QBTS | | $16C | 1.62 / 1.69 | 1.49 | $17.69 | $17.27 | Fails R5 ($1.69 vs $0.741) and R6. |
| QBTS | | $17C | 1.24 / 1.27 | 1.13 | $18.27 | $17.27 | **KILLED, R5 + R6.** Every strike at or above $16 has a BE over $17.27; every strike below it costs over $2. Strikes are $1-wide, so nothing is missing. Quantum IV (~76%) prices it out, as expected. |
| AORT | $22.11 | $22.5C | 0.95 / 4.90 | 0.01 (phantom) | | $26.92 | The bid alone ($0.95) is over the $0.741 line. OI 0. |
| AORT | | $25C | no bid / 2.65 | 0.01 (phantom) | $27.65 | $26.92 | **KILLED, R5 + liquidity.** No market on the only R6-passing strike (OI 4, no bid, ask $2.65). Strikes 22.5/25/30. |
| COLL | $21.73 | $22.5C | no bid / 3.60 | 0.01 (phantom) | | $24.90 | **KILLED, R5 + liquidity** (the queue's own kill condition: 2.5-wide strikes and the $22.5C asks over $0.74). OI 0. |
| COLL | | $25C | no bid / 2.90 | 0.01 | >= $25.01 | $24.90 | Fails R6 at any price. |
| REZI | $18.55 | $22.5C | no bid / 2.55 | 0.01 (phantom) | | $23.17 | **KILLED, R5 + liquidity.** Second straight run with no bid and no volume (OI 76). The real ask is $2.55 against a $0.67 R6 / $0.741 R5 line. Re-open only if a two-sided market under $0.67 ever shows up. The $20C failed R5 at OPEN. |
| ADTN | $7.34 | $7C | 0.85 / 1.05 | 0.85 | $8.05 | $8.26 (OPEN) | Alive, R5 fails (bid alone $0.85 > $0.741). The stock is up 2.7% today, which makes this worse. |
| COUR | $5.195 | $5C | **0.50 / 0.70** | 0.65 | $5.70 | $6.24 | **R5 PASSES at the ask** ($0.70 <= $0.741). R4: BE $5.70 vs low target $6.00, margin $0.30 (5.3%). R6: needs +9.7% vs cap 19.89%. **Entry still blocked on the date gate** (below). OI 3,137, vol 300. |

## COUR date

- Tool: Q3 2026 Oct 22 PM, `verified: false` (unchanged since Oct 5). The Q4 row (Feb 4, 2027) is also unverified.
- One web search: no company press release. An aggregator page says "expected Oct 26 after close" with a $0.07 EPS estimate. That doesn't match the tool's $0.16, so it looks like a stale or differently built estimate. It's still a second, unconfirmed date four days later than the tool's.
- Why this matters: the ramp-sell deadline (Oct 22 3:35pm vs Oct 26 3:35pm) depends on the date. The doc's verdict requires a company-confirmed date. Q2's date was announced 14 days ahead, so the announcement should land around Oct 8 (Oct 22 print) or Oct 12 (Oct 26 print).

## GLOSSARY

- **R1-R6:** the six Iron Rules for calls (binder Tab 1): range, earnings, ratings, bear floor, chain affordability, reachability.
- **Max BE (R6):** the highest breakeven a contract can have and still pass Rule 6 (stock price x (1 + 1.5 x median earnings move)).
- **Phantom quote:** a price that can't be real against its neighbors (a $0.01 close on a near-the-money strike). Never acted on.
- **Liquidity kill:** no bid, no volume, near-zero open interest. There's no real price to buy at and no one to sell to later.
- **Bid/ask:** what buyers will pay / sellers will take right now.
- **OI:** open interest, contracts outstanding.
- **Verified:** the company itself announced the earnings date.
- **IV:** implied volatility, how much movement the option price already assumes.
