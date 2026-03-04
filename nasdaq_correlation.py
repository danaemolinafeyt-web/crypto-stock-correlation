import yfinance as yf
import matplotlib.pyplot as plt

# Pulls Bitcoin data from 2020 (The institutional era)

btc = yf.download("BTC-USD", start="2020-01-01", end="2026-03-02")

# Pulls nasdaq data

nasdaq = yf.download("^IXIC", start="2002-01-01", end="2026-03-02")

# Plot both BTC & Nasdaq

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(btc["Close"], color="blue", label="Bitcoin")
ax1.set_ylabel("Bitcoin Price (USD)", color="blue")

ax2 = ax1.twinx()
ax2.plot(nasdaq["Close"], color="green", label="NASDAQ")
ax2.set_ylabel("NASDAQ Price (USD)", color="green")

plt.title("Bitcoin vs NASDAQ (2020-Present)")
fig.legend(loc="upper left")

# Calculate correlation
btc_returns = btc["Close"].squeeze().pct_change().dropna()
nasdaq_returns = nasdaq["Close"].squeeze().pct_change().dropna()
aligned = btc_returns.align(nasdaq_returns, join="inner")
correlation = aligned[0].corr(aligned[1])
print(f"Correlation between Bitcoin and NASDAQ: {correlation:.2f}")

plt.show()

# The correlation between Bitcoin and NASDAQ is: 0.41
