import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def plot_monthly_rolling_returns(data, period=12, benchmark=None):
    data = data.resample('M').last()
    data['Rolling Return'] = data['Value'].pct_change(period) * 100

    plt.figure(figsize=(12,6))

    if benchmark is not None:
        benchmark = benchmark.resample('M').last()
        benchmark['Rolling Return'] = benchmark['Value'].pct_change(period) * 100

        above_benchmark = data[data['Rolling Return'] > benchmark['Rolling Return']]
        below_benchmark = data[data['Rolling Return'] <= benchmark['Rolling Return']]

        plt.bar(above_benchmark.index, above_benchmark['Rolling Return'], width=20, color='green', label='Months above benchmark')
        plt.bar(benchmark.index, benchmark['Rolling Return'], label='Benchmark', alpha=0.7, width=20, color='gray')
        plt.bar(below_benchmark.index, below_benchmark['Rolling Return'], width=20, color='red', label='Months below benchmark')
    else:
        colors = ['green' if data_return > 0 else 'red' for data_return in data['Rolling Return']]
        plt.bar(data['Rolling Return'].index, data['Rolling Return'], width=20, color=colors)
    
    plt.title(f'Monthly rolling {period}-month returns')
    plt.xlabel('Date')
    plt.ylabel('Return (%)')
    plt.grid(True)

    yticks = mtick.FormatStrFormatter('%.0f%%')
    plt.gca().yaxis.set_major_formatter(yticks)
    
    plt.legend()
    plt.show()

def calculate_daily_rolling_returns(data):
    time_frames = list(range(3, 61, 3))

    data = data.resample('M').last()
    results = {}

    for tf in time_frames:
        rolling_returns = data['Value'].pct_change(tf).rolling(tf)
        min_return = rolling_returns.min().min() * 100
        max_return = rolling_returns.max().max() * 100
        avg_return = rolling_returns.mean().mean() * 100

        results[tf] = {"Min": min_return, "Max": max_return, "Avg": avg_return}

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

    plt.xticks(range(len(rolling_returns)), [f'{k}' for k in rolling_returns.keys()])
    plt.title('Rolling Returns')
    plt.xlabel('Months')
    plt.ylabel('Return')
    plt.grid(True)

    yticks = mtick.FormatStrFormatter('%.0f%%')
    plt.gca().yaxis.set_major_formatter(yticks)

    plt.legend()
    plt.show()