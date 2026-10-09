# ETF PROPOSAL: how the Island Fund would pick ETF calls

*Drafted Fri Oct 9, 2026, local session, right after the call where Michael asked for it. Michael's words: "This is one where we need to grind on it. Go ahead and put together a proposal for how we make decisions on ETFs. Do research rather than winging it. See if we can find any already-successful methods of selecting plays. It's ok to include multiple options. I want to get a doc ready that tees up Fable to do the big thinking."*

*Status: PROPOSAL. Nothing here is a rule yet. No ETF goes in the real fund or the paper book until a Fable session with Michael picks a method and an ETF tab is ratified.*

---

## 1. WHY ETFS NEED THEIR OWN RULEBOOK

Our whole method is built around one event: a company's earnings print. The Iron Rules depend on it:

| Rule | What it needs | ETF problem |
|---|---|---|
| R1 (bottom of the 52-week range) | a price history | Works as is. |
| R2 (earnings catalyst before expiry) | a company reporting earnings | **ETFs don't report earnings.** Dead as written. |
| R3 (near-zero Sells) | analyst ratings | ETFs have no analyst ratings. Dead as written. |
| R4 (lowest Buy target above breakeven) | analyst price targets | No targets. Dead as written. |
| R5 (affordability) | an option ask | Works as is. |
| R6 (move needed vs. median earnings move) | past earnings reactions | No earnings reactions. Needs a different "typical move on catalyst day." |
| R7 (liquidity floor) | OI and spread | Works, and most big ETFs pass easily. |

So four of the seven rules need a replacement, not a tweak. That's why this goes to Fable instead of getting patched in a sweep.

---

## 2. WHAT THE RESEARCH SAYS (the honest version)

I went looking for "already-successful methods" for picking ETF calls. Short version: **I did not find a documented, still-working method for buying ETF calls.** I found several real effects, but each one either faded after it was published, or is small next to what an option costs. Here's what's out there.

### 2a. The headwind behind all of it: option buyers pay a premium
- Index options usually price in more movement than actually happens. That's the **variance risk premium**. The buyer pays it, the seller collects it. Coval and Shumway (2001) found at-the-money S&P straddles lost about 3% a week on average. Later work found out-of-the-money calls have negative average returns, and the further out of the money, the worse.
- Buying when options look "cheap" (low IV, IV under realized) doesn't fix it. A study of VIX data from 1990 to 2014 found the premium was there 88% of the time, **including calm markets**. The low-IV long-options rules on TradingView and similar sites are heuristics, not tested results.
- **Why this matters to us:** our stock method gets around this by picking a specific stock with a specific catalyst that the market is underpricing (R1 + R3 + R4 + R6). An ETF is a diversified basket, and its options are some of the most efficiently priced contracts in the world. Any ETF method has to say where its edge comes from. If it can't, the premium eats it.

### 2b. Scheduled macro events (FOMC, CPI, jobs report)
- **Pre-FOMC drift** (Lucca and Moench, 2015): stocks used to rise in the 24 hours before Fed announcements. Follow-ups say it only held at meetings with a press conference, and Kurov, Wolfe and Gilbert found it **basically disappeared after 2015**. One regime result is still interesting: when implied vol was above its median, the pre-FOMC drift averaged 109 bps; below the median, only 9.7 bps.
- **Option pricing around events:** implied vol climbs about two days before FOMC and collapses after it. Fed and NBER papers find FOMC, CPI and jobs-report days carry a real premium, and it's already priced into the options. Holding a long call through the release means paying for the event and then eating the vol crush.
- **Read:** the macro calendar gives us a real Rule 2 replacement (a dated, scheduled event), but the research says the event is priced in. A method built on it needs a directional edge from somewhere else.

### 2c. Sector ETFs as earnings baskets
- Single-stock IV spikes into earnings. Index and sector IV runs lower because the names diversify each other. ORATS builds an "expected earnings move" for sector ETFs by weighting the members' implied earnings moves.
- A sector whose biggest holdings all report in the same 2-3 weeks (big banks for XLF/KRE, semis for SMH, oil majors for XLE/XOP) is the closest thing to our current method: it has a dated catalyst and analyst targets on the members.
- I found no rigorous study of whether sector-ETF options are under- or over-priced going into earnings season. A 2017 tastylive segment looked at it, but the result wasn't visible. This is a hole that we'd have to fill ourselves.
- **Read:** the closest fit to how we already think. Unknown edge.

### 2d. Momentum and trend
- **Industry momentum** (Moskowitz and Grinblatt, 1999): strong in 1963-1995 data. The cleanest out-of-sample test on **sector ETFs** after 2000 found **no momentum**. Practitioner backtests (rotate into the strongest SPDR sector monthly, 1998-2015) barely beat equal weight and change a lot with the lookback window.
- **Time-series momentum / trend following** (Moskowitz, Ooi, Pedersen, 2012): positive in every futures market they tested, 1985-2009. Later work says most of the alpha came from volatility scaling, and the edge vanished in 2009-2013.
- **Read:** slow, monthly effects with small edges. Bad match for a 30-60 day long call that pays theta every day.

### 2e. Mean reversion and buying fear
- **Connors RSI(2)** (2008): buy ETFs after a sharp 2-day drop. The ETF version "still works, slightly less effective" after 2009, per a practitioner re-test. A 2016-2026 Nasdaq-100 test trailed buy-and-hold badly (2.4% vs 20.2% a year). No peer-reviewed walk-forward test.
- **Buying after VIX spikes:** S&P forward returns after a 20% VIX spike averaged +0.8% (5 days), +0.9% (1 month), +1.6% (3 months), across 74 spikes since 1990. After a 5-point jump in SPY 30-day IV: +5.1% over 20 days, but on only 9 days, with overlapping windows.
- **The catch for us:** fear is exactly when calls are most expensive. A +1.6% index move over 3 months doesn't cover the premium on a call bought with VIX spiking.
- **Read:** this is the one that looks most like our Rule 1 (buy near the lows), and it's also the one where we'd pay the most for the option.

### 2f. Calendar effects (turn of the month, pre-holiday)
- Turn of the month: all excess market return in 1987-2005 came in a 4-day window around month-end. The Atlanta Fed found it disappeared in S&P futures after 1990. The 2011 ETF study says it shrank and moved to the 1st trading day.
- Pre-holiday: diminished since the late 1980s except in small caps.
- **Read:** 0.1-0.2% effects. Far too small for options. Listed so Fable doesn't have to look again.

---

## 3. THE FUND'S OWN CONSTRAINTS (any ETF method has to live inside these)

- **Long calls only** (hard limit 3). No spreads, no selling premium. Most of the "ETF options strategies that work" in the literature are on the **selling** side (collecting the variance risk premium). That door is closed to us by the hard limits, and should stay closed for a cash account this size.
- **Affordability.** Rule 5 line today: $0.676/share (10% of $676 reserve, 3.5/5 tier). Hard limit 7 caps one position at 20% of fund ($148). Rough rule of thumb (not a quote): a ~1-month at-the-money call costs about 0.4 x IV x sqrt(T) x price. At 20% IV and 30 days, that's ~2.3% of the price, so the real fund's line only covers ATM calls on ETFs priced near **$30** or less. Today's prices (Oct 9, `fetch_price.py`): FXI $34.20, XLU $41.37, IBIT $46.80, XLF $54.69, SLV $54.91, XLE $65.39, EEM $66.67, KRE $69.17, TLT $77.90, HYG $77.20, GDX $89.36, ARKK $89.94, XHB $94.93, XBI $154.03, XOP $193.17, XLK $198.59, IWM $279.25, SMH $603.30, QQQ $750.79, SPY $778.21. **Translation:** for the real fund, ETFs are a paper-book project for now, same as the large caps. That's fine; that's exactly what Michael said the paper book is for.
- **Rule 7** (OI >= 250, spread <= 25% of mid): most of the list above passes easily on near strikes. Not the constraint.
- **Leveraged ETFs** (TQQQ, SOXL, etc.) would be cheap per share, but they decay from daily rebalancing and behave differently from the index they track. Recommend: **excluded** unless Fable finds a reason.
- **Data we can get for free:** daily price history and 52-week ranges (`fetch_price.py`, `get_equity_historicals`), live chains and quotes (`fetch_puts_chain.py --calls`, `get_option_quotes`), option candles only while a contract is alive (`get_option_historicals`; Robinhood deletes them at expiry). **We have no historical implied vol.** That's the big gap for any back-test of option P&L, and the research warns that back-tests without real historical IV overstate results by 30-50%.

---

## 4. THE CANDIDATE METHODS

Four options plus a "no." Each is written as a draft rulebook so Fable has something concrete to attack.

### Option A: Sector earnings basket (closest to what we do now)
- **Universe:** sector ETFs where the top 10 holdings are >= 50% of the fund (XLF, KRE, SMH, XLE, XOP, XHB, XBI, etc.).
- **R1:** ETF in the bottom 25% of its 52-week range.
- **R2 replacement:** >= 50% of the ETF's weight reports inside the window, and expiry is >= 21 days after the last of those prints.
- **R3/R4 replacement:** weight-averaged across the reporting holdings: near-zero Sells, and the weighted lowest-Buy-target implies upside above breakeven.
- **R6 replacement:** the move needed to break even is <= 1.5x the ETF's median move across its last 4-8 earnings seasons (measured from the trading day before the first big print to the day after the last).
- **Where the edge would come from:** the same as our stock method (a beaten-down group the analysts still like, going into a dated catalyst), spread across a basket.
- **Open questions:** do sector ETFs actually move enough over an earnings season to clear R6 after premium? Is sector-ETF IV underpriced going into the season? (No study found. We'd measure it.)

### Option B: Macro event, high-uncertainty regime only
- **Universe:** SPY, QQQ, IWM, TLT, sector ETFs sensitive to rates (XLF, KRE, XHB, XLU).
- **R2 replacement:** a scheduled FOMC (press-conference meeting), CPI, or jobs report before expiry.
- **Gate:** only when implied vol is above its 1-year median (the regime where the pre-FOMC drift still showed up).
- **Exit:** sell **before** the release (the run-up is the trade, the vol crush is the risk). That's our sell-the-ramp rule, moved to macro events.
- **Where the edge would come from:** the pre-event drift in high-uncertainty regimes. **Weakest research support of the four**: most evidence says the drift is gone and the event premium is already priced.

### Option C: Buy the fear (Rule 1 at full strength)
- **Universe:** broad index and sector ETFs.
- **Trigger:** ETF in the bottom 10% of its 52-week range AND a volatility spike (VIX up >= 20% off its recent low, or the ETF's own IV jumps >= 5 points), OR RSI(2) < 5.
- **Contract:** 60-90 days out (the forward-return data is best at 1-3 months), strike where breakeven is reachable by the historical 3-month post-spike return.
- **Exit:** ladder on the bounce; hard time stop at half the contract's life.
- **Where the edge would come from:** documented positive forward returns after fear spikes. **Problem:** we'd be buying exactly when calls cost the most, and the average bounce (+1.6% over 3 months on the S&P) is small. Likely only works on higher-beta ETFs (KRE, XBI, XOP, ARKK, small caps).

### Option D: Earnings-season read-through on a single theme
- Use the stock method's own work: when the real or paper funnel finds 3+ names in one industry passing R1-R4 into the same season, buy the **sector ETF** call instead of (or alongside) the single names on paper.
- **Where the edge would come from:** if the funnel keeps finding the same beaten-down industry, that's a sector signal, and the ETF is the liquid, Rule-7-proof way to hold it.
- **Cheapest to test:** it piggybacks on research we already do every run.

### Option E: No ETFs
- Legitimate answer. The research says ETF calls are the most efficiently priced contracts we could buy, and the documented edges are on the selling side. If Fable can't find where an edge comes from, we say so and stay on single names.

---

## 5. MY RECOMMENDATION GOING IN (so Fable has something to disagree with)

- **Lead candidates: A and D,** tested together, because they come from the method we already trust and give us analyst data to work with. D costs nothing extra to run.
- **C as a test:** paper only, high-beta sector ETFs only. It's the one with real forward-return data behind it.
- **B: skip** unless Fable finds post-2019 evidence the drift came back.
- **Leveraged ETFs: excluded.**
- Everything starts in the **paper book**, under the same honest fills (ask in, bid out) and Rule 7. Real money only after N paper closes beat a written benchmark (Fable sets N and the benchmark).

---

## 6. WHAT FABLE SHOULD DO (the session agenda)

This clears the MODEL COST AWARENESS bar: its output writes a new binder tab.

1. **Attack section 2.** Is there a documented ETF long-option method I missed? Specifically: (a) post-2019 evidence on the pre-FOMC drift, (b) any study of sector-ETF implied vs realized moves around earnings season, (c) buying calls after volatility spikes, net of the higher premium.
2. **Pick or kill each of A-E,** with the reason, and say where the edge comes from for each survivor. "We'd measure it" is an acceptable answer only if the test is designed in the same session.
3. **Write the replacement rules** for R2, R3, R4, R6 for each surviving option, in binder language, with exact numbers.
4. **Design the back-test** we can actually run with free data (price history from Robinhood, no historical IV). Spell out what it can and can't tell us without IV, and what paper-book data closes that gap.
5. **Set the graduation bar:** how many paper closes, compared against what (SPY buy-and-hold over the same days? the large-cap paper book?), before an ETF tab can touch real money.
6. **Sanity check the affordability math** in section 3 against live chains on 4-5 ETFs from the list, so we know which ones the real fund could ever touch at a given reserve.

**Inputs to hand Fable:** this doc, binder Tab 1 (Rules 1-7) and Tab 4 (exits), `paper_book.md`, and whatever the large-cap paper book has closed by then.

---

## SOURCES

- Pre-FOMC drift: [NY Fed Liberty Street, more recent evidence (2018)](https://libertystreeteconomics.newyorkfed.org/2018/11/the-pre-fomc-announcement-drift-more-recent-evidence.html); [Kurov, Wolfe, Gilbert, The Disappearing Pre-FOMC Announcement Drift](https://www.skidmore.edu/economics/documents/KurovWolfeGilbert-TheDisappearingPre-FOMC-Announce-Drift-200914.pdf); [Quantpedia, FOMC drift in high uncertainty](https://quantpedia.com/fomc-equity-drift-occurs-in-periods-of-high-uncertainty/); [VoxEU, predictable movements around FOMC](https://cepr.org/voxeu/columns/predictable-movements-asset-prices-around-fomc-meetings)
- Event premia in options: [Federal Reserve IFDP 1376](https://www.federalreserve.gov/econres/ifdp/files/ifdp1376.pdf); [NBER w28306](https://www.nber.org/system/files/working_papers/w28306/w28306.pdf); [Samadi, event premia](https://foster.uw.edu/wp-content/uploads/2024/07/Samadi_eventpremia_UW.pdf); [arXiv, When the Fed Speaks](https://arxiv.org/pdf/2608.10693)
- Option buyer returns / variance risk premium: [Coval and Shumway, Expected Option Returns](https://deepblue.lib.umich.edu/items/455dbe73-b56b-44f3-841f-c7751deffc7a); [Carr and Wu, Variance Risk Premiums](https://engineering.nyu.edu/sites/default/files/2019-01/CarrReviewofFinStudiesMarch2009-a.pdf); [CFA digest, Still Not Cheap](https://rpc.cfainstitute.org/research/cfa-digest/2015/12/still-not-cheap-portfolio-protection-in-calm-markets-digest-summary); [Swedroe, The Cheap Volatility Illusion](https://www.etf.com/node/94249.md); [ORATS, implied over realized](https://orats.com/blog/trading-when-implied-is-a-specific-amount-over-realized-volatility)
- Sector ETFs and earnings: [ORATS, expected earnings moves by sector](https://orats.com/blog/where-is-the-chaos-expected-earnings-moves-by-sector); [tastylive, earnings and sector IV](https://tastylive.com/shows/market-measures/episodes/earnings-and-sector-implied-volatility-08-10-2017); [SpotGamma](https://spotgamma.com/?p=19744)
- Momentum: [Moskowitz and Grinblatt (1999)](https://ideas.repec.org/a/bla/jfinan/v54y1999i4p1249-1290.html); [Market states and momentum in sector ETFs](https://experts.nau.edu/en/publications/market-states-and-momentum-in-sector-exchange-traded-funds/); [CXO, sector ETF momentum robustness](https://www.cxoadvisory.com/momentum-investing/simple-sector-etf-momentum-strategy-robustnesssensitivity-tests/); [Alpha Architect, is TSMOM robust](https://alphaarchitect.com/are-trend-following-and-time-series-momentum-research-results-robust/); [Quantpedia, sector momentum](https://quantpedia.com/strategies/sector-momentum-rotational-system)
- Mean reversion / fear: [CXO, short-term strategies that work](https://www.cxoadvisory.com/technical-trading/a-few-notes-on-short-term-trading-strategies-that-work/); [Backtrex, RSI(2) on Nasdaq 100](https://backtrex.com/en/backtests/connors-rsi-2-nasdaq-100); [New Frontier, missed upside after VIX spikes](https://www.advisorperspectives.com/commentaries/2024/08/13/leaving-volatile-markets-can-result-missed-upside); [IVolatility, does high VIX predict SPY declines](https://www.ivolatility.com/news/3127)
- Calendar: [Atlanta Fed, Maberly and Waggoner](https://www.atlantafed.org/research/publications/wp/2000/11.aspx); [FPA, turn of the month in the age of ETFs](https://www.financialplanningassociation.org/article/journal/APR11-turn-month-anomaly-age-etfs-reexamination-return-enhancement-strategies); [Quantpedia, pre-holiday effect](https://quantpedia.com/strategies/pre-holiday-effect)

*Search caveat: these came from 10 standard web searches, mostly abstracts and summaries. Several are practitioner or vendor sources with an angle. Fable should treat section 2 as a map, not a verdict.*

---

## GLOSSARY

- **ETF (exchange-traded fund):** a basket of stocks (or bonds, or commodities) that trades like one stock. SPY is the S&P 500; XLF is the financial sector.
- **Sector ETF:** an ETF holding one industry (banks, semis, energy).
- **Leveraged ETF:** an ETF built to move 2x or 3x the index each day. The daily reset makes it drift away from 2x/3x over longer periods ("decay").
- **Implied volatility (IV):** how much movement the option price assumes. High IV = expensive options.
- **Realized volatility:** how much the price actually moved.
- **Variance risk premium:** the usual gap where IV is higher than what actually happens. Option buyers pay it; sellers collect it.
- **Vol crush:** IV falling right after a known event, which drops option prices even if the stock moved.
- **FOMC:** the Federal Reserve committee that sets interest rates; meets 8 times a year on a published schedule.
- **CPI:** the monthly inflation report.
- **Pre-FOMC drift:** the old finding that stocks rose in the day before Fed announcements.
- **Momentum (industry / time-series):** the idea that what went up recently keeps going up for a while. Industry momentum compares sectors to each other; time-series momentum compares an asset to its own past.
- **Mean reversion:** the opposite idea: a sharp drop tends to bounce.
- **RSI(2):** a 2-day "oversold" gauge from 0 to 100; Connors buys below 5 or 10.
- **VIX:** the market's implied volatility for the S&P 500, the "fear gauge."
- **Turn-of-the-month effect:** the old finding that most stock gains came in the last day and first 3 days of each month.
- **Out of sample:** testing a rule on data it wasn't built on. Effects that fail this were likely found by luck.
- **Data snooping:** trying enough rules on the same data until one looks good by chance.
- **Back-test:** running a rule on past data to see what it would have done.
- **Paper book:** our no-money track of entries with honest fills (`Baxter/paper_book.md`).
- **Rule 7 (liquidity floor):** OI >= 250 and spread <= 25% of mid on the exact contract.
- **OI (open interest):** how many contracts of that exact option are outstanding.
- **Spread:** ask minus bid.
- **ATM (at the money):** strike at about today's price.
