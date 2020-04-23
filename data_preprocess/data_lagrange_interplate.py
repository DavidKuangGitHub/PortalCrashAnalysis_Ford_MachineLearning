# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:25:38 2018
@author: Amos
"""

import pandas as pd
from scipy.interpolate import lagrange

inputfile = './data/catering_sale.xls' #Sales Data Path
outputfile = './tmp/sales.xls' #Output Data File with Path

data = pd.read_excel(inputfile)
#data[u'Date'].to_excel('./tmp/sales0.xls')
#Outlier filtering, become null
#null_raw = list((data['Sales']<400) | (data['Sales']>5000))
#data.loc[:, 'Sales'][(data['Sales']<400) | (data['Sales']>5000)] = None
#data.loc[(data['Sales']<400) | (data['Sales']>5000), 'Sales'] = None
data.loc[(data['Sales']<400) | (data['Sales']>5000), 'Sales'] = None
#data.to_excel('./tmp/sales1.xls')

#Custom column-vector interpolation function
def polyinterp_column(s, n, k=5):
    y = s.reindex(list(range(n-k, n)) + list(range(n+1, n+1+k)))
    # y = s [list(range(n-k, n)) + list(range(n+1, n+1+k))]
    y = y[y.notnull()]    #Eliminate null value(s)
    return lagrange(y.index, list(y))(n)    #Interpolate and return result

for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            #data[i][j] = polyinterp_column(data[i], j)
            data.loc[j, [i]] = polyinterp_column(data[i], j)

data.to_excel(outputfile)