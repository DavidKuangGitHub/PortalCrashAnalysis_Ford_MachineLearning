# -*- coding: utf-8 -*-

#Pareto Analysis
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #Display normal Chinese labels if applicable
plt.rcParams['axes.unicode_minus'] = False #Display normal negative sign

dish_profit = './data/catering_dish_profit.xls'
data = pd.read_excel(dish_profit, index_col = u'CourseName')

data = data[u'Profit'].copy()
data.sort_index(ascending = False)

plt.figure()
data.plot(kind='bar')    #Bar Image
plt.ylabel(u'Profit($)')

p = 1.0*data.cumsum()/data.sum()
p.plot(color = 'r', secondary_y = True, style = '-o',linewidth = 2)    #Line
#Put a mark at 85% of the whole chart with the accurate value, use arrow sign 
plt.annotate(format(p[6], '.4%'), \
             xy = (6, p[6]), \
             xytext=(6*0.9, p[6]*0.9), \
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) 
plt.ylabel(u'Profit(%)')

plt.show()