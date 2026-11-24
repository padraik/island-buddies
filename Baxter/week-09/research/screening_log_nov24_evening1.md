# Screening log: Tue Nov 24, EVENING 1 (6:00pm ET)

**Job (from the research queue):** (1) TAL's R1 call on Tuesday's close (the standing instruction: close > $9.93 = Stop Watching); (2) the low-IV hunt (queue item 2): find bottom-quartile, real-money-priced names with spring prints whose implied volatility is low enough that a near-the-money contract's time value fits inside 1.5x the median print. TAL was the template (37.5% IV, 9.3% median, ratio 1.29).

**Source:** Robinhood tools only, run ~23:00-23:40 UTC on Tuesday's closing data. 0 web searches. R5 line: 10% x $715.96 reserve / 100 = **$0.716/share** (3.5/5). Passes.md un-staling not due (done Monday Nov 23).

## (1) TAL: Stopped Watching on R1

- Last regular trade **$9.9389** at 3:59:57pm ET; minute bars 3:55-3:59 traded $9.93-9.95 the whole time. The official close hadn't posted by 6pm (quote still shows Monday's $9.71 as previous close).
- 252-day closing range $8.95 (Jun 25) to $12.86 (Oct 9): (9.939 - 8.95) / 3.91 = **0.253**. Line 0.25 = $9.9275. **Over.**
- Ratings 15 / 3 / 0, low $11.50, stamp 2026-11-01T21:58Z, unchanged.
- **Moved to Stopped Watching** in passes.md; addendum C in `research_TAL_feb19.md`. R7 OI (189) and R5 (ask 0.85 vs $0.716) were still failing anyway.

## (2) Low-IV hunt

**Scan (preview, not saved):** market cap $300M+, stock, earnings Jan 15 - Mar 31 2027, Last $3-15, R1 expression < 0.25 (52-week weekly-candle range), `FILTER_TYPE_IMPLIED_VOLATILITY` column. **305 rows.** Note for next time: the tool returns IV as a fraction (0.38 = 38%), so the `< 45` filter passed everything; filtered by hand at IV < 0.50 = **48 names**.

**Already dead in earlier logs, not re-rated (12):** HBAN, LADR, FLG, BXMT, IRT, BRSL (R6 structural / R6), GNW, AGNC, F, GOOS, VALE, MAT (R3).

**Rated (36), one `get_equity_analyst_ratings` call:**

| Ticker | Last | IV | Print | B/H/S | Low target | Verdict |
|---|---|---|---|---|---|---|
| DOLE | 12.37 | 23% | Feb 25 | none | | **No coverage (R3)** |
| DX | 10.01 | 25% | Jan 26 | 4/2/0 | 11.50 | passes screen; **already dead R6 structural** (~1% median) |
| BSM | 13.30 | 27% | Feb 23 | none | | **No coverage** |
| CCAP | 10.07 | 28% | Feb 26 | 2/6/0 | 10.00 | **KILLED R3** |
| RITM | 8.65 | 28% | Feb 3 | 11/0/0 | 10.00 | passes screen; **already dead R6 structural** (2.0% median, Nov 23) |
| ECVT | 9.72 | 29% | Feb 26 | 4/2/0 | 12.00 | passes screen; **already dead R6** (Nov 19 EVENING 2) |
| CLBK | 10.83 | 32% | Feb 2 | none | | **No coverage** |
| ITUB | 6.71 | 32% | Feb 4 | none | | **No coverage** |
| STWD | 11.36 | 32% | Feb 24 AM (f) | 6/2/0 | 13.00 | passes; median below |
| CGBD | 10.65 | 33% | Feb 24 | 2/5/1 | 10.50 | **KILLED R3** |
| JBS | 12.17 | 34% | Mar 24 PM (f) | 15/1/0 | 15.00 | passes; median below |
| NMFC | 6.67 | 34% | Feb 24 | 0/6/1 | 7.00 | **KILLED R3** |
| GEL | 12.36 | 35% | Feb 12 | none | | **No coverage** |
| INMD | 12.80 | 35% | Feb 10 | none | | **No coverage** |
| SLRC | 11.04 | 35% | Feb 23 PM (f) | 5/2/0 | 12.50 | passes; median below |
| GAIN | 13.89 | 37% | Feb 3 | none | | **No coverage** |
| BCSF | 10.60 | 38% | Feb 26 | none | | **No coverage** |
| CLB | 7.98 | 38% | Feb 4 | none | | **No coverage** |
| HUN | 9.02 | 39% | Feb 17 | 4/12/2 | 10.00 | **KILLED R3** |
| VTS | 14.14 | 39% | Mar 2 | none | | **No coverage** |
| ARR | 11.59 | 40% | Feb 18 | 2/4/0 | 14.50 | **KILLED R3** |
| CMRE | 12.61 | 40% | Feb 18 | none | | **No coverage** |
| MSDL | 13.13 | 40% | Feb 26 | 3/4/0 | 14.00 | **KILLED R3** |
| CIM | 6.85 | 41% | Feb 11 | none | | **No coverage** |
| MNSO | 9.87 | 41% | Mar 30 AM (f) | 14/4/0 | 11.50 | passes the R4 proxy now (killed there Nov 13 at $11.20); median below |
| SD | 11.80 | 41% | Mar 5 | none | | **No coverage** |
| CEPU | 10.27 | 42% | Mar 5 | none | | **No coverage** |
| ELE | 12.09 | 42% | Feb 18 AM (f) | 6/0/0 | 25.98 | passes the screen; **parked: only 2 prints on record** (Aug 11, Nov 10 2026), too few for a median |
| ETD | 14.73 | 42% | Jan 28 | none | | **No coverage** |
| GOOD | 9.47 | 42% | Feb 18 | none | | **No coverage** |
| FSK | 11.16 | 45% | Feb 25 | 1/9/1 | 10.00 | **KILLED R3** |
| AVBP | 12.64 | 46% | Mar 4 PM (f) | 12/0/0 | 22.00 | passes; median below |
| CCU | 9.62 | 46% | Feb 24 | 1/4/5 | 8.48 | **KILLED R3** |
| TME | 9.18 | 46% | Mar 17 | 21/13/0 | 8.96 | **KILLED R4 proxy** (low $8.96 < $9.18) |
| UMH | 14.37 | 47% | Feb 25 PM (f) | 6/2/0 | 16.00 | passes; median below |
| CX | 9.53 | 37% | Feb 5 | 17/2/0 | 12.00 | **Skipped: ratings stamp 2020** (stale, same as Nov 23) |

**Median prints for the 6 that passed and had no median yet** (earnings-day close-to-close from daily bars; AM: prior close to print-day close, PM: print-day close to next close; all past dates `verified: true`):

| Ticker | Prints (oldest first) | Median | R6 cap | Verdict |
|---|---|---|---|---|
| MNSO | -17.6 / +6.4 / -0.1 / +5.5 / -4.2 / -4.4 / +8.4 | 5.5% | 8.25% | **KILLED R6 structural** (< 8%) |
| JBS | -4.5 / -0.2 / +5.7 / -3.8 / -2.9 / -5.5 (6) | 4.15% | 6.2% | **KILLED R6 structural** |
| SLRC | +1.1 / +3.3 / +1.0 / +3.3 / -12.6 / -3.9 / +3.3 | 3.3% | 4.95% | **KILLED R6 structural** |
| AVBP | -0.8 / -3.3 / +3.1 / -7.2 / -0.2 / +0.2 / -4.7 | 3.1% | 4.65% | **KILLED R6 structural** |
| STWD | +0.7 / +2.0 / -2.9 / +0.2 / -1.7 / -1.7 / -6.4 | 1.7% | 2.55% | **KILLED R6 structural** |
| UMH | +0.1 / +0.2 / -0.9 / -2.8 / +1.2 / +3.4 / -3.4 | 1.2% | 1.8% | **KILLED R6 structural** |

## Tally

37 names moved (TAL + 36 rated). TAL to Stopped Watching (R1). 16 no coverage, 8 R3, 1 R4 proxy, 1 stale stamp, 3 already dead R6, 6 killed R6 structural, 1 parked (ELE). 0 chains, 0 searches, 0 advanced, 0 buyable.

**What it says:** in the real-money band ($3-15, bottom quartile, spring prints), low IV and big prints don't come together. All 48 sub-50%-IV names are banks, BDCs, mREITs, utilities, staples, or Latin American ADRs, and every one with coverage that we could date prints under 6%. TAL (9.3% median at 37.5% IV) looks like a one-off, not a category. The hunt is fished out in this band and window. The next real-money source is new print windows (Saturday's Apr 1-30 re-sweep), not lower IV.

## GLOSSARY

- **R1:** Iron Rule 1, the stock has to sit in the bottom quarter (< 0.25) of its 52-week range. TAL is measured on its 252-day closing range; the scanner uses weekly candle highs and lows.
- **R3:** at least 3 Buys, Buys >= Holds, at most 1 Sell. No coverage counts as a fail.
- **R4 proxy:** at the screen, the lowest analyst target has to sit above today's price. The real R4 test is the lowest Buy target above the contract's breakeven.
- **R5:** the per-share price cap on the contract, 10% of reserve / 100 at 3.5/5 conviction ($0.716 tonight).
- **R6:** reachability. The move to breakeven can't be more than 1.5x the stock's median earnings-day move. **R6 structural:** the median print is under ~8%, too small for any spring contract's time value to fit.
- **R7:** liquidity floor, open interest >= 250 and bid/ask spread <= 25% of mid on the exact contract.
- **IV:** implied volatility, the move the options market is pricing in, annualized. Low IV = cheap time value.
- **Median print:** the median absolute one-day stock move on earnings day.
- **Ratio:** median print / (near-the-money time value as % of the stock). About 0.67 or better passes R6 at the ask.
- **Stale stamp:** the ratings record's `updated_at` is old enough that the targets can't be trusted as a floor.
- **(f):** the tool's earnings date is `verified: false`, estimated from cadence.
- **BDC / mREIT:** business development company / mortgage REIT. Income vehicles with small earnings moves.
