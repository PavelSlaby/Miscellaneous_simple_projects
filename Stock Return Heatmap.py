"""
Created on Sun Jun 21 17:13:33 2020
Stock Return Heatmap using Seaborn
"""

import pandas as pd
import numpy as np
import pandas_datareader as data
import seaborn as sb
import matplotlib.pyplot as plt
import math

%matplotlib inline

def get_prices(tickers, start, end):
    prices = data.DataReader(tickers, data_source = 'yahoo', start = start, end = end)['Adj Close']
    return prices

dow_comps = 'https://money.cnn.com/data/dow30/'

dow = pd.read_html(dow_comps)[1]['Company']

symbols = []
companies = []

dow2 = []

for i in dow[:1]:
   dow2.append(dow[i].replace('\xa0', ' '))


dow = dow[0].replace('\xa0', ' ')
dow[1].find(' ')

dow[1].find('\xa0')
dow[1]

dow[1].replace('\xa0', ' ')

for i in list(dow.str.split()):
    symbols.append(i[0])
    companies.append(i[1])  # change it so that more of it gets there
    
symbols
companies

prices = get_prices(symbols, '01/01/2019', '01/01/2020')
prices.head()

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

prices.plot(figsize = (20, 10))


returns = (prices.iloc[-1] / prices.iloc[0] - 1 ).round(4) * 100

li = list(returns)
pos = []

a = 0
for i in li:
    if math.isnan(i):
        pos = a
    a += 1
    
companies[pos]    
    
companies.remove(companies[pos])
returns = returns.dropna()
                               
num = len(returns)

def get_dividers(num):
    dividers = []
    for i in range(2, num-1):
        if num % i == 0:
            dividers.append(i)
    return dividers        

if not get_dividers(num):
    returns = returns.append(pd.Series(0, index = ['NA']))   # index has to be defined as a list
    companies.append('NaN')

dividers = get_dividers(len(returns))

fin_div = []
for i in dividers:
    for j in dividers:
        if i >= j and i * j == len(returns) : fin_div.append([i, j, i - j])

def TakeSec(elem):  #function that takes a second element of an array
    return elem[2]    

fin_div.sort(reverse = False, key = TakeSec )
m = fin_div[0][0]
n = fin_div[0][1]

symb_name = zip(returns.index, companies)

symbs = np.asarray(returns.index).reshape(n, m)
symbs

per_change = np.asarray(returns).reshape(n, m)
per_change

comps = np.asarray(companies).reshape(n, m)

labels = (np.asarray(["{0} \n {1:.2f}".format(symbol, per_change) for symbol, per_change in zip(symbs.flatten(), per_change.flatten())])).reshape(n, m)
labels
 
labelsC = (np.asarray(["{0} \n {2} \n {1:.2f}".format(symbol, per_change, comp) for symbol, per_change, comp in zip(symbs.flatten(), per_change.flatten(), comps.flatten())])).reshape(n, m)
 
 
fig, ax = plt.subplots(figsize = (15, 7))
plt.title('Dow  30 Heat Map', fontsize = 18)
ax.title.set_position([0.5,1.05])
ax.tick_params(left=False, bottom=False) 
sb.heatmap(per_change, annot = labelsC, fmt="", cmap='RdYlGn', yticklabels = False, xticklabels = False)
plt.show()

