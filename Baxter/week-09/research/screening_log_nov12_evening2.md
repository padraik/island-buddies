# Screening log, Thu Nov 12, EVENING 2 (8:00pm ET)

*Session 2's job is research docs for names that cleared the chain stage. None did at EVENING 1, so this session started EVENING 3's job early: (1) the BZ cause, (2) a looser losers scan. All prices are Thursday's close or after-hours unless marked.*

## 1. BZ (Kanzhun): cause of the -25.2% day

- `get_earnings_results`: Q3 2026 **Nov 24 AM `verified: false`, `actual: null`**. Not reported, so the R2 "already reported" check doesn't kill it.
- SEC index since Nov 1: one 6-K, **Nov 5**. Nothing filed on or after the drop.
- One web search ("Kanzhun BZ stock plunge November 12 2026"): every hit was an older quarter (Q3 2025 guide-down, Aug 2026 slide). One aggregator lists the next report as Nov 26, 2026. That isn't the tool's date and isn't company-confirmed. If it held, Dec18 still clears R2 (Nov 26 + 21 = Dec 17).
- Ratings re-pull: 20/4/0, low **$16.99**, `updated_at` 2026-11-12 18:23 UTC. The record refreshed today, but the low target didn't move, so there's no new dated floor after the drop.
- AH $12.56. R1 ~0.00 (sitting on its 52-week low).
- **Verdict: cause still unread after one search. Stays KILLED R7 + R5 (EVENING 1's chain) and on watch.** The cause doesn't change the kill. It matters only if the chain fixes itself.

## 2. Looser losers scan `e8592399` (new tonight)

Filters: market cap >= $300M, earnings Nov 16 - Dec 22, stock, price >= $1, R1 < 0.25 (in-scanner expression), **call volume >= 50** (`2a4b3aa6` uses >= 100). **77 rows** (`2a4b3aa6` gave 65 at EVENING 1).

**Diff against every week-09 research file: 0 never-worked names.** All 77 have a prior verdict this week.

Re-rated free (one `get_equity_analyst_ratings` call, 63 symbols with coverage or prior coverage, on Thursday's close/AH):

| Bucket | Names |
|---|---|
| No coverage (R3) | IESC, BKE, BBW, PLAB, SUPV, JMIA, FWDI, BULL, VFS, TUYA (also CRML, POET, XXI, BMNR, ASPI, UROY, VZLA, CSHR, ASMB carried) |
| R3 fail (Sells > 1, or Buys < Holds) | INTU (2 Sells), DKS (2), RH (7/13/2), LULU, LEN, NKE, SYM (3), GIS, PDD (2), BLSH (7/8), AMTM (5/8), KLAR (11/15), LI, XPEV (3), FCEL (2), QFIN (2), FLNC, EH, BORR, BLDP |
| R4 proxy fail (lowest target at or under the stock) | AGX ($273 vs $316), ACM ($65 vs $70.10), TCOM ($42.21 vs $43.13), XP ($14.54 vs $15.13), BRBR ($9 vs $10.24), BIDU ($69.96 vs $78.19), ORCL ($110 vs $127.92), WRD ($4.01 vs $4.23), BURL ($250 vs $251.87), **MNSO ($10.87 vs $10.94: fails by $0.07, near miss; prints Tue Nov 17)** |
| Proxy passes, earlier structural kill stands | DY, AVAV, ROAD, SHAZ, GDS, BILI, UTI, FUBO, VNET, TIGR, GGAL, ALM (R7); FUTU, PONY, INFQ, UEC, RCAT, CLSK (R6); NNE (R7, parked); TME (proxy by $0.09, any call BE over the $9.11 low = R4); BZ (R7 + R5) |
| **Changed since last look, re-opened** | **AS**, **GENB** |

### AS (Amer Sports): re-opened, chained, KILLED R4

- Stock $30.22, R1 **0.247** (was 0.289-0.298 on Nov 11, out). 26/1/0, low **$31** (stamp Sep 21), proxy passes by 2.6%.
- `get_earnings_results`: Q3 **Tue Nov 17 AM `verified: true`**, `actual: null`. LY Nov 18. Dec18: later date Nov 18 + 21 = Dec 9 <= Dec 18, so **R2 passes**. A ramp sell would be due Mon Nov 16 3:35pm.
- Dec18 calls (Thursday close quotes):

| Strike | Bid / Ask | OI | BE at ask | vs $31 floor | Verdict |
|---|---|---|---|---|---|
| $25C | 5.30 / 5.80 | 49 | $30.80 | under | R7 (OI 49), R5 |
| $27.5C | 3.50 / 3.80 | 408 | $31.30 | **over by $0.30** | R4, R5 |
| $30C | 2.05 / 2.30 | 10,001 | $32.30 | over | R4, R5 |
| $32.5C | 1.15 / 1.20 | 13,196 | $33.70 | over | R4, R5 |
| $35C | 0.50 / 0.60 | 7,006 | $35.60 | over | R4 |

- **KILLED R4, real and paper.** The floor sits 2.6% over the stock, so no call clears it: the only strike that does fails R7. Real money also fails R5 at every strike at or below $32.5 (cap: transitional $1.00/share lock).

### GENB (Generate Biomedicines): re-opened, KILLED R2 (already reported)

- R1 0.135 (was 0.250 Nov 9), 6/0/0, low $22. Scanner shows Nov 30, but `get_earnings_results` shows Q3 **reported Thu Nov 12 AM** (-0.68 vs -0.54 est). The catalyst is spent. Next print Feb 3 PM (f). **Parked to the ~Dec 15 re-sweep.**

## Tally

Moved tonight: **BZ** (cause check), **AS** (re-opened -> chain -> KILLED R4), **GENB** (re-opened -> KILLED R2 spent), **MNSO** (near-miss logged), plus 63 symbols re-rated in one free call. 0 advanced, 0 buyable. Web searches: 1.

**Finding:** the scan's call-volume floor was not what was keeping names out. Dropping it from 100 to 50 added 12 rows, and every one of them was already worked this week. The Nov/Dec window is fished out. The ~Dec 12-15 re-sweep is still the next real source.

## GLOSSARY

- **R1 (Rule 1):** where the stock sits in its 52-week range, (price - low) / (high - low). Calls need under 0.25.
- **R2:** a confirmed earnings print lands before expiry: expiry at least 21 days past the later of the tool date and last year's date, and (10-Q filers) the 10-Q deadline at least 5 trading days before expiry. Also: the quarter must not already be reported.
- **R3:** at most 1 Sell, at least 3 Buys, and Buys >= Holds.
- **R4 / bear floor:** the lowest analyst Buy target must be above the call's breakeven (strike + premium). **R4 proxy** is the free screen version: lowest target above the current stock price.
- **R5:** one contract's ask x 100 fits the conviction tier's share of reserve (real money only; transitional cap $1.00/share).
- **R6:** breakeven move no more than 1.5x the median earnings-reaction move.
- **R7:** the exact contract has OI >= 250 and spread <= 25% of mid.
- **OI:** open interest. **BE:** breakeven. **AH:** after hours. **(f):** date not verified by the company.
- **Ramp sell:** selling before the print into elevated premium (binder Tab 4).
