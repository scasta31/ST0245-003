"""
Estructura de datos y algoritmos 1
Proyecto Entrega 1 
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610036014

"""
import numpy as np
import pandas as pd

''' 1. Depuración de los datos:
Se eliminan columnas:
- 2,3,5,6,7,9,10,11,12,14,15,16,17,18,19,20,21,23,24
25,27,28,29,30,31,33,34,37,38,39,40,41,42,43,44,46,47
48,49,50,53,55,56,57,58,60,61,62,63,64,65,66,67,68,69,70
71,72,73,74,75,76.

'''
def initial_conds():
    
    data=pd.read_csv("0_test_balanced_5000.csv",sep=';')
    data2=np.asarray(data)
    cont=0
    data_d=data2
    cols=[2,3,5,6,7,9,10,11,12,14,15,16,17,18,19,20,21,23,24,25,27,28,29,30,31,33,34,37,38,39,40,41,42,43,44,46,47,48,49,50,53,55,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76]
    for i in range (0,78):
        for j in cols:
            if i==j:
                data_d=np.delete(data_d,i-cont,1)
                cont=cont+1;
    return (data_d)

data_d=initial_conds()
            
def is_nan(x):
    return (x != x)
 
def attribute_values(num_col):
       
    attribute = data_d[:,num_col]
    values=[]

    for k in attribute:
        if k not in values and is_nan(k)==0:
            values.append(k)
    return (values)

def count_nans(num_col):
    
    attribute = data_d[:,num_col]
    cont4=0
    for k in attribute:
        if is_nan(k)==1:
            cont4=cont4+1  
     
    return(cont4)
      
def Gini(num_col):
    
    attribute = data_d[:,num_col]
    values=[]
    for k in attribute:
        if k not in values and is_nan(k)==0:
            values.append(k)
            
    right_node=np.zeros((len(values),1))
    right_positive=np.zeros((len(values),1))
    right_negative=np.zeros((len(values),1))
    
    cont1=0
    cont2=0
    cont3=0
    for k in range (0,len(values)):
        for m in range (0,len(attribute)):
            if values[k]==attribute[m] and data_d[m,15]==1:
                cont1=cont1+1
                cont2=cont2+1
            if values[k]==attribute[m] and data_d[m,15]==0:
                cont1=cont1+1
                cont3=cont3+1
                
        right_node[k]=cont1
        right_positive[k]=cont2
        right_negative[k]=cont3
        cont1=0
        cont2=0
        cont3=0
    
    left_node=np.zeros((len(values),1))
    left_positive=np.zeros((len(values),1))
    left_negative=np.zeros((len(values),1))
    
    cont1=0
    cont2=0
    cont3=0
    for k in range (0,len(values)):
        for m in range (0,len(attribute)):
            if values[k]!=attribute[m] and data_d[m,15]==1 and is_nan(attribute[m])==0:
                cont1=cont1+1
                cont2=cont2+1
            if values[k]!=attribute[m] and data_d[m,15]==0 and is_nan(attribute[m])==0:
                cont1=cont1+1
                cont3=cont3+1
                
        left_node[k]=cont1
        left_positive[k]=cont2
        left_negative[k]=cont3
        cont1=0
        cont2=0
        cont3=0
    
    right_gini=np.zeros((len(values),1))
    for j in range (0,len(right_gini)):
        right_gini[j]=1-((right_positive[j]/right_node[j])**2)-((right_negative[j]/right_node[j])**2)
    
    left_gini=np.zeros((len(values),1))
    for j in range (0,len(left_gini)):
        left_gini[j]=1-((left_positive[j]/left_node[j])**2)-((left_negative[j]/left_node[j])**2)
        
    cont4=count_nans(num_col) 
    
    avg_gini=np.zeros((len(values),1))
    for j in range (0,len(avg_gini)):
        avg_gini[j]=(((right_gini[j]*right_node[j])+(left_gini[j]*left_node[j]))/(np.shape(data_d)[0]-cont4))

    return (avg_gini)

# OUTPUT
columns=["Consecutivo","Estudiante exterior?","Tomó curso preparatorio?","Hizo simulacro?","Numero libros en la familia","Departamento de residencia","Área de residencia","Estrato","Tiene internet?","Tiene computador","Trabaja actualmente?","Tipo colegio","Naturaleza colegio","Colegio bilingue?","Ubicación colegio","Exito/Fracaso"]
for i in range (1,15):
    print("-------------------------------------------------------------------")
    valores=attribute_values(i)
    gini=Gini(i)
    print("Para la variable ",columns[i] ," los valores posibles son: ", valores, "Los respectivos coeficientes de Gini son: ", np.array(gini).T)

gini_estexterior=Gini(1)
gini_cursoprep=Gini(2)
gini_simulacro=Gini(3)
gini_numlibros=Gini(4)
gini_dptoreside=Gini(5)
gini_areareside=Gini(6)
gini_estrato=Gini(7)
gini_tieneinternet=Gini(8)
gini_tienepc=Gini(9)
gini_trabaja=Gini(10)
gini_tipocolegio=Gini(11)
gini_naturalezacolegio=Gini(12)
gini_colegiobilingue=Gini(13)
gini_ubicolegio=Gini(14)


pos_i=[-1,-1,-1,-1,-1]
pos_j=[-1,-1,-1,-1,-1]
atributo=["","","","",""]
repetido=0
cont_menores=[1,1,1,1,1]
for s in range(0,5):
    for i in range(2,15):
        Gini_momento=Gini(i)
        for j in range(0,len(Gini_momento)):         
            if Gini_momento[j]<cont_menores[s]:
                repetido=0  
                for l in range (0,5):
                    if pos_i[l]==i and pos_j[l]==j:
                        repetido=1
                if repetido==0:
                        cont_menores[s]=Gini_momento[j]
                        atributo[s]=attribute_values(i)[j]
                        pos_i[s]=i
                        pos_j[s]=j
                        
for i in range(0,5):
    print("El atributo ", atributo[i], "es el numero ", i+1, "con la impureza de GINI mas baja, con un GINI de: ", cont_menores[i])
                      
                