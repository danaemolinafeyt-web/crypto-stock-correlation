import yfinance as yf
import matplotlib.pyplot as plt

# This code will pull BTC data

btc = yf.download("BTC-USD", start="2020-01-01", end="2026-03-02")

# This code will pull S&P 500 data

sp500 = yf.download("^GSPC", start="2020-01-01", end="2026-03-02")

# This code will let us plot both on the same chart

fig, ax1 = plt.subplots(figsize=(12, 6))

# Bitcoin on the left axis (Blue)

ax1.plot(btc["Close"], color="blue", label="Bitcoin")
ax1.set_ylabel("Bitcoin Price (USD)", color="blue")

# S&P 500 on right axis (Red)

ax2 = ax1.twinx()
ax2.plot(sp500["Close"], color="red", label="S&P 500")
ax2.set_ylabel("S&P 500 Price (USD)", color="red")


plt.title("Bitcoin vs S&P 500")
fig.legend(loc="upper left")
plt.show()

# calculate correlation between S&P and BTC

btc_returns = btc["Close"].squeeze().pct_change().dropna()
sp_returns = sp500["Close"].squeeze().pct_change().dropna()

correlation = btc_returns.corr(sp_returns)
print(f"Correlation between Bitcoin and S&P 500: {correlation:.2f}")

# Correlation between Bitcoin and S&P 500: 0.38