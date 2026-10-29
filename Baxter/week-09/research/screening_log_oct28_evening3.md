# Screening log, Wed Oct 28, EVENING 3 (10:00pm ET)

*Job: refill the queue (2 live + 6 watch going in, under 10) by starting Saturday's sweep early. Reserve for Thursday: $622.24 spendable tonight, ~$657.19 once COUR's $34.95 settles Thu Oct 29, so the 3.5/5 R5 line is ~$0.657. All quotes are Wednesday closing prints (19:59:59 UTC); stock prices are the official close unless marked AH.*

## 1. Source: new saved scan

`Baxter Oct28 E3 early-sweep R1<0.25 Nov2-Feb12 prints callvol>=300` (`e6411b30-10ca-446f-a285-d47a7001c9a4`): market cap >= $300M, prints Nov 2, 2026 - Feb 12, 2027, stock, R1 range pct < 0.25 (in-scanner expression), total call volume >= 300.

- All prices: **290 rows** (the first page returns 200, sorted by price, so it stops at SGML $8.40).
- Re-run at $1 - $8.45 (the band where a $0.657 line can buy anything near the money): **91 rows**.

**Diff against every week-09 screening log and research doc: 0 never-screened names.** Every one of the 91 has been through the funnel at least once since Oct 5. Fished out by name, so the useful work tonight is re-rating and re-chaining the ones whose kill is old enough to have changed.

## 2. Free re-rating (get_equity_analyst_ratings, all 91 + ONDS/RCAT)

**Fail R3 tonight:** NAVI 1/3/2, STNE 10/6/2, SKYD 7/12/8, ARVN 7/8/1, MARA 10/4/2, CAPR 4/6/0, FLO 1/4/1, WU 1/11/9, FLNC 4/15/5, SMR 7/7/4, QFIN 7/3/2, JOBY 2/4/4, LUMN 3/9/2, GT 3/5/1, GTM 3/12/7, QS 0/6/2, ARRY 10/13/0, LCID 3/7/3, GEMI 3/5/2, DNUT 2/2/2, JBLU 0/12/5, SPCE 2/4/2, TLRY 3/7/0, WOOF 2/8/3, LAC 3/6/0, EOSE 4/7/0, HTZ 0/6/4, OPEN 2/6/2, UWMC 2/7/0, PLUG 8/12/3.
**No coverage:** SGML, LAND, LPTH, CRML, ITUB, DJT, POET, RUM, JMIA, BULL, IEP, LWLG, BW, SATL, IMSR, NUAI, VZLA, NRGV, UAMY, TMC, PUSA.
**R4 proxy out (tool low at or under the stock):** FUN (low $5 vs $7.59), INDI (low $1.75 vs $1.75).
**Pass R3 + R4 proxy (~32):** UUUU, UEC, TME, CLSK, FUBO, EXK, BTDR, IMTX, OCUL, METC, MFA, PONY, NUVB, SOUN, ACHR, INTR, TIGR, VNET, ENVX, NB, NIO, USAS, PCT, SOC, GRAB, SANA, TE, DNN, KEEL, HIVE, ALT, ALLO, plus QUBT (held), FRMI (doc), ONDS, RCAT (watch).

Of the passers, these were chain-killed inside the last 9 days and left dead without a re-chain (nothing in tonight's data says the kill changed): UEC, TE (R5, Oct 27), USAS, SOC, NB, FUBO (R7, Oct 27), HIVE (R6, Oct 27), EXK (R7, Oct 27), CLSK (watch, Oct 28), PONY (R7, Oct 20), ACHR, VNET (R6, Oct 20), UUUU (R5/R6, Oct 20), BTDR (R6, Oct 21), KEEL, GRAB, DNN, SANA, ALLO (structural R6, Oct 20), NIO (R4: $3.70 low vs $3.32 stock, no strike with BE under it at R5), INTR (Brazil, R4 dating), TME (doc on file, R6 history), MFA (mREIT, structural R6). 

## 3. Re-chained tonight (kills older than a week, or OI that could have grown)

| Name | Close | Print | Ratings / low | Contract | Bid / Ask | OI | Spread | BE / move | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| IMTX | $7.43 | Nov 17 | 11/0/0, $11.43 | Dec18 $7C / $8C | 0.30 / 1.40; 0 / 1.90 | 0 / 0 | 129% / no bid | | **KILL R7** |
| OCUL | $7.30 | Nov 4 | 13/0/0, $14 | Dec18 $7C / $8C | 0 / 2.95; 0 / 1.20 | 207 / 261 | no bid | | **KILL R7** |
| NUVB | $4.59 | Nov 4 | 12/1/0, $7 | Dec18 $5C | 0.30 / 0.50 | 153 | 50% | | **KILL R7** |
| SOUN | $4.44 | Nov 5 PM (v) | 6/2/0, $6 | Dec18 $5C | 0.29 / 0.33 | 697 | 12.9% | $5.33 / +20.0% | **KILL R6** (cap 11.7%) |
| SOUN | | | | Dec18 $4C | 0.61 / 0.81 | 396 | 28.2% | $4.81 / +8.3% | R5 (0.81 > 0.657) + R7 |
| ENVX | $3.50 | Nov 5 | 8/3/1, $5 | Dec18 $3C / $4C | 0.60 / 0.89; 0.18 / 0.40 | 1,863 / 438 | 39% / 76% | | **KILL R7** |
| ALT | $2.09 | Nov 6 | 9/1/0, $11 | Dec18 $2C / $2.5C | 0.20 / 0.45; 0.05 / 0.15 | 28 / 306 | 77% / 100% | | **KILL R7** |
| PCT | $3.16 | Nov 4 | 3/3/0, $6 | Dec18 $3C / $4C | 0.40 / 0.70; 0.10 / 0.35 | 140 / 129 | 55% / 111% | | **KILL R7** |
| METC | $7.52 | Nov 3 | 6/3/0, $8 | Dec18 $8C / $7C | 0.55 / 0.85; 0.95 / 1.35 | 307 / 32 | 43% / 35% | | **KILL R7** (+R5) |
| TIGR | $4.06 | Dec 4 | 7/0/1, $4.61 | Jan15 $4C / $4.5C | 0.30 / 0.55; 0.05 / 0.46 | 1,319 / 3,183 | 59% / 161% | | **KILL R7** |

**SOUN R6 math** (daily closes, print day close -> next day close): May 8 2025 -7.8%, Aug 7 2025 +26.4%, Nov 6 2025 -0.6%, Feb 26 2026 -4.2%, May 7 2026 -7.8%, Aug 5 2026 +10.1%. Median |move| **7.8%**, cap 1.5x = **11.7%**. The $5C needs +20.0% from $4.44. Note: this is the first time SOUN's $5C cleared R7 (OI 162 on Oct 20, 697 tonight). Revive line for the $5C: BE <= stock x 1.117, i.e. at a 0.33 ask the stock has to be at or above **~$4.77**. Goes to watch.

## 4. Result

91 names re-rated free, 10 contracts on 9 names chain-checked: **9 KILLED (8 R7, SOUN R6), 0 advanced.** One new watch line: **SOUN Dec18 $5C** (R7 now passes, R6 needs the stock at ~$4.77+; its $6 low is undated, so the R4 floor-dating check comes before any doc). The under-$8.45 bottom-quartile pool with prints through Feb 12 has no never-screened name left. Saturday's full sweep adds the $8.45+ bands (199 rows tonight) and the Jan-Feb print window.

## GLOSSARY

- **Range pct / R1:** (price - 52w low) / (52w high - 52w low). Under 0.25 = calls zone.
- **R2:** the earnings print is proven to land before expiry (21 days after the later of the tool date and last year's date; 10-Q deadline 5+ trading days before expiry). (v) = company-verified date.
- **R3:** at most 1 Sell, at least 3 Buys, Buys >= Holds. Shown as Buy/Hold/Sell.
- **R4 / R4 proxy:** the lowest Buy target must be above breakeven, and dated within 60 days after the decline. Proxy at the free screen: the tool's low target vs today's price.
- **R5:** ask x 100 <= 10% of reserve (3.5/5 tier). Reserve = settled spendable cash (~$657 Thursday).
- **R6:** the move to breakeven <= 1.5x the median earnings-day move (last 4-8 prints).
- **R7:** open interest >= 250 and (ask - bid) / mid <= 25%, on the exact contract.
- **BE:** breakeven, strike + premium paid.
- **OI:** open interest, contracts outstanding.
- **Structural R6:** a name whose print moves are too small for any affordable strike to reach breakeven, whatever the day's price.
- **Revive line:** the stock price at which a killed contract would pass again.
