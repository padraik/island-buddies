# SCREENING LOG -- JUL 30, 2026 (50-name batch, new ground)

*Michael approved DIS as the live pitch, then asked for a 50+ name screen of fresh names before anything else gets queued.*

## STAGE 1 -- RANGE PERCENTILE (free, `fetch_price.py --range`)

Sectors: rail, auto parts, specialty chemicals, apparel/footwear, water utilities, solar, fintech, industrial distributors, marine shipping, coal, big pharma.

**50 attempted. 4 unavailable** (NOVA, ARCH, CEIX -- all appear delisted/merged out of independent listing; DFS -- Discover, absorbed into the Capital One merger). **46 valid.**

- **28 MID-OUT**, no further work: UNP, NSC, BWA, ALV, DAN, LYB, CE, EMN, ALB, HUN, VFC, PVH, RL, COLM, DECK, AWK, WTRG, SEDG, AFRM, COF, SYF, FAST, ZIM, GOGL, BTU, CNX, PFE, GILD.
- **11 PUTS-zone**, logged to watch list, no searches: CSX (84th), CP (76th), CNI (89th), LEA (91st), CWT (80th), ARTNA (81st), GWW (86th), MATX (81st), SBLK (97th), BMY (100th), VTRS (96th).
- **7 CALLS-zone survivors**, advanced to chain check: APTV (22nd), ENPH (23rd), FSLR (21st), RUN (4th), SOFI (7th), WSO (3rd), POOL (9th).

## STAGE 2 -- CHAIN FEASIBILITY (free, `fetch_options_chain.py`)

| Ticker | Cheapest Rule-5-clean strike | Required move |
|---|---|---|
| APTV | $67.50C @ $0.70 | +18.7% |
| ENPH | $43C @ $1.00 | +20.3% |
| FSLR | $310C @ $0.82 | +53.1% |
| RUN | $10C @ $0.83 | +13.5% |
| SOFI | $16C @ $0.96 | **+4.6%** |
| WSO | thin chain, only $350C @ $1.25 (STRETCH) inside any near expiry | not usable |
| POOL | $220C @ $0.50 | +17.6% |

SOFI's number looked too good -- worth checking before anything else.

## STAGE 3 -- THE SOFI TRAP

Stock up **+6.47% today** on real volume (60.8M vs 79.5M avg). Checked why: **SOFI already reported Q2 2026 earnings.** Yahoo's own page has a "Replay the call" link and lists **Earnings Date (est.): Oct 27, 2026** as the *next* print -- there is no earnings catalyst before the Aug 21 expiry at all. The cheap breakeven is cheap because we'd be buying a stock that already made its move, not one about to. Same trap DSGX walked into in June (Tab 5: "never enter OTM on a stock that has already moved on the event the thesis requires"). **Killed on Rule 2 -- no catalyst before expiry.** Also: Morgan Stanley moved same-day (Jul 30), Underweight, target cut $16->$15 -- a fresh bear signal sitting right at current price, one more reason this wasn't the free lunch it looked like.

## THE REST

None of the other six chain survivors got a full workup -- respecting the same budget discipline that killed ZS/ISRG/PODD on sight Wednesday. Required moves of 17-53% on auto parts, solar installers, and industrial distributors are outside what those sectors' earnings days typically deliver (none of this fund's real Rule 6 pulls tonight -- SOUN, ZG, WYNN -- found a required move north of 12% that survived contact with real data). RUN in particular reads as a structurally pressured business (residential solar financing under sustained rate/policy pressure) rather than a single dated event -- Category 2 shape, not Category 1, on sight. None advance.

## RESULT

**50 attempted, 46 valid, 0 advance.** Two full-effort checks tonight (WYNN in batch 1, SOFI in batch 2) both died for real, specific reasons rather than marginal misses. DIS remains the only cleared name across roughly 68 names screened today.

---

## GLOSSARY

- **Post-earnings entry trap:** buying an option after the stock has already reacted to its catalyst. The move that would have paid the option off already happened; what's left is decay with no mechanism, the exact DSGX lesson from June.
- **Category 1 vs Category 2 decline:** Category 1 is a dated, identifiable overreaction (the market oversold one specific event); Category 2 is a structural, ongoing business deterioration with no single event to point to. Only Category 1 is tradeable under this fund's rules.
- **Rule 2 (confirmed catalyst):** the earnings date must fall before option expiry. A stock can look statistically cheap and still fail this rule flatly if its next print is months away.
