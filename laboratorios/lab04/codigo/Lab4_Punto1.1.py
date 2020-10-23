"""
Estructura de datos y algoritmos 1
Laboratorio 4
Punto 1.1
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""

import math
import pandas as pd
import numpy as np

data=pd.read_csv("PruebaLab4.txt",sep=',')
data=np.asarray(data)

def distance(a,b):
    lat1=data[a,0]
    lon1=data[a,1]
    lat2=data[b,0]
    lon2=data[b,1]
    alt1=data[a,2]
    alt2=data[b,2]
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia_xy=2*R*math.asin(math.sqrt(a))
    distancia_xy=distancia_xy*1000
    dalt=abs(alt1-alt2)
    distancia=math.sqrt((distancia_xy**2)+(dalt**2))
    return distancia

distances=[]
close_bees=[]
for i in range (0,len(data)):
    for n in range (i,len(data)): 
        distances.append(distance(i,n))
        if i!=n and distance(n,i)<100:
            close_bees.append(data[n])
            close_bees.append(data[i])    

close_bees=np.asarray(close_bees)

