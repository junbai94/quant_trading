# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:42:12 2017

@author: Junbai

Load SZ50 data from TuShare

Add in get_k_data tomorrow
"""

import tushare as ts
import pandas as pd
import sqlite3
import time
import datetime

DATABASE_PATH = "C:/Users/user/quant_analysis/Database/cn_stock.db"
sql_unadjusted = "insert into cn_stocks_daily_ts_unadj (code, date, open, high, close, low, volume, price_change, p_change, ma5, ma10, ma20, v_ma5, v_ma10, v_ma20, turnover) \
        values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
sql_adjusted = "insert into cn_stocks_daily_ts_adj (code, date, open, high, close, low, volume, amount) values \
                (?, ?, ?, ?, ?, ?, ?, ?)"
start_date = '2014-01-01'
end_date = datetime.datetime.now().strftime("%Y-%m-%d")

def ts_sz50_loader(adjustment=True, code_list=None, today_only=False, start_date=start_date, end_date=end_date):
    print('----------------------------------------------------------------------')
    print('loading commencing')
    print('----------------------------------------------------------------------')
    start = time.time()
    # get sz50 codes and company names
    sz50 = ts.get_sz50s()
    if code_list:
        codes = code_list
    else:
        codes = sz50['code']
    if today_only:
        start_date = end_date
    failed = []
    
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    
    for code in codes:
        try:
            if adjustment:
                df = ts.get_h_data(code, retry_count=5, pause=10, start=start_date, end=end_date)
                sql = sql_adjusted
            else:
                df = ts.get_hist_data(code, retry_count=5, pause=10, start=start_date, end=end_date)
                sql = sql_unadjusted
        except:
            print (code + ' loading FAILED')
            failed.append(code)
            continue
            
        for row in df.iterrows():
            if adjustment:
                date = row[0].isoformat()
            else:
                date = row[0]
            data = row[1]
            data = list(data)
            data.insert(0, date)
            data.insert(0, code)
            c.execute(sql, tuple(data))
        print (code + ' loaded')
    
    conn.commit()
    conn.close()
    end = time.time()
    print('----------------------------------------------------------------------')
    print('loading completed. total run time: %.2fs' % (end-start))
    print('----------------------------------------------------------------------')
    
if __name__ == '__main__':
    failed = ts_sz50_loader(adjustment=False, start_date='2016-01-01')

