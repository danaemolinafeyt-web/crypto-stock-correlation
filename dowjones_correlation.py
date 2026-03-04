import yfinance as yf
import matplotlib.pyplot as plt

# Pull Bitcoin data from 2020
btc = yf.download("BTC-USD", start="2020-01-01", end="2026-03-01")

# Pull Dow Jones data
dow = yf.download("^DJI", start="2020-01-01", end="2026-03-01")

# Plot both
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(btc["Close"], color="blue", label="Bitcoin")
ax1.set_ylabel("Bitcoin Price (USD)", color="blue")

ax2 = ax1.twinx()
ax2.plot(dow["Close"], color="orange", label="Dow Jones")
ax2.set_ylabel("Dow Jones Price (USD)", color="orange")

plt.title("Bitcoin vs Dow Jones (2020-Present)")
fig.legend(loc="upper left")

# Calculate correlation
btc_returns = btc["Close"].squeeze().pct_change().dropna()
dow_returns = dow["Close"].squeeze().pct_change().dropna()
aligned = btc_returns.align(dow_returns, join="inner")
correlation = aligned[0].corr(aligned[1])
print(f"Correlation between Bitcoin and Dow Jones: {correlation:.2f}")

plt.show()