# SCREENING LOG — Wed Oct 7, 2026, 6:00pm ET (VM EVENING, session 1 of 3)

**Source:** research_queue.md plan written by LASTCALL (3:35pm) and confirmed by WRAP: date checks on COUR / QUBT / ONDS, floor-dating on the blocked names (one look each), then a fresh scan for prints **Nov 20 - Dec 17**. Scan (preview, not saved): market cap $300M+, stock, price $2-15, earnings Nov 20 - Dec 17, 52-week range percentile < 0.25 (same expression filter as the Oct 5 sweep). **56 matches, all returned.** Dropped 10 closed-end funds / SPACs / zero-volume rows (NBB, NXP, AWF, EVV, TLNC, FCRS, SAC, SAAQ, MEVO, HDL), deduped the rest against this week's research files, passes.md and research_queue.md: **36 new names** (10 already seen: ASPI, BULL, BV, MNSO, MOMO, RERE, SHOE, VIPS, VNET, ZKH).

**Rule 5 line this run:** reserve = spendable $741.32 (unsettled $0.00). 3.5/5 line **$0.741**, 4/5 $1.00 (lock), screen $1.00.

## Summary

| Step | Count | Tool |
|---|---|---|
| Dates (queue) | COUR, QUBT, ONDS, BRSL | get_earnings_results |
| Ratings (queue) | 18 names, no count or low-target changes | get_equity_analyst_ratings (1 call) |
| Floor dating (queue) | TDUP, FRMI, BRSL, ADTN, MLCO, ENVX, PCT, TME (MarketBeat forecast pages); GAU, FRMI, TDUP, COUR date, BRSL date, Stifel/BRSL, Susquehanna/MLCO (web searches) | WebFetch (8), WebSearch (8) |
| Scanner | 1 preview scan, 36 new names | preview_scan |
| R3 / R4 proxy | 36 names, 14 survive | get_equity_analyst_ratings (1 call) |
| Dates + print count | 14 survivors | get_earnings_results |
| Chains | 8 names (Dec18 where listed, else Jan15 / Feb19) | get_option_chains, get_option_instruments, get_option_quotes |
| R6 history | PONY, WRD (4 AM prints each) | get_equity_historicals |
| Killed | **35** (21 R3, 1 R4 proxy, 5 print history, 1 R2 timing, 7 chain stage) | |
| Advanced | **WRD** (chain passed at mid only) | |
| Queue status changes | **BRSL floor gate cleared** (Stifel Buy $19, Sep 25); BRSL now fails R6 at the ask on today's lower price | |

## Queue gates

| Ticker | Stock | Contract | Bid / Ask | Ratings / low | Status |
|---|---|---|---|---|---|
| COUR | $5.115 | $5C Nov20 | 0.55 / 0.70 | 8/4/0, $6.00 | Oct 22 PM still `verified: false`. One search: no Coursera Q3 announcement yet (aggregators show Oct 22 PM). Passes R5 at the ask. |
| QUBT | $7.625 | $8C Nov20 | 0.51 / 0.64 | 5/2/0, $10 | Nov 13 PM `verified: false`. Max price stock x 1.1388 - 8.00 = $0.683; passes. |
| ONDS | $7.21 | $8C Nov20 | 0.45 / 0.49 | 11/0/0, $13 | Nov 12 AM `verified: false`. Max price $0.716; passes. |
| BRSL | $10.055 | $11C Nov20 | 0.10 / 0.20, OI 61 | 7/3/0, $11.90 | **Floor gate cleared** (below). Nov 3 AM `verified: false`. **R6 at today's price: max BE 10.055 x 1.1101 = $11.16; ask BE $11.20 fails by 4 cents, mid BE $11.15 passes. Max price now $0.16.** |
| TDUP | $2.23 | $2.5C Nov20 | (not requoted) | 6/1/0, $5.70 | Still blocked. MarketBeat: newest Buy-side actions are Roth Buy $6.50 and Telsey Outperform $6 (both Aug 6, 62 days old); the $5.70 is TD Cowen Buy, May 5. Nothing dated after Aug 8. |
| FRMI | $3.965 | $4C Nov20 | (not requoted) | 6/2/0, $6 | Still blocked. MarketBeat's newest is Weiss Sell (Aug 14); last Buy-side target Mizuho Outperform $11 (Jul 28, 71 days). |
| GAU | $1.96 | $2C Nov20 | (not requoted) | 5/1/0, $2.99 | Still blocked. Search found nothing newer than HCW Buy $4.25 (Feb 19). |
| ADTN | | $8C Nov20 | | 7/2/0, $11 | Still blocked. Only post-Aug 8 actions: Zacks Hold (Oct 5), Weiss Sell (Sep 16). |
| MLCO | | $4C Nov20 | | 11/4/0, $5.30 | Still blocked. Susquehanna Positive $7 (Aug 14) is inside 60 days but was set at $5.60, before the drop to ~$4.2, so it fails the "set after the decline" half of Tab 6. Same verdict as Oct 6; ages out Oct 13 anyway. |
| ENVX | | $3C Nov20 | | 7/3/1, $5 | Still blocked. Post-Aug 8: TD Cowen upgrade to Hold (Oct 5), Weiss Sell. No Buy target. |
| PCT | | $4C Nov20 | | 3/3/0, $6 | Still blocked. Cantor Overweight $12 is Aug 7 (61 days). |
| TME | $8.00 | $8C Nov20 | | 22/14/0, $9.04 | Still blocked after Oct 11. Only post-Aug 8 action is Weiss Hold (Sep 28). |

**BRSL floor dating.** MarketBeat lists Stifel (Jeffrey Stantial) "set target $19.00" on **Sep 25, 2026**, with no rating shown. Stifel has carried a Buy on Brightstar without a break: "reaffirmed a buy rating and issued a $19.00 price target (down from $20.00) ... on Wednesday, May 13th," then "Maintain" Buy $19 on Jun 4. No Stifel downgrade appears anywhere. Treating Sep 25 as **Stifel Buy $19, 12 days old, set with the stock ~$10.5, after the slide.** This is an inference from an unbroken Buy record; I didn't find a page that quotes the rating on the Sep 25 note itself. Also on file: Jefferies upgrade Hold -> Buy $16 (Aug 13; ages out Oct 12). The tool's $11.90 low is still unnamed, but it's the lowest target of any rating, so the lowest Buy is at least $11.90 > $11.15 mid breakeven. **Gate (2) in `research_BRSL.md` is closed.** Gate (1), the company date, is still open.

## New names (Nov 20 - Dec 17 prints)

### Killed at the free screen (22)

| Ticker | Price | Ratings | Kill |
|---|---|---|---|
| ABTC | $8.22 | none | R3: no coverage |
| BTQ | $3.10 | none | R3: no coverage |
| FWDI | $7.57 | none | R3: no coverage |
| HTT | $2.26 | none | R3: no coverage |
| IMSR | $3.67 | none | R3: no coverage |
| LE | $10.63 | none | R3: no coverage |
| NKLR | $3.41 | none | R3: no coverage |
| NOAH | $7.73 | none | R3: no coverage |
| OWLS | $5.43 | none | R3: no coverage |
| SCZM | $8.45 | none | R3: no coverage |
| SPIR | $10.63 | none | R3: no coverage |
| VZLA | $3.42 | none | R3: no coverage |
| YB | $12.01 | none | R3: no coverage |
| CXM | $5.19 | 4/5/1 | R3: Holds > Buys |
| EH | $4.15 | 2/4/2 | R3: 2 Sells |
| FLNC | $7.69 | 4/15/5 | R3: 5 Sells |
| GEMI | $4.54 | 3/5/2 | R3: 2 Sells |
| LI | $10.99 | 13/14/2 | R3: 2 Sells, Holds > Buys |
| SFIX | $2.70 | 1/5/0 | R3: 1 Buy |
| WOOF | $2.22 | 2/8/2 | R3: 2 Sells |
| YSS | $7.44 | 5/7/0 | R3: Holds > Buys |
| PHR | $10.50 | 10/8/0, low $10 | R4 proxy: low $10 < price |

### Past R3 (14)

| Ticker | Price | Ratings / low | Next print (tool) | Prints on record | Result |
|---|---|---|---|---|---|
| AGMB | $8.80 | 8/0/0, $27.25 | Nov 14 AM, unverified | 0 reported | **Killed, R6: no print history** (every row `actual: null`) |
| BTGO | $7.26 | 11/2/0, $7.50 | Nov 26 AM, unverified | 3 | **Killed, R6: 3 prints** (ZURA precedent); R4 proxy also thin ($7.50 vs $7.26) |
| EIKN | $7.50 | 5/0/1, $4.00 | Nov 6 PM, unverified | 3 | **Killed, R6: 3 prints** |
| GENB | $13.57 | 6/0/0, $22 | Nov 3 PM, unverified | 2 | **Killed, R6: 2 prints** |
| INFQ | $11.686 | 6/0/0, $19 | Nov 28 PM, unverified | 1 | **Killed, R6: 1 print** |
| GLOO | $3.91 | 6/0/0, $7 | **Jan 13 2027** PM, unverified | 4 | **Killed, R2 timing:** tool puts the print after any Dec/Jan15 window the scanner implied (scanner said Dec 17) |
| CLSK | $11.55 | 15/0/0, $21 | Nov 24 PM, unverified | 6 | **Killed, R5:** Dec18 $12C 1.40 / 1.51, $13C 1.04 / 1.51; the ask is double the line two strikes out |
| NIO | $3.54 | 16/7/1, $3.90 | Nov 24 AM, unverified | 6 | **Killed, R4:** no Dec18; Jan15 $3.5C 0.40 / 0.43, BE $3.93 > $3.90 low (at the bid, BE = the low) |
| TIGR | $4.42 | 7/0/1, $4.61 | Dec 3 AM, unverified | 6 | **Killed, R4:** no Dec18; Jan15 $4.5C 0.44 / 0.53, BE $5.03 > $4.61 |
| UEC | $9.48 | 8/3/0, $10 | Dec 9 AM, unverified | 6 | **Killed, R4 + R5:** no Dec18; Jan15 $10C 1.10 / 1.21, BE $11.21 > $10 low |
| PFLT | $6.74 | 5/2/0, $9 | **Nov 23 PM, verified** | 6 | **Killed, R6 + liquidity:** only Nov20 / Feb19; Feb19 $7.5C no bid / 0.15, needs +13.5% on a BDC (prints move 1-3%) |
| MPLT | $9.37 | 11/3/0, $13 | Dec 3 AM, unverified | 4 | **Killed, liquidity:** only Nov20 / Feb19; Feb19 $10C 0.35 / 3.90, OI 4 |
| PONY | $6.07 | 18/1/0, $10 | Nov 24 AM, unverified | 6 | **Killed, R6:** no Dec18, no $7C; Jan15 $7.5C 0.36 / 0.54, OI 873, BE $7.95 at mid = +31%. Prints (AM, prior close -> print-day close): Nov 25 2025 +5.88, Mar 26 -14.66, May 26 +4.71, Aug 18 -2.94. Median 5.30%, cap 7.94%. |
| **WRD** | $4.965 | 13/0/0, $10.51 | Nov 23 AM, unverified | 6 | **ADVANCED, chain passed at mid only.** No Dec18; Jan15 $5C (id a952b2ab-f6b2-4f87-a097-676a4c35b72a) 0.55 / 0.75, OI 2,263. Prints (AM): Nov 24 2025 +14.72, Mar 23 +8.98, May 13 -0.78, Aug 12 -9.64. Median 9.31%, cap 13.97%, max BE $5.66. Mid $0.65 -> BE $5.65, +13.8% (99% of cap). Ask $0.75 fails R5 (> $0.741) and R6. **Max price = stock x 1.1397 - 5.00 ($0.659 at $4.965).** R1 0.004. Floor undated. |

**What the Dec-print scan taught:** most small and mid names don't list a Dec 18 expiry at all. PONY, WRD, NIO, UEC, TIGR jump from Nov 20 to Jan 15; PFLT and MPLT from Nov 20 to Feb 19. Only CLSK had Dec 18. So a late-November print means a Jan or Feb contract, with 7-11 weeks of extra time premium in the price. That's why NIO and TIGR, which would have been close on a Dec contract, died on R4 at the Jan15 ask. Future Dec-print scans should check `get_option_chains` expirations first, before any strike lookup.

## GLOSSARY

- **R1-R6:** the Iron Rules (binder Tab 1). R1 bottom of the 52-week range; R2 confirmed earnings before expiry; R3 Sell count and Buy consensus; R4 lowest Buy target above breakeven, dated within 60 days and set after the decline; R5 ask under the sizing line; R6 breakeven move no more than 1.5x the median earnings move.
- **R4 proxy:** at the free screen, the tool's lowest target (any rating) against the stock price. If even the lowest target is below the price, no OTM call can pass R4.
- **Floor dating:** finding who set the lowest Buy target, and when, to check the 60-day / after-the-decline rule.
- **BE (breakeven):** strike + premium paid.
- **Cap (R6):** 1.5 x the median absolute earnings-day move over the last 4 prints.
- **Max price:** the highest premium that keeps BE under the R6 cap: stock x (1 + cap) - strike.
- **Chain passed at mid only:** the contract passes at the bid/ask midpoint but not at the ask; it needs a fill at or under the max price.
- **AM / PM print:** before the open / after the close. For AM prints the move is prior close -> print-day close; for PM prints, print-day close -> next close.
- **OI:** open interest, contracts outstanding.
- **Jan15 / Feb19 / Dec18 / Nov20:** option expiration dates (2027-01-15, 2027-02-19, 2026-12-18, 2026-11-20).
- **BDC:** business development company (lends to private firms; its stock barely moves on earnings).
