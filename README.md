# Stocks
buying and selling stocks automatically.

in this branch we use these methods (listed according to each corresponding level):

1. stockqoutes and yfinance for basic data, py-stocks will be used for when more advanced data will be taken into account (dividends, number of employees, etc). it's important to note py-stocks wraps stockqutes and yfinance for ease of use.
2. shawn's calculation:
  based on stock prices and percentages of change:
  if (percentage of change == +0.1% && stock.strongBuy == True):
      Buy stocks
  if (percentage of change == +0.35%)
      Sell stocks
3. API to sell and buy stocks: TBD 

