---
date: 2026-06-06
advisor: consensus
focus: crisis recovery + WWDC/World Cup catalyst week
capital: $450 (~$250 BOTZ salvage+existing + $200 new from Matt)
---

# Weekly Consensus -- June 6, 2026

## Points of Agreement
1. **SELL BOTZ Monday** -- First unanimous action. Semiconductor thesis broken.
2. **HOLD SOFI spread** -- Defined-risk structure + 76 DTE. Let it work.
3. **DKNG is the play** -- World Cup starts Jun 11. Sheldon + Bulldon both want in.
4. **Cash reserve matters** -- Nobody wants a repeat of -35%.
5. **KO as defensive anchor** -- Sheldon + Beardon agree. World Cup sponsor angle.

## Points of Disagreement
1. **AAPL $355C** -- Sheldon/Bulldon: HOLD through WWDC. Beardon: SELL NOW.
2. **AAPL weekly ($320C Jun12)** -- Bulldon wants it. Everyone else: no.
3. **Cash reserve** -- Bulldon: 10%. Sheldon: 32%. Beardon: 55%. Compromise: 39%.
4. **OSCR** -- Bulldon loves the squeeze. Others pass (for now).

## The Verdict (Validated Against Yahoo)

| # | Ticker | Action | Type | Strike | Expiry | Qty | Real Cost | Risk | Source |
|---|--------|--------|------|--------|--------|-----|-----------|------|--------|
| 0 | BOTZ | SELL | call | $41 | Jul 17 | 1 | +$45-65 | -- | Unanimous |
| 1 | AAPL | HOLD | call | $355 | Jul 17 | 1 | -- | 4/5 | Sheldon+Bulldon. Sell Tue if WWDC duds. |
| 2 | SOFI | HOLD | spread | $17/$19 | Aug 21 | 1 | -- | 3/5 | Unanimous |
| 3 | DKNG | BUY | call | $27.50 | Aug 20 | 1 | $161 | 3/5 | Verified: last=$1.61, bid=$1.59, ask=$1.69, OI=4,912 |
| 4 | KO | BUY | call | $85 | Aug 20 | 1 | $114 | 2/5 | Verified: last=$1.14, bid=$1.08, ask=$1.18, OI=9,490 |
| 5 | CASH | -- | -- | -- | -- | -- | ~$175 | 0/5 | 39% reserve |

**New deployment: $275. Cash reserve: ~$175 (39%).**

## Curl Commands (NOT YET EXECUTED)

```bash
# DKNG $27.50C Aug 20
curl -X POST https://dangoledevs.duckdns.org/sheldon/api/trades \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "sheldon",
    "ticker": "DKNG",
    "action": "buy",
    "quantity": "1",
    "price": "0",
    "option_type": "call",
    "strike": "27.50",
    "expiry": "2026-08-20",
    "premium": "1.61",
    "notes": "Weekly Sheldon consensus: World Cup catalyst. Full tournament coverage (Jun 11-Jul 19). UBS PT $49."
  }'

# KO $85C Aug 20
curl -X POST https://dangoledevs.duckdns.org/sheldon/api/trades \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "sheldon",
    "ticker": "KO",
    "action": "buy",
    "quantity": "1",
    "price": "0",
    "option_type": "call",
    "strike": "85",
    "expiry": "2026-08-20",
    "premium": "1.14",
    "notes": "Weekly Sheldon consensus: Defensive anchor. FIFA World Cup sponsor. Dave-approved."
  }'
```

*Paper trades for Sheldon Compare competition. Not financial advice.*
