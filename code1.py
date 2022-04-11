#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 11:54:52 2022

@author: damienvanoldeneel
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math 
"""
with open("data.txt") as f :
    lines = f.readlines()
index = 0
dat = np.array([])
for line in lines :
    if (index < 12) :
        l = np.array(line.strip())
        dat = np.concatenate((dat,[l]))
        print(line)
        index+=1
"""

data = pd.read_csv('classeur1.csv',sep=';') 
Wpop = data["Estimated number of wolves"].to_numpy()

def Wolf(x) :
    y = np.zeros(len(x))
    for i in range(len(x)) :
        y[i] = 0.5e-251*math.exp(0.29*x[i]) #0.5e-251
    return y



#plt.plot(np.arange(12),Wpop)
y = np.arange(2001.5,2013.5)

plt.scatter(y,Wpop)
plt.plot(y,Wolf(y))
plt.show()
