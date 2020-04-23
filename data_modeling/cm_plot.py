# -*- coding: utf-8 -*-

# cm_plot.py file including confusion matrix visualization function
# Under folder site-packages of python, ready to be invoke
# For example: ~/anaconda2/lib/python2.7/site-packages

def cm_plot(y, yp):
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
    return plt
