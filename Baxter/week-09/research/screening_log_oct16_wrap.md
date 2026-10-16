# Screening log, Fri Oct 16, 2026, 4:15pm ET (WRAP, VM)

PREPARE slot. No chains beyond the queue's own contracts, no web searches. Closing quotes (3:59pm ET) and free ratings only. Three decisions owed to WRAP from the week: ALGM kill vote, TTWO re-vote, ONDS Friday test.

| Ticker | Contract | Stock (close) | Bid / ask | BE (at ask) | Needs | R6 cap | R7 (OI / spread) | Verdict |
|---|---|---|---|---|---|---|---|---|
| RIOT | Nov20 $13C (paper) | $13.735 (-11.4%) | 1.92 / 2.13 | $15.13 | +10.2% | 10.69% | 568 / 10.4% | PARK, floor gate only (R6 margin 0.5 pt) |
| NRG | Dec18 $105C (paper) | $103.745 (+0.9%) | 8.60 / 9.20 | $114.20 | +10.1% | 13.42% | 517 / 6.7% | PARK, floor gate only |
| NXT | Nov20 $80C (paper) | $80.00 (-4.1%) | 7.60 / 8.10 | $88.10 | +10.1% | 13.14% | 258 / 6.4% | PARK, floor gate only |
| INSM | Nov20 $105C (paper) | $96.30 (-2.9%) | 3.90 / 5.80 | $110.80 | +15.1% | 17.1% | 5,117 / 39.2% (closing book) | PARK; R7 re-test on a mid-day quote Monday |
| PL | Jan15 $10C (paper) | $13.56 (-6.7%) | 4.00 / 4.30 | $14.30 | +5.5% | | 4,139 / 7.2% | PARK, floor gate; low $17 still above BE |
| TTWO | Dec18 $190C (paper) | $205.21 (-2.0%) | 25.30 / 27.60 | $217.60 | +6.04% | 7.35% | 850 / 8.7% | **Re-vote: PARK on R4 dating** (see below) |
| ALGM | Nov20 $35C (paper) | $31.61 (-2.3%) | 1.55 / 2.05 | $37.05 | **+17.2%** | 10.5% (kill line 15%) | 6,822 / 27.8% | **KILLED, R6** (and R7 at the close) |
| PAAS | Jan15 $40C (paper) | $44.215 (+1.0%) | 6.00 / 6.70 | $46.70 | | | 5,369 / 11.0% | R1 (over the $42.31 line) |
| BTBT | Jan15 $1C (real) | $0.96 (-11.1%) | 0.15 / 0.18 | $1.18 | +22.9% | 8.23% | 3,290 / 18.2% | R6; moved to watch line |
| ONDS | Dec18 $8C (real) | $6.045 (-4.8%) | 0.27 / 0.32 | $8.32 | +37.6% | 20.89% | 38,086 / 16.9% | R6; moved to watch line |

Ratings (free, unchanged from 3:35 on every name): RIOT 24/1/0 low $22; NRG 16/4/0 low $159 (record Oct 3); NXT 27/4/0 low $101 (record Oct 13); INSM 24/1/0 low $165; PL 8/5/0 low $17; TTWO 29/1/1 low $270 (record Aug 7); ALGM 14/1/0 low $48; PAAS 6/2/0 low $51; BTBT 6/0/0 low $3.50; ONDS 11/0/0 low $13.

## Decisions

**ALGM: killed on R6.** The Wednesday rule was simple: if the breakeven move is still over 15% at Friday's close, it's gone. It closed at +17.2% against a 10.5% cap, the third hour in a row over the line, and the closing spread (27.8%) fails R7 too. Back on the queue only if a fresh scan finds it with a contract that passes R6 on its own.

**TTWO: re-vote, stays parked on R4 dating.** Two things were in the way. (1) The Argus $192 that an Oct 7 search turned up: three searches since (Oct 13-15) found Argus Buy $284 undated and nothing at $192. It's dropped as unverified, not counted against TTWO. (2) What's left is the tool's low, $270, stamped Aug 7. Binder Tab 6 says a floor counts only if it's dated within 60 days; Aug 7 was 70 days ago. So the $192 question is settled, and the dating gate is what's left. Next check (EVENING, one search): a Buy-side target action dated after Aug 17. If one exists at or above ~$218, TTWO goes to a paper doc.

**ONDS: Friday test.** I couldn't find a written definition of the "drop-to-bottom test" anywhere in the journal or queue, so I'm reading it the plain way: if it still failed R6 at Friday's close, it drops to the bottom of the queue and stops getting hourly re-quotes. It failed badly (+37.6% vs 20.89%, worse than any day this week), so ONDS and BTBT both move to a watch line at the bottom, re-quoted once a day.

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + ask.
- **Needs**: the stock move from the close to BE.
- **Dated floor**: binder Tab 6: a Rule 4 target counts only if it's within 60 days and published after the stock's decline.
- **Closing book**: quotes at 3:59pm, often wider than mid-day; a spread fail on the closing book gets re-tested on a mid-day quote before it kills anything.
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
- **Watch line**: names kept at the bottom of the queue, re-quoted once a day instead of every run.
