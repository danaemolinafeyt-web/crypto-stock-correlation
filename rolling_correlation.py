import yfinance as yf
import matplotlib.pyplot as plt

# Pull Data
btc = yf.download("BTC-USD", start="2020-01-01", end="2026-03-03")
sp500 = yf.download("^GSPC", start="2020-01-01", end="2026-03-03")

# Calculate daily returns

btc_returns = btc["Close"].squeeze().pct_change().dropna()
sp_returns = sp500["Close"].squeeze().pct_change().dropna()

# Align the dates
btc_aligned, sp_aligned = btc_returns.align(sp_returns, join="inner")

# Calculate 90 day rolling correlation

rolling_corr = btc_aligned.rolling(window=90).corr(sp_aligned)

# Plot it

plt.figure(figsize=(12, 6))
plt.plot(rolling_corr, color="purple")
plt.axhline(y=0, color="black", linestyle="--", alpha=0.5)
plt.title("90-Day Rolling Correlation: Bitcoin vs S&P 500")
plt.ylabel("Correlation")
plt.xlabel("Date")
plt.show()