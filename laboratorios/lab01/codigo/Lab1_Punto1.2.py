"""
Estructura de datos y algoritmos 1
Laboratorio 1 Punto 1.2
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""

def llenar_rect(n):
    if n<=2:
        return (n)
    else:
        return llenar_rect(n-1)+llenar_rect(n-2) 
    
'Test'
for i in range (1,11):
        print(llenar_rect(i))