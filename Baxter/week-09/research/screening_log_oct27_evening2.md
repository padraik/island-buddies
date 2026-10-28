# SCREENING LOG: Tue Oct 27, 2026, EVENING 2 (8:00pm ET)

*Market closed; stock quotes are Tuesday's close or after-hours, option quotes are the closing book (~3:59pm). EVENING 1 left no chain survivor, so this session ran the refill EVENING 1 asked for: a liquidity-first scan. 2 searches (FRMI floor date, FRMI decline cause).*

## Held (fact check)

| Contract | Close quote | Stock | Earnings | Ratings / low vs BE | Verdict |
|---|---|---|---|---|---|
| COUR $5C Nov20 | 0.20 / 0.35 (OI 3,357, closing-minute quote) | $4.75 close, AH $4.77 | Thu Oct 29 PM `verified: true`, `actual: null` | 8/4/0, low $6.00 vs BE $5.65 | Unchanged. Sell window opens Wed; hard deadline Thu Oct 29 3:35pm. GTC $1.65 `confirmed`. |
| QUBT $7C Dec18 | 0.56 / 0.70 (OI 1,175) | $6.87 close, AH $6.92 | Mon Nov 9 PM `verified: true`, `actual: null` | 5/2/0, low $10 vs BE $7.54 | Unchanged. Ramp sell Mon Nov 9 3:35pm. GTC $1.35 `confirmed`. |

## Source: new preview scan (not saved)

Filters: market cap >= $0.3B, stocks, last $1-25, R1 < 0.25 (the standard expression), prints **Nov 9 2026 - Jan 29 2027**, **total call volume >= 500** (the filter EVENING 1 asked for). **89 rows.** Diff against every week-09 file, passes.md and paper_book.md: **0 never-logged names.** Every liquid bottom-quartile name with a print in the window has been through this month's funnel.

So the session re-rated the pool instead: one `get_equity_analyst_ratings` call on 75 of the 89 (skipped: the two holdings, and XP, BBAR, BILI, GDS, LINC, CMCSA, NLY, LBRT, INFY, AGNC, TLRY, PICS, ARTV, already re-checked this week). R3 passers with a stock cheap enough to carry a contract under the $0.622 line went to the chain. 22 names in all moved at least one stage.

## Chain stage (Dec18, closing book)

| Ticker | Stock | Print | Ratings / low | Contract: bid / ask, OI, spread | R6 (median, cap, need) | Verdict |
|---|---|---|---|---|---|---|
| **FRMI** | $2.62 | Thu Nov 12 AM v (LY Nov 10 PM) | 6/2/0, low $6 (Cantor OW $8, Oct 16) | **$2.5C 0.45 / 0.60, OI 345, 28.6%**; $3C 0.30/0.40 OI 170; $3.5C 0.20/0.30 OI 639, 40% | 13.35% on 4 prints, cap 20.0%, $2.5C needs +17.0% (pass) | **ADVANCED: DOC WRITTEN** (`research_FRMI_dec18.md`). Passes R1-R6; R7 spread fails by 3.6 pt at the close. Daytime gate. |
| RCAT | $4.87 (AH $4.98) | Mon Nov 16 PM v | 7/1/0, low $6 | $5C 0.55 / 0.68, OI 688, 21%; $6C 0.16/0.33, 69% | 6.86% on 6 prints, cap 10.29%, $5C needs +12.8% at mid | **R6 near-miss, to watch.** R7 now passes (Oct 20: OI 107, 70%). Revives if a daytime quote shows BE <= stock x 1.1029 with ask <= $0.622 (roughly stock >= ~$5.15 with the ask still <= 0.62). |
| TE | $2.51 | Nov 13 AM (f), LY Nov 14 AM | 6/3/0, low $5 | $2C 0.60 / 0.75, OI 730, 22%; $3C 0.25 / 0.30, OI 1,579, 18% | 9.66% on 6, cap 14.49%; $3C needs +31.5%, $2C fits R6 | **KILLED, R5/R6** ($2C ask $0.75 > $0.622; $3C fails R6) |
| HIVE | $2.02 | Nov 13 PM (f), LY Nov 17 AM | 8/1/0, low $4.50 | $2C 0.25 / 0.35, OI 697, 33%; $3C 0.05/0.10 | 4.35% on 6, cap 6.5%; $2C needs +16.3% | **KILLED, R6** |
| USAS | $3.19 | Fri Nov 13 AM v | 10/0/0, low $5.72 | $3C 0.45/0.55 OI 164; $3.5C OI 52; $4C 0.10/0.15 OI 565, 40% | not needed | **KILLED, R7** |
| SOC | $3.09 | Mon Nov 9 AM v | 8/1/0, low $8 | $3C 0.40/0.61 OI 39; $4C OI 147 | not needed | **KILLED, R7** |
| NB | $3.43 | Nov 12 PM (f) | 6/1/0, low $4.70 | $2.5C OI 54; $5C OI 2 (strikes in $2.50 steps) | not needed | **KILLED, R7** |
| AMPX | $8.96 | Tue Nov 10 PM v | 13/0/0, low $14 | $9C 1.00/1.25 OI 77; $10C 0.65/0.85 OI 57 | not needed | **KILLED, R7** (and R5) |
| FUBO | $7.78 | Nov 13 | 8/2/0, low $12 | $8C 0.71 / 1.22, OI 7 | not needed | **KILLED, R7** |
| UEC | $8.04 | Dec 10 | 8/3/0, low $10 | $8C 0.78 / 0.92, OI 276, 16% | not needed | **KILLED, R5** ($0.92 > $0.622) |
| ZURA | $4.10 | Nov 13 | 8/0/0, low $11 | $5C 1.15 / 1.90, OI 1,846, 49% | not needed | **KILLED, R5 + R7** |
| INFQ | $9.74 | Nov 28 PM (f) | 6/1/0, low $12 | $10C listed | one print in its history | **KILLED, R6 unverifiable** (1 print; the rule needs 4) and R2 (no last-year date) |
| WRD | $4.35 | Nov 24 | 14/1/0, low **$4.005** | n/a | n/a | **KILLED, R4** (low under the stock; no strike's BE clears it) |

## Ratings stage (free; R3 or R4 fails at the screen)

| Ticker | Ratings | Verdict |
|---|---|---|
| CPB | 1/14/8 | KILLED, R3 |
| CAG | 1/12/6 | KILLED, R3 |
| SKYD | 7/12/8 | KILLED, R3 |
| FLNC | 4/15/5 | KILLED, R3 |
| CSIQ | 2/6/3 | KILLED, R3 |
| LCID | 3/7/3 | KILLED, R3 |
| SPCE | 2/4/2 | KILLED, R3 |
| GEMI | 3/5/2 | KILLED, R3 |
| LAC | 3/6/0 (Buys < Holds) | KILLED, R3 |

Also no coverage (no ratings): BMNR, PPTA, BCSF, CCXI, LPTH, CRML, RUM, POET, JMIA, BULL, LWLG, IMSR, UAMY, NUAI, NRGV, TMC, ASPI. Not re-counted as moves; they died on coverage earlier this month.

**Names moved: 22** (13 at the chain, 9 at ratings). **Killed: 20** (R7: USAS, SOC, NB, AMPX, FUBO; R5: UEC, TE; R5+R7: ZURA; R6: HIVE; R6/R2: INFQ; R4: WRD; R3: CPB, CAG, SKYD, FLNC, CSIQ, LCID, SPCE, GEMI, LAC). **Advanced: 1** (FRMI, to a full doc). **To watch: 1** (RCAT).

**Finding:** the call-volume filter didn't surface new names, but re-quoting old R7 kills did. FRMI's Dec18 $2.5C went from OI 246 to 345 in a week, and RCAT's $5C from 107 to 688. Open interest builds into a print. An R7 kill from two weeks before the print is worth re-quoting a week before it.

## GLOSSARY

- **R1-R7:** the Iron Rules, binder Tab 1. R1 range percentile (bottom 25%), R2 earnings before expiry with the 21-day cushion, R3 Buy consensus (<= 1 Sell, >= 3 Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 price vs the conviction-tier cap, R6 required move <= 1.5x the median print reaction, R7 OI >= 250 and spread <= 25% of mid.
- **Range pct:** where the stock sits in its 52-week range, 0 = at the low, 1 = at the high.
- **(f) / v:** earnings date from the tool, `verified: false` (estimated) / `verified: true` (company-announced).
- **Print median:** the median absolute move on earnings: PM reports from that day's close to the next, AM reports from the prior close to that day's close.
- **OI (open interest):** contracts outstanding on that exact strike and expiry.
- **Spread %:** (ask - bid) / midpoint.
- **Preview scan:** a scanner run that isn't saved; nothing persists.
- **No coverage:** no analyst ratings in the tool, so Rule 3 can't pass.
