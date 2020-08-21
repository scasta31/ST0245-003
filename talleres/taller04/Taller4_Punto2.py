"""
Estructura de datos y algoritmos 1
Taller 4 Punto 2
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""
import time
import matplotlib.pyplot as plt

def subgrupo(volumenes,  maximo):
        return subgrupo1(0, volumenes, maximo)
    
    
def subgrupo1(start,  volumenes, maximo):
        if (start >= len(volumenes)): 
            return maximo == 0 # T(n) = c1 = 5
        else:
            esta = subgrupo1(start+1,volumenes,maximo)
            noEsta = subgrupo1(start+1,volumenes,maximo-volumenes[start])
            return esta or noEsta
            # T(n) = c2 + T( n - 1 ) + T( n - 1 ) , donde c2 = 7
            # T(n) = c2 (2^n - 1) + c1 2^(n-1) = constantota * 2 ^n + constante 
tiempos=[]
tamaño=[] 
def tomartiempos():
        for n in range(10, 30-1): 
            ti = time.time()
            subgrupo([0]*n, 10)
            tf = time.time()
            tiempos.append(tf-ti)
            tamaño.append(n)
            'print(tf - ti)'
            
'Test'            
print(subgrupo([5,6,8],15))
tomartiempos()
print(tiempos)
plt.plot(tamaño,tiempos,'ro')
plt.ylabel('Tiempo (s)')
plt.xlabel('Tamaño (n)')

'''Se observa un comportamiento exponencial, tanto en la
grafica como visualizando los valores en segundos obtenidos,
el cual corresponde a lo esperado ya que la complejidad del algoritmo 
es exponencial.'''