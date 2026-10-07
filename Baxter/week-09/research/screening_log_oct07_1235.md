# SCREENING LOG — Wed Oct 7, 2026, 12:35pm ET (VM MIDDAY run)

**Source:** research_queue.md plan written by the 11:35 run: date checks on COUR / QUBT / ONDS, then write `research_ONDS.md` (next best past the chain stage). Per Step 6, the run was spent on the doc, not new names.

| Step | Names | Tool |
|---|---|---|
| Dates | COUR, QUBT, ONDS | get_earnings_results |
| Ratings | 15 queue names (COUR, QUBT, ONDS, FUBO, FRMI, SERV, GAU, OBDC, BRSL, TME, FINV, ADTN, PCT, MLCO, ENVX) | get_equity_analyst_ratings (1 call) |
| Requotes | COUR, QUBT, ONDS, FUBO (+ 15 underlyings) | get_option_quotes, get_equity_quotes |
| ONDS fundamentals | 52w range, market cap | get_equity_fundamentals |
| ONDS 10-Qs | Q1 2026 (filed May 15), Q2 2026 (filed Aug 13) | get_sec_filing_index, get_sec_filing_facts |
| ONDS 8-Ks | Sep 14, Sep 23 (get_sec_filing 404 -> EDGAR) | WebFetch (EDGAR) |
| Moved this run | **3**: ONDS (DOC NEXT -> DOC COMPLETE), COUR, QUBT (date checks + requotes); FUBO requoted | |
| Killed | 0 | |

## Dates

| Ticker | Date (tool) | Verified | Note |
|---|---|---|---|
| COUR | Oct 22 PM | false | Unchanged. |
| QUBT | Nov 13 PM | false | Unchanged (web aggregators: Nov 9 PM). |
| ONDS | Nov 12 AM | false | Unchanged. Not in the Sep 14 / Sep 23 press releases. |

## Requotes (12:35pm ET)

| Ticker | Stock | Contract | Bid / Ask | R5 / R6 at the ask |
|---|---|---|---|---|
| COUR | $5.09 | $5C Nov20 | 0.40 / 0.65, OI 3,137 | Passes both (BE $5.65). Date gate only. |
| QUBT | $7.575 | $8C Nov20 | 0.53 / 0.54, OI 769 | Passes. BE $8.54, +12.7% vs cap 13.88% (91%). Max price $0.626. Date gate only. |
| ONDS | $7.045 | $8C Nov20 | 0.41 / 0.42, OI 10,604, vol 1,703 | Passes. BE $8.42, +19.5% vs cap 20.89% (93%). Max price $0.517. Date gate only. |
| FUBO | $9.01 | $10C Nov20 | 0.68 / 0.96 | Ask fails R5 ($0.741). Mid $0.82 fails R5 too. |

Underlyings: FRMI $3.99, SERV $4.575, GAU $1.975, OBDC $9.895, BRSL $9.955, TME $7.955, FINV $2.925, ADTN $7.815, PCT $3.785, MLCO $4.175, ENVX $2.572.

**Ratings:** all 15 unchanged (COUR 8/4/0 $6; QUBT 5/2/0 $10; ONDS 11/0/0 $13; FUBO 8/2/0 $12; FRMI 6/2/0 $6; SERV 6/2/0 $7; GAU 5/1/0 $2.99; OBDC 11/2/0 $11; BRSL 7/3/0 $11.90; TME 22/14/0 $9.04; FINV 6/1/0 $4.11; ADTN 7/2/0 $11; PCT 3/3/0 $6; MLCO 11/4/0 $5.30; ENVX 7/3/1 $5).

## ONDS: doc written (`research_ONDS.md`)

- **Income anomaly answered from the 10-Q:** Q1 2026 net income +$362.8M = operating loss -$42.7M + nonoperating income +$404.2M, of which **$389.5M is the change in fair value of the warrant liability** (Level 3, non-cash). Stock fell during Q1, the liability shrank, the drop was booked as income.
- **Burn:** operating loss -$162.9M in Q2 2026 on $83.8M revenue. Cash $550.7M (Dec 31) -> $1,026.0M (Mar 31) -> $657.9M (Jun 30).
- **Sep 14 8-K (EX-99.2):** "Ondas Acquires GATE Technologies and Bron Technologies"; "$205 million upfront, comprised of $105 million in cash and $100 million in Ondas common stock," "$22.5 million of such stock consideration" within nine months, earn-outs "up to $185 million through 2028"; guides "$65 million of revenue in full year 2026, increasing to $180 million revenue in 2028."
- **Sep 23 8-K (EX-99.1):** "Ondas Acquires Three Defense Technology Businesses" (Insignito, Ottopia Defense, Caribou Labs); "purchase price represents less than three times the businesses' expected 2027 revenue"; inducement awards "2,979,063 shares... at $7.72 per share" to 37 new hires.
- Two 424B7 resale prospectuses (Sep 14, Sep 23); Item 3.02 on Aug 10, Aug 28, Sep 14, Sep 23 8-Ks.
- R1 0.203 (52w $4.95 Nov 7 2025 / $15.28 Jan 12 2026). 3.5/5, low confidence, 1 contract, max price $0.51.

## State of the top of the queue

Three docs, all DOC COMPLETE, all blocked only on a company-confirmed date: COUR (Oct 22 PM), QUBT (Nov 13 PM / Nov 9 PM), ONDS (Nov 12 AM). Limit 10 allows one entry per day; if two clear the same run, compare on that run's numbers.

## GLOSSARY

- **Requote:** a fresh bid/ask on a contract already chain-checked.
- **R1 (52w):** (price - 52-week low) / (52-week high - 52-week low); calls need <= 0.25.
- **R2:** a confirmed earnings date before expiry. `verified: false` means the date is estimated from the company's cadence, not announced.
- **R3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4:** lowest Buy target, dated within 60 days, above breakeven.
- **R5:** one contract's ask <= 10% of reserve / 100 at 3.5/5 (today $0.741).
- **R6:** move to breakeven <= 1.5x the median earnings-day move (the "cap"); max price = stock x (1 + cap) - strike.
- **DOC COMPLETE:** research doc with Iron Rules, Five-Baxter meeting, EXIT PLAN, sizing and GLOSSARY committed; entry waits only on the named gates.
- **Warrant liability fair-value gain:** non-cash income booked when the market value of warrants the company owes falls.
- **424B7 / Item 3.02:** resale prospectus / unregistered share issuance; both add stock supply.
