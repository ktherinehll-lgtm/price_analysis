import numpy as np

def calculate_returns(prices):
    """Calculate the returns from a list of prices"""
    prices = np.asarray(prices, dtype=float)
    return np.diff(prices) / prices[:-1]

def summarise_returns(returns):
    """Summarise the returns by calculating mean and standard deviation"""
    mean_return = np.mean(returns, dtype=float)
    std_return = np.std(returns)
    return mean_return, std_return
