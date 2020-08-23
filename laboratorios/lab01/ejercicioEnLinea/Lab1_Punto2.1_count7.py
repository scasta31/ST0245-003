"""
Estructura de datos y algoritmos 1
Laboratorio 1 Punto 2.1
Ejercicios Recursión 1 CodingBat

Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

Given a non-negative int n, return the count of the occurrences 
of 7 as a digit.
"""
def count7(n):
    if (n<=0):
        return 'No es posible, ingrese valores enteros mayores a cero.' # C_1 = 1 
    if n<10:
        if n==7:
            return 1
        else:
            return 0  # C_2 = 4    
    else:
        return count7(n%10)+count7(int(n/10)) # C_3 = 3
    
"Test"
print('n -> cantidad de 7 en n')   
 
for i in [7,75,772,9,57987246777,-58]:  
    print(str(i)+' -> '+str(count7(i)))
    