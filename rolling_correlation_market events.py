import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd


# Pull Data

btc = yf.download("BTC-USD", start="2020-01-01", end="2026-03-03")
sp500 = yf.download("^GSPC", start="2020-01-01", end="2026-03-03")

# Calculate the daily returns

btc_returns = btc["Close"].squeeze().pct_change().dropna()
sp_returns = sp500["Close"].squeeze().pct_change().dropna()

# Align Dates

btc_aligned, sp_aligned = btc_returns.align(sp_returns, join="inner")

# Calculate 90 day rolling correlation

rolling_corr = btc_aligned.rolling(window=90).corr(sp_aligned)

# Plot it

plt.figure(figsize=(14, 7))
plt.plot(rolling_corr, color="purple", linewidth=1.5)
plt.axhline(y=0, color="black", linestyle="--", alpha=0.3)

# Add market events
events = {
    "COVID Crash": "2020-03-15",
    "BTC ATH $69k": "2021-11-10",
    "2022 Crash": "2022-06-15",
    "ETF Approval": "2024-01-11",
    "BTC $100k": "2024-12-05"
}

for event, date in events.items():
    event_date = pd.Timestamp(date)
    plt.axvline(x=event_date, color="red", linestyle="--", alpha=0.5)
    plt.text(event_date, 0.62, event, rotation=45, fontsize=8, color="red")

plt.title("90-Day Rolling Correlation: Bitcoin vs S&P 500\\nWith Key Market Events")
plt.ylabel("Correlation")
plt.xlabel("Date")
plt.tight_layout()
plt.show()