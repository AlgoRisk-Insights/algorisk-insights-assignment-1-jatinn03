import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetching stock data for Tata Motors
def fetch_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data['Close']

# Calculate 10-day SMA manually
def calculate_10day_sma(closing_prices):
    sma_10day = []
    for i in range(len(closing_prices)):
        if i < 9:
            sma_10day.append(None)  # SMA not available for first 9 days
        else:
            sma = sum(closing_prices[i-9:i+1]) / 10
            sma_10day.append(sma)
    return sma_10day

# Fetching data for Tata Motors
tata_motors_data = fetch_stock_data('TATAMOTORS.NS', '2023-04-01', '2024-03-31')

# Calculate 20-day SMA using rolling function
sma_20day = tata_motors_data.rolling(window=20).mean()

# Calculate 10-day SMA manually
closing_prices = tata_motors_data.values
sma_10day = calculate_10day_sma(closing_prices)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(tata_motors_data.index, tata_motors_data, label='Closing Price', color='blue')
plt.plot(tata_motors_data.index, sma_20day, label='20-day SMA', color='red')
plt.plot(tata_motors_data.index, sma_10day, label='10-day SMA', color='green')
plt.title('Tata Motors - Closing Price and Simple Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()
