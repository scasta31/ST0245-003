  
"""
Estructura de datos y algoritmos 1
Laboratorio 5
Punto 2.1
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""

import numpy as np

class Graph:
  def __init__(self, size):
    self.size = size
    aux = []
    matriz = []
    for i in range(self.size+1):
      aux = []
      for j in range(self.size+1):
        aux.append(None)
      matriz.append(aux)
    array = np.array(matriz)
    self.matriz = array

  def addArc(self, vertex, edge, weight=1):
    vertex_exist = False
    edge_exist = False
    fila = None
    columna = None
    for i in range(1,len(self.matriz),1): 
      if vertex == self.matriz[0][i]:
        vertex_exist = True
      if edge == self.matriz[0][i]:
        edge_exist = True
    if vertex_exist == False:
      for i in range(1,len(self.matriz),1):
        if self.matriz[0][i] == None:
          self.matriz[0][i] = vertex
          self.matriz[i][0] = vertex
          break
    if edge_exist == False: 
      for i in range(1,len(self.matriz),1):
        if self.matriz[0][i] == None:
          self.matriz[0][i] = edge
          self.matriz[i][0] = edge
          break
    for i in range(len(self.matriz)):
      if self.matriz[i][0] == vertex:
        fila = i
      if self.matriz[0][i] == edge:
        columna = i
    self.matriz[fila][columna] = weight
    self.matriz[columna][fila] = weight
    return (self.matriz)

n = int(input("Ingrese número de nodos:  "))
g = Graph(n)
arcos = int(input("Ingrese número de arcos:  "))
for i in range(arcos):
  arcos_pares = str(input("Ingrese arco (Nodo inicial seguido por nodo final Ej: 23):   "))
  vert1 = arcos_pares[0]
  vert2 = arcos_pares[1]
  b = g.addArc(vert1,vert2)
a = b[1:,1:]
colores = True
for i in range(len(a)):
  for j in range(len(a)-1):
    if a[i][j] == a[i][j+1]:
      colores = False

if colores == True:
  print("Los nodos del grafo:\n " + str(b) + "\n  pueden ser coloreados con dos colores")
else:
  print("Los nodos del grafo:\n " + str(b) + "\n  NO pueden ser coloreados con dos colores")