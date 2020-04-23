# -*- coding: utf-8 -*-

# Use K-Means algorithm to cluster consumption behavior feature data
import pandas as pd
from sklearn.cluster import KMeans

k = 3 #Cluster Category
iteration = 5 #Maximum number of cycles aka loops

inputfile = './data/consumption_data.xls'
outputfile = './tmp/out_consumption_data.xls'
#Read and Standarize data
data = pd.read_excel(inputfile)
data_zs = 1.0*(data - data.mean())/data.std()

#K cluster and concurrent number
model = KMeans(
        n_clusters=k, n_jobs=1, max_iter = iteration) 
#start clustering
model.fit(data_zs)

#clustering result
r1 = pd.Series(model.labels_).value_counts() #Get number of categories
r2 = pd.DataFrame(model.cluster_centers_) #Find core of cluster
#Horizontal connection (0 is vertical), get the number under the category corresponding to the cluster center
r = pd.concat([r2, r1], axis=1)
r.columns = list(data.columns) + [u'NumberOfCategories']
#print([u'NumberOfCategories'])
#print(r)

#Detailed output of original data and its categories
r_detail = pd.concat(
        [data, pd.Series(model.labels_, index=data.index)], axis=1)
r_detail.columns = list(data.columns) + [u'ClusterCategory']
#print([u'ClusterCategory'])
#print(r_detail)

#Visual display of K-Means results
from sklearn.manifold import TSNE

tsne = TSNE()
#Data Dimension Reduction Degree
tsne.fit_transform(data_zs)
tsne = pd.DataFrame(tsne.embedding_, index = data_zs.index)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #Display Chinese labels normally if applicable
plt.rcParams['axes.unicode_minus'] = False #Display negative sign normally

#Draw in different colors and styles for different categories
d = tsne[r_detail[u'ClusterCategory'] == 0]
plt.plot(d[0], d[1], 'r.')
d = tsne[r_detail[u'ClusterCategory'] == 1]
plt.plot(d[0], d[1], 'go')
d = tsne[r_detail[u'ClusterCategory'] == 2]
plt.plot(d[0], d[1], 'b*')
plt.show()