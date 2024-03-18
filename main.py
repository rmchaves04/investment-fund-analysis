from rolling import *
import pandas as pd
import numpy as np

data = pd.read_csv('Data/data.csv', index_col='Date', date_format='%d/%m/%Y', sep=';')

cagr = (data['Close'].iloc[-1] / data['Close'].iloc[0]) ** (1 / (len(data) / 252)) - 1

rolling_max = data['Close'].cummax()
daily_drawdown = data['Close'] / rolling_max - 1
max_dd = daily_drawdown.min()

data_monthly = data['Close'].resample('M').last()
monthly_volatility = data_monthly.pct_change().std()
annualized_monthly_volatility = monthly_volatility * np.sqrt(12)

print(f"CAGR: {cagr:.2%}")
print(f"Max Drawdown: {max_dd:.2%}\n")
print(f"Anualized Monthly Volatility: {annualized_monthly_volatility:.2%}")

# returns = calculate_daily_rolling_returns(data)
# plot_vertical_rolling_returns(returns)
plot_monthly_rolling_returns(data, 3)