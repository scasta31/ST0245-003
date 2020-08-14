"""
Estructura de datos y algoritmos 1
Taller 3 Punto 1
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""
def Hanoi (N):
    Noriginal=N
    Hanoi_int(N,Noriginal)
    
def Hanoi_int(N,Noriginal,a="Torre 1",b="Torre 2",c="Torre 3"):

    if N==1:
        print("Mover de "+a+" a "+c)
    else:
        Hanoi_int(N-1,a,c,b)
        Hanoi_int(1,a,b,c)
        Hanoi_int(N-1,b,a,c)

"Test"

Hanoi(3)