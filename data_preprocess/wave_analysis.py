# -*- coding: utf-8 -*-
"""
Created by David Kuang
Last updates in Sep 2019
"""

#Data Analysis using wavelet transform

from scipy.io import loadmat

inputfile= './data/leleccum.mat' #Extract signal files via Matlab
mat = loadmat(inputfile)
signal = mat['leleccum'][0]

#import PyWavelets
import pywt
coeffs = pywt.wavedec(signal, 'bior3.7', level=5) # The returned result is level+1 numbers: The 1st array is the approximation coefficient array, followed by the detailed coefficient array i