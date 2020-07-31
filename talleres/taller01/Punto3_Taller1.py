"""
Estructura de datos y algoritmos 1
Taller 1 Punto 3 
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610036014

"""
import math
class Line2D():
    
    def __init__(self,xi,yi,xf,yf):
        self.xi=xi
        self.yi=yi
        self.xf=xf
        self.yf=yf
    def obtener_puntos(self):
        print("Los puntos son",(self.xi,self.yi),"y",(self.xf,self.yf))        
    def obtener_xi(self):
        return self.xi
    def obtener_yi(self):
        return self.yi
    def obtener_xf(self):
        return self.xf
    def obtener_yf(self):
        return self.yf
    def calc_puntos(self):
        magnitud=math.sqrt(((self.xf-self.xi)**2 +(self.yf-self.yi)**2))
        angulo=math.atan2(self.yf-self.yi,self.xf-self.xi)
        x1=self.xi+((magnitud/3)*math.cos(angulo))
        x1=round(x1,2)
        y1=self.yi+((magnitud/3)*math.sin(angulo))
        y1=round(y1,2)
        x2=self.xi+(magnitud*(2/3)*math.cos(angulo))
        x2=round(x2,2)
        y2=self.yi+(magnitud*(2/3)*math.sin(angulo))
        y2=round(y2,2)
        print("Los puntos intermedios son","[",(self.xi,self.yi),",",(x1,y1),",",(x2,y2),",",(self.xf,self.yf),"]")
        
"""Test"""
Linea1=Line2D(2,3,5,5)
Line2D.obtener_puntos(Linea1)
Line2D.calc_puntos(Linea1)