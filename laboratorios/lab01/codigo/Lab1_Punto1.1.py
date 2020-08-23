
"""
Estructura de datos y algoritmos 1
Laboratorio 1 Punto 1.1
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""
import random
import string
import time
import matplotlib.pyplot as plt

def long_sub(cadena1,cadena2): 
    m=len(cadena1) # C_1 = 1
    n=len(cadena2) # C_2 = 1
    if m==0 or n==0:
        cont=0 # C_3 = 4
    else:
        if cadena1[m-1]==cadena2[n-1]: # C_4 = 1
            cont=1+long_sub(cadena1[0:m-1],cadena2[0:n-1]) # T(m-1)+T(n-1) + C_5 
        else:
            cont= max(long_sub(cadena1[0:m-1],cadena2), # T(m-1)+T(n-1) + C_6
                      long_sub(cadena1,cadena2[0:n-1])) 
    
    return(cont) # C_7 = 1
"Test"
print(long_sub("ABCDGH","AEDFHR"))

tiempos=[]
tamaño=[] 
def tomartiempos():
        for n in range(1, 17): 
            ti = time.time()
            a=(random.sample(string.ascii_letters, n))
            a=("".join(a))
            b=(random.sample(string.ascii_letters, n))
            b=("".join(b))
            long_sub(a,b)
            tf = time.time()
            tiempos.append(tf-ti)
            tamaño.append(n)
            print(tf - ti)
tomartiempos()
print(tiempos)
plt.plot(tamaño,tiempos,'ro')
plt.ylabel('Tiempo (s)')
plt.xlabel('n')
