# SCREENING LOG: Mon Oct 26, 2026, EVENING 3 (10:00pm ET)

*Market closed; stock quotes are Monday's close or after-hours, option quotes are the closing book. EVENING 3's job is the refill. The five Oct24 SAT sweep scans were already diffed at 6pm on post-close data, so re-running them now would return the same rows. Two new sources instead: a **slide-in band** (R1 0.25-0.29, names one bad day from the bottom quartile) and the **January print window** (bottom quartile, prints Dec 24 - Feb 12). 0 searches.*

## Held (fact check)

| Contract | Close quote | Stock | Earnings | Ratings / low vs BE | Verdict |
|---|---|---|---|---|---|
| COUR $5C Nov20 | 0.40 / 0.55 (OI 3,257, IV 95%) | $4.97 close, AH $4.98 | Thu Oct 29 PM `verified: true`, `actual: null` | 8/4/0, low $6.00 vs BE $5.65 | Nothing changed. Ramp sell Thu Oct 29 3:35pm (window opens Wed). GTC $1.65 `confirmed`. |
| QUBT $7C Dec18 | 0.31 / 0.66 (OI 1,170) | $6.41 close, AH $6.46 | Mon Nov 9 PM `verified: true`, `actual: null` | 5/2/0, low $10 vs BE $7.54 | Nothing changed. Ramp sell Mon Nov 9 3:35pm. GTC $1.35 `confirmed`. |

## Source 1: slide-in band (new saved scan)

`Baxter Oct26 E3 slide-in R1 0.25-0.29 Oct28-Dec23 prints` (`696cbe51-64eb-4fd9-8bbf-8e018808e4e5`): cap >= $0.3B, stock >= $1, prints Oct 28 - Dec 23, range pct 0.25-0.29, call volume >= 300. **25 rows.** Already killed or queued this month (not re-worked): SANM, POWL, CAMT (R6/R7 Sat), MSTR (R1), O, CAG, HRL, RXRX (R3), AUR (R4 proxy), AQST (R6+R7), ITUB (no coverage), OUST (on the queue).

| Ticker | Range pct | Print | Ratings / low | Check | Verdict |
|---|---|---|---|---|---|
| ONON | 0.271 | Nov 12 | 27/5/1, low $20.14 (stamp Sep 24) vs $33.06 | R4 proxy | **KILLED, R4** (low under the stock) |
| SBET | 0.262 | Nov 11 PM (unverified; LY Nov 12) | 7/0/0, low $8 vs $7.20 | Dec18 chain: $7C 0.87 / 1.05 (OI 77, BE $8.05 at ask); $8C 0.40 / 0.66 (OI 516, BE $8.66) | **KILLED, R4** (low $8 under every listed BE; $7C also R7) |
| APO | 0.266 | Nov 3 AM | 19/6/0, low $127 | 2.15% print median (Oct logs) | **KILLED, R6 structural** |
| HUBS | 0.287 | Nov 5 | 13/23/2 | R3 | **KILLED, R3** (Holds > Buys, 2 Sells) |
| INMD, RXT, HIMX, FSM, INOD, PSIX | 0.25-0.29 | Nov 4-9 | none | R3 | **KILLED, no coverage** |
| TEX, EGO | 0.28 / 0.27 | Oct 28 | 10/4/1 low $58; 8/4/1 (stamp 2019) | timing | **Dropped:** print is Wednesday, nothing to ramp |
| AAOI | 0.255 | Nov 5 PM | 6/3/0, low $92 | prior | Already **KILLED R7** Oct 22 (Dec18 $70C OI 75). Not re-worked. |

## Source 2: January prints (preview, not saved)

Prints Dec 24 - Feb 12, bottom quartile, call volume >= 300: **37 rows.** 25 were already through a week-09 log (AA, AAL, AGNC, ALK, APLD, CALM, CMCSA, DECK, F, FLG, HBAN, LAZ, MKC, NG, ORC, PCG, PLD, QS, ROL, SHAZ, T, TLRY, TSCO, TTMI, XRPN). The other 12:

| Ticker | Range pct | Print | Ratings / low | Check | Verdict |
|---|---|---|---|---|---|
| GE | 0.168 | Jan 22 | 22/2/2 | R3 | **KILLED, R3** (2 Sells) |
| NOK | 0.241 | Jan 28 | 26/6/4 | R3 | **KILLED, R3** (4 Sells) |
| INFY | 0.116 | Jan 14 | 23/23/5 | R3 | **KILLED, R3** |
| NFLX | ~0 | Jan 20 | 33/16/2 | R3 | **KILLED, R3** (2 Sells) |
| PEP | 0.245 | Feb 3 | 8/16/1 | R3 | **KILLED, R3** (Holds > Buys) |
| SCHW | 0.190 | Jan 21 | 19/6/1, low $82 vs $89.78 | R4 proxy | **KILLED, R4** |
| LVS | 0.041 | Jan 28 | 17/7/0, low $37 vs $36.48 | R4 proxy | **KILLED, R4** (+1.4% of room, no call fits) |
| AXP | 0.249 | Jan 29 | 17/16/0, low $320 vs $314.98 | R4 proxy | **KILLED, R4** |
| CBRE | 0.023 | Feb 11 AM (unverified; LY Feb 12) | 13/2/0, low $158 vs $122.89 | Print median from the last 6 verified prints: +7.84, +0.26, -8.84, -2.74, +0.50, -2.53 -> **2.64%**, R6 cap 3.96%. Mar19 is the first expiry passing R2 (Feb 12 + 21 = Mar 5). A Mar19 call within +4% of $123 would need a premium under ~$5 on an ATM strike 4.5 months out. | **KILLED, R6 structural** |
| FR | 0.063 | Feb 3 PM | 10/7/0, low $58 vs $55.19 | Print median (5 prints): 1.40, 2.24, -0.79, -2.04, -6.92 -> **2.04%**, cap 3.06% | **KILLED, R6 structural** |
| NLY | 0.081 | Jan 28 | 9/4/0, low $19.50 vs $18.26 | mREIT, print moves ~1-2% | **KILLED, R6 structural** (proxy) |
| BAC | 0.235 | Jan 14 | 23/5/0, low $55 | prior R6 kill (money-center bank, ~1.5% medians) | **KILLED, R6 structural** |

## Queue (re-pulled ratings, no change)

XP 12/1/0 low $22.87; ARCO 9/2/0 low $8.55; MELI 22/6/0 low $1,750 (stamp Oct 26 18:31Z); AFYA 4/3/1 low $11.26; ZVRA 9/0/0 low $20; TTWO 29/1/1 low $270 (stamp Aug 7). Identical to 8pm. Still parked on their gates.

**Names moved: 25** (13 slide-in, 12 January). **Killed: 25. Advanced: 0.** The queue stays 7 live + 3 watch. It's under 10, and I can't fix that honestly tonight: both new sources came back with nothing that survives R3/R4/R6. The fix is the slide-in scan as a daily diff (anything crossing 0.25 with coverage gets screened) and Saturday's full sweep.

## GLOSSARY

- **R1-R7:** the Iron Rules, binder Tab 1. R1 range percentile (bottom 25%), R2 earnings before expiry with the 21-day cushion, R3 Buy consensus (<= 1 Sell, >= 3 Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 price vs the conviction-tier cap, R6 required move <= 1.5x the median print reaction, R7 OI >= 250 and spread <= 25% of mid.
- **Range pct:** where the stock sits in its 52-week range, 0 = at the low, 1 = at the high.
- **Slide-in band:** stocks at 0.25-0.29 of their range, just above the bottom quartile. Not buyable under R1; watched so a name that slips under 0.25 gets screened the same evening.
- **R4 proxy:** the free version of Rule 4 at the screen: if the lowest Buy target is at or under the stock, no call's breakeven can be under it.
- **R6 structural:** the stock's typical earnings move is so small (2-3%) that no listed call can reach breakeven on one print.
- **Print median:** the median absolute close-to-close move across a company's recent earnings reports (AM reports: prior close to that day's close; PM: that day's close to the next).
- **mREIT:** a mortgage real-estate investment trust; prices track book value and barely move on earnings.
