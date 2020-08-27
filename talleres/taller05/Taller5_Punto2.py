"""
Estructura de datos y algoritmos 1
Taller 5 Punto 2
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""
import time
import random
import matplotlib.pyplot as plt

def sumar(n):
    total=0 # O(1)
    for i in range (0,len(n)):
        total=total+n[i] # O(2) + O(n-1)
    return total # O(1)

n=[5,3,2,4,8,16,43]
print("Para el vector "+ str(n)+" la suma de sus elementos es igual a "+str(sumar(n))+".")

Tiempo = []
x=[]
for i in range(1, 21000,1000):
    array = [random.randint(0, x) for x in range(i)]
    start_time = time.time()
    sumar(array)
    Tiempo.append(time.time() - start_time)
    'print(time.time() - start_time)'
    x.append(i)

print(Tiempo)
plt.plot(x,Tiempo,'ro')
plt.ylabel('Tiempo')
plt.xlabel('Tamaño')


        