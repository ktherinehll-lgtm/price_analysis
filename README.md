# Price Analysis

'Analysis' is a small Python package used to analyse and visualise a set of (sample, simulated) data. It calculates the percentage return and summarises them with their mean, standard deviation, and plots the prices and returns in a histogram and graph.

## Installation

From inside the 'price_analysis' directory, install teh package in editable mode:

```sh
py -m pip install -e .
```

The required dependencies are specified in 'pyproject.toml' and will be installed automatically.

## Examples of use 

A percentage return can be calculated and summarised as follows:

```python

from Analysis import calculate\_returns, summarise\_returns

prices = [100.0, 102.0, 101.0]

returns = calculate\_returns(prices)
mean\_return, std\_return = summarise\_returns(returns)

print("Returns:", returns)
print("Mean return:", mean\_return)
print("Standard deviation:", std\_return)

```

A histogram of the return can be displayed and visualised as follows:

```python 

import matplotlib.pyplot as plt

from Analysis import plot\_return\_histogram

prices = [100.0, 102.0, 101.0, 105.0]

plot\_return\_histogram(prices)
plt.show()

```
The prices can be plotted against the days as follows:

```python

import matplotlib.pyplot as plt

from Analysis import plot\_prices

days = [1, 2, 3, 4]
prices = [100.0, 102.0, 101.0, 105.0]

plot\_prices(days, prices)
plt.show()

```

## Demonstration

The complete demonstration can be run from the root directory using:

```sh
py -m demo.plotReturns
```