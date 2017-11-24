# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:27:36 2017

@author: junbai

BackTrader base code: cerebro handler
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import sys
sys.path.append("C:/Users/j291414/my algorithms")

import pandas as pd
import backtrader as bt
import numpy as np
import matplotlib.pyplot as plt
import strategies as st 
import analyzers as ay
import observers as ob

def start_backtest(df_list, strategy, params=None, commission=None, observer_list=None, \
                   analysis=True, draw=True):
    cerebro = bt.Cerebro()
    
    ###########################################################################
    # add data feed to cerebro
    for df in df_list:
        data = bt.feeds.PandasData(dataname=df)
        cerebro.adddata(data)
    ###########################################################################
    
    
    ###########################################################################
    # add strategy
    if params:
        cerebro.addstrategy(strategy, **params)
    else:
        cerebro.addstrategy(strategy)
    ###########################################################################
    
    
    ###########################################################################
    # add analysers
    if analysis:
        cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")
        cerebro.addanalyzer(bt.analyzers.SQN, _name="sqn")
        cerebro.addanalyzer(ay.LegDownUpAnalyzer, _name="legdownup")
    ###########################################################################    
    
    
    ###########################################################################
    # add observers
    if observer_list:
        for observer in observer_list:
            cerebro.addobserver(observer)

    ###########################################################################
    
    
    ###########################################################################
    # handle brokers
    # set commision - 0.001 rate
    cerebro.broker.setcommission(commission or 0.001)
    # set cash - 1 million
    cerebro.broker.setcash(1000000.0)
    ###########################################################################
    
    
    ###########################################################################
    print ('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    strategies = cerebro.run()
    firstStrat = strategies[0]
    print ('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    ###########################################################################
    
    
    ###########################################################################
    # plot and analysis output
    # print the analyzers
    if analysis:
        ay.printTradeAnalysis(firstStrat.analyzers.ta.get_analysis())
        ay.printSQN(firstStrat.analyzers.sqn.get_analysis())
        firstStrat.analyzers.legdownup.print()
    # plot 
    if draw:
        cerebro.plot()
    ###########################################################################
    
if __name__ == '__main__':
    start_backtest([df,], st.TestStrategy, observer_list=[ob.DummyObserver], analysis=True)