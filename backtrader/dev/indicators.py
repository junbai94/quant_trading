# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:21:18 2017

@author: junbai

BackTrader Indicators
"""

import backtrader as bt
import backtrader.indicators as btind

class MyTrix(bt.Indicator):
    
    lines = ('trix',)
    params = (('period', 15), )
    
    def __init__(self):
        ema1 = btind.EMA(self.data, period=self.p.period)
        ema2 = btind.EMA(ema1, period=self.p.period)
        ema3 = btind.EMA(ema2, period=self.p.period)
        
        self.lines.trix = 100.0 * (ema3 - ema3(-1)) / ema3(-1)
        
        
class MyTrixSignalComposed(bt.Indicator):
    
    lines = ('trix', 'signal')
    params = (('period', 5), ('sigperiod', 9))
    
    def __init__(self):
        self.lines.trix = MyTrix(self.data, period=self.p.period)
        self.lines.signal = btind.EMA(self.lines.trix, period=self.p.sigperiod)
        
class MyTrixSignalInherited(MyTrix):
    
    lines = ('signal', )
    params = (('sigperiod', 9),)
    
    def __init__(self):
        super(MyTrixSignalInherited, self).__init__()
        self.lines.signal = btind.EMA(self.lines.trix, period=self.p.sigperiod)


class LegDown(bt.Indicator):
    
    lines = ('legdown', )
    params = (('period', 10),)
    
    def __init__(self):
        self.lines.legdown = self.data.high(-self.p.period) - self.data.low
     
        
class LegUp(bt.Indicator):
    
    lines = ('legup', )
    params = (('period', 10), ('writeback', True), )
    
    def __init__(self):
        self.lu = self.data.high - self.data.low(-self.p.period)
        self.lines.legup = self.lu(self.p.period * self.p.writeback)
