# -*- coding: utf-8 -*-

import pandas as pd

catering_sale = './data/catering_sale_all.xls' #Dinner Data with other attributes
data = pd.read_excel(catering_sale, index_col = u'Date') #Read data, use Date as indexing

#print(data.corr()) 
print(data.corr()[u'GarlicFillet']) #Only display 'GarlicFillet' relavent parameters
print('\n')
print(data[u'GarlicFillet'].corr(data[u'ChickenFriedSteak'])) #Correlation coefficient between GarlicFillet and ChickenFriedSteak