"""
Estructura de datos y algoritmos 1
Laboratorio 1 Punto 2.1
Ejercicios Recursión 1 CodingBat

Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

Given base and n that are both 1 or more, compute recursively (no loops) 
the value of base to the n power.
"""

def powerN(base,n):
    if base<1 or n<1: # C_1 = 4
        return "No es posible, ingrese valores enteros iguales o superiores a 1."
    if n==1: 
        return base # C_2 = 2 
    else:
        return base*powerN(base,n-1) # C_3 = T(n-1) + C

"Test"
for i in range (2,11):
    for j in range (2,11):        
            print(str(i)+"^"+str(j)+"="+str(powerN(i,j)))  
        