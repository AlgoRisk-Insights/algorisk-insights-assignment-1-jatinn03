# i am not yet proficient in pandas , numpy and matplotlib so i have taken many references from different
# sites regarding their pre defined functions. but i am practicing these libraries side by side daily.  


import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fetching data
def fetch_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

# defining function
def simulate_trading_strategy(stock_data, initial_capital):
    # Initialize variables
    num_days = len(stock_data)
    capital = np.zeros(num_days)
    capital[0] = initial_capital
    risk_free_return = 2.5 / 100  # Risk-free rate 2.5%, as mentioned by prakhar in group

    # Calculate daily returns and capital over time
    for i in range(1, num_days):
        open_price = stock_data['Open'][i]
        close_price = stock_data['Close'][i]
        daily_return = ((close_price - open_price) / open_price) * 100
        capital[i] = capital[i-1] * (1 + daily_return / 100)  # Adjusting for percentage return

    # Calculations
    daily_returns = [(capital[i] / capital[i-1]) - 1 for i in range(1, num_days)]
    excess_returns = np.array(daily_returns) - risk_free_return
    avg_daily_return = np.mean(excess_returns)
    std_dev_daily_return = np.std(excess_returns)
    sharpe_ratio = (avg_daily_return / std_dev_daily_return) * np.sqrt(252)  # Annualized Sharpe ratio
    max_drawdown = np.max(np.maximum.accumulate(capital) - capital)
    final_capital = capital[-1]

    return final_capital, daily_returns, sharpe_ratio, max_drawdown, capital

# Fetch data for HDFC Bank stock and NIFTY 50 index
hdfc_bank_data = fetch_stock_data('HDFCBANK.NS', '2023-04-01', '2024-03-31')
nifty_data = fetch_stock_data('^NSEI', '2023-04-01', '2024-03-31')

# Initial capital for Alice
initial_capital = 100000  

# HDFC Bank stock
hdfc_final_capital, hdfc_daily_returns, hdfc_sharpe_ratio, hdfc_max_drawdown, hdfc_capital = \
    simulate_trading_strategy(hdfc_bank_data, initial_capital)

# NIFTY 50 index
nifty_final_capital, nifty_daily_returns, nifty_sharpe_ratio, nifty_max_drawdown, nifty_capital = \
    simulate_trading_strategy(nifty_data, initial_capital)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(hdfc_bank_data.index, hdfc_capital, label="HDFC Bank")
plt.plot(nifty_data.index, nifty_capital, label="NIFTY 50 Index")
plt.title("Capital Over Time")
plt.xlabel("Date")
plt.ylabel("Capital (Rupees)")
plt.legend()
plt.grid(True)
plt.show()

# Print results
print("Results for HDFC Bank Trading Strategy:")
print(f"Final Capital: Rs. {hdfc_final_capital:.2f}")
print(f"Sharpe Ratio: {hdfc_sharpe_ratio:.2f}")
print(f"Maximum Drawdown: Rs. {hdfc_max_drawdown:.2f}")

print("\nResults for NIFTY 50 Index Trading Strategy:")
print(f"Final Capital: Rs. {nifty_final_capital:.2f}")
print(f"Sharpe Ratio: {nifty_sharpe_ratio:.2f}")
print(f"Maximum Drawdown: Rs. {nifty_max_drawdown:.2f}")
print("Hence we can see that investing in Nifty 50 index would be a better choice rather than investing in a randomly choosen stock HDFC Bank here")
