"""
Estructura de datos y algoritmos 1
Taller 4 Punto 3 Opcional
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

""" 
import time
import matplotlib.pyplot as plt

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci (n-2)+ fibonacci(n-1)

"Test"
for i in range (0,10):
    print(fibonacci(i))
    
tiempos=[]
tamaño=[] 
def tomartiempos():
        for n in range(10, 35-1): 
            ti = time.time()
            fibonacci(n)
            tf = time.time()
            tiempos.append(tf-ti)
            tamaño.append(n)
            'print(tf - ti)'
tomartiempos()
print(tiempos)
plt.plot(tamaño,tiempos,'ro')
plt.ylabel('Tiempo (s)')
plt.xlabel('n')

'''Se observa un comportamiento exponencial, tanto en la
grafica como visualizando los valores en segundos obtenidos,
el cual corresponde a lo esperado ya que la complejidad del algoritmo 
es exponencial.'''