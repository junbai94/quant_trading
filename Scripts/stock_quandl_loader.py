# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import quandl as ql
import pandas as pd
import sqlite3 
import time

conn = sqlite3.connect("C:/Users/user/quant_analysis/Database/cn_stock.db")
c = conn.cursor()

ql.ApiConfig.api_key = 'nyx_P-hc9fPJHegEXqzy'

free_stocks = ['600016', '601628', '601398',
               '600010', '601390', '601328',
               '600000', '601288', '601169',
               '000858', '601166', '600887',
               '000776', '601988', '601857',
               '000651', '601818', '601766',
               '000333', '600837', '600519',
               '000009', '600104', '600050',
               '000002', '600036', '600030',
               '000001', '600028']

    
codes = pd.read_csv("C:/Users/user/Desktop/DY4-datasets-codes.csv", names=['code', 'company'])
index = [u'Pre_Close', u'Open', u'High', u'Low', u'Close', u'Adj_Pre_Close',
       u'Adj_Open', u'Adj_High', u'Adj_Low', u'Adj_Close', u'Turnover_Volume',
       u'Turnover_Value', u'Deal_Amount', u'Circulation_Market_Value',
       u'Market_Value', u'Turnover_Rate', u'Adj_Factor', u'Adj_Reason']
sql = "insert into cn_stocks_daily values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

print('----------------------------------------------------------------------')
print('loading commencing')
print('----------------------------------------------------------------------')
start = time.time()

for code in free_stocks:
    df = ql.get('DY4/'+code)
    for row in df.iterrows():
        date = row[0].isoformat()
        data = row[1]
        if data.index.tolist() == index:
            data = list(data.values)
            data.insert(0, date)
            data.insert(0, code)
            c.execute(sql, tuple(data))
    print (code + ' loaded')       
            
end = time.time()
print('----------------------------------------------------------------------')
print('loading completed. total run time: %.2fs' % (end-start))
print('----------------------------------------------------------------------')            
conn.commit()
conn.close()