# -*- coding: utf-8 -*-
"""
Created by David Kuang
Last updates since Jun 2019
"""

#Principla Component Analysis - Reduce dimension aka Dimensionality Reduction
import pandas as pd

#Parameter Initialization
inputfile = './data/principal_component.xls'
outputfile = './tmp/dimention_reducted.xls' #DataFile_output_after_dimention_reduced

data = pd.read_excel(inputfile, header = None) #Read input data

from sklearn.decomposition import PCA

pca = PCA(3)
pca.fit(data)
#pca.components_ #Return each feature vector of the model
#pca.explained_variance_ratio_ #Return the percentage variance of each component

low_d = pca.transform(data) #Reduce Dimension
pd.DataFrame(low_d).to_excel(outputfile)
pca.inverse_transform(low_d)    #Restore Data
