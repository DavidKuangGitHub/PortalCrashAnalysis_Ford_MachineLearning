# -*- coding: utf-8 -*-
"""
Created by David Kuang
Last updates since Oct 2019
Description: Normalization and Standardization

"""

import pandas as pd
import numpy as np

datafile = './data/normalization_data.xls'
data = pd.read_excel(datafile, header = None)

data_n1 = (data - data.min())/(data.max() - data.min())    #Minimum-Maximum Standardization
data_n2 = (data - data.mean())/data.std()                  #Zero-Means Normalization
data_n3 = data/10**np.ceil(np.log10(data.abs().max()))     #Decimal Scaling Normalization

print(data_n1)
print(data_n2)
print(data_n3)
