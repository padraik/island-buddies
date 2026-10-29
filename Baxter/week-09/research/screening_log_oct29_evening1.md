# Screening log, Thu Oct 29, EVENING 1 (6:00pm ET)

*Job: holdings fact check, the three cause reads WRAP left (FRMI, CAVA, AVGO), the daily slide-in scan, and a diff of the early-sweep scan for names that crossed into it today. Reserve for Friday: **$592.15** spendable (cash $592.15, unsettled 0), so the 3.5/5 R5 line is **$0.592** (0.55 on a $0.05 tick, 0.59 on a $0.01 tick). All quotes are Thursday closing prints (19:59 UTC); stock prices are the regular close unless marked AH.*

## 1. Cause reads (3 web searches)

| Name | Move | What the search found | Verdict |
|---|---|---|---|
| FRMI (held) | +15.6% Wed, -5.5% Thu | Same set as Oct 28: coverage initiations "Oct 27" (Evercore $37, Stifel $29, Berenberg $37, Redburn $31) and a Zacks upgrade "Tuesday, October 28th". Oct 28 was a Tuesday in **2025**, a Wednesday in 2026, and FRMI's IPO quiet period ended late Oct 2025. Tool counts unchanged (6/2/0). | **Still unexplained.** Treated as 2025 echoes, not counted. No 8-K since Oct 16. |
| AVGO (paper) | -2.8% AH Thu ($335.25 vs $345.05 close) | TipRanks / The Fly: "Broadcom down 2% after Bloomberg report on Apple in-house chip efforts" (undated in the result). | **Probable cause, date unconfirmed.** Not a Rule 4 event (tool low $350+, dated floor $400 per WRAP). AH is under the $340.90 BE; no exit rule fires on an AH print. |
| CAVA (paper) | +9.1% Thu ($59.19) | Only last quarter's "jumps 9% after earnings beat" (Aug). The tool says Q3 is **Wed Nov 4 PM, `verified: true`, `actual: null`**, so Thursday was not a print. | **Cause unread.** Real finding is the date: the paper ramp sell moves Mon Nov 2 -> **Wed Nov 4 3:35pm** (paper_book.md fixed). |

## 2. Sources

- Slide-in scan `696cbe51-64eb-4fd9-8bbf-8e018808e4e5` (R1 0.25-0.29, prints Oct 28 - Dec 23, call vol >= 300): **32 rows, all MID-OUT tonight** by construction. Notables: MSTR 0.252, FTAI 0.252, HESM 0.250, BETA 0.251, SBET 0.252, KBH 0.253 are a hair over the line. Nothing to chain.
- Early-sweep scan `e6411b30-10ca-446f-a285-d47a7001c9a4` (R1 < 0.25, prints Nov 2 - Feb 12, call vol >= 300, still filtered $1 - $8.45 from last night): **101 rows** (91 last night). Diffed against last night's log: 22 names in tonight's list that weren't in last night's. Only **PAGS** has never appeared in a week-09 log; the other 21 were last killed Oct 6 - Oct 27.

## 3. Free screen (get_equity_analyst_ratings, 30 symbols in one call)

| Name | Close | R1 | Print | B/H/S, low | Verdict |
|---|---|---|---|---|---|
| PAGS | $8.08 | -0.09 | Nov 12 | 6/9/2, $6.72 | **KILL R3** (Holds > Buys, 2 Sells) |
| YSS | $6.99 | 0.04 | Nov 30 | 5/9/0, $8 | **KILL R3** |
| UAA | $4.98 | 0.21 | Nov 6 | 3/20/4 | **KILL R3** |
| GILT, ABTC, RYAM, ORC, VFS, SVIA, GOGO, ASPI, PSEC, TRON | | | | none | **KILL, no coverage** |
| AUR | $4.41 (-13.4%) | 0.16 | Feb 11 | 8/6/0, **$3.59 (stamped today)** | **KILL R4 proxy** (low under the stock) |
| RUN | $7.51 | 0.05 | Nov 4 | 14/8/1, $4.63 (stamp May 7) | **KILL R4 proxy** (stale and under the stock; same as Oct 15) |
| GNL | $7.22 | 0.06 | Nov 4 | 6/2/1, $9 | **KILL R6 structural** (carried: 6-print median 4.70%, cap 7.05%; $2.50 strike grid) |
| CIFR | $8.105 (-8.6%; AH $7.75) | -0.01 | **Mon Nov 2 AM, verified** | 23/2/0, $12 (was $18 on Oct 20) | **KILL R2 timing:** ramp deadline is Fri Oct 30 3:35pm, the only entry slot left. No window to own the ramp. Back next quarter. |
| NG | $6.15 | 0.12 | Thu Jan 21 AM (f) (LY Jan 22) | 6/0/0, $12.02 | **PARK to Saturday:** needs a Feb19 expiry (Dec18 / Jan15 fail the 21-day cushion). Chain-check there. |
| CRMD, STUB, UNIT, AIOT | | | | pass | to chains (below) |

Watch list re-rated: ONDS 11/0/0 low $13, close $6.895 (AH $6.65), under the ~$7.10 revive line. SOUN 6/2/0 low $6, $4.355 (revive ~$4.77). CLSK 16/0/0, $8.19 (> ~$9.20). BTBT 6/0/0, $0.933 (>= ~$1.10). OUST 6/1/0, $32.14 (AH $30.62; R1 under ~$28.25). QURE 12/2/0, $25.29 (R1 under ~$24.3). **TTWO** 29/1/1, low $270 **still stamped Aug 7** (past the 60-day dating limit), $193.55: stays floor-gated, Saturday decides.

## 4. Chains (Dec18 calls, closing quotes)

| Name | Stock | Print | Contract | Bid / Ask | OI | Spread | BE / move | Verdict |
|---|---|---|---|---|---|---|---|---|
| CRMD | $7.63 | Wed Nov 11 AM (f) (LY Nov 12) | $7C / $8C | 0.85 / 2.00; 0.50 / 1.55 | 56 / 37 | 81% / 102% | | **KILL R7** (+R5) |
| STUB | $5.82 | Tue Nov 10 PM (v) | $5C | 1.00 / 1.15 | 626 | 14% | $6.15 / +5.7% | **R5** (1.15 > 0.59) |
| STUB | | | $7.5C | 0.15 / 0.20 | 1,756 | 28.6% | $7.70 / +32.3% | **KILL R7** (spread 28.6%). R6 not computed tonight (killed on R7 first); +32.3% would need a 21.5%+ print median |
| UNIT | $5.165 | Mon Nov 9 AM (v) | $5C / $6C | 0.25 / 1.00; 0.25 / 0.40 | 15 / 0 | 120% / 46% | | **KILL R7** |
| AIOT | $2.865 | Mon Nov 9 AM (f) (LY Nov 10) | $2.5C | 0 / 0.75 | 1 | no bid | | **KILL R7** |
| RCAT (watch) | $5.065 | Mon Nov 16 PM (v) | $5C | 0.64 / 0.82 | 805 | 24.7% | $5.82 / +14.9% | **R5** (0.82 > 0.59) and R6 (cap 10.29%) |
| RCAT | | | $6C | 0.37 / 0.44 | 571 | 17.3% | $6.44 / +27.1% | **R6** |

RCAT note: the old "revive at ~$5.15" line assumed the $5C would sit near a $0.62 ask. At $5.065 it's 0.82, so the real revive needs the stock up AND the ask under 0.59, which can't both happen on the $5C. RCAT stays on watch only as an R1/R3 name for a future quarter.

## 5. Result

**30 names re-rated free, 7 contracts on 5 names chain-checked. 21 killed** (3 R3, 10 no coverage, 2 R4 proxy, 1 R6 structural carried, 1 R2 timing, 4 R7 incl. STUB, whose $5C also fails R5), **0 advanced**, NG parked to Saturday, 8 watch names re-rated, unchanged. With $592 of reserve, the binding constraint is the same one all week: the liquid contracts cost more than $0.59, and the ones under $0.59 have no open interest. Saturday's sweep adds the $8.45+ bands (paper) and Jan/Feb prints.

## GLOSSARY

- **Range pct / R1:** (price - 52w low) / (52w high - 52w low). Under 0.25 = calls zone. Negative = under the 52-week weekly-candle low.
- **R2:** the earnings print is proven to land before expiry (21 days after the later of the tool date and last year's date; 10-Q deadline 5+ trading days before expiry). (v) = company-verified date, (f) = not verified. "R2 timing" here means the ramp-sell deadline lands before the next entry slot, so there's no window to own the position.
- **R3:** at most 1 Sell, at least 3 Buys, Buys >= Holds. Shown as Buy/Hold/Sell.
- **R4 / R4 proxy:** the lowest Buy target must be above breakeven and dated within 60 days after the decline. Proxy at the free screen: the tool's low target vs today's price.
- **R5:** ask x 100 <= 10% of reserve (3.5/5 tier). Reserve = settled spendable cash ($592.15 for Friday).
- **R6:** the move to breakeven <= 1.5x the median earnings-day move (last 4-8 prints).
- **R7:** open interest >= 250 and (ask - bid) / mid <= 25%, on the exact contract.
- **BE:** breakeven, strike + premium paid.
- **OI:** open interest, contracts outstanding.
- **AH:** after-hours trade.
- **Structural R6:** a name whose print moves are too small for any affordable strike to reach breakeven, whatever the day's price.
- **Revive line:** the stock price at which a killed contract would pass again.
- **Ramp sell:** selling before the print into the pre-earnings premium (binder Tab 4).
