# SCREENING LOG: Wed Nov 11, EVENING 2 (8:00pm ET), VM

*Session 2 of 3. Job (from EVENING 1): no name cleared the chain at 6pm, so there's no doc to write. Start EVENING 3's refill early: (1) Wednesday's losers against the rally (R1 < 0.25, prints Nov 16 - Dec 22), diffed against week-09 logs; (2) the ~Dec 15 re-sweep scan definitions (prints Feb 13 - Mar 20). Nothing held. Real-money reserve $706.01 spendable, so the 3.5/5 R5 line is $0.706. Stock prices: Wednesday 4pm close, with after-hours where the scanner used it (`tradeAllDay.price`). Option books are the 3:59pm closing quotes.*

## Source 1: losers scan, new saved scan `2a4b3aa6` ("Baxter Nov11 E2 losers R1<0.25 Nov16-Dec22 prints callvol>=100")

Filters: market cap $300M+, earnings date Nov 16 - Dec 22, stock, last >= $1, R1 expression < 0.25, call volume >= 100. **67 rows. All 67 already appear in week-09 logs (0 never-worked).** The scanner reads after-hours prices, so the "% Change" column is mostly AH drift, not Wednesday's session.

Ratings pulled on all 67 in one free call. Cut at the free screen:

| Bin | Names |
|---|---|
| No coverage (R3) | BBW, PLAB, BMNR, JMIA, CRML, POET, XXI, BULL, VZLA, VFS, UROY, ASPI |
| R3 (Sells > 1, Buys < 3, or Holds > Buys) | INTU (2 Sells), DKS (2), RH, LULU, LEN, PDD (2), NKE, SYM (3), GIS, BLSH, AMTM, KLAR, LI, FCEL (2), QFIN (2), FLNC, EH, BORR, BLDP, XPEV (3) |
| R4 proxy (lowest target at or under the stock) | AGX ($273 vs $318.78; also 1 Sell), ACM ($65 vs $69.32), TCOM ($42.21 vs $43.51), XP ($14.54 vs $15.22), MNSO ($10.87 vs $10.99), BRBR ($9 vs $10.11) |
| Pass the free screen, left dead on an earlier structural kill (these don't change in a day) | GGAL, SHAZ, UTI, GDS, BILI, VNET, TIGR, FUBO (R7); INFQ, PONY, UEC (R6); WRD (R4); MPLT (OI 4); AVAV (R7); NNE (R7 parked); RCAT (R6, now $4.21, further from its line) |
| Pass, already on the queue / paper book | POWL, CRDO, PL, NIO (gated, see EVENING 1 log); BABA (paper book); BURL (paper closed Tue on R4) |
| Pass, re-opened tonight because the price moved | **NVDA, FUTU, KC, CLSK** (below) |

CRDO note: AH $137.01 puts R1 at **0.229**, back under the line (close $141.41 = 0.247). Floor gate unchanged ($235 low, no Buy dated after Oct 12). Stays on the queue as is.

## Re-opened names, R2 / R6 / chain

Print reactions from daily closes (`get_equity_historicals`, PM prints = print-day close to next close; AM = prior close to print-day close), last 6 prints.

| Ticker | Stock | B/H/S, low | Next print (`get_earnings_results`) | Last 6 reactions | Median, R6 cap | Chain check | Verdict |
|---|---|---|---|---|---|---|---|
| **NVDA** | close **$173.73** (flat); **AH $159.49 (-8.2%)**, below the $164.27 52w low | 68/4/1, **$180** (stamp Nov 11 18:09 UTC) | FQ3 **Tue Nov 17 PM `verified: true`**; LY Nov 19 | +3.25, -0.79, -3.15, -5.46, -1.77, +8.74 | **3.2%, cap 4.8%** | Dec11 (first expiry 21 days past Nov 19; 10-Q deadline ~Dec 4 = 5 trading days before) at the 3:59 close: $175C **10.55 / 10.80**, OI 1,814, BE **$185.80 = +6.9%**; $170C 13.10 / 13.40, BE $183.40 = +5.6%; $160C 19.00 / 19.90, BE $179.90 (+3.5%, but it's $14 ITM and $1,990 a contract) | **KILLED R6** for any OTM or ATM strike: at-the-money premium alone (~6.2% of spot at 55% IV) is over the 4.8% cap. Also R4 at the close: every BE from $175 up sits over the $180 low. At the AH price the R4 room opens ($180 vs ~$169 BE on a $160C) but R6 doesn't. Paper too. Nov 5 kill was R4 proxy; tonight's is R6, which is structural. |
| FUTU | $98.00 (AH $97.00) | 19/2/0, $121.95 | Q3 **Thu Nov 19 AM `verified: true`** (scanner said Nov 18) | -0.32, +6.02, -0.49, -6.31, -4.82, +3.03 | 3.9%, cap 5.9% | Not re-chained: a $100C Dec18 at ~31 DTE and FUTU's IV costs more than the 5.9% cap before the strike gap. Same structure as the Oct R6 kill. Paper-size anyway. | **Stays dead, R6.** |
| KC | $8.52 | 18/0/0, $15.47 | Q3 **Tue Nov 24 AM `verified: true`** | -7.91, +1.32, -0.56, +6.71, +0.69, +14.11 | 4.0%, cap 6.0% | No Dec chain (Nov20 -> Jan15, per Nov 5). Jan15 $9C needs +5.6% before premium. | **Stays dead, R6** (same as Oct 8). |
| CLSK | $6.905 (AH $6.76) | 15/1/0, $9.50 | FQ4 **Tue Nov 24 PM `verified: false`**; LY Nov 25. FQ4 = 10-K (FY Sep): large accelerated deadline Nov 30, passes R2(b) for Dec18 | +5.99, -6.06, +13.79, +21.96, -5.80, -3.53 | **6.0%, cap 9.0%** (max BE $7.53 at the close) | Dec18 $7C `82b52b72` **0.88 / 0.92**, OI 788, spread 4.4%, BE **$7.92 = +14.7%**; $8C 0.51 / 0.55, OI 8,003, BE $8.55 = +23.8%; $6C 1.04 / 1.77 (52% spread), BE $7.77 = +12.5%. IV ~107%. | **KILLED R6** (+14.7% vs 9.0%) **and R5** ($7C 0.92 > $0.706). R7 passes. |

NVDA cause, one search: results cover the **Nov 5 AI-chip rout (-9.3%)** and a **Nov 9 board investigation tied to the CEO (-4.3%, AH -3.4% to ~$180)**. Nothing on tonight's -8.2% after-hours move. Unread. It's NVDA-specific: AVGO AH $353 (+2.2%), CRDO AH -3.1%, MRVL not checked.

## Source 2: ~Dec 15 re-sweep scan definitions (prints Feb 13 - Mar 20, Mar19 / Apr16)

The base already exists: **`a5439121`** ("Baxter Nov9 E2 just-reported R1<0.25 Feb13-Mar20 prints callvol>=100"): market cap $300M+, earnings Feb 13 - Mar 20 2027, stock, R1 < 0.25, call vol >= 100. 162 rows on Nov 9. Not re-saved tonight: each banded copy returns up to 200 rows into the session, and December runs can create them in one call each. **Definitions for the Dec 12-15 run** (same filters, no call-volume floor, split by price so every band is under 200):

| Band | FILTER_TYPE_LAST | Expected use |
|---|---|---|
| A | 1 - 8.19 | real-money size (R5 line ~$0.70 on 3.5/5) |
| B | 8.19 - 25 | real-money size on cheap OTM strikes; R6 decides |
| C | 25 - 100 | mostly paper |
| D | 100 - 100000 | paper only |

R2 rule for this window, written out (from the Nov 7 finding): December-quarter prints are **10-K quarters** for calendar-year filers. Mar19 passes R2(b) only for **large accelerated** filers (10-K due Mar 1); accelerated (Mar 16) and other (Mar 31) filers need **Apr16**. Mar19 also needs the later of tool date / LY date on or before **Feb 26** (21-day cushion). Run `get_option_chains` expirations first, since many small names skip from Jan15 to Feb19 or Mar19.

## Tally

**67 re-rated free, 4 re-opened to R2 / R6 (NVDA, CLSK chained; FUTU, KC on the strike grid), 0 advanced, 0 buyable.** Kills tonight: NVDA R6 (new reason), CLSK R6 + R5 (new). FUTU, KC stay dead on R6. Source 1 is fished out: every Nov 16 - Dec 22 bottom-quartile name with options volume has already been worked this week. passes.md Keep Watching is ONDS only (already on watch). Searches spent: 1 (NVDA cause).

## GLOSSARY

- **R1 (range percentile):** (price - 52-week low) / (52-week high - 52-week low). Under 0.25 = calls candidate.
- **R2:** earnings print proven to land before expiry: expiry 21+ days after the later of the tool date and last year's date, and the 10-Q / 10-K deadline 5+ trading days before expiry.
- **R3:** at most 1 Sell, at least 3 Buys, Buys >= Holds.
- **R4 proxy / R4:** the lowest analyst target must sit above the stock (screen) and above the call's breakeven (rule).
- **R5:** one contract's ask x 100 fits the conviction tier's share of reserve ($0.706/share at 3.5/5 tonight).
- **R6:** breakeven move no larger than 1.5x the median absolute earnings reaction over the last 4-8 prints.
- **R7:** open interest >= 250 and spread <= 25% of mid on the exact contract.
- **BE (breakeven):** strike + premium paid.
- **AH:** after-hours trading, after the 4pm close.
- **OI:** open interest, the number of contracts outstanding.
- **IV:** implied volatility, the option market's priced-in yearly move.
- **10-K quarter:** a company's fiscal Q4, reported in the annual 10-K, which has a later SEC deadline than a 10-Q.
- **Large accelerated filer:** public float of $700M+; shortest SEC filing deadlines (10-Q 40 days, 10-K 60 days).
