# Screening log — Tue Oct 6, 2026, EVENING session 2 (8:00pm ET, VM)

**Job (EVENING 2):** research docs, with the Five-Baxter meeting and the EXIT PLAN, for every name that cleared the chain stage. Order from the queue: BRSL, OBDC, TME, then ADTN/QUBT if time.

**Rule 5 line this run:** reserve = spendable $741.32 (cash $741.32, unsettled $0.00). 3.5/5 line **$0.741**, 4/5 $1.00 (lock), screen $1.00.

**Quotes:** all option and stock quotes are the Oct 6 4:00pm close (market closed; `updated_at` ~19:59:59Z). Nothing intraday moved since EVENING 1.

## Tools used

| Step | Names | Tool |
|---|---|---|
| Requotes | BRSL $11C/$10C, OBDC $10C, TME $8C, ADTN $8C, QUBT $8C, COUR $5C | get_option_quotes, get_equity_quotes |
| Ratings | 11 queue names | get_equity_analyst_ratings (1 call) |
| Dates | BRSL, OBDC, TME, COUR | get_earnings_results |
| R1 + R6 history | BRSL, OBDC, TME (1 year daily) | get_equity_historicals |
| Dividend / 52w | OBDC | get_equity_fundamentals |
| Floor dating | BRSL, OBDC, TME, ADTN, QUBT | WebFetch (MarketBeat forecast pages, 5) |
| Web | BRSL date, TME decline, OBDC NAV/merger, OBDC Sep slide, BRSL Q2 | WebSearch (5) |

## Results

| Ticker | Stock | Contract | Bid / Ask | R1 | Date | Ratings / low | R6 (median / cap / needs) | Floor dating | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| **BRSL** | $10.22 | $11C Nov20 | 0.20 / 0.30 | 0.068 | Nov 3 AM `verified: false` (web: Nov 4 or Nov 5) | 7/3/0, $11.90 | 7.34 / 11.01 / 10.57 (96% of cap) | Stifel $19 Sep 25 (rating not shown); Jefferies Buy $16 Aug 13; $11.90 holder unnamed | **DOC COMPLETE, BLOCKED** (date; Stifel rating / $11.90 holder; entry window on/after Oct 22). Max price $0.30. `research_BRSL.md` |
| **TME** | $7.94 | $8C Nov20 | 0.40 / 0.45 | 0.017 | Nov 11 AM `verified: false` | 22/14/0, $9.04 | 10.16 / 15.23 / 6.42 (42%) | Aug 12 cluster: Mizuho Outperform $15, China Renaissance Hold $9.30; **60 days on Oct 11** | **DOC COMPLETE, BLOCKED** (date; fresh dated Buy target after Oct 11; entry window on/after Oct 26). `research_TME.md` |
| **OBDC** | $10.04 | $10C Nov20 | 0.30 / 0.45 | 0.017 | **Nov 4 PM `verified: true`** | 11/2/0, $11.00 | 3.13 / 4.69 / 4.08 (87%) | $11 = Wells Fargo Equal Weight (Hold) May 8; Buy targets $13 from Feb-Jul, all >60 days and set at $11+ | **DOC COMPLETE, BLOCKED ON R4 DATING** (stale floor). Max price $0.47. Ex-div Sep 30, next after expiry. No pending M&A (OBDC II deal terminated Nov 2025). `research_OBDC.md` |
| **ADTN** | $7.625 | $8C Nov20 | 0.50 / 0.75 | 0.07 | Nov 2 PM `verified: false` | 7/2/0, $11 | 10.95 / 16.42 / 14.8 at ask | Aug 5 cluster (Rosenblatt Buy $15, Evercore $11, Craig Hallum $12, Northland $15) is **62 days old**; Needham Buy $14 Jul 23 | **BLOCKED ON R4 DATING** (stale floor), on top of R5 at the ask ($0.75 vs $0.741). No doc. |
| **QUBT** | $7.855 | $8C Nov20 | 0.47 / 0.84 | 0.10 | Nov 13 PM `verified: false` | 5/2/0, $10 | 9.25 / 13.88 / 10.2 at mid | Ascendiant Buy $32 Aug 26 (41 days); Cantor Neutral $10 Aug 11 is the tool low | **CHAIN PASSED AT MID ONLY.** Floor is dated; the gate is R5 at the ask ($0.84). No doc until the ask is <= $0.741. |
| COUR | $5.115 | $5C Nov20 | 0.50 / 0.75 | | Oct 22 PM `verified: false` | 8/4/0, $6.00 | | BMO $6 Oct 5 (dated) | Unchanged: date gate + ask $0.75 > $0.741. |

**Other queue names (ratings only):** MLCO 11/4/0 low $5.30, PCT 3/3/0 low $6, ENVX 7/3/1 low $5, BXMT 5/4/0 low $16, CWH 11/2/0 low $6. Unchanged.

## Findings worth carrying

- **Entry timing is a real variable for ramp trades on low-IV names.** On BRSL (IV 36%) and TME (IV 40%), a flat stock bought a month out loses about as much to theta as the IV ramp gives back. Bought ~2 weeks before the print, the ramp outruns the decay. Both docs now carry an entry window (BRSL on/after Oct 22, TME on/after Oct 26, OBDC on/after Oct 21). That's a doc-level decision, not a binder rule; if it holds up across closes, it's a sweep agenda item.
- **R6 sets a lower max price than R5 on two names:** BRSL $0.30, OBDC $0.47. The R5 line ($0.741) isn't the binding cap there.
- **Stale floors are the most common block now:** OBDC and ADTN join PCT, MLCO and ENVX. Five names on the queue wait on an analyst publishing something.

## GLOSSARY

- **R1-R6:** the six calls Iron Rules (binder Tab 1): range percentile, earnings before expiry, ratings, bear floor, chain price, reachability.
- **Floor dating:** binder Tab 6 (Jul 10): a Rule 4 target counts only if it's dated within 60 days and was set after the decline.
- **Max price:** the highest ask at which both R5 and R6 still pass.
- **Entry window:** the earliest date a doc allows a buy, set so theta from entry to the ramp-sell deadline stays smaller than the expected IV ramp.
- **Theta / vega:** daily time decay / gain per one-point rise in implied volatility.
- **verified: false:** the earnings date is a data vendor's estimate, not the company's announcement.
- **Stale floor:** an analyst target set before the latest drop or more than 60 days ago.
