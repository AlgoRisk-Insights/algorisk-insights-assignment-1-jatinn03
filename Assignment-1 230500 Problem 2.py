#QUESTION 2


#PART A

# I would suggest including uncorrelated stocks in the portfolio. Uncorrelated stocks tend to
# have lower correlations with each other, which can help in diversifying the portfolio and
# reducing overall risk, because they are not interdependent. For example if one stock is in loss,
# our other stocks will not be affected by it. Highly correlated stocks are dependent on each other,
# so if one stock in the portfolio experiences a significant price movement, the others are likely to
# move in the same direction, and that means if one is making loss, other stocs will also go in loss,
# and thus increasing the portfolio's risk.


#PART B

import yfinance as yf

#taking high correlation stocks to be ICICI bank and AXIS bank 
#taking low correlation stocks to be ITC and TCS

# Define the tickers for ICICI Bank, Axis Bank, ITC, and TCS
tickers = ["ICICIBANK.BO", "AXISBANK.BO", "ITC.BO", "TCS.BO"]

# Fetch data from Yahoo Finance
data = yf.download(tickers, start="2023-04-01", end="2024-03-31")

# Extract daily closing prices for each stock
icici_bank_prices = data["Close"]["ICICIBANK.BO"]
axis_bank_prices = data["Close"]["AXISBANK.BO"]
itc_prices = data["Close"]["ITC.BO"]
tcs_prices = data["Close"]["TCS.BO"]

# Calculate mean prices
mean_icici = sum(icici_bank_prices) / len(icici_bank_prices)
mean_axis = sum(axis_bank_prices) / len(axis_bank_prices)
mean_itc = sum(itc_prices) / len(itc_prices)
mean_tcs = sum(tcs_prices) / len(tcs_prices)

# Calculate covariance
cov_icici_axis = sum((icici_bank_prices[i] - mean_icici) * (axis_bank_prices[i] - mean_axis) for i in range(len(icici_bank_prices))) / (len(icici_bank_prices) - 1)
cov_itc_tcs = sum((itc_prices[i] - mean_itc) * (tcs_prices[i] - mean_tcs) for i in range(len(itc_prices))) / (len(itc_prices) - 1)

# Calculate standard deviation
std_dev_icici = (sum((x - mean_icici) ** 2 for x in icici_bank_prices) / (len(icici_bank_prices) - 1)) ** 0.5
std_dev_axis = (sum((x - mean_axis) ** 2 for x in axis_bank_prices) / (len(axis_bank_prices) - 1)) ** 0.5
std_dev_itc = (sum((x - mean_itc) ** 2 for x in itc_prices) / (len(itc_prices) - 1)) ** 0.5
std_dev_tcs = (sum((x - mean_tcs) ** 2 for x in tcs_prices) / (len(tcs_prices) - 1)) ** 0.5

# Calculate correlation
correlation_icici_axis = cov_icici_axis / (std_dev_icici * std_dev_axis)
correlation_itc_tcs = cov_itc_tcs / (std_dev_itc * std_dev_tcs)

print("Correlation between ICICI Bank and Axis Bank:", correlation_icici_axis)
print("Correlation between ITC and TCS:", correlation_itc_tcs)



# PART C
# i) AXIS bank and ICICI bank behaves so because these both are private banks, and so they 
# both have same business structure, same kind of customers and so they both are affected by
# same market ups and downs. Hence these are correlated stocks with correlation > 0.5 !
# ii) other examples include IT compaines like infosys and TCS. these also work in similar
# business model and so are expected to be correlated !
