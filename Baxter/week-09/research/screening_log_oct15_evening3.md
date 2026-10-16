# Screening log, Thu Oct 15, EVENING 3 (10:00pm ET)

EVENING 3's job: refill the queue to 10+ and leave PREMARKET a loaded plan. The queue started at 7, every name parked on a gate or R6. Two scans tonight: the untouched Nov 20 - Dec 4 print window (all prices), then the $50+ band for prints Oct 22 - Nov 19. All numbers are Thursday's close (quotes stamped 3:59pm ET); option quotes after hours are the closing book.

Names moved past the free screen: 13 (CLSK, VNET, HDL, DRS, ETOR, SKHY, INSM, FTAI, CRH, NRG, WYNN, VSEC, TPB). Free ratings screen: 74 + 97 names. Killed with a written rule: 8 (CLSK, VNET, HDL, DRS, ETOR, SKHY, FTAI, plus 3 R3 / proxy batches below). Advanced: 1 (INSM, paper, dated-floor gate). Queued for a chain check: 5 (NRG, TPB, VSEC, CRH, WYNN). No web searches.

## Held position: COUR

Unchanged since 8pm. Q3 Thu Oct 29 PM `verified: true` (LY Oct 23 PM), `actual: null`. Close 0.50 / 0.60 (OI 3,159, IV 78.6%), stock $5.09. 8/4/0, low $6.00 vs BE $5.65. No SEC filing since Oct 2. Ramp sell Thu Oct 29 3:35pm; Oct 21 3:35pm fallback until PREMARKET finds a second source.

## Scan 1: prints Nov 20 - Dec 4, all prices

Preview (not saved): market cap >= $300M, `FILTER_TYPE_EARNINGS_DATE` 20261120-20261204, 52w range pct < 0.25. **85 rows.** Every ticker had already appeared somewhere in week-08/09, but many only in the Oct 5 sweep table, so all 74 operating companies went back through `get_equity_analyst_ratings` on Thursday's prices. Skipped: closed-end funds and SPACs (NBB, NXP, AWF, EVV, PFLT, CEPF, FCRS, TLNC, SAC, SAAQ, MEVO).

| Result | Names |
|---|---|
| No coverage | IESC, FORTY, HOV, CLFD, ELVR, BBW, BMNR, MATW, APC, YB, SCZM, NOAH, YDES, BULL, XXI, OWLS, NUAI, IMSR, BTQ, ASPI, HTT, ZKH, TUYA, EMAT, TRX, WDH, ORBS, LOT |
| R3 | INTU (2 Sells), DKS (2), DCI (2/7/1), THO (5/10/1), SYM (3 Sells), HRL (4/8), AMTM (5/8), LI (2 Sells), FLNC (5 Sells), YSS (5/9), GEMI (2 Sells), SFIX (1/5), WOOF (2/8/2) |
| R4 proxy | AGX (low $273 vs $367), CPRT ($25 vs $27.71), VIPS ($12.84 vs $13.17), BV ($10 vs $10.53), EIKN ($4 vs $7.78), POST ($79 vs $77.80, record stamped Jan 2023) |
| Pass, left dead on a structural earlier kill | ROAD (R7, OI 0), DOO (R7, OI 2), LGN (R7, OI 13), GGAL (R6, 1.29% median), ATAT (R7, 151% spread), FPS (R2, no provable print), MWH (R7 + R6), BETA (R6), AKTS / EQPT / GENB / INFQ / AGMB / BTGO (print history), MPLT (OI 4), RERE (no options), PXED (no options). These don't change in a day. |
| Pass, in the paper book already | BABA |
| Pass, re-checked tonight (price moved since the kill) | CLSK, VNET, HDL (below); also PONY ($5.23, was $6.07 at its R6 kill: further away), NIO (R4: $3.90 low vs Jan15 $3.5C BE ~$3.93, unchanged), MNSO, TIGR, WRD (R6 on every earlier run; nothing moved in their favor) |

### Re-checks

| Ticker | Stock | Print (tool / LY) | R6 base (6 prints) | Contract | Quote | OI | Spread | BE (ask) | Needs | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| CLSK | $9.35 | Nov 24 PM (f) / Nov 25 PM | +6.0, -6.1, +13.8, +22.0, -5.8, -3.5: median 6.03%, cap 9.04% | Dec18 $9C | 1.44 / 1.59 | 357 | 9.9% | $10.59 | +13.3% | **KILL, R6.** $10C (1.02 / 1.12, OI 1,022) needs +18.9%. Floor $19, 15/0/0, so it's only the clock |
| VNET | $4.40 | Nov 19 AM (f) / Nov 20 AM (6-K: both dates present) | -10.8, -8.0, -1.2, -9.3, +4.0, -16.9: median 8.67%, cap 13.0% | Dec18 $4C / $5C | 0.70 / 1.00; 0.35 / 0.50 | 9; 9,054 | 35%; 35% | $5.00; $5.50 | +13.6%; +25% | **KILL, R6 + R7.** $4C is 0.6 pts over the cap and has OI 9; $5C fails both |
| HDL | $11.61 | Nov 26 | n/a | none | | | | | | **KILL: no listed options** |
| DRS (watch) | $35.47 | Oct 29 AM verified | cap 9.91% (EVENING 1) | Nov20 $33-$36, Dec18 $34-$36 | e.g. Nov20 $34C 2.25 / 3.20 | 0-13 every strike | 30-120% | | | **KILL for good, R7.** No strike near the money has OI over 13 in either month |
| ETOR (watch) | $24.89 | Nov 10 AM verified | cap 15.08% | Dec18 $22.5 / $24 / $25 / $26 | e.g. $24C 2.30 / 3.30 | 0, 0, 23, 0 | 36-58% | | | **KILL for good, R7** |

## Scan 2: $50+, prints Oct 22 - Nov 19

Preview (not saved): market cap >= $300M, earnings 20261022-20261119, `FILTER_TYPE_LAST` >= 50, range pct < 0.25. **201 rows** (at the 200 cap; the bottom row or two may be cut). 97 had not been rated in any Oct 12-15 log; only SKHY and APO were never seen anywhere. All 97 rated in two calls.

- **R3 fails (sample):** NVR, MKL, FICO (4 Sells), LII, WSO, AON (3), HUBS, HON, LOW, COIN (3), GPI, DUOL, DHI, MAA, PHM, CHTR, CPT, CLX, DECK (3), CRWV (3), EIX, BLDR, RBLX, VMC, PDD, SAH, ABG, HSY, ATO, LDOS, MNDY, TXT, ZTS, SF, PFSI, WPC, O, TSN, TDG (12/12/1 passes on a tie; proxy below).
- **R4 proxy fails (low <= ~1.01x price):** LHX, PATK, EQT, NHI, CVNA, UBER, BIDU, TDG, SITE, MCD, ALC, LPX, OLED, TMDX, SRE, SUI, SYK, EXE, AXP, OSK, BKNG.
- **Pass with room (low / price):** INSM 1.65, FTAI 1.63, NRG 1.54, TPB 1.49, VSEC 1.42, SKHY 1.40, BDC 1.35 (record stamped Aug 2025), WYNN 1.33, RBA 1.26, NVMI 1.26, CW 1.24, SGI 1.24, HLNE 1.23, CRH 1.22, IDXX 1.22, NXT 1.21, AZN 1.19, CCJ 1.16 (record stamped 2021), PTCT 1.15, APO 1.13, AXON 1.13, ALB, KKR, EVR, APH, FLUT, ORA (record 2022), AN, BWXT, MLM, XYL, CHRW, TKO, DTE, OTIS, RYAAY (1.04-1.11).

Tonight took the top eight by floor room through dates and R6 (free), then chains on the two that can use Nov 20.

| Ticker | Stock | Print (tool / LY) | Expiry that passes R2 | R6 base (6 prints) | Median / cap | Verdict |
|---|---|---|---|---|---|---|
| **INSM** | $99.21 | Oct 29 AM verified / Oct 30 AM | Nov20 (exactly 21 days past LY; 10-Q Nov 9) | -3.9, -1.8, +16.3, +6.5, -23.4, +33.9 | 11.4% / 17.1% | **ADVANCE (paper).** Chain below |
| FTAI | $168.56 | Oct 29 AM verified / Oct 27 PM | Nov20 | -18.9, +26.6, -3.1, +2.7, +17.2, +0.1 | 10.15% / 15.23% | **KILL, R7.** Nov20 $160 / $165 / $170 / $175 / $180: OI 4, 5, 6, 40, 115; spreads 24-41% |
| SKHY | $142.81 | Nov 13 PM (f); one print on record (Jul 29) | | | | **KILL, print history** (1 print; ZURA precedent) |
| NRG | $102.86 | Nov 5 AM (f) / Nov 6 | Dec18 | +26.2, -13.6, -1.8, +4.3, -4.3, -15.5 | 8.95% / 13.42% | QUEUE: Dec18 chain, max BE $116.66 |
| TPB | $60.31 | Nov 4 AM (f) / Nov 5 | Dec18 | +24.8, +14.2, +6.3, -20.8, +11.0, +2.6 | 12.6% / 18.9% | QUEUE: Dec18 chain, max BE $71.71; watch R7 (small cap) |
| VSEC | $161.55 | Nov 4 PM verified / Oct 27 | Dec18 | +7.8, +10.6, +1.8, +3.2, +16.9, +4.5 | 6.15% / 9.23% | QUEUE: Dec18 chain, max BE $176.46; stock's own after-hours book is $12 wide, R7 likely |
| CRH | $82.32 | Oct 29 AM verified / Nov 5 PM | Dec18 (Nov20 is 15 days past LY) | -4.4, +9.5, -0.8, +0.6, +4.4, -3.7 | 4.05% / 6.08% | QUEUE: Dec18 chain, max BE $87.33; tight |
| WYNN | $76.97 | Nov 5 PM verified / Nov 6 | Dec18 | +0.7, -0.8, +2.9, +5.1, -4.1, +3.6 | 3.25% / 4.88% | QUEUE (low odds): max BE $80.73; needs a ~$77-78 strike under ~$3 |

R6 method: AM prints, prior close to print-day close; PM prints, print-day close to next close (daily bars, regular session).

### INSM Nov20 calls (chain `e8aadc38-a088-43dc-bef2-9e399c0223ec`)

| Strike | Bid / Ask | OI | Spread | BE (ask) | Needs | R6 (<= 17.1%) | R7 | R4 ($165) |
|---|---|---|---|---|---|---|---|---|
| $95C | 9.00 / 12.10 | 66 | 29% | $107.10 | +8.0% | pass | **fail** | pass |
| $100C | 6.90 / 9.60 | 247 | 33% | $109.60 | +10.5% | pass | **fail** (OI 3 short) | pass |
| **$105C** `dc6214c4-3fa5-4299-9179-d1cf03ec5a34` | **4.90 / 5.90** | **5,107** | **18.5%** | **$110.90** | **+11.8%** | **pass** | **pass** | **pass** |
| $110C | 3.00 / 5.40 | 4,372 | 57% | $115.40 | +16.3% | pass | **fail** | pass |

**INSM summary:** R1 0.079, R2 pass (Oct 29 AM verified; Nov 20 is 21 days past LY Oct 30; 10-Q Nov 9 is 9 trading days before expiry), R3 24/1/0, R4 tool low $165 vs BE $110.90, R6 +11.8% vs 17.1%, R7 5,107 / 18.5%. Real money: R5 fails (ask $590 vs the $67.63 line). **Gate: the floor is undated** (the tool's INSM record has no `updated_at`), and the stock is at the bottom 8% of its range after a +33.9% August print, so something big happened between August and now. Until the next DO run knows what (one news search) and who owns the $165, it can't be scored. Ramp sell would be **Wed Oct 28 3:35pm** (pre-market print Thu Oct 29), never past the Oct 29 OPEN.

## What this batch says

The under-$15 bottom quartile is fished out for this print window: of 85 rows, every name that passed ratings had already died on something that doesn't heal overnight (no options, three prints, OI in single digits). The $50+ band is where the floors are healthy and the chains are deep. That's the paper book's hunting ground, and it's where tomorrow's chain checks should go. It is not where the real fund can buy: every contract tonight that passed R7 costs 5-10x the $0.676 line.

## GLOSSARY

- **R1-R7:** the Iron Rules in binder Tab 1. R1 range position, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 price cap on reserve, R6 required move vs. typical earnings move, R7 liquidity (OI >= 250, spread <= 25% of mid).
- **R4 proxy:** a free screen: if the lowest analyst target is already under (or within a hair of) the stock price, no call can have its breakeven under that target, so the name dies before a chain check.
- **Dated-floor gate (Tab 6):** a Rule 4 target only counts if it was published within 60 days and after the stock's decline. An old target from before the drop is a downgrade waiting to happen.
- **BE (breakeven):** strike plus the premium paid, here at the ask.
- **OI (open interest):** contracts currently open at that strike. A thin number means a wide, expensive exit.
- **Print history kill:** fewer than 4 reported quarters means there's no honest median earnings move to test R6 against.
- **(f) / verified:** the earnings tool's flag. `verified: true` means the company announced the date; false is an estimate from its cadence.
- **6-K filer:** a foreign company (most ADRs) that doesn't file 10-Qs, so R2 needs both the tool date and last year's date.
- **Ramp sell:** selling before the print, into the rising pre-earnings premium, instead of holding through the IV crush.
- **Paper:** tracked in `paper_book.md` with no money; real-money entries also need Rule 5.
