"""
Estructura de datos y algoritmos 1
Taller 1 Punto 1 
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610036014

"""
import math

class Punto2D():
    """Representacion de punto en 2 dimensiones"""

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def obtener_punto(self):
        return(self.x,self.y)
    
    def obtener_x(self):
        return self.x

    def obtener_y(self):
        return self.y

    def radio_polar(self):
        return math.sqrt(self.x**2 + self.y**2)
 
    def angulo_polar(self):
        return math.atan2(self.y,self.x)

    def dist_euclidiana(self,  other):
        return math.sqrt((self.x - other.x)**2 +  (self.y - other.y)**2)
    
"""Test"""

Punto1=Punto2D(1,3)
print("El punto 1 es",Punto2D.obtener_punto(Punto1))
print("La coordenada del punto 1 en x es",Punto2D.obtener_x(Punto1))
print("La coordenada del punto 1 en y es",Punto2D.obtener_y(Punto1))
print("El radio polar es",Punto2D.radio_polar(Punto1))
print("El ángulo polar es",Punto2D.angulo_polar(Punto1),"radianes")
Punto2=Punto2D(8,2)
print("El punto 2 es",Punto2D.obtener_punto(Punto2))
print("La distancia euclidiana entre ambos puntos es",Punto2D.dist_euclidiana(Punto1,Punto2))