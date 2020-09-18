"""
Punto 1.1
Dennis Castrillon
Sebastian Castaño

"""
import numpy as np
import pandas as pd

dataVertices = pd.read_csv('Vertices.csv')
N_filasV=(dataVertices.shape[0])
print(dataVertices.head())
dataVertices=dataVertices.values.tolist()


dataArcos = pd.read_csv('Arcos.csv')
N_filasA=(dataArcos.shape[0])
print(dataArcos.head())
dataArcos=dataArcos.values.tolist()

N_columnasV=len(dataVertices[0])
N_columnasA=len(dataArcos[0])


Info_Ver=np.zeros((N_filasV,N_columnasV-1))
for i in range(0,N_filasV):
    for j in range(0,N_columnasV-1):
        Info_Ver[i][j]=dataVertices[i][j]
print(Info_Ver)


Info_Arc=np.zeros((N_filasA,N_columnasA-1))
for i in range(0,N_filasA):
    for j in range(0,N_columnasA-1):
        Info_Arc[i][j]=dataArcos[i][j]
print(Info_Arc)


def acceder_vertices(i,j):
    return Info_Ver[i,j] # O(1)
    
def acceder_arcos(i,j):
    return Info_Arc[i,j] # O(1)
    
def size(M):
    Fil_Col=[M.shape[0],len(M[0])]
    return Fil_Col # O(1)

def agregar(M,V_agg):
    return np.append(M,[V_agg], axis=0) # O(1)

def eliminar(M,Fila):
    return np.delete(M, Fila, axis=0) # O(1)

