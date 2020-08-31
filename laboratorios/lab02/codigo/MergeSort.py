"""
Estructura de datos y algoritmos 1
Laboratorio 2 Punto 1.1
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""
import time
import random
import matplotlib.pyplot as plt

def mergeSort(array):
    if len(array)<=1: 
        return (array) #C_1 = 4
    else:           
        m = len(array)//2 
        izq = array[:m]
        der = array[m:]
        mergeSort(izq) # T(n/2)
        mergeSort(der) # T(n/2)
        i=j=k=0       
        while i < len(izq) and j < len(der):
            if izq[i] < der[j]: # T(n)= n/2
                array[k]=izq[i]
                i=i+1
            else: 
                array[k]=der[j]
                j=j+1
            k=k+1

        while i < len(izq):
            array[k]=izq[i]
            i=i+1
            k=k+1

        while j < len(der):
            array[k]=der[j]
            j=j+1
            k=k+1
            
        return (array)      
 
array = [14,46,43,27,57,41,45,21,70]
print(mergeSort(array))


Tiempo = []
x=[]
for i in range(1,10000000,50000):
    array = [random.randint(0, x) for x in range(i)]  
    start_time = time.time()
    array.sort()
    array.reverse()
    mergeSort(array)
    Tiempo.append(time.time() - start_time)
    print(time.time() - start_time)
    x.append(i)

print(Tiempo)
plt.plot(x,Tiempo,'ro')
plt.ylabel('Tiempo')
plt.xlabel('Tamaño')
