# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import quandl
import matplotlib.pyplot as plt
import pandas as pd

quandl.ApiConfig.api_key = "nyx_P-hc9fPJHegEXqzy"

def cut(df, start, end=None):
    res = df[df.index > start]
    if end:
        res = res[res.index < end]
    return res

###################################################

# Industrial and Commercial Bank of China
#data = quandl.get("DY4/601398")     

###################################################

# plot current year daily close data
segment = data[data.index>='2017-01-01']
close = segment['Close']

# plot 5, 10, 20, 60-day moving average
sma_5 = pd.rolling_mean(segment['Close'], window=5)
sma_10 = pd.rolling_mean(segment['Close'], window=10)
sma_20 = pd.rolling_mean(segment['Close'], window=20)
sma_60 = pd.rolling_mean(segment['Close'], window=60)

zoom = '2017-06-01'
plt.plot(cut(close, zoom), label='close')
plt.plot(cut(sma_5, zoom), label='sma_5')
plt.plot(cut(sma_10, zoom), label='sma_10')
plt.plot(cut(sma_20, zoom), label='sma_20')
plt.plot(cut(sma_60, zoom), label='sma_60')

plt.xticks(rotation='vertical')
plt.legend()
plt.show()


###################################################

# Volume plot
plt.bar(segment.index[segment.index>zoom], cut(segment['Deal_Amount'], zoom))
volume_5 = pd.rolling_mean(segment['Deal_Amount'], window=5)
plt.plot(cut(volume_5, zoom), 'r')

plt.xticks(rotation='vertical')
plt.show()

###################################################