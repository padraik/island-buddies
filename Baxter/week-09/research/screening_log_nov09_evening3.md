# SCREENING LOG: Mon Nov 9, EVENING 3 (10:00pm ET), VM

*Session 3 of 3. Job (from EVENING 2's handoff): FRMI fact check, then two untried sources for the Nov/Dec window at real-money size: (1) names whose Q3 print is still ahead (next earnings Nov 10 - Nov 20), R1 < 0.30, Dec18 expiry; (2) the R1 0.25-0.35 band for prints Nov 16 - Dec 22 (watch-only). All data is Monday's close (option books are the 3:59pm closing quotes, so spreads carry closing width). Real-money line from Tuesday: spendable ~$706.01 once the $166.90 settles, so the 3.5/5 R5 line is ~$0.706 and the screen line ~$1.41.*

## Holdings fact check

FRMI $2.5C Dec18: official close $1.66, AH $1.70. Book 0.05 / 0.10 (OI 1,042). Q3 **Thu Nov 12 AM `verified: true`**, `actual: null`. 6/2/0, low $6 vs BE $3.15: Rule 4 holds. SEC index and EDGAR submissions (CIK 2071778): newest still the Nov 5 Form 4 / 144. **Facts unchanged.** Ramp sell Wed Nov 11 3:35pm.

## Source 1: Q3 still ahead (preview, not saved)

Market cap >= $300M, stock, `FILTER_TYPE_EARNINGS_DATE` **20261110-20261120**, range pct (52W) expression **< 0.30**, total call volume >= 100. **107 rows.** 88 appear in a week-09 log since Oct 26 and stay as logged. **19 fresh.** One ratings call covered all 19.

| Ticker | Stock | Direction | B/H/S, low | Verdict |
|---|---|---|---|---|
| IDR | $21.90 | CALLS | no coverage | KILLED, R3 |
| SPIR | $9.63 | CALLS | no coverage | KILLED, R3 |
| SSYS | $6.69 | CALLS | no coverage | KILLED, R3 |
| CDZI | $3.77 | CALLS | no coverage | KILLED, R3 |
| HYLN | $3.15 | CALLS | no coverage | KILLED, R3 |
| OGG | $2.67 | CALLS | no coverage | KILLED, R3 |
| SLI | $1.60 | CALLS | no coverage | KILLED, R3 |
| GEVO | $1.47 | CALLS | no coverage | KILLED, R3 |
| SES | $0.915 | CALLS | no coverage | KILLED, R3 |
| NAK | $0.68 | CALLS | no coverage | KILLED, R3 |
| FLNG | $26.50 | CALLS | 0/5/2 | KILLED, R3 |
| SID | $0.82 | CALLS | 0/7/4 | KILLED, R3 |
| TEO | $10.26 | CALLS | 5/0/1, $9.20 | KILLED, R4 proxy (low under the stock) |
| OFRM | $10.12 | CALLS | 5/4/1, $10.00 | KILLED, R4 proxy |
| LIF | $41.41 | CALLS | 8/2/0, $40.00 | KILLED, R4 proxy |
| MUX | $15.30 | CALLS | 6/0/0, $28 | **KILLED R2 (already reported):** Q3 printed Mon Nov 9 PM, EPS -0.60 vs +0.09 est; the scanner's date was stale. Next print Mar 11 (f). **Park ~Dec 15** (Apr16). |
| YPF | $38.01 | CALLS | 10/3/0, $55 | **KILLED R2 (already reported):** Q3 printed Oct 29 AM. Next Feb 26 (f). Paper-size. Park ~Dec 15. |
| KURA | $7.67 | CALLS | 15/1/0, $15 | **KILLED, no ramp window:** Q3 Tue Nov 10 PM `verified: true`. The ramp deadline would be Tuesday 3:35pm, the same day as the earliest possible entry, and no doc exists. Next print Mar 4 (f). Park ~Dec 15. |
| ARWR | $49.80 | CALLS | 15/1/0, $74 | Q4 (FY Sep) Thu Nov 12 PM `verified: true`, LY Nov 25; R2 passes on Dec18 (Nov 25 + 21 = Dec 16; 10-K due ~Nov 29). Paper-size. **KILLED R7** on Dec18: $50C 2.50 / 4.20 OI 2; $52.5C 1.90 / 4.00 OI 0; $55C 1.50 / 3.30 OI 1; $60C 0.25 / 1.50 OI 326 (spread 143% of mid). Next print Feb 4 (f). Park ~Dec 15 (Mar19). |

**Source 1: 19 moved, 0 advanced.**

## Source 2: R1 0.25-0.35 band, prints Nov 16 - Dec 22, last < $20 (preview, not saved)

Same filters with range pct **between 0.25 and 0.35** and `FILTER_TYPE_LAST` < 20. **3 rows.** GENB ($13.92, R1 0.250) stays KILLED R7 (Nov 5 EVENING 3); YMM ($8.94, R1 0.264) stays KILLED R4 proxy (Nov 9 EVENING 1). **FWDI** ($5.43, R1 0.252, print Dec 11): no coverage, **KILLED R3**.

**Source 2: 1 moved, 0 advanced.**

## Totals

20 fresh names moved, 0 advanced, 0 buyable. With EVENING 2's work, the Nov/Dec window at real-money size has now been worked from four sides: slide-in, Q3-still-ahead, R1-looser band, and just-reported. Nothing is left in it. The next real-money candidates are the ~Dec 15 parks (Mar19/Apr16 chains once OI builds), and the best of those boards are now WVE 19/1/0, KURA 15/1/0, ALLO 10/1/0, and MUX 6/0/0 (low $28 against a $15 stock that just missed).

## GLOSSARY

- **R1 (range percentile):** where the stock sits in its 52-week range, 0 = at the low. Calls want under 0.25.
- **R2 (calendar):** the print has to land at least 21 days before expiry (later of the tool date and last year's date), with the 10-Q/10-K deadline at least 5 trading days before expiry. "Already reported" means the catalyst is spent.
- **R3 (ratings):** 3+ Buys, Buys at least equal to Holds, 0-1 Sells. No coverage fails it.
- **R4 (floor):** breakeven has to sit under the lowest Buy-side price target. "Proxy" means using the tool's low target against the stock price, before a strike is picked.
- **R7 (liquidity floor):** open interest of at least 250 and a spread of at most 25% of mid on the exact contract.
- **OI:** open interest, the contracts currently outstanding.
- **BE:** breakeven, strike plus premium paid.
- **(f):** forecast earnings date, not yet announced by the company.
- **Ramp window:** the trading days before a print when a call can be held and then sold into the pre-print premium. With an after-close print tomorrow, there is no window.
- **Park:** the name passed what can be checked now; the next check waits on a date (here, ~Dec 15, when spring chains carry OI).
- **Preview scan:** a scanner run that isn't saved to the account.
