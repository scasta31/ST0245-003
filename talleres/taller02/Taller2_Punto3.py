"""
Estructura de datos y algoritmos 1
Taller 2 Punto 3
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

"""

def subconjuntos(respuesta,pregunta):
    if len(pregunta)==0:
        print(respuesta)
    else:
        subconjuntos(respuesta+pregunta[0],pregunta[1:])
        subconjuntos(respuesta,pregunta[1:])

"Test"
subconjuntos("","abc")