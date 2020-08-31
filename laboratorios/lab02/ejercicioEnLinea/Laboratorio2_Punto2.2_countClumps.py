"""
Estructura de datos y algoritmos 1
Laboratorio 2 Punto 2.2 
Ejercicios CodingBat Array-3
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""

import time
import random
import matplotlib.pyplot as plt

def countClumps(array):
    cont=0    
    aux=0 
    for i in range (0,len(array)-1): # T(n) = n-1 * C_2 
        if array[i]==array[i+1] and aux==0: # C_2 = 8
            aux=1
            cont=cont+1
        if array[i]!=array[i+1]: # C_1 = 4
            aux=0                
    ''''print(cont)''' # C_3 = 3
 
countClumps([1, 2, 2, 3, 4, 4])
countClumps([1, 1, 2, 1, 1])
countClumps([1, 1, 1, 1, 1])


Tiempo = []
x=[]
for i in range(10000,870000,45000):
    array = [random.randint(0, x) for x in range(i)]  
    start_time = time.time()
    countClumps(array)
    Tiempo.append(time.time() - start_time)
    print(time.time() - start_time)
    x.append(i)

print(Tiempo)
plt.plot(x,Tiempo,'ro')
plt.ylabel('Tiempo')
plt.xlabel('Tamaño')