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

def canBalance(array):
    suma1=0
    suma2=0
    array2=array[::-1] # C_4 = 3
    for i in range (0,len(array)):
        suma1=suma1+array[i] # T(n) = n * n * C_1 * C_2
        for j in range(0,len(array2)):
            suma2=suma2+array2[j]
            if suma1==suma2: 
                return True # C_1 = 7 T(n)= n * C_1 
        j=j+1 # C_2 = 2
    i=i-1 # C_3 = 2
    return False # C_5 = 1

print(canBalance([1, 1, 1, 2, 1]))
print(canBalance([2, 1, 1, 2, 1]))
print(canBalance([10, 10]))

Tiempo = []
x=[]
for i in range(1,10000,500):
    array = [random.randint(0, x) for x in range(i)]  
    start_time = time.time()
    canBalance(array)
    Tiempo.append(time.time() - start_time)
    print(time.time() - start_time)
    x.append(i)

print(Tiempo)
plt.plot(x,Tiempo,'ro')
plt.ylabel('Tiempo')
plt.xlabel('Tamaño')
