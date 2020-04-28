# -*- coding: utf-8 -*-

import pandas as pd

inputfile = './data/sales_data.xls'
data = pd.read_excel(inputfile, index_col = u'SequenceNumber')

data[data == u'high'] = 1
data[data == u'yes'] = 1
data[data == u'good'] = 1
data[data != 1] = -1
x = data.iloc[:,:3].astype(int)
y = data.iloc[:,3].astype(int)

from keras.models import Sequential
from keras.layers.core import Dense, Activation

#Build model
model = Sequential();
model.add(Dense(input_dim = 3, output_dim = 10))
model.add(Activation('relu')) #Use relu function as igntion function, improve accurancy
model.add(Dense(input_dim = 10, output_dim = 1))
model.add(Activation('sigmoid')) #Because of 0-1 output, use sigmoid function as igniton function

#Compile Model:
#Because of binary classify, we use binary_crossentropy and binary
#Other loss functions are mean_squared_error, categorical_crossentropy etc, see help docs
#We also use adam，and sgd, rmsprop as options
model.compile(loss = 'binary_crossentropy',
              optimizer = 'adam')

model.fit(x, y, epochs = 100, batch_size = 10) #Train model, machine-learning 1000 times
yp = model.predict_classes(x).reshape(len(y)) #Classify predict

#!pip install cm_plot

"""def cm_plot(y, yp):
    from sklearn.metrics import confusion_matrix#Import confusion_matrix function
    cm = confusion_matrix(y, yp)#confusion matrix
    import matplotlib.pyplot as plt #Import plotlibrary
    #More usage of cm.Greens，please read official website
    plt.matshow(cm, cmap=plt.cm.Greens)
    plt.colorbar()
    for x in range(len(cm)): #Data Label
        for y in range(len(cm)):
            plt.annotate(cm[x,y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
    plt.ylabel('True label') #Axis Label
    plt.xlabel('Predicted label') #Axis Label
    return plt"""
from cm_plot import *
cm_plot(y, yp).savefig('./data/neiral_network.png')

print("Done on this run of neural_network_model_training by DK ", datetime.now())
