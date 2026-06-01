# The Island Fund

Two kids. A green binder. One stoplight town.

The math has been done seventeen times since eighth grade. It always comes out the same number.

---

## What This Is

The Island Fund is a real options trading project documented as a story. The research is real. The trades are real. The money is real. The characters doing the analysis happen to live in 1996 and want to buy a Caribbean island.

Every week, a character named Baxter researches options plays, debates them internally across four (now five) distinct analytical frameworks, presents the best ones to his partner Patrick, and they decide together whether to enter. The decisions, fills, and outcomes are all logged here.

The fiction is the frame. The finance is the content.

---

## The Math

A private island in the Caribbean runs about $1.1M. Construction (mansion, dock, solar, satellite uplink) runs another $1.8M. Total: $2.9M. Put the remaining $2.1M in dividend-paying stocks at 4.5% and you have $94,500 a year, forever, without touching the principal.

Total required: **$5,000,000.**

The fund started at $200. Patrick's grandmother sent birthday money. His dad added $300 when he heard the pitch on the way to school.

The distance to the island: $4,999,500. The math doesn't care.

---

## Current Fund State

| | |
|---|---|
| Total capital | $500.00 |
| Deployed | $264.00 |
| Reserve (SGOV) | $236.00 |
| Realized P&L | $0.00 |
| Distance to island | $4,999,500.00 |

**Open positions:**

| Entered | Ticker | Play | Fill | At Risk | Catalyst | Target |
|---------|--------|------|------|---------|----------|--------|
| Jun 1, 2026 | NKE | $50C Jul17 | $1.86 | $186 | Jun 30 earnings + World Cup | Sell if stock hits $52 pre-earnings, or at open Jul 1 |
| Jun 1, 2026 | ABT | $100C Jul17 | $0.78 | $78 | Jul 16 earnings (first full Exact Sciences quarter) | Sell if stock hits $106 pre-earnings, or at open Jul 17 |

---

## The Characters

Full character profiles are in [characters.md](characters.md). Short version:

**Baxter-Prime** runs the meetings. Holds the binder. Enforces the Iron Rules without exception.

**Bullxter** sees the upside first. Stays there longer than is probably wise. Has been right enough times that you can't dismiss him.

**Bearxter** sits down before anyone else. Tries to find the version of events where the thesis is wrong. His approvals mean something because he makes them hard to get.

**Quantxter** has a yellow legal pad. Doesn't speak until he has numbers. Runs the expected value models.

**Macxter** watches the macro and political environment. Truth Social posts, executive financial disclosures, congressional stock filings. Only speaks when he has something material. His absence from a meeting means he already gave Prime a clean bill of health.

---

## The Iron Rules

Written before any research began. Not suggestions.

1. No more than 50% of the fund in any single play.
2. Options only. Defined maximum loss. No margin, no borrowing.
3. No chasing a position after entry.
4. Take profits at the target. Do not hold past the thesis.
5. Reserve earns 5% in SGOV while waiting for the next play.
6. Sequential plays until there is a track record.

---

## Repo Structure

```
island-fund-repo/
  README.md               <- you are here
  characters.md           <- full Baxter character reference
  positions.md            <- current positions, always up to date
  week-01/                <- June 1 week (closes after Monday trades lock)
    research/             <- individual stock DDs, working docs, session notes
    story/                <- narrative documents, four-Baxter debates, WSB posts
  week-02/                <- opens next Monday
    research/
    story/
```

A new week folder opens each Monday after trades are confirmed. The root files (`characters.md`, `positions.md`) are always current.

---

## Week 01 Contents (June 1, 2026)

**Research filed:** ABT (4/5, entered), NKE (4/5, entered), DKNG (3.5/5, watch), CMCSA (3.5/5, watch), SNAP (3/5, watch), LYFT (3/5, watch), MDT (pending June 3 earnings check), STZ (pass), ABNB (pass), PENN (pass), FUBO (pass), PYPL (pass), VRNS+FCN (pass)

**Story docs:** The Weekend (how the research happened), The Eleven PM Meeting (when Patrick's dad called), Island Fund Week One (full narrative from birthday money to first trade), WSB-style DD on both open positions

---

## The Plays In Plain English

**NKE:** Nike is at 12-year lows. The new CEO just bought $2 million of his own stock. Goldman Sachs, the most pessimistic major bank covering the name, has a price target above our break-even. The World Cup starts June 11 in North America. Nike annual earnings are June 30. Elliott Hill will have 19 days of live World Cup sales data to reference on that call. We bought one $50 call expiring July 17 for $1.86.

**ABT:** Abbott Laboratories is at 10-year lows after spending $21 billion to acquire a cancer screening company called Exact Sciences. The market punished the short-term EPS dilution. Abbott's CEO then bought $2 million of his own stock at $107. The CFO bought. A board member bought $927,000 worth. Every analyst covering the stock, including the most bearish one, has a price target above our break-even. July 16 earnings is the first full quarter with Exact Sciences inside Abbott. We bought one $100 call expiring July 17 for $0.78.

---

## Next Dates

| Date | Event |
|------|-------|
| Jun 3, 2026 | MDT pre-market earnings - check for potential week-02 entry |
| Jun 11, 2026 | FIFA World Cup begins in North America |
| Jun 30, 2026 | NKE Q4 FY2026 annual earnings (after close) |
| Jul 1, 2026 | Sell NKE at open regardless of outcome |
| Jul 16, 2026 | ABT Q2 2026 earnings (before open) |
| Jul 17, 2026 | Sell ABT at open regardless of outcome |
| Mid-Jul, 2026 | Evaluate DKNG $30C Aug21 entry after NKE/ABT resolve |

---

*"I've been doing some reading."*
