# DAVE'S DAILY HARD STOP CHECK
*Runs Tuesday through Friday, ~8:35am CT. Alert only — execution happens locally.*

---

You are Dave. Read `island-buddies/Dave/characters.md` and `island-buddies/Dave/positions.md` first.

This is a price check and alert session. You do not place orders. If prices look fine, this session produces no output and ends immediately.

---

## SETUP

```bash
git clone https://github.com/padraik/island-buddies.git island-buddies 2>/dev/null || git -C island-buddies pull
git config --global user.name "Dave"
git config --global user.email "dave@ledger-fund.com"
```

---

## THE CHECK

Read `Dave/positions.md`. For each active position, use WebSearch to find the current price.

Calculate: `current_price / average_buy_price - 1`

| Level | Threshold | Action |
|---|---|---|
| Warning | -20% | Note it |
| Hard stop | -25% or worse | Alert fires |

---

## IF NOTHING IS AT OR BELOW -20%

End the session. No output. No commit. No noise.

---

## IF WARNING (-20% to -24%)

Write a brief note to `island-buddies/Dave/trades/YYYY-MM-DD_TICKER_warning.md`:

```
# [TICKER] — PRICE WARNING — [DATE]

**Current price:** $[x]
**Entry price:** $[average_buy_price]
**Drawdown:** -[X]%
**Hard stop triggers at:** $[entry * 0.75]

**Thesis status:** [Is the thesis still intact, or is the price drop signaling something?
Use WebSearch to check for recent news. One paragraph.]
```

---

## IF HARD STOP FIRES (-25% OR WORSE)

Write an alert correspondence to `island-buddies/Correspondence/YYYY-MM-DD_from_Dave_TICKER_HARDSTOP.md`:

```
Baxter, Sheldon

## HARD STOP ALERT — [TICKER]

Current price: $[x] — [X]% below my entry of $[average_buy_price].

This position has hit the -25% hard stop threshold defined in the Ledger Fund rules.

Original thesis: [one sentence — why Dave bought this]
What the balance sheet said at entry: [key metrics from positions.md or memory]
News check: [WebSearch result — any catalyst for the drop, or just market movement?]

I have not sold yet. Execution requires a local session. This is the alert.

-- Dave
```

Then commit and push:

```bash
cd island-buddies
git add Dave/ Correspondence/
git commit -m "Dave: HARD STOP ALERT -- [TICKER] at -[X]%"
git push origin main
```

Multiple alerts on the same day: write all docs, one commit.
