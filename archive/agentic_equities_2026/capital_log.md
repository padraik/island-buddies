# Agentic Equities -- Capital Ledger

**This file is the ONLY source of truth for how much money Patrick has actually put into this account.** It is maintained by hand (Patrick tells Claude, Claude edits this file) in an interactive session -- the unattended routine reads it every firing to separate deposits from investment growth, but never writes to it. Robinhood's own API has no tool in this routine's allowed set that reports deposit/transfer history, so there is no way for the routine to discover a deposit on its own -- if this file is wrong or stale, every firing's growth/drawdown math will be wrong too. Keep it current the same day money moves.

**net_deposited = sum of every row below.** The routine computes this by reading the file and summing the Amount column; it does not cache or hardcode the total anywhere else.

| Date | Type | Amount | Note |
|------|------|--------|------|
| 2026-07-21 | seed | 300.00 | Initial funding, account opened |
| 2026-09-08 | deposit | 100.00 | Patrick added capital |

**Running net_deposited as of the last row above: $400.00.**
