# Screening Log: Mon Oct 5, 2026, MIDDAY run (VM)

**Source:** the research queue left by the OPEN run (`screening_log_oct05_open.md`). No fresh scanner pass: this run worked the queue top-down.

**Rule 5 line this run:** reserve = spendable cash $450.78 (sale proceeds of $290.54 still unsettled). Under $500 the 20%-of-reserve cap governs: 0.20 x 450.78 / 100 = **$0.90/share max ask**. At 3.5/5 (revisions unverifiable on this machine) the tier top is 10% = **$0.45/share**.

**Prices pulled 10:35-10:37am ET.**

## Funnel

| Stage | Names | Tool |
|---|---|---|
| Queue in | 6 (CWH, MRP, AEVA, CIFR, PRME, LRMR) | research_queue.md |
| Rule 2 date check | 6, all unverified, all before Nov 20 | get_earnings_results |
| Chain check (cap 5) | 5 (CWH, MRP, AEVA, CIFR, PRME) | get_option_instruments / get_option_quotes, Nov 20 calls |
| Rule 6 history | 1 (MRP, kill) | get_equity_historicals, 6 prints |
| Survivors | **1: CWH, still blocked on its own 8-K** | |

## Chain-checked (5 of 5)

| Ticker | Direction | Price | Earnings (tool) | Low tgt | Contract tried | Bid/Ask | Breakeven (ask) | Needs | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| CWH | CALLS | $4.38 (-12.9% today) | Oct 27 PM (unverified) | $6.00 | $5C Nov20 | 0.25 / 0.40 | $5.40 | +23.3% | **HOLD IN QUEUE.** R6 cap 23.90%: passes at 97.5% of cap (was 81% at the open). R4 $6.00 > $5.40. R5 $0.40 fits the 3.5/5 $0.45 line. Blocked: Oct 5 8-K unreadable (404 twice), $6 low target still undated. $4C Nov20: 0.65 / 0.90, BE $4.90, +11.9%, but $0.90 > $0.45 at 3.5/5 and OI 15. |
| MRP | CALLS | $22.31 | Oct 22 AM (unverified) | $35.00 | $25C Nov20 | 0.25 / 0.50 | $25.50 | +14.3% | **KILL, R6.** 6-print median 2.24%, cap 3.37%. $22.5C ask 1.45 fails R5. |
| AEVA | CALLS | $14.28 | Nov 4 PM (unverified) | $20.00 | $15C / $17.5C Nov20 | 1.55/2.40, 0.90/1.60 | $17.40 / $19.10 | +22% / +34% | **KILL, R5 + R4.** Every strike under the $20 floor asks over $0.90; any $20+ strike has breakeven above $20. |
| CIFR | CALLS | $15.06 | Nov 2 AM (unverified) | $18.00 | $16C / $17C / $18C Nov20 | 1.66/1.69, 1.33/1.37, 1.08/1.09 | $17.69 / $18.37 / $19.09 | +17% to +27% | **KILL, R5 + R4.** $16-18 asks all over $0.90; $17C and up have breakeven above the $18 floor. |
| PRME | CALLS | $2.89 | Nov 6 AM (unverified) | $4.25 | $3C / $4C Nov20 | 0.05/1.05, 0.00/0.30 | $4.05 / $4.30 | +40% / +49% | **KILL, R5 + R4 + liquidity.** $3C ask $1.05 over cap on a 0.05 bid (no real market); $4C has no bid and breakeven $4.30 > $4.25 floor. |

### MRP Rule 6 detail (AM prints: prior close -> print-day close)

| Print | Prior close | Print close | Move |
|---|---|---|---|
| 2025-05-14 | 26.64 | 27.81 | +4.39% |
| 2025-07-31 | 30.54 | 29.99 | -1.80% |
| 2025-10-23 | 33.03 | 32.80 | -0.70% |
| 2026-02-26 | 31.00 | 31.11 | +0.35% |
| 2026-05-06 | 30.09 | 28.19 | -6.31% |
| 2026-08-04 | 28.65 | 29.42 | +2.69% |

Median |move| 2.24%, cap 3.37%. Needs +14.3%. Not close.

## CWH: what changed since OPEN

- Stock $4.565 at 9:37 -> $4.38 at 10:35, -12.9% on the day ($5.03 Fri close).
- 8-K filed Oct 5 (filing_id d9d05b80...): `get_sec_filing` still 404 "content not available". One search ("Camping World CWH stock falls October 5 2026 8-K") turned up only older items (Truist $20 -> $15 cut, Moody's downgrade). **Cause of today's drop is unknown.** A same-day 8-K plus a double-digit drop is exactly the shape where the floor moves next (pre-announcement, financing, covenant). No doc until it's read.
- Ratings unchanged from OPEN: 11 Buy / 2 Hold / 0 Sell, low $6.00, mean $10.33.

## Queue refill (free checks only)

| Ticker | Price | Earnings (tool) | Ratings | Low tgt | Note |
|---|---|---|---|---|---|
| PCT | $4.045 | Nov 5 PM (unverified) | 3 B / 3 H / 0 S | $6.00 | floor +48% over price |
| RWT | $3.465 | Oct 28 PM (unverified) | 7 B / 2 H / 0 S | $5.22 | mortgage REIT, R6 risk like MRP |
| MFA | $7.29 | Nov 5 AM (unverified) | 3 B / 3 H / 0 S | $10.00 | mortgage REIT, R6 risk like MRP; ex-div today (prev close 7.65 adj 7.29) |

## GLOSSARY

- **Rule 2:** a confirmed earnings date before the option expires. "Unverified" means the tool estimated it from the company's cadence.
- **Rule 4 (bear floor):** the lowest analyst target must sit above the call's breakeven (strike + premium).
- **Rule 5:** one contract's ask must fit the cap: $0.90/share at the 20% screen line, $0.45/share at the 3.5/5 tier top.
- **Rule 6 (reachability):** the move to breakeven can't exceed 1.5x the stock's median earnings-day move over its last 4-8 prints.
- **Breakeven:** strike + premium; where the call neither makes nor loses money at expiry.
- **8-K:** a company's filing for a material event (results, financing, management changes) that can't wait for the quarterly report.
- **Open interest (OI):** contracts outstanding. Low OI plus a wide spread means there may be nobody to sell to.
- **Ex-dividend:** the day the stock trades without its upcoming dividend; the price drops by about the dividend, which isn't a real loss.
- **Kill:** out for this cycle, with the rule that killed it.
