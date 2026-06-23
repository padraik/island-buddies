"""
fetch_puts_chain.py — Pull live PUT options chain from Robinhood for a given ticker.
Filters to puts priced $0.10-$2.00 (Island Fund puts Iron Rule range).

Usage:
  python scripts/fetch_puts_chain.py TICKER
"""

import sys
import os
import json
import pickle
import requests
import robin_stocks.robinhood as r

BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDS_FILE  = os.path.join(BASE_DIR, "scripts", "robinhood_creds.json")
PICKLE_PATH = os.path.join(os.path.expanduser("~"), ".tokens", "robinhoodlifecoach_rh.pickle")
RH_CLIENT_ID = "c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS"


def try_refresh_token():
    if not os.path.exists(PICKLE_PATH):
        return False
    try:
        with open(PICKLE_PATH, "rb") as f:
            stored = pickle.load(f)
        resp = requests.post(
            "https://api.robinhood.com/oauth2/token/",
            json={
                "grant_type": "refresh_token",
                "refresh_token": stored["refresh_token"],
                "client_id": RH_CLIENT_ID,
                "expires_in": 86400 * 7,
                "scope": "internal",
                "device_token": stored["device_token"],
            },
        )
        data = resp.json()
        if "access_token" not in data:
            return False
        with open(PICKLE_PATH, "wb") as f:
            pickle.dump({
                "token_type": data["token_type"],
                "access_token": data["access_token"],
                "refresh_token": data.get("refresh_token", stored["refresh_token"]),
                "device_token": stored["device_token"],
            }, f)
        return True
    except Exception as e:
        print(f"Token refresh failed: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_puts_chain.py TICKER")
        sys.exit(1)

    ticker = sys.argv[1].upper()

    # Auth
    if os.path.exists(PICKLE_PATH):
        if try_refresh_token():
            with open(PICKLE_PATH, "rb") as f:
                stored = pickle.load(f)
            r.authentication.set_login_state(True)
            r.authentication.SESSION.headers["Authorization"] = f"Bearer {stored['access_token']}"
            print("Session refreshed via refresh token.")
        else:
            with open(CREDS_FILE) as f:
                creds = json.load(f)
            r.login(creds["username"], creds["password"])
            print("Starting login process...")
    else:
        with open(CREDS_FILE) as f:
            creds = json.load(f)
        r.login(creds["username"], creds["password"])
        print("Starting login process...")

    # Get current stock price
    quote = r.stocks.get_latest_price(ticker)
    stock_price = float(quote[0]) if quote else 0.0
    print(f"\n{ticker} current price: ${stock_price:.2f}")

    # Get expiration dates
    chain = r.options.get_chains(ticker)
    exp_dates = chain.get("expiration_dates", []) if chain else []

    # Filter to Aug 2026 and nearby expirations
    target_dates = [d for d in exp_dates if "2026-08" in d or "2026-07" in d]
    if not target_dates:
        target_dates = exp_dates[:4]

    import datetime
    today = datetime.date.today()

    for exp_date in sorted(target_dates):
        exp_obj = datetime.date.fromisoformat(exp_date)
        dte = (exp_obj - today).days

        print(f"\nLoading PUT data for {exp_date} ({dte}d)...")
        opts = r.options.find_options_by_expiration(ticker, exp_date, optionType="put")
        if not opts:
            continue

        rows = []
        for o in opts:
            try:
                ask = float(o.get("ask_price") or 0)
                strike = float(o.get("strike_price") or 0)
                if ask < 0.10 or ask > 2.00:
                    continue
                breakeven = strike - ask
                if stock_price > 0:
                    needs_pct = (breakeven / stock_price - 1) * 100
                else:
                    needs_pct = 0
                # Iron Rule check: put breakeven relative to stock (puts need stock to FALL)
                # We want breakeven well below current price
                if needs_pct >= 0:
                    continue  # breakeven above stock price means deep ITM put — skip
                if needs_pct < -80:
                    continue  # too far OTM
                rows.append((strike, ask, breakeven, needs_pct))
            except (ValueError, TypeError):
                continue

        if not rows:
            print(f"  No puts in $0.10-$2.00 range with breakeven 0-80% below stock.")
            continue

        rows.sort(key=lambda x: x[0], reverse=True)
        print(f"  Expiring {exp_date} ({dte}d)")
        print(f"  PUT CHAIN — ask $0.10–$2.00, breakeven below current stock")
        print(f"  {'STRIKE':>8}  {'ASK':>6}  {'AT RISK':>8}  {'BREAKEVEN':>10}  {'NEEDS%':>8}  IRON RULE")
        print(f"  {'-'*72}")
        for strike, ask, breakeven, needs_pct in rows:
            at_risk = int(ask * 100)
            rule = "OVER" if ask > 1.50 else ("STRETCH" if ask > 1.25 else "OK")
            print(f"  ${strike:>7.0f}  ${ask:>5.2f}  ${at_risk:>7}  ${breakeven:>9.2f}  {needs_pct:>7.1f}%  {rule}")

    r.logout()
    print("\nLogged out successfully.")


if __name__ == "__main__":
    main()
