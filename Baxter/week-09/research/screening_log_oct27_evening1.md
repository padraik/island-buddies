# SCREENING LOG: Tue Oct 27, 2026, EVENING 1 (6:00pm ET)

*Market closed; stock quotes are Tuesday's close or after-hours, option quotes are the closing book (~3:59pm). Sources: the slide-in scan `696cbe51` and the five Oct24 SAT sweep scans re-run as a diff against every week-09 log, plus the live queue. 1 search (TTWO floor).*

## Held (fact check)

| Contract | Close quote | Stock | Earnings | Ratings / low vs BE | Verdict |
|---|---|---|---|---|---|
| COUR $5C Nov20 | 0.20 / 0.35 (OI 3,357, IV 78%, closing-minute quote) | $4.745 close, AH $4.88 | Thu Oct 29 PM `verified: true`, `actual: null` | 8/4/0, low $6.00 vs BE $5.65 | Nothing changed. Sell window opens Wed; hard deadline Thu Oct 29 3:35pm. GTC $1.65 `confirmed`. |
| QUBT $7C Dec18 | 0.56 / 0.70 (OI 1,175) | $6.885 close, AH $6.90 | Mon Nov 9 PM `verified: true`, `actual: null` | 5/2/0, low $10 vs BE $7.54 | Nothing changed. Ramp sell Mon Nov 9 3:35pm. GTC $1.35 `confirmed`. |

## Source 1: the scans (diff)

- Slide-in `696cbe51` (R1 0.25-0.29): 27 rows. 25 already through a week-09 log; 2 new (SGHC, BLZE). Nearly every row was **up** on the day (AVGO +3.9%, FLEX +9.4%, QURE +15.3%): Tuesday's rally carried names up out of the bottom quartile, not down into it.
- Oct24 SAT scans (bottom quartile, prints Oct 28 - Dec 23): 40 + 236 + 393 + 395 + 397 rows (each capped at 200 returned; the price bands overlap, so the cascade covers the truncated tails). 809 distinct names; **5 never logged** this week (BSRT, NTES, ORIC, PAM, REAX).

| Ticker | Range pct | Print | Ratings / low | Check | Verdict |
|---|---|---|---|---|---|
| BSRT | 0.161 | Nov 11 | no coverage | R3 | **KILLED, no coverage** |
| SGHC | 0.284 | Nov 3 PM verified | 8/1/0, low $13 vs $10.55 | R1 | **KILLED, R1** (MID-OUT at 0.284) |
| BLZE | 0.289 | Nov 2 PM verified | 6/1/0, low $21 vs $9.24 | R1 | **KILLED, R1** (MID-OUT at 0.289) |
| NTES | 0.187 | Nov 19 AM (unverified; LY Nov 20), 6-K filer | 36/2/0, low $132.93 (stamp Oct 3) vs $114.08 | Dec18 $115C 5.40 / 8.20, **OI 19**; Jan15 $115C 5.70 / 8.90, **OI 71** | **KILLED, R7** (both expiries; spreads 41% / 44%) |
| ORIC | 0.238 | Nov 12 PM (unverified; LY Nov 13) | 15/1/0, low $14 vs $9.00 | Dec18 $9C 0.10 / 4.90 and $10C 0.35 / 4.80, **OI 0**; Jan15 $10C 0.85 / 4.80, **OI 9** | **KILLED, R7** |
| PAM | 0.240 | Nov 2 PM verified | 8/2/0, low $100 vs $75.38 | Dec18 $80C 1.25 / 4.70, **OI 96** | **KILLED, R7** |
| REAX | 0.074 | Nov 5 AM verified | 7/0/0, low $35 vs $15.29 | Dec18 $15C 0.80 / 3.90 (**OI 1**), $17.5C 0.65 / 1.50 (**OI 47**) | **KILLED, R7** |

## Source 2: the live queue

| Ticker | Stock | Check | Verdict |
|---|---|---|---|
| XP | $15.955 (+1.6%) | **Gate 1 passed:** Dec18 now lists $1-$19 strikes (Monday it started at $20). Quotes: $16C 1.30 / 1.45, $17C 0.90 / 1.05, $18C 0.55 / 0.75, $19C 0.35 / 0.55, all **OI 0** (new listings). Print median from the last 6 verified prints (all PM, close to next close): +0.48, -8.57, +1.93, +0.51, -3.86, +0.89 -> **1.41%**, R6 cap 2.1%. Cheapest BE needs +9.4% ($16C at the ask). Tool low $23.145 (12/1/0). | **KILLED, R6 structural** (and R7 today). The crash made the range pct, it didn't make the stock move on prints. |
| ARCO | $6.99 | Dec18 $7.5C 0.00 / 0.90, **OI 2** | **KILLED, R7** |
| MELI | $1,681.95 | Q3 Wed Nov 4 PM verified -> Nov20 fails R2 (Nov 25 cushion), Dec18. $1,600C 150.00 / 163.40 (**OI 43**, BE $1,763.40 > low $1,750, R4 fails too); $1,500C 215.40 / 231.90 (**OI 24**, BE $1,731.90). Print median 4.81% (5 prints). Tool stamp refreshed Oct 27 04:32Z, low unchanged at $1,750. | **KILLED, R7** (every strike that passes R4 is thin) |
| AFYA | $10.81 | Dec18 $10C 0.00 / 4.90 (**OI 0**), $12.5C 0.00 / 4.90 (**OI 2**) | **KILLED, R7** |
| ZVRA | $10.05 (+5.5%) | Dec18 $10C 0.80 / 1.80 (OI 632, spread 77%), $11C 0.45 / 1.10 (OI 1,123, 84%), $12C 0.30 / 0.85 (OI 1,377). 9/0/0, low $20. Closing spreads, so R7 isn't a fair read at the close. R6 line on the $10C (BE <= ~$11.12 per Monday's median) means an ask <= ~$1.10; closing ask is $1.80. | **Parked, R6/R7.** Print Mon Nov 3 PM: a buy would have at most 4 sessions to its ramp. If it isn't a doc by Thursday, it's dead for the quarter. |
| TTWO | $201.28 | Tool 29/1/1, low $270, stamp still **Aug 7** (81 days). 1 search: newest dated action found is an Oct 8 Buy raised to $300; nothing dates the $270 low. | **Parked, R4 dating** (paper-only). Saturday decides: dated or dropped. |
| OUST | $32.80 (+10.4%) | R1 re-entry line was <= ~$28.25 | **Moved to watch** (R1 out) |
| ONDS / BTBT / CLSK | $6.64 / $0.918 / $8.185 | Watch lines >= ~$6.90 / >= ~$1.10 / > ~$9.20 | **Watch**, none crossed |

**Names moved: 17. Killed: 11** (XP R6; ARCO, MELI, AFYA, NTES, ORIC, PAM, REAX R7; SGHC, BLZE R1; BSRT no coverage). **Advanced: 0.** Queue after: 2 live (ZVRA, TTWO) + 4 watch (OUST, ONDS, BTBT, CLSK). The Brazil cluster is done: XP died on R6, the other three on liquidity. EVENING 2 has no doc to write, so it starts EVENING 3's refill.

## GLOSSARY

- **R1-R7:** the Iron Rules, binder Tab 1. R1 range percentile (bottom 25%), R2 earnings before expiry with the 21-day cushion, R3 Buy consensus (<= 1 Sell, >= 3 Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 price vs the conviction-tier cap, R6 required move <= 1.5x the median print reaction, R7 OI >= 250 and spread <= 25% of mid.
- **Range pct:** where the stock sits in its 52-week range, 0 = at the low, 1 = at the high.
- **MID-OUT:** range pct between 0.25 and 0.75; no direction, no play.
- **Slide-in band:** stocks at 0.25-0.29 of their range, watched so a name that slips under 0.25 gets screened the same evening.
- **R6 structural:** the stock's typical earnings move is so small that no listed call can reach breakeven on one print.
- **Print median:** the median absolute close-to-close move across a company's recent earnings reports (PM reports: that day's close to the next).
- **OI (open interest):** contracts outstanding on that exact strike and expiry. New strikes start at 0.
- **6-K filer:** a foreign company reporting under SEC foreign-issuer rules; no 10-Q deadline, so Rule 2 needs both the tool date and last year's date.
- **Gate 1 / Gate 2 (XP):** the two conditions set Monday: strikes low enough to be reachable get listed, and a post-crash Buy target with a date.
