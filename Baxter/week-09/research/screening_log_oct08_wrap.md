# Screening log, Thu Oct 8, 4:15pm ET (WRAP, PREPARE)

WRAP slot: no order tools, no chains, no searches. Closing quotes on 18 queue names, ratings on 22, `get_earnings_results` on the six names at the top of the queue (ARDX, UPBD, MRP, ORN, RWT, ALHC). Reserve $676.28 settled (COUR holds $65), 3.5/5 line $0.676.

## Top of the queue (chain stage next)

| Ticker | Close | Day | Ratings (B/H/S, low) | Print (tool) | Last year | Status |
|---|---|---|---|---|---|---|
| ARDX | $3.265 | +0.2% | 11/0/0, $8.00 | Oct 29 PM, `verified: false` | Oct 30 PM | Unchanged. Floor-blocked ($8 holder unknown). Citi $11 goes stale after Fri Oct 9. |
| UPBD | $15.695 | +0.5% | 5/1/0, $20.00 | Oct 29 AM, `verified: false` | Oct 30 AM | Unchanged. Floor-blocked, R3 in doubt (MarketBeat 1 Buy / 3 Hold). |
| MRP | $22.63 | 0.0% | 5/1/0, $35.00 | Oct 27 AM, `verified: true` | Oct 23 AM | Unchanged. Chain + filer class next. |
| ORN | $9.08 | +0.1% | 7/0/0, $13.00 | Oct 27 PM, `verified: true` | Oct 28 PM | Unchanged. Chain + filer class next. |
| RWT | $3.35 | +0.3% | 7/2/0, $4.25 | Oct 28 PM, `verified: false` | Oct 29 PM | Unchanged. Chain + R6 next (mREIT). |
| **ALHC** | $8.725 | +2.0% | 12/2/0, $10.00 | Oct 29 PM, `verified: false` | Oct 30 PM | **After hours $7.50 (20:15 UTC), -14.0% from the close, bid 7.34 / ask 7.54. Cause not checked (no searches in WRAP).** At $7.50, a Nov20 $9C needs +20% before premium; the $10 low is +33%. First job for the next DO run: one search for the cause (Medicare Advantage star ratings season is the first thing to check), then re-rate R1 and re-pull ratings. |
| LKQ | $22.015 | -0.1% | 10/2/0, $25.00 (`updated_at` May 2025) | | | Ratings data stale. Date the low first. |
| CX | $9.55 | -0.4% | 15/4/0, $11.00 (`updated_at` 2020) | | | Ratings data stale; 6-K filer. |
| RKT | $11.765 | +2.8% | 10/8/0, $13.00 | | | Thin R4 room (+10.5%). |
| WY | $19.17 | +3.2% | 9/3/1, $21.00 (`updated_at` Nov 2025) | | | Thin R4 room (+9.5%), one Sell. |

## Doc / floor-blocked names (close marks)

| Ticker | Close | Day | Ratings (B/H/S, low) | Note |
|---|---|---|---|---|
| WRD | $4.515 | **-9.0%** | 13/0/0, $10.51 | Lowest close of the week; still no cause found. R6 fails at any realistic ask. BofA floor ages out Oct 13. |
| ONDS | $6.857 | -4.6% | 11/0/0, $13.00 | Nov20 fails R2 (Oct 8 text); Dec18 needs stock ~$7.15 at a $0.65 ask. passes.md row added. |
| QUBT | $7.45 | -2.2% | 5/2/0, $10.00 | Nov20 fails R2; Dec18 failed R6 at 11:35. |
| TME | $7.95 | -0.5% | 22/14/0, $9.0494 | Floor cluster ages out Sun Oct 11. |
| TDUP | $2.34 | +5.4% | 6/1/0, $5.70 | Floor stale (Aug 6). Jan15 $2.5C is the contract. |
| FRMI | $3.655 | -7.9% | 6/2/0, $6.00 | Second big down day. Floor-blocked. |
| GAU | $2.105 | +7.9% | 5/1/0, $2.9859 | Floor-blocked. |
| OBDC | $10.175 | +1.5% | 11/2/0, $11.00 | Floor-blocked. |
| ADTN, MLCO, PCT, ENVX | | | 7/2/0 $11; 11/4/0 $5.30; 3/3/0 $6; 7/3/1 $5 | Unchanged. |

No kills, no advances. Ratings unchanged on all 22 names versus 3:35pm. Dates unchanged on all six checked.

## GLOSSARY

- **Close mark:** the last regular-session trade at 4:00pm ET.
- **After hours (AH):** trading after the 4:00pm close; thinner and wider than the regular session.
- **R1 / Rule 1:** stock in the bottom 20-25% of its 52-week range.
- **R2 / Rule 2 (Oct 8):** (a) expiry at least 21 days after the later of the tool's date and last year's date; (b) the 10-Q deadline at least 5 trading days before expiry.
- **R3 / Rule 3:** at most 1 Sell, at least 3 Buys, Buys at least equal to Holds.
- **R4 / Rule 4:** lowest Buy target above breakeven, dated within 60 days and set after the decline.
- **R5 line:** max ask per share for one contract at the conviction tier ($0.676 at 3.5/5 on a $676.28 reserve).
- **R6 / Rule 6:** the move to breakeven must be no more than 1.5x the median earnings-day move.
- **BE:** breakeven, strike + premium. **verified:** company-announced date (true) vs estimated from cadence (false).
- **6-K filer:** foreign issuer, no 10-Q deadline. **mREIT:** mortgage real estate investment trust.
- **`updated_at`:** when the ratings tool last refreshed that symbol's targets; an old stamp means the low may not be real.
