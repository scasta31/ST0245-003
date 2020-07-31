"""
Estructura de datos y algoritmos 1
Taller 1 Punto 2
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014
"""

class Fecha():
    """un TAD fecha"""
    def __init__(self,dia,mes,anyo):
        self.__dia__= dia
        self.__mes__= mes
        self.__anyo__= anyo

    def mes(self):
        return self.__mes__
    def dia(self):
        return self.__dia__
    def anyo(self):
        return self.__anyo__

    def toString(self):
        meses_texto=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octumbre","noviembre","diciembre"]
        return str(self.__dia__) + "/" + str(meses_texto[self.__mes__-1]) + "/" + str(self.__anyo__)


    def comparar(self,FechaComparar):
        """Compara un fecha y retorna -1 si es menor 0 si es igual y 1 si es mayor"""
        meses_texto=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octumbre","noviembre","diciembre"]
        fecha1= self.__anyo__*10000+ self.__mes__*100+ self.__dia__*1
        fecha2= FechaComparar.anyo()*10000 + FechaComparar.mes()*100 + FechaComparar.dia()*1

        if fecha1 == fecha2:
            return "La fecha " + str(self.__dia__) + " de " + str(meses_texto[self.__mes__-1]) + " de " + str(self.__anyo__) + " es igual a la fecha " + str(FechaComparar.dia()) + " de " + str(meses_texto[FechaComparar.mes()-1]) + " de " + str(FechaComparar.anyo())
        if fecha1 < fecha2:
            return "La fecha " + str(self.__dia__) + " de " + str(meses_texto[self.__mes__-1]) + " de " + str(self.__anyo__) + " esta antes de la fecha " + str(FechaComparar.dia()) + " de " + str(meses_texto[FechaComparar.mes()-1]) + " de " + str(FechaComparar.anyo())
        else:
            return "La fecha " + str(self.__dia__) + " de " + str(meses_texto[self.__mes__-1]) + " de " + str(self.__anyo__) + " esta despues de la fecha " + str(FechaComparar.dia()) + " de " + str(meses_texto[FechaComparar.mes()-1]) + " de " + str(FechaComparar.anyo())


"""Test"""

fecha1= Fecha(15,12,2005)
fecha2= Fecha(12,12,2005)
print (fecha1.toString())
print (fecha2.toString())
print (fecha1.comparar(fecha2))
