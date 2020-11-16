"""
Estructura de datos y algoritmos 1
Proyecto Entrega Final
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610036014

"""

import pandas as pd
from time import time

class leaf:
    def __init__(self, Rows):
        self.Prediction = counting(Rows)
        
class pregunta:

    def __init__(self, column, value, headers):
        self.column = column
        self.value = value
        self.headers = headers

    def match(self, ejemplo):
        val = ejemplo[self.column]
        if is_number(val):
            if self.value == '':
                return float(val) >= 0
            return float(val) >= float(self.value)
        else:
            return val == self.value

    def __repr__(self):
        cond = "=="
        if is_number(self.value):
            cond = ">="
        return "Is %s %s %s?" % (
            self.headers[self.column], cond, str(self.value))

class select_node:
    def __init__(self,
                 pregunta,
                 rama_verdadera,
                 rama_falsa):
        self.pregunta = pregunta
        self.rama_verdadera = rama_verdadera
        self.rama_falsa = rama_falsa
        
def read_data(train_file,test_file):
    train_data = []
    test_data = []
    rows = []

    training_file = open(train_file,encoding='utf-8')
    testing_file = open(test_file,encoding='utf-8')

    
    for linea in training_file:
        linea = linea[:-1] 
        rows = linea.split(";")
        train_data.append(rows)

    
    headers = train_data[0] 

    rows = []

    for linea in testing_file:
        linea = linea[:-1] 
        estudiante = linea.split(";")
        test_data.append(estudiante)
    
    train_data.pop(0) 
    test_data.pop(0) 

    a = ['estu_consecutivo.1',
    'periodo',
    'fami_numlibros',
    'estu_inst_cod_departamento',
    'estu_tipodocumento.1',
    'estu_nacionalidad.1',
    'estu_genero.1',
    'estu_fechanacimiento.1',
    'periodo.1',
    'estu_estudiante.1',
    'estu_pais_reside.1',
    'estu_cod_reside_depto.1',
    'estu_cod_reside_mcpio.1',
    'fami_ocupacionpadre.1',
    'fami_ocupacionmadre.1',
    'fami_tienedvd',
    'cole_codigo_icfes',
    'cole_nombre_establecimiento',
    'cole_sede_principal',
    'cole_cod_dane_establecimiento',
    'estu_trabajaactualmente',
    'cole_cod_dane_sede',
    'cole_cod_mcpio_ubicacion',
    'cole_cod_depto_ubicacion',
    'desemp_ingles']

    train_data_df = pd.DataFrame.from_records(train_data,columns = headers)
    test_data_df = pd.DataFrame.from_records(test_data,columns = headers)

    for i in range(len(a)):
        del train_data_df[a[i]]
        del test_data_df[a[i]]
        headers.remove(a[i])

    train_data = train_data_df.values.tolist()
    test_data = test_data_df.values.tolist()

    return train_data,test_data,headers


def tree(rows,headers):

    gain, pregunta = best_division(rows,headers)

    if gain == 0:
        return leaf(rows)
    rows_verdaderas, rows_falsas = division(rows, pregunta)
    rama_verdadera = tree(rows_verdaderas,headers)
    rama_falsa = tree(rows_falsas,headers)
    return select_node(pregunta, rama_verdadera, rama_falsa)

def division(rows, question):

    rows_true, rows_false = [], []
    for row in rows:
        if question.match(row):
            rows_true.append(row)
        else:
            rows_false.append(row)
    return rows_true, rows_false

def gini(rows):

    cont = counting(rows)
    impureza = 1
    for lbl in cont:
        prueba = cont[lbl] / float(len(rows))
        impureza -= prueba**2
    return impureza

def info_gain(left, right, incertidumbre):

    p = float(len(left)) / (len(left) + len(right))
    return incertidumbre - p * gini(left) - (1 - p) * gini(right)

def is_number(value):
    aux = False
    
    if isinstance(value, int):
        aux = True  
        return aux 
    try:
        value = float(value)
        if isinstance(value, float) :
            aux = True
            return aux
    except:
           aux = False
           return aux
                   
def best_division(rows,headers):

    mejor_gain = 0  
    mejor_pregunta = None  
    incertidumbre = gini(rows)
    caracteristicas = len(rows[0]) - 1  

    for col in range(caracteristicas):  
        valores = set([fila[col] for fila in rows])  
        for val in valores:  
            preg = pregunta(col, val, headers)     
            rows_verdaderas, rows_falsas = division(rows, preg)  
                   
            if len(rows_verdaderas) == 0 or len(rows_falsas) == 0:
                continue       
            gain = info_gain(rows_verdaderas, rows_falsas, incertidumbre)

            if gain >= mejor_gain:
                mejor_gain, mejor_pregunta = gain, preg

    return mejor_gain, mejor_pregunta

def Sort(Rows, Node):

    if isinstance(Node, leaf):
        return Node.Prediction

    if Node.pregunta.match(Rows):
        return Sort(Rows, Node.rama_verdadera)
    else:
        return Sort(Rows, Node.rama_falsa)

def counting (Rows):
    counting = {}  
    for Row in Rows:
        
        success = Row[-1] 
        if success not in counting:
            counting[success] = 0
        counting[success] += 1
    return counting

def Accuracy(data_array_test, tree):
    real_values = []
    predicted_values = []
    
    
    for row in data_array_test:
        real_values.append(row[-1])
        predicted_values.append([*Sort(row, tree).keys()])

    total = 0

    for i in range(len(real_values)):
        if int(real_values[i]) == int(predicted_values[i][0]):
            total += 1
    
    return (print('Accuracy: ' +str((total/len(real_values))*100) +'%'))

def print_tree(node, spacing=""):

    if isinstance(node, leaf):
        print (spacing + "Predict", node.Prediction)
        return
    print (spacing + str(node.pregunta))
    print (spacing + '--> True:')
    print_tree(node.rama_verdadera, spacing + "  ")

    print (spacing + '--> False:')
    print_tree(node.rama_falsa, spacing + "  ")
    
# MAIN 

data_train,data_test,headers = read_data("Train_data.csv","Test_Data.csv")


time_ini = time()
Tree = tree(data_train,headers)
Accuracy(data_test,Tree)
time_fin = time()
exe_time = time_fin -time_ini
print_tree(Tree)
print("Tarda " + str(round(exe_time,2)) +" segundos en ejecutar")
