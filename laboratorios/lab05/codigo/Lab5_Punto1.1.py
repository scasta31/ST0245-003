"""
Estructura de datos y algoritmos 1
Laboratorio 5
Punto 1.1
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014
"""

import numpy as np
import pandas as pd
from itertools import permutations

data=pd.read_csv("Ejemplo_Datos.txt",sep=' ')
data=np.asarray(data)

def distance(ini,fin):
    for i in range (0,len(data)):
        
        if data[i][0]==ini and data[i][1]==fin:
            return data[i][2]


for i in range (0,len(data)):
    number=1
    if data[i][0]>number:
        number=data[i][0]

vector=[]

for i in range(0,number+1):
    if i>1:
        vector.append(i)
        
permutaciones=list(permutations(vector))

permutaciones=np.asarray(permutaciones)

vector2=np.zeros((len(permutaciones),4))

columns=permutaciones.shape[1]

for n in range (0,len(permutaciones)):
    for k in range (1,columns):
        vector2[n][k-1]=distance(permutaciones[n][k],permutaciones[n][k-1])+vector2[n][k-2]
        vector2[n][3]=distance(permutaciones[n][0],1)


mayor=0;
menor=100;

for i in range (0,len(vector2)):
    if vector2[i][3]>=mayor:
        mayor=vector2[i][3]
for i in range (0,len(vector2)):       
    if vector2[i][1]<menor and vector2[i][3]==mayor:
        menor=vector2[i][1]
        posicion=i

camino=permutaciones[posicion][:]
Ruta2=[]
Ruta1=camino[:][3]
for i in range(0,len(camino)-1):
    Ruta2.append(camino[i])
print("Los caminos optimos son: ", Ruta2, " y ", Ruta1)