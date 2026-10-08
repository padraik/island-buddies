# Screening log, Thu Oct 8, 3:35pm ET (LASTCALL, PREPARE)
**Source:** scanner preview (not saved), same filters as the 1:35 pass: market cap $300M+, stock, price $2-25, earnings **Oct 19 - Oct 30**, 52-week range percentile < 0.25. **120 rows.** Deduped against every Oct 7-8 screening log: **45 names never touched this week** (some may sit in Oct 5-6 logs). Free tools only (LASTCALL is a PREPARE slot: no chains, no searches).
**Rule 5 line:** reserve = spendable = $676.28 -> 3.5/5 line **$0.676**.

## 1. Leftovers from the 2:35 plan (free kills)
| Ticker | Stock | Ratings / low | Verdict |
|---|---|---|---|
| FLG | $11.335 | 12/7/0, $12.00 | **KILL, R4 proxy.** Low only 5.9% over the stock: any OTM strike's BE ($12 + premium) sits above it; the $10C carries $1.34 intrinsic (R5). |
| OWL | $9.265 | 12/7/0, $9.50 | **KILL, R4 proxy.** Low 2.5% over the stock; $10C BE > $9.50, $7.5C carries $1.77 intrinsic (R5). |

## 2. Free ratings screen on the 45 new names
- **R3 fails:** REYN 2/5/1, GNTX 4/6/1, NXRT 1/4/1, UE 2/4, HR 4/9, OCFC 3/4, ARR 2/4, PCG 9/11, LBTYA/LBTYB/LBTYK 4/6/1, HAYW 4/6, SMPL 4/6, FMC 6/12/2, AGNC 3/11, PMT 1/7, MBLY 11/12/1, IVR 1/4/1, ESRT 2/3/1, BRSP 5/0/2 (two Sells), MPT 3/3/2, VRRM 0/8, LPL 6/6/2, CYH 2/5/3, TV 3/8/1.
- **No coverage:** DGICB, GEL, MGPI, VCV, GMTL, TTI, METCB, VNDA.
- **R3 pass, R4 proxy fail:** CORZ 21/2/0 (low $16 vs $15.345, +4.3%), TLK 19/2/1 (low $13.05 vs $12.885, +1.2%).
- **R3 pass, R4 proxy pass: 8 to the queue.**

| Ticker | Stock | R1 | Ratings / low | Low vs stock | Print (tool) / last year | R2 on Nov20 | Note |
|---|---|---|---|---|---|---|---|
| **MRP** | $22.61 | -0.08 | 5/1/0, $35 | +54.8% | Oct 27 AM **verified** / Oct 23, 2025 | PASS (Nov 17 <= Nov 20) | Millrose Properties, $4.8B. Young filer: 10-Q deadline 40 or 45 days? If 45 (Nov 14) it's 4 trading days before Nov 20: fails leg (b). Probably a $2.5 strike grid. |
| **ORN** | $9.02 | 0.10 | 7/0/0, $13 | +44.1% | Oct 27 PM **verified** / Oct 28, 2025 | leg (a) PASS (Nov 18) | Orion Group, $370M: likely 45-day filer -> Nov 14 deadline, 4 trading days before Nov 20: **leg (b) likely fails Nov20**; check Dec18. |
| **RWT** | $3.335 | 0.03 | 7/2/0, $4.25 | +27.4% | Oct 28 PM (f) / Oct 29, 2025 PM | leg (a) PASS (Nov 19) | Redwood Trust, $490M mortgage REIT: filer status to check; R6 risk (REIT prints move little). |
| **ALHC** | $8.74 | 0.08 | 12/2/0, $10 | +14.4% | Oct 29 PM (f) / Oct 30, 2025 PM | PASS (edge, Nov 20) | Alignment Healthcare, $1.8B. Low only 14% up: R4 needs a strike with BE < $10. |
| LKQ | $21.90 | 0.05 | 10/2/0, $25 | +14.2% | Oct 30 (scan) | edge | Ratings `updated_at` May 2025: the $25 low may be stale. |
| CX | $9.58 | 0.13 | 15/4/0, $11 | +14.8% | Oct 26 (scan) | 6-K filer | Ratings `updated_at` 2020: data quality suspect. |
| RKT | $11.77 | 0.04 | 10/8/0, $13 | +10.5% | Oct 30 (scan) | edge | Thin R4 room. |
| WY | $19.10 | 0.07 | 9/3/1, $21 | +9.9% | Oct 30 (scan) | edge | Ratings `updated_at` Nov 2025; one Sell; thin. |

## 3. Tally
47 names screened free: **2 killed on the R4 proxy from the queue (FLG, OWL)**, 2 more R4 proxy kills (CORZ, TLK), 27 R3 fails, 8 no coverage, **8 advanced to the chain stage** (MRP, ORN, RWT, ALHC first; LKQ, CX, RKT, WY behind them). No chains or web searches this run.

## GLOSSARY
- **R1 / Rule 1:** stock in the bottom 20-25% of its 52-week range (0 = at the low; negative = trading under the weekly-candle low).
- **R2 / Rule 2 (Oct 8):** (a) expiry at least 21 days after the later of the tool's date and last year's date; (b) the 10-Q deadline (Nov 9 for 40-day filers, Nov 14 for 45-day filers) at least 5 trading days before expiry. "(f)" = `verified: false`.
- **R3 / Rule 3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4 proxy:** the tool's lowest target vs the stock price, before a strike is chosen. A real R4 pass needs the lowest *Buy* target above breakeven, dated within 60 days and set after the decline.
- **R5 / Rule 5:** one contract's ask must fit the conviction tier's budget ($0.676/share at 3.5/5 on a $676.28 reserve).
- **R6 / Rule 6:** the move to breakeven must be no more than 1.5x the median earnings-day move.
- **BE:** breakeven, strike + premium.
- **6-K filer:** foreign issuer, no 10-Q deadline; both the tool date and last year's date must clear leg (a).
- **Strike grid:** spacing between listed strikes.
