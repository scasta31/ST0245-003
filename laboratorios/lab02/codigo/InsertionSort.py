"""
Estructura de datos y algoritmos 1
Laboratorio Punto 1.1
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""
import time
import matplotlib.pyplot as plt
import random

def InsertionSort(array):
    for k in range (1,len(array)): # C_1 = n 
        j=array[k] # C_2 = n-1
        i= k-1 # C_3 = n-1
        while i>=0 and j<array[i]: 
                array[i+1]=array[i]
                array[i]=j
                i=i-1
                
    return(array)   # O(n)= n^2
    
tiempos=[]
tamaño=[] 
def tomartiempos():
        for i in range(0, 21000,1000): 
            ti = time.time()
            array=[random.randint(0,x) for x in range (i)]
            array.sort()
            array.reverse()
            InsertionSort(array)
            tf = time.time()
            tiempos.append(tf-ti)
            tamaño.append(i)
            print(tf - ti)

vector=[2,4,2,7,9,10,2]        
print("El vector "+str(vector)+" se organiza de manera ascendente y queda "+str(InsertionSort(vector)))

tomartiempos()
print(tiempos)
plt.plot(tamaño,tiempos,'ro')
plt.ylabel('Tiempo (s)')
plt.xlabel('Tamaño (n)')   