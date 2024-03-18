from rolling import *
import pandas as pd

data = pd.read_csv('Data/FGS.csv', index_col='Date', date_format='%d/%m/%Y', sep=';')

cagr = (data['Close'].iloc[-1] / data['Close'].iloc[0]) ** (1 / (len(data) / 252)) - 1

rolling_max = data['Close'].cummax()
daily_drawdown = data['Close'] / rolling_max - 1
max_dd = daily_drawdown.min()

print(f"CAGR: {cagr:.2%}")
print(f"Max Drawdown: {max_dd:.2%}\n")

returns = calculate_rolling_returns(data)
plot_rolling_returns(returns)