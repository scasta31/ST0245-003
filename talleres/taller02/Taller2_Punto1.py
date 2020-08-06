"""
Estructura de datos y algoritmos 1
Taller 2 Punto 1
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""
def baldosa(m,n):
    
    if m<=0 or n<=0:
        return print("Los valores ingresados no son correctos, se calcula para valores positivos.")        
    if m==n:
        print(m)
    if m<n:
        return(baldosa(m,n-m))
    if m>n:
        return(baldosa(m-n,n))

"Test"
baldosa(6000,120)