"""
Estructura de datos y algoritmos 1
Proyecto Entrega 1 
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610036014

"""
import numpy as np
import pandas as pd

data=pd.read_csv("0_test_balanced_5000.csv",sep=';')

data2=np.asarray(data)

''' 1. Depuración de los datos:
Se eliminan columnas:
- 2,3,5,6,7,9,10,11,12,14,15,16,17,18,19,20,21,23,24
25,27,28,29,30,31,33,34,37,38,39,40,41,42,43,44,46,47
48,49,50,53,55,56,57,58,60,61,62,63,64,65,66,67,68,69,70
71,72,73,74,75,76,77 

'''
cont=0
data_d=data2
cols=[2,3,5,6,7,9,10,11,12,14,15,16,17,18,19,20,21,23,24,25,27,28,29,30,31,33,34,37,38,39,40,41,42,43,44,46,47,48,49,50,53,55,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77]
for i in range (0,78):
    for j in cols:
        if i==j:
            data_d=np.delete(data_d,i-cont,1)
            cont=cont+1;

def valores(num_col):
    
    estrato=data_d[:,num_col]
    valores=[]
    
    for k in estrato:
        if k not in valores:
            valores.append(k)
    
    contadores=np.zeros((len(valores),1))
    cont1=0
    for k in range (0,len(valores)):
        for m in range (0,len(estrato)):
            if valores[k]==estrato[m]:
                cont1=cont1+1
        contadores[k]=cont1
        cont1=0
    
    contadores_no=np.zeros((len(valores),1))
    for n in range (0,len(contadores)):
        contadores_no[n]=len(estrato)-contadores[n]
    
    gini_array=np.zeros((len(valores),1))
    for j in range (0,len(gini_array)):
        gini_array[j]=1-((contadores[j]/len(estrato))**2)-((contadores_no[j]/len(estrato))**2)
    
    for i in range (0,len(gini_array)):
        if gini_array[i]==0:
            gini_array=np.delete(gini_array,i,0)
            valores=np.delete(valores,i,0)
            
    return (valores)

def Gini(num_col):
    
    estrato=data_d[:,num_col]
    valores=[]
    
    for k in estrato:
        if k not in valores:
            valores.append(k)
    
    contadores=np.zeros((len(valores),1))
    cont1=0
    for k in range (0,len(valores)):
        for m in range (0,len(estrato)):
            if valores[k]==estrato[m]:
                cont1=cont1+1
        contadores[k]=cont1
        cont1=0
    
    contadores_no=np.zeros((len(valores),1))
    for n in range (0,len(contadores)):
        contadores_no[n]=len(estrato)-contadores[n]
    
    gini_array=np.zeros((len(valores),1))
    for j in range (0,len(gini_array)):
        gini_array[j]=1-((contadores[j]/len(estrato))**2)-((contadores_no[j]/len(estrato))**2)
    
    for i in range (0,len(gini_array)):
        if gini_array[i]==0:
            gini_array=np.delete(gini_array,i,0)
            valores=np.delete(valores,i,0)
    return (gini_array)

def Promedio_Gini(gini_array,num_col):
    estrato=data_d[:,num_col]
    valores=[]
    
    for k in estrato:
        if k not in valores:
            valores.append(k)
    
    contadores=np.zeros((len(valores),1))
    cont1=0
    for k in range (0,len(valores)):
        for m in range (0,len(estrato)):
            if valores[k]==estrato[m]:
                cont1=cont1+1
        contadores[k]=cont1
        cont1=0
    
    contadores_no=np.zeros((len(valores),1))
    for n in range (0,len(contadores)):
        contadores_no[n]=len(estrato)-contadores[n]
    
    gini_array=np.zeros((len(valores),1))
    for j in range (0,len(gini_array)):
        gini_array[j]=1-((contadores[j]/len(estrato))**2)-((contadores_no[j]/len(estrato))**2)
    
    for i in range (0,len(gini_array)):
        if gini_array[i]==0:
            gini_array=np.delete(gini_array,i,0)
            valores=np.delete(valores,i,0)
    suma_contadores=0        
    suma_gini=0;
    for o in range (0,len(gini_array)):
        suma_contadores=suma_contadores+contadores[o]
        suma_gini=(suma_gini)+(gini_array[o]*contadores[o])
    promedio_gini=suma_gini/suma_contadores
    return (promedio_gini)

# CÁLCULO DE GINI PARA ATRIBUTO

promedios=[]



# AREA DE RESIDENCIA

valores_area=valores(6)
Gini_area=Gini(6)
Promedio_area=Promedio_Gini(Gini_area,6)
print("------------------------------------------------------------------------------------------")
print("Para la variable area de residencia los valores posibles son: ", valores_area, "Los respectivos coeficientes de Gini son: ",np.array(Gini_area).T,"y el promedio de los coeficientes es:",Promedio_area)
promedios.append(Promedio_area)

# ESTRATO
valores_estrato=valores(7)
Gini_estrato=Gini(7)
Promedio_estrato=Promedio_Gini(Gini_estrato,7)
print("------------------------------------------------------------------------------------------")
print("Para la variable estrato los valores posibles son: ", valores_estrato, "Los respectivos coeficientes de Gini son: ",np.array(Gini_estrato).T,"y el promedio de los coeficientes es:",Promedio_estrato)
promedios.append(Promedio_estrato)

# INTERNET

valores_internet=valores(8)
Gini_internet=Gini(8)
Promedio_internet=Promedio_Gini(Gini_internet,8)
print("------------------------------------------------------------------------------------------")
print("Para la variable familia tiene internet los valores posibles son: ", valores_internet, "Los respectivos coeficientes de Gini son: ",np.array(Gini_internet).T,"y el promedio de los coeficientes es:",Promedio_internet)
promedios.append(Promedio_internet)

# ESTUDIANTE TRABAJA?

valores_esttrabaja=valores(10)
Gini_esttrabaja=Gini(10)
Promedio_esttrabaja=Promedio_Gini(Gini_esttrabaja,10)
print("------------------------------------------------------------------------------------------")
print("Para la variable estudiante trabaja los valores posibles son: ", valores_esttrabaja, "Los respectivos coeficientes de Gini son: ",np.array(Gini_esttrabaja).T,"y el promedio de los coeficientes es:",Promedio_esttrabaja)
promedios.append(Promedio_esttrabaja)

# TIPO GENERO DEL COLEGIO

valores_tipocolegio=valores(11)
Gini_tipocolegio=Gini(11)
Promedio_tipocolegio=Promedio_Gini(Gini_tipocolegio,11)
print("------------------------------------------------------------------------------------------")
print("Para la variable tipo de colegio los valores posibles son: ", valores_tipocolegio, "Los respectivos coeficientes de Gini son: ",np.array(Gini_tipocolegio).T,"y el promedio de los coeficientes es:",Promedio_tipocolegio)
promedios.append(Promedio_tipocolegio)

# NATURALEZA DEL COLEGIO

valores_natcolegio=valores(12)
Gini_natcolegio=Gini(12)
Promedio_natcolegio=Promedio_Gini(Gini_natcolegio,12)
print("------------------------------------------------------------------------------------------")
print("Para la variable naturaleza del colegio los valores posibles son: ", valores_natcolegio, "Los respectivos coeficientes de Gini son: ",np.array(Gini_natcolegio).T,"y el promedio de los coeficientes es:",Promedio_natcolegio)
promedios.append(Promedio_natcolegio)


# AREA DEL COLEGIO

valores_areacol=valores(14)
Gini_areacol=Gini(14)
Promedio_areacol=Promedio_Gini(Gini_areacol,14)
print("------------------------------------------------------------------------------------------")
print("Para la variable área del colegio los valores posibles son: ", valores_areacol, "Los respectivos coeficientes de Gini son: ",np.array(Gini_areacol).T,"y el promedio de los coeficientes es:",Promedio_areacol)
promedios.append(Promedio_areacol)

menor_promedios=1
for l in range (0,len(promedios)):
    if promedios[l]<menor_promedios:
        menor_promedios=promedios[l]
        posicion_menor=l
        
atributos=["area de residencia","estrato","tiene internet","¿Estudiante trabaja?","tipo genero colegio","naturaleza del colegio","area ubicacion del colegio"]
print("------------------------------------------------------------------------------------------")
print("Según el cálculo de impureza de Gini, el atributo a seleccionar es", atributos[posicion_menor])