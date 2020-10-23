"""
Taller 11 Punto 1
Estructura datos y algoritmos 1
Sebastian Castaño Orozco 201610054014
Dennis Castrillon Sepulveda 201610035014
"""
import numpy as np

class GraphAl:
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


  def addArc(self, source, destination, weight):
    source_exist = False
    destination_exist = False
    fila = None
    columna = None
    for i in range(1,len(self.matriz)): 
      if source == self.matriz[0][i]:
        source_exist = True
      if destination == self.matriz[0][i]:
        destination_exist = True
    if source_exist == False: 
      for i in range(1,len(self.matriz)):
        if self.matriz[0][i] == None:
          self.matriz[0][i] = source
          self.matriz[i][0] = source
          break
    if destination_exist == False:
      for i in range(1,len(self.matriz)):
        if self.matriz[0][i] == None:
          self.matriz[0][i] = destination
          self.matriz[i][0] = destination
          break
    for i in range(len(self.matriz)):
      if self.matriz[i][0] == source:
        fila = i
      if self.matriz[0][i] == destination:
        columna = i
    self.matriz[fila][columna] = weight
    return (self.matriz)

    print(self.matriz)

  def getSuccessors(self, vertice):
    fila = 0
    columna = 0
    adyacentes = []

    for i in range(len(self.matriz)):
      if self.matriz[i][0] == vertice:
        for j in range(1,len(self.matriz)):
          if self.matriz[i][j] != None:
            adyacentes.append(self.matriz[0][j])

    for i in range(len(self.matriz)):
      if self.matriz[0][i] == vertice:
        for j in range(1,len(self.matriz)):
          if self.matriz[j][i] != None:
            adyacentes.append(self.matriz[j][0])

    adyacentes = list(set(adyacentes)) 
    for i in range(len(adyacentes)):
      print("El nodo " + str(adyacentes[i]) + " es adyacente al nodo " +str(vertice) + str(" y viceversa"))
    return adyacentes

  def getWeight(self, source, destination):
    fila = None
    columna = None
    for i in range(len(self.matriz)):
      if self.matriz[i][0] == source:
        fila = i
      if self.matriz[0][i] == destination:
        columna = i
    peso = (self.matriz[fila][columna])
    if peso == None:
      return "No existe peso desde " + str(source) + " hacia " + str(destination)
    else:
      return "El peso ejercido desde " + str(source) + " hacia " + str(destination) + " es de " + str(peso)

# Ejemplo Taller
print("-----------------EJEMPLO TALLER---------------------------")
g = GraphAl(8) 
g.addArc("5","11","1")
g.addArc("11","2","1")
g.addArc("11","9","1")
g.addArc("7","11","1")
g.addArc("7","8","1")
g.addArc("3","8","1")
g.addArc("3","10","1")
print(g.addArc("8","9","1"))
print(g.getSuccessors("11")) #
print(g.getWeight("7","11"))

print("----------------------------------------------------------")

# Ejemplo plantilla
print("-----------------EJEMPLO PLANTILLA------------------------")
ga = GraphAl(3)
print(ga.addArc(0, 3, 10))
print(ga.getWeight(0, 3))
print(ga.addArc(0, 4, 7))
print(ga.getSuccessors(0))