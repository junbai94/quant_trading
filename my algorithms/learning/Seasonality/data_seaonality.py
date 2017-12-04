# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 11:51:53 2017

@author: junbai

Price seasonality plot and volatility seasonality plot
"""

import sys
sys.path.append("C:/Users/j291414/my algorithms")

import pandas as pd
from data_handling.new_data import get_data
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np
import warnings
pd.options.mode.chained_assignment = None  # default='warn'
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=FutureWarning) 


def price_seasonality(data):
    data = data.copy()
    px = data.columns[1]
    start_year = data['date'][0].year
    end_year = data['date'].iloc[-1].year
    num_years = end_year - start_year + 1
    
    for i in range(num_years):
        temp = data[data['date'].dt.year==start_year+i]
        temp['trend'] = pd.ewma(temp[px], span=20)
        plt.plot(temp['date'], temp['close'] - temp['trend'])
        plt.title("Seasonality plot of year {}".format(start_year+i))
        plt.xticks(rotation="vertical")
        plt.show()
        

def vol_seasonality(data):
    data = data.copy()
    px = data.columns[1]
    start_year = data['date'][0].year
    end_year = data['date'].iloc[-1].year
    num_years = end_year - start_year + 1
    
    for i in range(num_years):
        temp = data[data['date'].dt.year==start_year+i]
        temp['log'] = np.log(temp[px])
        temp['log_ret'] = temp['log'] - temp['log'].shift()
        plt.plot(temp['date'], pd.rolling_std(temp['log_ret'], 10))
        plt.title("Volatiliy seasonality plot of year {}".format(start_year+i))
        plt.xticks(rotation="vertical")
        plt.show()

        
        
    