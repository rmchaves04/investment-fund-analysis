import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def plot_monthly_rolling_returns(data, period=12):
    data = data.resample('M').last()
    data['Rolling Return'] = data['Close'].pct_change(period) * 100

    colors = ['green' if x > 0 else 'red' for x in data['Rolling Return']]

    plt.bar(data['Rolling Return'].index, data['Rolling Return'], width=20, color=colors)
    plt.title(f'{period}-month returns')
    plt.xlabel('Date')
    plt.ylabel('Return (%)')
    plt.grid(True)

    yticks = mtick.FormatStrFormatter('%.0f%%')
    plt.gca().yaxis.set_major_formatter(yticks)
    plt.show()

def calculate_daily_rolling_returns(data):
    time_frames = [252, 504, 756, 1260]
    results = {}

    for tf in time_frames:
        rolling_returns = data['Close'].pct_change(tf).rolling(tf).mean() * 100
        min_return = rolling_returns.min()
        max_return = rolling_returns.max()
        avg_return = rolling_returns.mean()

        results[tf//252] = {"Min": min_return, "Max": max_return, "Avg": avg_return}

    return results

def plot_vertical_rolling_returns(rolling_returns):
    plt.figure(figsize=(12,6))

    i = 0
    for r in rolling_returns.values():
        plt.vlines(i, r['Min'], r['Max'], colors='k', linestyles='solid')
        plt.plot(i, r['Max'], 'g^', label='Maximum Return' if i == 0 else "")
        plt.plot(i, r['Avg'], 'o', color='gray', label='Average Return' if i == 0 else "")
        plt.plot(i, r['Min'], 'rs', label='Minimum Return' if i == 0 else "")
        i += 1

    plt.xticks(range(len(rolling_returns)), [f'{k} years' for k in rolling_returns.keys()])
    plt.title('Rolling Returns')
    plt.xlabel('Time Frame')
    plt.ylabel('Return')
    plt.grid(True)

    yticks = mtick.FormatStrFormatter('%.0f%%')
    plt.gca().yaxis.set_major_formatter(yticks)

    plt.legend()
    plt.show()