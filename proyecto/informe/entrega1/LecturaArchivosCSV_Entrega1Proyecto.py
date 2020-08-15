"""
Estructura de datos y algoritmos 1
Proyecto Entrega 1 
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610036014

"""
import numpy as np
import pandas as pd

class LeerCSV():
    "Lectura de archivo CSV separado por puntos y coma"
    
    def __init__(self,filename):
        self.filename=filename
        
    def LeerArchivo(self):
        dataset=pd.read_csv(self.filename,sep=';')
        dataset=np.asarray(dataset)
        return(dataset.shape)

"Test"
Archivo0=LeerCSV("0_test_balanced_5000.csv")
print("El dataset 0 fue leído correctamente y tiene un tamaño de " + str(LeerCSV.LeerArchivo(Archivo0)))
        
Archivo1=LeerCSV("1_test_balanced_15000.csv")
print("El dataset 1 fue leído correctamente y tiene un tamaño de " + str(LeerCSV.LeerArchivo(Archivo1)))    
        
Archivo2=LeerCSV("2_test_balanced_25000.csv")
print("El dataset 2 fue leído correctamente y tiene un tamaño de " + str(LeerCSV.LeerArchivo(Archivo2)))

Archivo3=LeerCSV("3_test_balanced_35000.csv")
print("El dataset 3 fue leído correctamente y tiene un tamaño de " + str(LeerCSV.LeerArchivo(Archivo3)))

Archivo4=LeerCSV("4_test_balanced_45000.csv")
print("El dataset 4 fue leído correctamente y tiene un tamaño de " + str(LeerCSV.LeerArchivo(Archivo4)))

Archivo5=LeerCSV("4_train_balanced_135000.csv")
print("El dataset 5 fue leído correctamente y tiene un tamaño de " + str(LeerCSV.LeerArchivo(Archivo5)))        
