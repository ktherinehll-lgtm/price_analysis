import matplotlib.pyplot as plt 

from .analysis import calculate_returns

def plot_return_histogram(prices):
    """ Plot a histogram of returns calculated from a list of prices"""
    returns = calculate_returns(prices)

    fig, ax = plt.subplots(figsize = (8,5))
    ax.hist(returns, bins=8, color = 'blue', edgecolor='black')
    ax.set_title('Histogram of Returns')
    ax.set_xlabel('Returns')
    ax.set_ylabel('Frequency')
    fig.tight_layout()

    return fig, ax

def plot_prices(days,prices):
    fig, ax = plt.subplots(figsize = (8,5))
    ax.plot(days, prices, color = 'blue', marker = 'o')
    ax.set_title('Prices over Days')
    ax.set_xlabel('Days')
    ax.set_ylabel('Prices')
    ax.grid(True)
    fig.tight_layout()

    return fig, ax
