# SCREENING LOG — Wed Oct 7, 2026, 8:00pm ET (VM EVENING, session 2 of 3)

**Source:** research_queue.md plan written by EVENING 1 (6:00pm): date checks, WRD floor dating (doc if dated), FINV and OBDC floor checks, then start EVENING 3's Jan15-expiry pass. All four done. Scan (preview, not saved): market cap $300M+, stock, price **$15-25**, earnings **Nov 20 - Jan 8**, 52-week range percentile < 0.25 (Oct 5 sweep expression). **16 matches, all returned, all new this week.**

**Rule 5 line this run:** reserve = spendable $741.32 (unsettled $0.00). 3.5/5 line **$0.741**, 4/5 $1.00 (lock), screen $1.00.

## Summary

| Step | Count | Tool |
|---|---|---|
| Dates (queue) | COUR, QUBT, ONDS, BRSL, WRD | get_earnings_results |
| Ratings (queue) | 19 names, no count or low-target changes | get_equity_analyst_ratings (1 call) |
| Floor dating | WRD, FINV, OBDC (MarketBeat forecast pages) | WebFetch (3) |
| WRD doc | thesis search (Q2 results) | WebSearch (1), get_equity_fundamentals, get_equity_historicals |
| Scanner | 1 preview scan, 16 new names | preview_scan |
| R3 / R4 proxy | 16 names, 6 survive | get_equity_analyst_ratings (1 call) |
| Dates + print count | 6 survivors | get_earnings_results |
| Chains | CHWY Dec18, PL Dec18, NNE Jan15 | get_option_chains, get_option_instruments, get_option_quotes |
| R6 history | CHWY, PL, NNE (6 prints each) | get_equity_historicals |
| Killed | **16** (10 R3, 3 print history, 3 chain stage) | |
| Advanced | none | |
| Docs written | **research_WRD.md** | |

## Queue gates

| Ticker | Stock | Contract | Bid / Ask | Ratings / low | Status |
|---|---|---|---|---|---|
| COUR | $5.115 | $5C Nov20 | 0.55 / 0.70 | 8/4/0, $6.00 | Oct 22 PM still `verified: false`. Passes R5 at the ask. |
| QUBT | $7.625 (AH $7.72) | $8C Nov20 | 0.51 / 0.64 | 5/2/0, $10 | Nov 13 PM `verified: false`. Max price $0.683 at the close; passes. |
| ONDS | $7.21 | $8C Nov20 | 0.45 / 0.49 | 11/0/0, $13 | Nov 12 AM `verified: false`. Max $0.716; passes. |
| BRSL | $10.055 | $11C Nov20 | 0.10 / 0.20 | 7/3/0, $11.90 | Nov 3 AM `verified: false`. Max $0.16; mid only. |
| WRD | $4.965 | $5C Jan15 | 0.55 / 0.75 | 13/0/0, $10.51 | Nov 23 AM `verified: false`. **Floor dated (below). Doc written.** |
| FINV | | $2.5C Dec18 | | 6/1/0, $4.11 | **Still blocked.** MarketBeat: only post-Aug 8 actions are Citi Buy -> Neutral $4.10 (Aug 28) and Weiss Hold -> Sell (Oct 2). Last Buy target UBS $12.10, May 2025. |
| OBDC | $10.025 | $10C Nov20 | | 11/2/0, $11 | **Still blocked.** MarketBeat's newest Buy-side actions are Jul 24 (Lucid Strong Buy, Capital One $13), 75 days. Nothing after Aug 8. |

**WRD floor dating.** MarketBeat forecast page: **Bank of America Buy $10.70 (Aug 14, 2026, reiterated)**, **Morgan Stanley Overweight $12.00 (Aug 19, 2026, reiterated)**; older: HSBC Buy $11.40 (Mar 31), BNP Paribas Exane Outperform $11 (Mar 26), CLSA Outperform $13 (Jan 5), UBS Buy $12 (Aug 2025), Goldman Buy (Apr 16), Citi Buy (Jan 19), no targets on the last two. Weiss Sell (D-) Sep 25 is a quant grade. Post-decline: WRD traded $5.64-6.49 in the weeks of Aug 10 and Aug 17 against a 52w high of $12.405 (Oct 8 2025), so both August targets were set after the slide. Floor is valid tonight and **ages out Oct 13 (BofA) / Oct 18 (MS)**. Doc written with that as an entry gate.

## Jan15-pass scan: 16 names

| Ticker | Stock | Ratings / low | Date (tool) | Prints | Result |
|---|---|---|---|---|---|
| BMNR | $24.665 | no coverage | | | KILLED, R3 |
| ARQQ | $22.70 | no coverage | | | KILLED, R3 |
| HRL | $19.682 | 4/8/0, $23 | | | KILLED, R3 (Holds > Buys) |
| MATW | $19.60 | no coverage | | | KILLED, R3 |
| CPB | $18.92 | 1/14/8 | | | KILLED, R3 (8 Sells) |
| AMTM | $18.80 | 5/7/0 | | | KILLED, R3 (Holds > Buys) |
| CHWY | $18.296 | 22/9/0, $21 | Dec 9 AM, unverified | 6 | **KILLED, R5 + R6 (strike grid).** Prints (AM): -10.98, -16.60, +1.52, +13.30, -2.06, -10.83; median 10.91%, cap 16.36%, max BE $21.29. Dec18 strikes 2.5-wide: $20C 1.02 / 1.13 (bid over the $0.741 line), $22.5C BE > $22.50 > max BE. Also the $21 low sits under any $20C breakeven. |
| AKTS | $18.00 | 9/0/0, $31.25 | Nov 12 AM, unverified | 2 | KILLED, print history (2 prints; also the tool date is before Nov 20, not inside the scan window) |
| DAKT | $17.83 | no coverage | | | KILLED, R3 |
| EQPT | $17.70 | 8/4/0, $22 | Nov 15 PM, unverified | 3 | KILLED, print history (3 prints) |
| PL | $17.70 | 8/3/0, $22 | Dec 9 PM, unverified | 6 | **KILLED, R5 + R4 proxy.** Prints: +49.37, +47.93, +35.01, +25.48, -25.98, -1.25; median 30.49%, cap 45.74%, max BE $25.80 (R6 has room). But Dec18 $20C 1.70 / 1.85, $22C 1.20 / 1.40, $24C 0.70 / 1.05 (mid $0.875) all fail R5; the only strikes that could price under $0.741 ($25C+) put BE above the $22 tool low. **Reopen only if** the $22 holder is a Hold (then the lowest Buy may be above $25.7); one MarketBeat look, not tonight. |
| AEO | $17.39 | 2/14/1 | | | KILLED, R3 |
| OFRM | $16.75 | 5/4/0, $19 | Nov 10 AM, unverified | 3 | KILLED, print history (3 prints) |
| APC | $16.24 | no coverage | | | KILLED, R3 |
| NNE | $16.186 | 7/1/0, $22 | Dec 17 PM, unverified | 6 | **KILLED, R6 + R5.** Prints: +4.53, +1.96, +0.80, -0.63, -9.51, +7.94; median 3.25%, cap 4.87%, max BE $16.97. No Dec18; Jan15 $16C 2.20 / 2.75, $17C 1.95 / 2.30. Nothing fits at any strike. |
| XZO | $15.22 | no coverage | | | KILLED, R3 |

**What this pass taught:** the $15-25 band with late prints is thin (16 rows) and mostly uncovered or Hold-heavy. The two real businesses that cleared R3 (CHWY, PL) both died on price: a $741 fund can't afford near-the-money premium on $18 stocks with 2.5-wide or $1-wide grids two months out. Same structural result as the $12-20 slice on Oct 7. EVENING 3 should go back to the cheap end: **$2-15 with prints Dec 18 - Jan 8** (the Dec-print scan stopped at Dec 17), Jan15 contracts.

## GLOSSARY

- **Range percentile:** where the stock sits between its 52-week low (0) and high (1). Under 0.25 = calls zone.
- **R3 (calls):** at most 1 Sell, at least 3 Buys, Buys >= Holds.
- **R4 proxy:** the tool's lowest target vs our breakeven; a free first pass before dating the actual lowest Buy.
- **R5 line:** the most one contract's ask can cost at the 3.5/5 tier (10% of reserve / 100 = $0.741 tonight).
- **R6 cap:** 1.5x the median absolute earnings-day move; breakeven can't need more than that.
- **Max BE / max price:** stock x (1 + cap) is the highest breakeven R6 allows; minus the strike, that's the most we can pay.
- **Strike grid:** the spacing between listed strikes (1, 2.5, 5 wide). Wide grids leave no strike between "too expensive" and "too far."
- **Print history kill:** fewer than 4 reported prints, so R6 can't be measured.
- **Floor dating:** finding who holds the lowest Buy-side target and when they set it (must be within 60 days and after the decline).
- **Quant grade (Weiss):** a formula rating, not a covering analyst; not counted under R3.
- **Jan15:** the Jan 15 2027 monthly expiry; the first contract covering late-Nov/Dec prints on names that list no Dec18.
