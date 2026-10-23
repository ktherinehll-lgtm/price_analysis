from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from Analysis import (calculate_returns, summarise_returns, plot_return_histogram,plot_prices)


from data.samplePrices import sample_prices

print("Days \t Prices")
print("----------------")
for day, price in sample_prices[1:]:
    print(f"{day} \t {price}")

project_dir = Path(__file__).resolve().parents[1]
csv_path = project_dir / "data" / "samplePrices1.csv"

data = np.loadtxt(csv_path, delimiter=',', skiprows=1,)
prices= data[:,1]

returns = calculate_returns(prices)
mean_return, std_return = summarise_returns(returns)

print(f"Mean return: {mean_return}")
print(f"Standard deviation of returns: {std_return}")

plot_return_histogram(prices)
plt.show()

project_dir = Path(__file__).resolve().parents[1]
csv_path = project_dir / "data" / "samplePrices1.csv"

data = np.loadtxt(csv_path, delimiter=",", skiprows=1)
days = data[:,0]
prices = data[:,1]

plot_prices(days, prices)
plt.show()