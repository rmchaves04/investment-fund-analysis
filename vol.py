import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def plot_annualized_monthly_vol(data):
    data['Monthly Volatility'] = data['Value'].pct_change().rolling('30D').std() * np.sqrt(252) * 100
    
    print(data['Monthly Volatility'].max())

    plt.figure(figsize=(12,6))
    plt.plot(data['Monthly Volatility'], label='Volatility', color='blue')
    plt.title('Volatility')
    plt.xlabel('Date')
    plt.ylabel('Vol')
    plt.grid(True)

    yticks = mtick.FormatStrFormatter('%.2f%%')
    plt.gca().yaxis.set_major_formatter(yticks)

    plt.legend()
    plt.show()