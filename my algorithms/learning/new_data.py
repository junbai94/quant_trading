# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:13:57 2017

@author: junbai

New Data computation class
"""

import pandas as pd
import sqlite3
from datetime import datetime

DATABASE = "C:/Users/j291414/Desktop/market_data.db"

def get_data(ID, table, db=DATABASE):
    conn = sqlite3.connect(db)
    if table == 'fx_daily':
        sql = "select date, rate from fx_daily where tenor='0W'"
        temp = pd.read_sql_query(sql, conn)
    elif table == 'spot_daily':
        sql = "select date, close from spot_daily where spotID = '{}'".format(ID)
        temp = pd.read_sql_query(sql, conn)
    elif table == 'fut_daily':
        sql = "select date, close from fut_daily where instID = '{}'".format(ID)
        temp = pd.read_sql_query(sql, conn)
    else:
        raise ValueError('FUNCTION NOT SUPPORT THIS TABLE')
    
    temp['date'] = pd.to_datetime(temp['date'], format='%Y-%m-%d %H:%M:%S')
    conn.close()
    return temp

def date_range(frm, to, df):
    try:
        return df[(df['date']>=frm)&(df['date']<=to)]
    except KeyError:
        raise KeyError("NAME YOUR DATE COLUMN TO BE 'date'")
        
def monthly_avg(df):
    return df.resample("M", how ='mean', on='date')

def times_fx(df, fx):
    temp = df.merge(fx, on='date')
    if 'result' not in temp.columns:
        temp['result'] = temp.iloc[:,1].multiply(temp.iloc[:,2])
        return temp
    else:
        raise ValueError('Do not choose result as column name')
        
def divide_fx(df, fx):
    temp = df.merge(fx, on='date')
    if 'result' not in temp.columns:
        temp['result'] = temp.iloc[:,1].divide(temp.iloc[:,2])
        return temp
    else:
        raise ValueError('Do not choose result as column name')
        
