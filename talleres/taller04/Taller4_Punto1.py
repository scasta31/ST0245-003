"""
Estructura de datos y algoritmos 1
Taller 4 Punto 1
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""
import time
import matplotlib.pyplot as plt

def array_max(array):
    return array_maxint(array,(len(array)))

def array_maxint(array,n):
    if (n==1):
        return array[0]
    else:
        return max(array[n-1],array_maxint(array,n-1))
    
tiempos=[]
tamaño=[]     
def tomartiempos():
        for n in range(10, 30-1): 
            ti = time.time()
            array_max([0]*n)
            tf = time.time()
            tiempos.append(tf-ti)
            tamaño.append(n)
            'print(tf - ti)'

'Test'
vector=[5,54,7,-8]    
print('El valor maximo del vector '+str(vector)+' es '+str(array_max(vector)))
tomartiempos()
plt.plot(tamaño,tiempos,'ro')
plt.ylabel('Tiempo (s)')
plt.xlabel('Tamaño del arreglo (n)')

'''Se observa un comportamiento constante, el cual corresponde a lo esperado
ya que la complejidad del algoritmo es constante.'''