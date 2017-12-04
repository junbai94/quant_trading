# -*- coding: utf-8 -*-
"""
Created on Fri Dec 01 17:15:42 2017

@author: junbai

Seasonality analysis:
    plot data for each year
"""
import sys
sys.path.append("C:/Users/j291414/my algorithms")

import pandas as pd
from data_handling.new_data import get_data
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import warnings
pd.options.mode.chained_assignment = None  # default='warn'
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=FutureWarning) 


rebar = get_data('tj_rebar', 'spot_daily')
start_year = rebar['date'][0].year
end_year = rebar['date'].iloc[-1].year


rebar14 = rebar[rebar['date'].dt.year==2014]
rebar14['ewa'] = pd.ewma(rebar14['close'], span=20)
plt.plot(rebar14['date'], rebar14['close'] - rebar14['ewa'])
plt.xticks(rotation='vertical')
plt.show()



rebar15 = rebar[rebar['date'].dt.year==2015]
rebar15['ewa'] = pd.ewma(rebar15['close'], span=20)
plt.plot(rebar15['date'], rebar15['close'] - rebar15['ewa'])
plt.xticks(rotation='vertical')
plt.show()


rebar16 = rebar[rebar['date'].dt.year==2016]
rebar16['ewa'] = pd.ewma(rebar16['close'], span=20)
plt.plot(rebar16['date'], rebar16['close'] - rebar16['ewa'])
plt.xticks(rotation='vertical')
plt.show()


rebar17 = rebar[rebar['date'].dt.year==2017]
rebar17['ewa'] = pd.ewma(rebar17['close'], span=20)
plt.plot(rebar17['date'], rebar17['close'] - rebar17['ewa'])
plt.xticks(rotation='vertical')
plt.show()
    