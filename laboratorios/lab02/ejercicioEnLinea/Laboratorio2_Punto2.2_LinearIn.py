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

def BorrarRepetidos(array):
    new_array=[]
    for i in range (0,len(array)): # T(n) = n * C_2
        if array[i] not in new_array: # C_2 = 3
            new_array.append(array[i])
    return (new_array)
    
    
def linearIn(array1,array2):
    array1=BorrarRepetidos(array1) # T(n) = n * C_2
    array2=BorrarRepetidos(array2) # T(m) = m * C_2
    cont=0
    for i in range (0,len(array2)): # T(n,m) = m * n * C_1
        for j in range (0,len(array1)): # T(n) = n * C_1
            if (array2[i]==array1[j]): # C_1 = 4
                cont=cont+1   
    i=i+1 
    if cont==len(array2): # C_3 = 6
        return True
    else:
        return False
    
print(linearIn([1, 2, 4, 6], [2, 4]))
print(linearIn([1, 2, 4, 6], [2, 3, 4]))
print(linearIn([1, 2, 4, 4, 6], [2, 4]))

Tiempo = []
x=[]
for i in range(1,21000,1000):
    array = [random.randint(0, x) for x in range(i)]  
    array2 = [random.randint(0, x) for x in range(i)] 
    start_time = time.time()
    linearIn(array,array2)
    Tiempo.append(time.time() - start_time)
    print(time.time() - start_time)
    x.append(i)

print(Tiempo)
plt.plot(x,Tiempo,'ro')
plt.ylabel('Tiempo')
plt.xlabel('Tamaño')