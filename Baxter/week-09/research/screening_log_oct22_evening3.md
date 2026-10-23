# SCREENING LOG: Thu Oct 22, 2026, EVENING 3 (10:00pm ET)

*Market closed; quotes are the 4:00pm close (AH noted where it matters). Session 3's job: finish the queue EVENING 2 left, refill it, and leave PREMARKET a plan. R1 was re-computed from split-adjusted `get_equity_historicals` bars for every name before its chain check (practice from EVENING 2). 1 web search (PAAS floor).*

## Held (fact check)

| Contract | Close quote | Stock | Earnings | Ratings / low vs BE | SEC since Oct 15 | Verdict |
|---|---|---|---|---|---|---|
| COUR $5C Nov20 | 0.45 / 0.65 (OI 3,257) | $5.07, AH $5.06 | Thu Oct 29 PM `verified: true`, `actual: null` | 8/4/0, low $6.00 vs BE $5.65 | none | Nothing changed. Ramp sell Thu Oct 29 3:35pm. |
| QUBT $7C Dec18 | 0.38 / 0.58 (OI 1,125) | $6.59, AH $6.56 | Fri Nov 13 PM `verified: false` (LY Nov 14 PM), `actual: null` | 5/2/0, low $10 vs BE $7.54 | none | Nothing changed. Ramp sell Thu Nov 12 3:35pm. |

## EVENING 2's queue: KRUS, CALX, LTM, BMA (all killed)

R1 on split-adjusted weekly bars, Oct 20 2025 - Oct 16 2026 (none split; all agree with the scanner):

| Ticker | Close | R1 (adj.) | R3 / low | Q3 print (tool) | LY | R2 contract | Chain (close) | Verdict |
|---|---|---|---|---|---|---|---|---|
| KRUS | $34.41 | 0.009 (H 80.84 / L 33.97) | 6/3/0, $51 | Nov 5 PM (v) | Nov 6 | Nov20 fails (15 days); Dec18 | **No option chain at all** (`get_option_chains` empty) | **KILL: no options** |
| CALX | $36.91 | 0.117 (H 71.22 / L 32.35) | 8/1/0, $52 | Nov 2 PM (v) | Oct 29 | Nov20 fails (18 days); Dec18 | $35C 2.80 / 4.80 OI 0; $37.5C 2.45 / 3.10 OI 0; $40C 0.75 / 2.25 OI 1 | **KILL R7** |
| LTM | $47.22 | 0.154 (H 70.42 / L 43.00) | 12/0/0, $62.90 | Nov 13 PM (unv.) | Nov 14 | Dec18 (6-K filer, both dates present) | $45C 3.40 / 5.70 OI 23; $50C 1.00 / 3.10 OI 473 (spread 102%) | **KILL R6** (+R7): print table below |
| BMA | $62.95 | 0.02-0.21 (H 106.15; L $62.00 Oct 2026, or $51.35 if the Oct 20 2025 week counts) | 7/1/0, $85 | Nov 25 PM (unv.) | Nov 26 | Dec18 = 22 days past LY (passes by 1) | $60C 4.00 / 8.80 OI 0; $65C 1.70 / 6.40 OI 0; $70C 0.10 / 4.90 OI 0 | **KILL R7** |

**LTM print table** (PM prints; next-day close vs print-day close): Nov 14 2025 -0.09%, Feb 3 2026 -5.31%, May 5 2026 +12.08%, Aug 4 2026 +3.67% (listed Jul 2025, four prints). Median **4.49%**, cap **6.74%**, line **$50.40**. $50C BE at the ask $53.10 (+12.5%); $45C BE $50.70 (+7.4%) and OI 23. Dead both ways.

## Refill scans

1. **`Baxter Oct22 E3 25-30 Oct28-Dec4 prints`** (`4d60a627-2909-49e7-b5d2-13e734e47ea5`): the $25-30 split of EVENING 2's capped scan. 33 rows. Every one already has a verdict on file this month, including the names EVENING 2's 200-row cap cut off. Nothing new here.
2. **`Baxter Oct22 E3 PAPER large-cap Oct28-Dec4 prints`** (`0569129f-44a5-4e37-8508-ed7f76478aa4`): cap > $10B, prints Oct 28 - Dec 4, scanner range pct < 0.25, call volume column. 128 rows.

Checked both against every week-08 / week-09 research file and the queue: **only 3 never-screened names (EME, MKSI, TPL).** Then looked for names whose latest kill on file was R1, since Thursday's drop could have moved them into the bottom quartile: **PAAS** (killed Oct 20 MIDDAY at $44.835, R1 0.318).

| Ticker | Close | R1 (adj.) | R3 / low | Q3 print (tool) | Contract | Chain (close) | Verdict |
|---|---|---|---|---|---|---|---|
| TPL | $333 | n/a | **no coverage** | Nov 4 PM (v) | n/a | not pulled | **KILL R3** |
| EME | $660.41 (-5.5% Thu) | 0.246 (H 951.96 / L 564.92) | 9/3/0, $795 | Oct 29 AM (v), LY Oct 30 | Nov20 (21-22 days, passes) | $660C 38.40 / 46.00 OI 0; $670C OI 0; $680C OI 3; $700C OI 8 | **KILL R7** |
| MKSI | $196.11 (-9.3% Thu, -30% since Oct 6) | ~0.20 (H 447.62 / L 134.74) | 14/1/1, $270 | Nov 4 PM (v), LY Nov 5 | Nov20 fails (15-16 days); Dec18 | $195C 19.70 / 22.10 OI 1; $200C OI 2; **$210C 12.80 / 16.90 OI 408** (spread 27.6%) | **KILL R6** (+R7 on spread): table below |
| **PAAS** | $41.07 (AH $40.40) | **0.216** (H 69.99 / L 33.08) | 6/2/0, $51 | Nov 4 PM (v), LY Nov 12 | Dec18 OI 0-41 on $40-50 (R7); **Jan15 $40C** | **4.10 / 4.60, OI 5,378, vol 1,222, spread 11.5%** | **ADVANCE (paper), floor-dating gate** |

**MKSI print table** (PM prints): May 7 2025 +4.02%, Aug 6 2025 +10.21%, Nov 5 2025 +10.96%, Feb 17 2026 -4.78%, May 6 2026 +2.39%, Aug 5 2026 -6.96%. Median **5.87%**, cap **8.81%**, line **$213.38**. $210C BE at the ask $226.90 (+15.7%). Dead.

**PAAS print table** (PM prints): May 7 2025 +3.99%, Aug 6 2025 +7.12%, Nov 12 2025 +1.77%, Feb 18 2026 +5.52%, May 5 2026 +12.02%, Aug 12 2026 -9.70%. Median **6.32%**, cap **9.48%**, line **$44.96** at the $41.07 close.
- Jan15 $40C `7e29c70a-671f-4457-a7cb-b73c0e903ad1`: BE at the ask **$44.60 (+8.6%)**, passes R6 by 0.88 pt. At the AH $40.40 the line is $44.23 and the ask would need to come in with the stock. R6 has to be re-checked on a live quote.
- Jan15 $42C (3.20 / 3.60, OI 157): R7 + R6 ($45.60). Jan15 $45C (2.15 / 2.50, OI 2,065): R6 ($47.50, +15.7%).
- R2: Jan15 is 64 days past the later date (Nov 12). PAAS is a foreign private issuer (no 10-Q test), so both dates are needed, and both are present. Ramp sell if entered: **Wed Nov 4 3:35pm** (print Nov 4 PM, verified).
- R4: low $51 vs BE $44.60, room $6.40. **Undated.** One search: MarketBeat/StockAnalysis show a ~$70 average and "1 sell, 1 hold, 8 buy" (the tool says 6/2/0, and the tool is the rule's source). Nothing dates the $51. Gate: find a Buy at or under ~$51 dated after the slide (PAAS high $69.99) and within 60 days.
- Paper-size only: $460 a contract vs the $62 real-money line.
- Driver bucket (for the correlation proposal): **precious metals / silver.** None of the open paper names share it.

## Watch line + TTWO (free re-check)

| Name | Close | Ratings / low | Revive at | Verdict |
|---|---|---|---|---|
| TTWO | $207.81 | 29/1/1, $270, stamp **Aug 7** (still) | a Buy target dated after Aug 17 | parked on R4 dating |
| ONDS | $6.02 | 11/0/0, $13 | >= ~$6.90 | under |
| BTBT | $0.907 | 6/0/0, $3.50 | >= ~$1.10 | under |
| CLSK | $8.15 | 16/0/0, $19 | > ~$9.20 | under |

## Tally

8 names to a verdict (KRUS, CALX, LTM, BMA, TPL, EME, MKSI, PAAS): **7 killed, 1 advanced (PAAS, paper)**. The two rows EVENING 2's scan cut off already had verdicts on file, so they aren't counted. 161 scan rows checked against the month's files for free. 4 watch/parked names re-checked free. 1 web search.

**What tonight says:** the AI-capex selloff is pushing big names (EME, MKSI) into the bottom quartile, but their near-money options either aren't traded (EME OI 0-8) or need moves twice their print history (MKSI). The one name that cleared is in a different driver bucket entirely (silver). That's useful for the correlation question: the paper book's next entry, if it happens, wouldn't add to the AI bucket.

## GLOSSARY
- **R1-R7:** the binder's Iron Rules (Tab 1). R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability, R6 reachability, R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **Range percentile (R1):** (price - 52-week low) / (52-week high - 52-week low). Bottom quartile (< 0.25) is a calls candidate; 0.25-0.75 is MID-OUT.
- **Split-adjusted:** historical prices divided by the split ratio so a split doesn't look like a crash. The scanner's high/low expression is not adjusted; `get_equity_historicals` is.
- **OI:** open interest, contracts outstanding. **Spread:** ask minus bid, as a share of the mid.
- **(v) / (unv.):** `get_earnings_results` verified flag: company-announced vs estimated.
- **LY:** last year's same-quarter report date.
- **Median print / cap / line:** median absolute next-day move over the last six prints (four for LTM); R6 allows a breakeven move up to 1.5x that, and the line is the stock price times (1 + cap).
- **Tab 6 dating:** a floor counts only if the Buy target is dated within 60 days and published after the decline.
- **6-K filer:** a foreign private issuer; it has no 10-Q deadline, so R2 needs both the tool date and last year's date.
- **Driver bucket:** the primary macro driver a position shares with others (Tab 3's 35% correlated cap; see `paper_correlation_proposal_oct22.md`).
- **Paper book:** tracked-only positions, entered at the ask and exited at the bid, no money.
