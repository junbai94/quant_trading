# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 14:55:30 2017

@author: junbai

EastMoney stock data scooping
"""

import urllib
import re
import pandas as pd
import datetime
import time


today = datetime.datetime.now().strftime("%Y%m%d")

proxies = {'http':'http://j291414:Battleship1!@10.252.22.102:4200', 
           'https':'https://j291414:Battleship1!@10.252.22.102:4200'}
URL = 'http://quote.eastmoney.com/stocklist.html'
code = '000333'
# 0 for shanghai 1 for sz
url_sh = 'http://quotes.money.163.com/service/chddata.html?code=0'+code+'&end=20171204'
url_sz = 'http://quotes.money.163.com/service/chddata.html?code=1'+code+'&start=20170101&end=20171204'


def getHtml(url):
    html = urllib.urlopen(url, proxies=proxies).read()
    html = html.decode('gbk')
    return html

def getStackCode(html):
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
    pat = re.compile(s)
    code = pat.findall(html)
    return code



codes = getStackCode(getHtml(URL))
content = urllib.urlopen(url_sz, proxies=proxies).read()
reader = content.split('\n')

row1 = reader[1].split(',')
row150 = reader[150].split(',')

def eastmoney_data_scooping(code_list, end=None, proxy=None):
    print('----------------------------------------------------------------------')
    print('loading commencing')
    print('----------------------------------------------------------------------')
    start = time.time()
    if not end:
        end = today
    if not proxy:
        proxy = {}
    
    for code in code_list:
        if code[0] == '0':
            url = 'http://quotes.money.163.com/service/chddata.html?code=1'+code+'&end='+end
        elif code[0] == '6':
            url = 'http://quotes.money.163.com/service/chddata.html?code=0'+code+'&end='+end
        else:
            print (code + 'does not start with 6 or 0')
            continue
        
        # scoop data
        content = urllib.urlopen(url, proxies=proxy).read()
        reader = content.split('\n')
        print (code + ' loaded')
            
        
            
    end = time.time()
    print('----------------------------------------------------------------------')
    print('loading completed. total run time: %.2f' % (end-start))
    print('----------------------------------------------------------------------')
    return reader

#if __name__ == '__main__':
#    reader = eastmoney_data_scooping(['0003333',], end='20171204', proxy=True)
