# Screening log, Mon Oct 19, 2026, 4:15pm ET (WRAP, VM)

PREPARE slot. Closing stock quotes (3:59pm ET) and free ratings only: no option chains, no web searches. Job: confirm nothing moved in the queue since LASTCALL, and hand EVENING 1 and Tuesday's OPEN a clean list.

| # | Ticker | Stock (close) | Day | Ratings (B/H/S, low) | Gate it's waiting on | Verdict |
|---|---|---|---|---|---|---|
| 1 | MSTR | $135.80 | -0.8% | 20/2/0, low $165 (no stamp) | R4 dating: who owns $165, and is it post-slide | PARK; R1 holds (under $137.90) |
| 2 | CIFR | $8.94 | -0.4% | 23/2/0, low $18 | R4 dating | PARK |
| 3 | UEC | $7.885 | -0.3% | 8/3/0, low $10 | R4 dating | PARK |
| 4 | RIOT | $13.97 | +1.8% | 24/1/0, low $22 | R4 dating (kill Oct 27) | PARK |
| 5 | FLUT | $77.30 | +2.2% | 27/9/1, low $85 (stamp Oct 16) | Dec ask <= $9.95 for R4 at the ask | PARK; re-quote Tue OPEN |
| 6 | NRG | $99.41 | -4.2% | 16/4/0, low $131 (stamp Oct 3) | who cut to $131; R6 margin ~1 pt at Monday's ask | PARK |
| 7 | NXT | $79.72 | -0.4% | 27/4/0, low $101 (stamp Oct 13) | R4 dating (kill Oct 26) | PARK |
| 8 | INSM | $95.285 | -1.0% | 24/1/0, low $165 | R4 dating (kill Oct 26) | PARK |
| 9 | PL | $13.59 | +0.2% | 8/5/0, low $17 | R4 dating | PARK |
| 10 | TTWO | $204.92 | -0.2% | 29/1/1, low $270 (stamp Aug 7, >60 days) | a Buy target dated after Aug 17 | PARK |
| 11 | PAAS | $44.44 | +0.5% | 6/2/0, low $51 | R1 (needs <= $42.31) | PARK |
| W | ONDS | $6.06 | +0.3% | 11/0/0, low $13 | R6 (failing by miles) | watch |
| W | BTBT | $0.905 | -5.7% | 6/0/0, low $3.50 | R6 | watch |
| W | CLSK | $8.445 | +0.5% | 15/0/0, low $19 | needs > ~$9.20 | watch |

No count or low moved on any queue name since LASTCALL. 0 killed, 0 advanced.

**Paper book Rule 4 check (same pull):** BA's tool low read **$195** (was $206 since Oct 3; `updated_at` unchanged), under the $202.70 breakeven: paper BA closed at the $6.55 closing bid (-$115), per `research_BA_paper.md`'s exit plan. Every other paper floor holds (paper_book.md, WRAP Oct 19 marks).

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **B/H/S**: Buy / Hold / Sell rating counts from `get_equity_analyst_ratings`.
- **Dated floor**: binder Tab 6: a Rule 4 target counts only if it's within 60 days and published after the stock's decline.
- **Kill date**: the day a floor-gated name comes off the queue if no dated Buy target turns up.
- **PARK**: stays on the queue, waiting on the named gate.
- **Watch line**: names at the bottom of the queue, re-quoted once a day instead of every run.
