# SCREENING LOG -- JUL 30, 2026 (18 names, fresh sectors)

*Michael asked for a larger screen before locking in DIS. Fresh ground: transportation/logistics, cybersecurity, casinos/lodging, medical devices -- none of these have had a broad screen before.*

## STAGE 1 -- RANGE PERCENTILE (free, `fetch_price.py --range`)

| Ticker | Price | 52wk Range | Pctile | Direction |
|---|---|---|---|---|
| JBHT | $266.60 | 130.12-299.76 | 80th | PUTS-zone (logged, no search) |
| ODFL | $209.88 | 126.01-252.03 | 67th | MID-OUT |
| CHRW | $144.94 | 96.89-210.33 | 42th | MID-OUT |
| KNX | $69.15 | 38.62-82.86 | 69th | MID-OUT |
| WERN | $36.98 | 23.06-47.49 | 57th | MID-OUT |
| PANW | $322.86 | 139.57-368.80 | 80th | PUTS-zone (logged, no search) |
| FTNT | $153.75 | 70.12-170.35 | 83th | PUTS-zone (logged, no search) |
| ZS | $147.39 | 114.62-336.99 | 15th | CALLS-zone -- chain checked |
| OKTA | $137.81 | 62.66-157.00 | 80th | PUTS-zone (logged, no search) |
| TENB | $33.76 | 15.72-43.67 | 65th | MID-OUT |
| WYNN | $100.69 | 92.52-134.72 | 19th | CALLS-zone -- chain checked |
| MGM | $45.97 | 29.18-51.59 | 75th | MID-OUT |
| CZR | $29.63 | 17.86-30.88 | 90th | PUTS-zone (logged, no search) |
| HLT | $322.94 | 253.54-358.00 | 66th | MID-OUT |
| ISRG | $350.87 | 328.57-603.88 | 8th | CALLS-zone -- chain checked |
| ZBH | $94.67 | 79.12-108.29 | 53th | MID-OUT |
| DXCM | $73.95 | 54.11-89.98 | 55th | MID-OUT |
| PODD | $163.63 | 138.79-354.88 | 11th | CALLS-zone -- chain checked |

**18 attempted, 18 valid. 9 MID-OUT, 5 PUTS-zone (watch list only), 4 CALLS-zone survivors.**

## STAGE 2 -- CHAIN FEASIBILITY (free, `fetch_options_chain.py`)

- **ZS:** cheapest Rule-5-clean strike $185C, requires **+26.3%**. Killed on feasibility -- no software name in this fund's history has cleared a quarter that large; not worth a Rule 6 pull.
- **ISRG:** cheapest clean strike $415C, requires **+18.5%**. Killed on feasibility -- large stable medtech, unlikely to clear.
- **PODD:** no Aug 21 calls in the tradeable ask range at all. Killed, no viable instrument.
- **WYNN:** cheapest clean strike $112C, requires **+12.2%**. Survived feasibility -- advanced to full check.

## STAGE 3 -- WYNN FULL CHECK

Earnings **Aug 4, 2026** (5 days out). Rule 1 pass (19th pctile). Rule 3/4 look clean on the surface -- lowest analyst target $118 (well above $112.85 breakeven), most recent action Mizuho Jul 28 maintains Outperform at $125. Didn't need to go further, because:

**Rule 6, real data (three verified prints, Robinhood equity historicals):**
- Nov 6, 2025: $122.54 -> $126.14, **+2.9%**
- Feb 12, 2026: $115.51 -> $107.85, **-6.6%**
- May 5, 2026: $103.44 -> $106.24, **+2.7%**

Median: **2.9%.** 1.5x cap: **4.35%.** Requirement: **+12.2%** -- roughly 2.8x the ceiling even before quibbling over exact report timing (the most generous single print, -6.6%, only buys a 9.9% cap, still short). Decisive fail. **Killed.**

Also worth flagging even though it's moot: WYNN carries real Macau exposure (Wynn Palace, Wynn Macau segments), the same macro bucket LVS just lost $67 in. Correlated-risk reason to be extra skeptical of this name even if Rule 6 had passed.

## RESULT

**18 screened, 0 advance.** Every CALLS-zone survivor died on chain feasibility or real Rule 6 data, no exceptions, nothing borderline. Three of four killed without spending a single search -- the fourth (WYNN) needed the full historical pull and died anyway.

DIS remains the only name on the table tonight that cleared every rule on real data.

---

## GLOSSARY

- **Range percentile:** where price sits between 52-week low (0%) and high (100%). Bottom quartile = calls candidate, top quartile = puts candidate, middle = no edge.
- **MID-OUT:** a name in the 25-74th percentile band -- no directional edge, screened out at Stage 1, no further work.
- **Chain feasibility:** whether any strike in the option chain has both an ask ≤ $1.00 (Rule 5) and a plausible breakeven, before spending a search on ratings or Rule 6.
- **Rule 6 (Reachability):** the move required to reach breakeven must be no more than 1.5x the stock's own median real earnings-day move (last several verified quarters). A hard gate -- passing every other rule doesn't matter if the catalyst can't plausibly deliver the move.
- **Correlated exposure:** two positions sharing the same macro driver (e.g., Macau gaming) count against the same 35%-of-reserve bucket even if only one is currently open.
