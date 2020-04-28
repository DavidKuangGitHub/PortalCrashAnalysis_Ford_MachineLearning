# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.tree import export_graphviz as to_graphviz
from sklearn.externals.six import StringIO
from datetime import datetime

filename = "./data/sales_data.xls"
data = pd.read_excel(filename, index_col=u'SequenceNumber')

#Change Data to Category Label
data[data == u'high'] = 1
data[data == u'yes'] = 1
data[data == u'good'] = 1
data[data != 1] = -1
x = data.iloc[:,:3].astype(int)
y = data.iloc[:,3].astype(int)

#Create and train decision-tree model based on infomation-shan
dtc = DTC(criterion='entropy')
dtc.fit(x, y)

with open("./tmp/tree.dot", 'w') as f:
    f = to_graphviz(dtc, feature_names = x.columns, out_file= f)

print("Done - DK ", datetime.now())
