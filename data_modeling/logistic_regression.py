# -*- coding: utf-8 -*-
#Logistic Regression of BOA (Bank of America) to reduce loan debt based on Big Data
#Logistic Regression with modelling automation
import pandas as pd
import numpy

#Init parameters
filename = './data/bankloan.xls'
data = pd.read_excel(filename)

x = data.iloc[:, :8].values
y = data.iloc[:, 8].values

from sklearn.linear_model import LogisticRegression as LR
#from sklearn.linear_model import RandomizedLogisticRegression as RLR 


lr = LR() #Logistic Regression model creation
lr.fit(x, y) #Train model with filtered data
print(u'Logistic Regression model training is completed.')
print(u'Average Correct Rate of unfiltered model = ', lr.score(x, y))

#Create Random Logistic Regression model
#rlr = RLR() #Filter variable(s)
#rlr.fit(x, y)
#rlr.get_support()   #Get filtered results, also you can use .scores method to get each of every characters
#selected_col = numpy.append(rlr.get_support(),[False])

"""print(u"Random Logistic Regression model filtering process is completed.")"""

#print(u"Usful character is ：%s" % ",".join(data.columns[selected_col]))
#x = data[data.columns[selected_col]].as_matrix()    # Filter good character(s)
#x = data[data.columns[selected_col]].values

"""lr = LR() #Logistic Regression model creation
lr.fit(x, y) #Train model with filtered data
print(u'Logistic Regression model training (the 2nd) is completed.')
print(u'Average Correct Rate is = ', lr.score(x, y)) #Output average correct rate of this model, in this case it is 81.4%
"""