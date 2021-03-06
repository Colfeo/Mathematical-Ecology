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
Wpop= Wpop.astype(np.float)
Wpop1 = data["Estimated number of wolves.1"].to_numpy()
POPrate = data["Annual rate of popultion increase"].to_numpy()
POPrate= POPrate[1:].astype(np.float)
Npacks = data["N packs"].to_numpy()
Npacks= Npacks.astype(np.float)
Npacks1 = data["N packs.1"].to_numpy()
Npairs = data["N pairs"].to_numpy()
Npairs= Npairs.astype(np.float)
Nloners = data["N loners"].to_numpy()
Nloners= Nloners.astype(np.float)
MeanGS = data["Mean group size"].to_numpy()
#MeanGS= MeanGS.astype(np.float)
Largest_group = data["Largest group"].to_numpy()
Largest_group= Largest_group.astype(np.float)
PACKrate = data["Annual rate of pack number increase"].to_numpy()
PACKrate= PACKrate[1:].astype(np.float)
Area_occupied = data["Area occupied"].to_numpy()
Area_occupied= Area_occupied.astype(np.float)
AREArate = data["Annual rate of increase of occupied area"].to_numpy()
AREArate= AREArate[1:].astype(np.float)
Nearest_dist = data["Nearest neighbour distance between wolf groups"].to_numpy()
Nlitters = data["N litters"].to_numpy()
Ndead = data["N dead wolves"].to_numpy()

add = [171,201,362,441,840]
Wpop2 = np.concatenate((Wpop,add))

def WolfEmp(x) : #Inspire from original paper
    y = np.zeros(len(x))
    for i in range(len(x)) :
        y[i] = 0.5e-251*math.exp(0.29*x[i]) #0.5e-251
    return y
def Wolf_ExpMod(x) : #solution of exponetiel model fit
    y = np.zeros(len(x))
    for i in range(len(x)) :
        y[i] = 9*math.exp(0.253457826*x[i]) 
    return y
def Wolf_Logsol(x) : #logistical equation sol : dN/dt = rN(1-N/K)
    K = 850
    #k= 0.176363
    k= 0.253457826
    #k = 0.35
    y = np.zeros(len(x))
    for i in range(len(x)) :
        #y[i] = K/(1+(K-9)*math.exp(-x[i]*k)*1/9)
        y[i] = K/(1+ ((K-10)/10) * math.exp(-x[i]*k ))
    return y
def plotpop() :
    #plt.plot(np.arange(12),Wpop)
    y = np.arange(2001.5,2013.5)
    yadd = np.arange(2001.5,2018.5)
    y2 = np.arange(2001.5,2033.5)
    y1 = np.arange(0,32)
    yy = np.arange(12)
    #plt.scatter(y,Wpop,label="data")
    plt.scatter(yadd[:13],Wpop2[:13],label="data1")
    plt.scatter(yadd[12:],Wpop2[12:],label="data2")
    #plt.plot(y2,WolfEmp(y2),label='exponentiel model')
    #plt.plot(y2,Wolf_ExpMod(y1), label='exponentiel model 2')
    plt.plot(y2,Wolf_Logsol(y1),label="logistic model")
    #print(WolfEmp(y2)[16])
    #print(Wolf_ExpMod(y1)[16])
    plt.legend()
    plt.show()

def plotrate() :
    y = np.arange(2001.5,2013.5)
    plt.plot(y[1:],POPrate,label='population rate')
    plt.plot(y[1:],PACKrate,label='packs rate')
    plt.plot(y[1:],AREArate,label='rate of occupied area')
    plt.legend()
    plt.show()
def plotvalue() :
    t = np.arange(2001.5,2013.5)

        
    data1 = np.exp(t)
    data2 = np.sin(2 * np.pi * t)
    
    fig, ax1 = plt.subplots()
    
    color = 'tab:red'
    ax1.set_xlabel('years')
    ax1.set_ylabel('Wolf population', color=color)
    ax1.plot(t, Wpop, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    
    color = 'tab:blue'
    ax2.set_ylabel('Area occupied', color=color)  # we already handled the x-label with ax1
    ax2.plot(t, Area_occupied, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()

def syspack() : 
    y = np.arange(2001.5,2013.5)
    plt.plot(y,Npacks,label="Number of packs")
    plt.plot(y,Npairs,label="Number of pair")
    plt.plot(y,Nloners,label="Number of loners")
    plt.title('Exact value from the data collected')
    plt.legend()
    plt.show()

def system() :
    L = [Nloners[0],Nloners[1],Nloners[2],Nloners[3]]
    Pi = [Npairs[0]]
    Pc = [Npacks[0]]
    #Fp = [0]#31
    for i in range(0,31) :
        if (i >=3) :
            L.append(0.3* Pc[i])
        Pi.append(0.5 *L[i] + 0.5*Pi[i]  )
        val = 1.10* Pc[i] + 0.55 * Pi[i] 
        Pc.append( val )
        #Fp.append(0.2 * Pc[i])
        
        
    y1 = np.arange(2001.5,2013.5)
    y = np.arange(2001.5,2033.5)
    plt.plot(y,Pc,label="packs according to the system")
    plt.plot(y,Pi,label="pair according to the system")
    plt.plot(y,L,label="Loners according to the system")
    plt.title('computed value from the first model')
    
    plt.plot(y1,Npacks,label="Number of packs")
    plt.plot(y1,Npairs,label="Number of pair")
    plt.plot(y1,Nloners,label="Number of loners")
    

    
    plt.legend()
    plt.show()


def final_sys() :
    L = [Nloners[0],Nloners[1],Nloners[2],Nloners[3]]
    Pi = [Npairs[0]]
    Pc = [Npacks[0]]
    #Fp = [0]#31
    for i in range(0,31) :
        if (i >=3) :
            L.append(0.3* Pc[i])
        Pi.append(0.5 *L[i] + 0.5*Pi[i]  )
        val = 0.3*Pc[i]*(1 - Pc[i]/55) + 0.9*Pc[i] + 0.45 * Pi[i] 
        Pc.append( val )
        
    print(L)
    y = np.arange(2001.5,2013.5)
    y1 = np.arange(2001.5,2033.5)
    plt.plot(y1,Pc,label="packs according to the system")
    plt.plot(y1,Pi,label="pair according to the system")
    plt.plot(y1,L,label="Loners according to the system")
    
    plt.plot(y,Npacks,label="Number of packs")
    plt.plot(y,Npairs,label="Number of pair")
    plt.plot(y,Nloners,label="Number of loners")
    
    plt.title('computed value from the second model')
    

    
    plt.legend()
    plt.show()
    
# system()  
# final_sys() 
    
plotpop()  
    
    
    
    
    
    