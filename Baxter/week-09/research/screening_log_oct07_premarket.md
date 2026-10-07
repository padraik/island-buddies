# Screening log: Wed Oct 7, PREMARKET (8:30am ET)

*PREMARKET is a prepare slot: no chains, no orders. This batch is date and floor dating on the top of the queue, plus overnight filings. Ratings pulled live this run (`get_equity_analyst_ratings`) are unchanged from Oct 6 on all 14 queue names.*

| Ticker | Direction | Check | Result | Stage after |
|---|---|---|---|---|
| COUR | CALLS | Q3 date | Tool Oct 22 PM, `verified: false`. No 8-K since Sep 21. Web aggregators split Oct 22 / Oct 26. Last quarter's date was announced ~2 weeks ahead (Jul 15 for Jul 29). | Doc complete, date gate shut |
| BRSL | CALLS | Q3 date | Nothing announced. Last year's Q3 call was Tue Nov 4. | Doc complete, blocked |
| TME | CALLS | Q3 date | Nothing announced. Last year: Nov 12, before the US open. | Doc complete, blocked |
| OBDC | CALLS | Date + OBDC II story | 8-K Oct 1 (EX-99.1): "will release its financial results for the third quarter ended September 30, 2026" on "Wednesday, November 4, 2026 after market close", call "Thursday, November 5, 2026 at 10:00 a.m. Eastern Time". OBDC II redemption halt is an early-2026 episode (closed since Nov 2025, return-of-capital plan by Mar 31, 2026), not new news. | Doc complete, blocked on R4 dating |
| GAU | CALLS | R4 floor dating | MarketBeat: HC Wainwright Buy $4.25 (Feb 19, 2026); Canaccord upgrade to Strong-Buy Aug 13 with no target; Zacks Hold Aug 26. Tool's $2.99 low is unattributed. No Buy target dated inside 60 days. | **BLOCKED, R4 dating** |
| SERV | CALLS | R4 floor dating | MarketBeat: Oppenheimer Outperform, $20 -> $7 (Aug 7); Guggenheim Buy, $13 -> $7 (Aug 10). Both cut after the Q2 print. Fresh through Fri Oct 9 only. Nov 11 date unverified. 8-K Oct 5: updated investor deck adding a FY26 cost-of-revenue estimate (no Q3 results, no date). | Chain passed at the ask, floor dated (expires Oct 9) |
| FRMI | CALLS | R4 floor dating | MarketBeat: $6 low = UBS Neutral (May 5), a Hold. Buy-side: Cantor Overweight $8 (Apr 9), Stifel Buy $17 (Jun 23), Mizuho Outperform $11 (Jul 28). None inside 60 days. | **BLOCKED, R4 dating** |
| QUBT | CALLS | Filings | 8-K Oct 2, Items 7.01/9.01: investor presentation. Nothing thesis-moving. | Chain passed at mid only |
| ADTN, MLCO | CALLS | Filings | None since Oct 1. | Blocked (stale floors) |

**Pre-market quotes (12:30 UTC):** COUR 5.18 (close 5.12), TME 7.87 (7.93), OBDC 10.00 (10.03), GAU 2.10 (2.06), SERV 4.73 (4.77), QUBT 7.75 (7.86), FRMI 4.14 (4.23), ADTN 7.47 (7.62). Thin pre-market books; OPEN requotes before anything.

**Kills this batch:** none outright. Two names moved to blocked (GAU, FRMI) on the Tab 6 dated-floor rule.

## GLOSSARY
- **R4 / bear floor:** the lowest Buy-rated analyst target must sit above the call's breakeven (strike + premium).
- **Dated floor (Tab 6):** a target counts only if it was published within 60 days and after the stock's decline.
- **Hold vs Buy:** a Neutral / Equal Weight / In-Line target is a Hold; it can't be the floor.
- **verified: false:** the earnings date in the tool is estimated from the company's cadence, not announced by the company.
- **8-K Item 2.02 / 7.01:** results of operations / Regulation FD disclosure (often an investor deck).
- **EX-99.1:** the press release or presentation attached to an 8-K.
