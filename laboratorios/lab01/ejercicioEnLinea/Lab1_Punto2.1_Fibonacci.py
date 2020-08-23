"""
Estructura de datos y algoritmos 1
Taller 4 Punto 3 Opcional
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

""" 

def fibonacci(n):
    if n==0:
        return 0 # C_1 = 2
    if n==1:
        return 1 # C_2 = 2
    else:
        return fibonacci (n-2)+ fibonacci(n-1) # T(n-2)+T(n-1) + C

"Test"
for i in range (0,10):
    print(fibonacci(i))
