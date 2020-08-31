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

def fix34(array):
    i=0
    j=0
    for i in range (0,len(array)): # T(n) = n * n * C_1
        if array[i]==3: 
            if i==0:
                j=i
            else:
                j=i-1
            for j in range (j,len(array)): # T(n) = n * C_1
                if array[j]==4: # C_1 = 7 
                    value=array[i+1]
                    array[i+1]=array[j]
                    array[j]=value
            j=j+1               
    i=i+1
    print(array) # C_2 = 7

fix34([1, 3, 1, 4])
fix34([1, 3, 1, 4, 4, 3, 1])
fix34([3, 2, 2, 4])
    
Tiempo = []
x=[]
for i in range(1,1000000,50000):
    array = [random.randint(0, x) for x in range(i)]  
    start_time = time.time()
    fix34(array)
    Tiempo.append(time.time() - start_time)
    print(time.time() - start_time)
    x.append(i)

print(Tiempo)
plt.plot(x,Tiempo,'ro')
plt.ylabel('Tiempo')
plt.xlabel('Tamaño')
  