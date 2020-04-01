#Import Libraries
import numpy as np 
import pandas as pd 
import pandas_datareader as wb 
import matplotlib.pyplot as plt 
from scipy.stats import norm
%matplotlib inline
﻿
#Settings for Monte Carlo asset data, how long, and how many forecasts
ticker = 'XTZ_USD' # ticker
t_intervals = 30 # time steps forecasted into future
iterations = 25 # amount of simulations
#Acquiring data
data = pd.read_csv('XTZ_USD Huobi Historical Data.csv',index_col=0,usecols=['Date', 'Price'])
data = data.rename(columns={"Price": ticker})
#Preparing log returns from data
log_returns = np.log(1 + data.pct_change())
#Plot of asset historical closing price
data.plot(figsize=(10, 6));

#Plot of log returns
log_returns.plot(figsize = (10, 6))


#Setting up drift and random component in relation to asset data
u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5 * var)
stdev = log_returns.std()
daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))

#Takes last data point as startpoint point for simulation
S0 = data.iloc[-1]
price_list = np.zeros_like(daily_returns)
price_list[0] = S0

#Applies Monte Carlo simulation in asset
for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]
﻿
﻿﻿#Plot simulations
plt.figure(figsize=(10,6))
plt.plot(price_list);
