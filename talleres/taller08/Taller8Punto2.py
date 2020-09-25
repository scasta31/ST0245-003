
"""
Taller 8 Punto 2
Estructura de Datos y Algoritmos 1
Sebastian Castaño Orozco 201610054014
Dennis Castrillon Sepulveda 201610035014

"""

def neveras(almacen,solicitudes):
  resultado=[]
  i=len(solicitudes)-1
  while i>=0:
    resultado.append(solicitudes[i][0])
    for j in range(0,solicitudes[i][1]):
      if len(almacen)!=0:
        resultado.append(almacen.pop())
      else:
        return resultado
    i=i-1
  return resultado

almacen = [(1,"haceb"), (2,"lg"), (3,"ibm"), (4,"haceb"),
(5,"lg"), (6,"ibm"),(7,"haceb"), (8,"lg"), (9,"ibm"),(8,"lg"),
(9,"ibm")]
solicitudes = [("eafit", 10), ("la14", 2), ("olimpica", 4),
("éxito", 1)]
print(neveras(almacen,solicitudes))