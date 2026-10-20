# Screening log, Tue Oct 20, 2026, 4:15pm ET (WRAP, VM)

PREPARE slot. Closing quotes (3:59pm ET) on the queue's stocks and on the three contracts already picked, plus free ratings. No chain pulls, no web searches. Job: re-measure the parked contracts at the close and hand EVENING 1 and Wednesday's OPEN a clean list.

| # | Ticker | Stock (close) | Day | Ratings (B/H/S, low) | Contract, closing quote | Gate it's waiting on | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | BX | $110.35 | +3.0% | 15/11/1, low $116 (stamp Oct 13) | Nov20 $110C 4.65 / 5.50, OI 976, spread 16.7% | R4: BE $115.50 vs $116, holds by $0.50. **R6: +4.67% vs 4.65% cap, fails by 0.02pt.** Prints Thu Oct 22 AM | PARK (paper only; kill Thu Oct 22) |
| 2 | INSM | $95.69 | +0.4% | 24/1/0, low $165 (no stamp) | Nov20 $100C 3.40 / 5.70, OI 289, **spread 50.5%** | R7 fails on the closing spread (passed at 2:35); R4 dating ($165 owner and date) | PARK (kill Fri Oct 23) |
| 3 | APH | $79.36 | -1.1% | 22/2/0, low $90 (stamp Oct 3) | Nov20 $80C 4.00 / 4.30, OI 5,713 | **R6: ask must be <= $4.18, is $4.30** | PARK (kill Fri Oct 23) |
| 4 | FLUT | $79.02 | +2.1% | 27/9/1, low $84 (stamp Oct 16) | not pulled | Dec18 chain; R4 BE < $84 at the ask | PARK |
| 5 | TTWO | $206.75 | +0.9% | 29/1/1, low $270 (stamp Aug 7, >60 days) | not pulled | a Buy target dated after Aug 21 | PARK |
| W | ONDS | $6.095 | +0.6% | 11/0/0, low $13 | not pulled | R6 (needs ~$6.90) | watch |
| W | BTBT | $0.905 | 0.0% | 6/0/0, low $3.50 | not pulled | R6 (needs ~$1.10) | watch |
| W | CLSK | $8.44 | -0.2% | 15/0/0, low $19 | not pulled | needs > ~$9.20 | watch |

No count or low moved on any queue name since LASTCALL. 0 killed, 0 advanced. Queue 5 live + 3 watch.

**Paper book Rule 4 check (same pull):** every paper floor holds (paper_book.md, WRAP Oct 20 marks). BURL's tool `updated_at` reads 2023-06-28, which can't be a real stamp for a $290 low; the doc's dated Buys (Bernstein $355, BofA $365, Aug 27-28) are the floor of record and $290 stays the binding number. BABA's Baird $160 ages out today; Bernstein $165 (Sep 7) holds.

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **B/H/S**: Buy / Hold / Sell rating counts from `get_equity_analyst_ratings`.
- **BE (breakeven)**: strike + premium, at the ask.
- **Dated floor**: binder Tab 6: a Rule 4 target counts only if it's within 60 days and published after the stock's decline.
- **Kill date**: the day a floor-gated name comes off the queue if no dated Buy target turns up.
- **PARK**: stays on the queue, waiting on the named gate.
- **Watch line**: names at the bottom of the queue, re-quoted once a day instead of every run.
