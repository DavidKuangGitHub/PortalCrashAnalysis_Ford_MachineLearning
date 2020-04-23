# -*- coding: utf-8 -*-D:\GitWork\Data\chapter3\demo\code\3-1_abnormal_check.py
# 3-1
'''
Created by David Kuang
Last updates since Apr 2019
'''

import pandas as pd
import matplotlib.pyplot as plt

catering_sale = './data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col = u'Sales')

plt.rcParams['font.sans-serif'] = ['SimHei'] #Display Chinese labels if applicable
plt.rcParams['axes.unicode_minus'] = False #Display normal format of negative

#Build Image
plt.figure()
p = data.boxplot(return_type = 'dict')
x = p['fliers'][0].get_xdata()    #‘flies’ is abnormal value
y = p['fliers'][0].get_ydata()

y.sort()

#Use annotate to add comments
for i in range(len(x)):
    if i>0:
        plt.annotate(y[i], xy = (x[i], y[i]), xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.08,y[i]))

plt.show()