# -*- coding: utf-8 -*-
"""
Created by David Kuang
Last updates since Aug 2019
"""
import pandas as pd

#Attribute/Property: Line Loss Rate

inputfile= './data/electricity_data.xls' #Electricity_Data_InputOutputFile
outputfile = './tmp/electricity_data.xls' #Electricity_Data_OutputFile

data = pd.read_excel(inputfile)
data[u'Linelossrate'] = (data[u'Electricity_input'] - data[u'Electricity_output'])/data[u'Electricity_input']
data.to_excel(outputfile)
