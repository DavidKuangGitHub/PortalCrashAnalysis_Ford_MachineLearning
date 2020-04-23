# -*- coding: utf-8 -*-
"""
Created by David Kuang
Last updates on Nov 3rd 2019
"""
#Data Dispersed
import pandas as pd

DATA_FILE = './data/discretization_data.xls' #Initialization
DATA = pd.read_excel(DATA_FILE) #Read Data
DATA = DATA.loc[:, u'Coefficient_of_Stagnation_of_Body_Liver']
k = 4

#Equal width Dispersed
d1 = pd.cut(DATA, k, labels=range(k))

#Equal frequency Dispersed
w = [1.0*i/k for i in range(k+1)]
#m = DATA.describe()
#n = DATA.describe(percentiles=w)
w = DATA.describe(percentiles=w)[4:(4+k+1)]
w[0] = w[0]*(1-1e-10)
d2 = pd.cut(DATA, w, labels=range(k))

from sklearn.cluster import KMeans #Import KMeans
#First Dimension Dispersed
kmodel = KMeans(n_clusters=k, n_jobs=2) #Create Model
#kmodel.fit(DATA.reshape((len(DATA), 1)))  #Train Model
#c = pd.DataFrame(kmodel.cluster_centers_).sort(0)   #Output Core with sequence
#w = pd.rolling_mean(c, 2).iloc[1:] #Find the middle point in between as boudary
#w = [0] + list(w[0]) + [DATA.max()] #Add First and Last 
#d3 = pd.cut(DATA, w, labels = range(k))

def cluster_plot(d, k): #Define customization for display result
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei'] #Display Chinese Label if its the case
    plt.rcParams['axes.unicode_minus'] = False #Display normal format of negative

    plt.figure(figsize=(8, 3))
    for j in range(0, k):
        plt.plot(DATA[d==j], [j for i in d[d==j]], 'o')
    plt.ylim(-0.5, k-0.5)
    return plt

cluster_plot(d1, k).show()
cluster_plot(d2, k).show()
#cluster_plot(d3, k).show()   
