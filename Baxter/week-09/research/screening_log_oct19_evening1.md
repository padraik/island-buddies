# Screening log, Mon Oct 19, 2026, 6:00pm ET (EVENING 1, VM)

*Market closed; stock prices are the 3:59pm close plus after-hours where noted. Reserve $676.28 (3.5/5 real-money line $0.676). Every name here is paper-track: none has a contract under the real-money line that passes R6. Job tonight: the LASTCALL plan's floor-dating searches (10 searches, 8 names), plus free ratings and quotes on all 14 queue names.*

## Part 1: floor owners (Rule 4 dating, binder Tab 6)

| # | Ticker | Tool low (B/H/S) | BE on the queued contract | What the search found | Verdict |
|---|---|---|---|---|---|
| 1 | **MSTR** | $165 (20/2/0) | Dec18 $120C ~$143-146 at recent asks | **Barclays (Cremo), Overweight: $125 -> $160 on Sep 15, then $160 -> $175 on Oct 9.** Canaccord $179 (Sep 8, raised). The $165 itself still has no owner, but a Buy dated Oct 9 sits at $175, well after the $306 -> $82 slide, and $29+ over BE. Caveat: read through search snippets (cryptobriefing / KuCoin / stocktwits), not the note itself, and Oct 9 is before Friday's -9.6% day | **ADVANCE to paper doc (EVENING 2).** R1 needs the stock under $137.90 at the entry run (closed $135.80, AH $136.00) |
| 2 | **NRG** | $131 (16/4/0, stamp Oct 3) | Dec18 $105C, $111.60 | No $131 cut found. Results: Morgan Stanley $165 -> $162 (Aug 21), Scotiabank $226 -> $211 (Aug 5), Raymond James $220 -> $210, and an old Jefferies "$113 -> $132" headline. The $131 may be a stale Jefferies line resurfacing in the feed, not a fresh cut | **PARK.** Floor still undated; R6 margin ~1 pt at Monday's ask |
| 3 | **NXT** | $101 (27/4/0, stamp Oct 13) | Nov20 $80C ~$89.70 | $101.20 is an old *average* target headline; Needham $102 (initiation), Jefferies $104, Barclays $105 all undated, and they read like 2025 headlines | **PARK, kill Mon Oct 26** if nothing dated turns up |
| 4 | **INSM** | $165 (24/1/0) | Nov20 $105C ~$109.90 | **$165 = Mizuho, Outperform, Aug 13 2025** (raised from $130). That's 14 months old and from before the stock fell to $95 | **KILL, R4 (Tab 6 stale floor).** The tool's low is a pre-decline target; nothing dated was found to replace it |
| 5 | **RIOT** | $22 (24/1/0) | Dec18 $13C ~$15.40 | Cantor (Knoblauch) has been at $22 before, but has raised since ($24, $26, then $25 -> $31 on Jan 16 2026). One aggregator says a "$22-$45 verified range, checked Oct 6," which suggests somebody holds $22 now, owner and date unknown | **PARK, kill Tue Oct 27** |
| 6 | **CIFR** | $18 (23/2/0) | Dec18 $10C ~$11.45 | **$18 = JP Morgan upgrade, Nov 24 2025.** Saturday found KBW $28 (Aug 6), also >60 days | **KILL, R4 (Tab 6 stale floor)** |
| 7 | **UEC** | $10 (8/3/0) | Jan15 $7C ~$8.72 | $10 = National Bankshares / Roth $10.25, both 2025-era (same finding as Saturday). HC Wainwright $26.75 (Mar 11 2026), also >60 days | **KILL, R4 (Tab 6 stale floor)** |
| 8 | **PL** | $17 (8/5/0) | Nov20 $10C ~$14.70 | **$17 = Northland and Deutsche Bank, Dec 2025** (Wedbush went $17 -> $20 the same month). Ten months old | **KILL, R4 (Tab 6 stale floor)** |

**Pattern worth writing down:** in five of eight names (INSM, CIFR, UEC, PL, and probably RIOT and NRG), the tool's `low_price_target` traced back to a target from 2025. The tool doesn't seem to drop old targets, so its low can be a ghost. That's why "floor-gated" names never cleared: there was never a dated floor to find. Going forward, if one search traces a tool low to a pre-decline target, that's a kill on Tab 6, not a park.

## Part 2: free re-checks (no search)

| Ticker | Close | Ratings | Gate | Verdict |
|---|---|---|---|---|
| FLUT | $77.30 | 27/9/1, $85 (Oct 16) | Dec ask <= $9.95 (R4 at the ask) | PARK, Tue OPEN re-quote |
| TTWO | $204.92 | 29/1/1, $270 (stamp Aug 7) | needs a Buy dated after Aug 17 | PARK |
| PAAS | $44.44 | 6/2/0, $51 | R1 (needs <= $42.31) | PARK |
| ONDS / BTBT / CLSK | $6.06 / $0.905 / $8.445 | 11/0/0 $13; 6/0/0 $3.50; 15/0/0 $19 | revive lines ~$6.90 / ~$1.10 / ~$9.20 | watch |

Held position: **COUR** 8/4/0, low $6.00 (BMO, Oct 5, dated) vs BE $5.65. Unchanged. Paper LVS 17/7/0 low $40 (BE check in paper_book). BA low still $195 (owner not searched; paper position already closed).

## Tally

14 names moved or re-checked: **MSTR advanced** (dated Buy found, to a paper doc); **INSM, CIFR, UEC, PL killed** (R4, stale floor); NRG, NXT, RIOT parked with kill dates/gates; FLUT, TTWO, PAAS free re-check; 3 watch names re-quoted. 10 searches.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules: R1 range percentile <= 0.25, R2 earnings proven before expiry, R3 consensus (<= 1 Sell, >= 3 Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability, R6 breakeven move <= 1.5x median earnings move, R7 OI >= 250 and spread <= 25% of mid.
- **Tab 6 stale floor:** a Rule 4 target counts only if it's dated within 60 days and published after the stock's decline. A target older than that isn't a floor.
- **Tool low:** `low_price_target` from `get_equity_analyst_ratings`.
- **BE:** breakeven, strike + ask.
- **PARK / kill date:** stays on the queue waiting on one gate; comes off on the kill date if the gate doesn't clear.
- **Paper:** tracked in `paper_book.md`, no money; R5 dropped.
- **AH:** after-hours.
