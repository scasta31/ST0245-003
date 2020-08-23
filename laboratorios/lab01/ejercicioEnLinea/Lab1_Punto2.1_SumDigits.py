"""
Estructura de datos y algoritmos 1
Laboratorio 1 Punto 2.1
Ejercicios Recursión 1 CodingBat

Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

Given a non-negative int n, return the sum of its digits recursively 
(no loops). Note that mod (%) by 10 yields the rightmost digit 
(126 % 10 is 6), while divide (/) by 10 removes the rightmost digit 
(126 / 10 is 12).

"""


def SumDigits(n):
    if (n<=0): 
        return 'No es posible, ingrese valores enteros mayores a cero.' # C_1 = 2
    if n<10: 
        return n # C_2 = 2
    else:
        return SumDigits(n%10)+SumDigits(int(n/10)) # C_3 = 3

"Test"
print('n -> suma de sus digitos')    
for i in [135,1234,7643,98653,-58]:  
    print(str(i)+' -> '+str(SumDigits(i)))
    
