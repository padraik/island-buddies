# SCREENING LOG — Wed Oct 7, 2026, 10:00pm ET (VM EVENING, session 3 of 3)

**Source:** research_queue.md plan written by EVENING 2 (8:00pm): refill from a **$2-15 scan with prints Dec 18 - Jan 8** (Jan15 contracts), then leave PREMARKET a plan. Plus one question from Michael that turned into the session's real work: for names whose date won't be confirmed in time, is the next expiry out affordable, one that sits safely past any realistic report date?

**Rule 5 line this run:** reserve = spendable $741.32 (unsettled $0.00). 3.5/5 line **$0.741**, 4/5 $1.00 (lock), screen $1.00.

## Summary

| Step | Count | Tool |
|---|---|---|
| Scanner | 1 preview scan: $2-15, prints Dec 18 - Jan 8, bottom quartile, $300M+ | preview_scan |
| Scan result | **2 rows, both closed-end funds (EAD, HIX). Nothing usable.** | |
| Dates (queue) | COUR, QUBT, ONDS, BRSL, TME, WRD, with last year's same-quarter date | get_earnings_results (6) |
| Next-out expiry check | WRD Apr16, QUBT Dec18, ONDS Dec18, TME Jan15, BRSL Jan15 | get_option_chains, get_option_instruments, get_option_quotes |
| Ratings (queue) | 20 names, no count or low-target changes | get_equity_analyst_ratings (1 call) |
| Killed | 0 names (2 contract variants failed: WRD Apr16, QUBT Dec18, BRSL Jan15) | |
| Advanced | **ONDS Dec18 $8C** passes R5/R6 (at mid on the official close, at the ask on the $7.21 last) | |

**The Dec 18 - Jan 8 window is a holiday dead zone.** Almost nobody reports then. With the Oct 20 - Nov 20 pool fished out at $2-15 and the Nov 20 - Dec 17 and $15-25 passes done, the scanner has no fresh bottom-quartile names under $15 until the January print season. The queue (19 names) is now gated on dates and floors, not on sourcing.

## Next expiry out (Michael's question, Oct 7 9:17pm ET)

"Safe" = expiry past last year's same-quarter date, the tool date, and the 10-Q deadline (Q3 ends Sep 30: Nov 9 for accelerated filers, Nov 16 for others, +5 days on an NT 10-Q).

| Ticker | Tool date | Last year's Q3 | Doc contract | Margin past tool date | Next out | Next-out quote | Verdict |
|---|---|---|---|---|---|---|---|
| COUR | Oct 22 PM | Oct 23, 2025 PM | $5C Nov20 | 29 days | Jan15 | (not needed) | Nov20 is already safely past. Ask 0.70 passes R5. |
| BRSL | Nov 3 AM | Nov 4, 2025 AM | $11C Nov20 | 17 days | Jan15 $11C | 0.10 / 0.85, mid BE $11.475 | Nov20 already safely past. Jan15 fails R6 (max BE $11.16). |
| WRD | Nov 23 AM | Nov 24, 2025 AM | $5C Jan15 | 53 days | Apr16 $5C | 0.55 / 1.40, OI 6 | **Jan15 already is the next-out contract** (no Dec expiry listed). Apr16 fails R5 and R6 (mid BE $5.975 vs max $5.66). |
| QUBT | Nov 13 PM | Nov 14, 2025 PM | $8C Nov20 | 7 days | Dec18 $8C | 0.75 / 0.77, OI 1,298 | Dec18 fails R5 at the bid (0.75 > 0.741) and R6 (max price $0.683 at $7.625). Nov20 stays the only fit. |
| ONDS | Nov 12 AM | Nov 13, 2025 AM | $8C Nov20 | 8 days | **Dec18 $8C** (id cfbc25b7-60bc-43e8-84dd-501ae271ec7f) | **0.64 / 0.71, OI 37,404** | **Passes.** Max price = stock x 1.2089 - 8.00: $0.716 at $7.21 last (ask passes), $0.692 at the $7.19 official close (mid $0.675 passes). Under the R5 line. $9C BE $9.45 fails R6. |
| TME | Nov 11 AM | Nov 12, 2025 AM | $8C Nov20 | 9 days | Jan15 $8C | 0.60 / 0.85, OI 1,033 | Mid $0.725 passes R5 and R6 (BE $8.725 vs ~$9.07 max); ask fails R5. Still floor-blocked, so moot for now. |

**What this shows:** for COUR, BRSL and WRD the contract in the doc already sits 2-8 weeks past every realistic date. The thing blocking them isn't the expiry, it's the binder reading Rule 2 as "the company has announced the date" (`verified: true`). For ONDS, the Dec18 contract removes the only real timing risk on the Nov20 (a late filing), at about $0.20 more per contract.

## Queue gates (ratings unchanged on all 20)

| Ticker | Stock (last) | Contract | Bid / Ask | Ratings / low | Status |
|---|---|---|---|---|---|
| COUR | $5.115 | $5C Nov20 | 0.55 / 0.70 | 8/4/0, $6.00 | Oct 22 PM `verified: false`. Passes R5 at the ask. |
| QUBT | $7.625 (AH $7.69) | $8C Nov20 | 0.51 / 0.64 | 5/2/0, $10 | Nov 13 PM `verified: false`. Max $0.683. |
| ONDS | $7.21 | $8C Nov20 / Dec18 | 0.45 / 0.49 / 0.64 / 0.71 | 11/0/0, $13 | Nov 12 AM `verified: false`. Both pass. |
| BRSL | $10.055 | $11C Nov20 | 0.10 / 0.20 | 7/3/0, $11.90 | Nov 3 AM `verified: false`. Max $0.16, mid only. |
| WRD | $4.965 | $5C Jan15 | 0.55 / 0.75 | 13/0/0, $10.51 | Nov 23 AM `verified: false`. Max $0.659, mid only. Floor ages out Oct 13 / Oct 18. |
| TME | $8.00 | $8C Nov20 | (not requoted) | 22/14/0, $9.04 | Floor ages out Oct 11. |

## GLOSSARY

- **Next expiry out:** the option expiration date after the one in the research doc. Costs more (more time value) but sits further past the earnings date.
- **10-Q deadline:** the SEC deadline for a quarterly report: 40 days after quarter end for larger (accelerated) filers, 45 for smaller ones. An NT 10-Q filing buys 5 more days. A company almost always reports earnings by then.
- **`verified: true`:** the earnings tool's flag meaning the company itself announced the date. `false` means the date is estimated from the company's past pattern.
- **R5 line ($0.741):** the most we can pay per share for one contract at 3.5/5 conviction: 10% of the $741.32 reserve, divided by 100.
- **Max price (R6):** the highest premium that keeps breakeven within 1.5x the stock's median earnings move: stock x (1 + cap) - strike.
- **Mid:** halfway between bid and ask.
- **OI (open interest):** how many contracts of that strike and expiry exist. Higher means easier fills.
- **Bottom quartile:** stock trading in the lowest 25% of its 52-week range (Rule 1).
- **Closed-end fund:** a pooled fund that trades like a stock. No earnings catalyst in our sense; never a candidate.
