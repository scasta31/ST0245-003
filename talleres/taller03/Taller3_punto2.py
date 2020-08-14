"""
Estructura de datos y algoritmos 1
Taller 3 Punto 2
Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

""" 
def permutation(pregunta):

     return permutations("", pregunta, pregunta)


def permutations(respuesta, pregunta, preguntaOriginal):
    if (len(respuesta) == len(preguntaOriginal)):
        print(respuesta)
        

    else:
        for i in range(0,len(pregunta)):
            permutations(respuesta+pregunta[i] , pregunta[0:i]+pregunta[i+1:] , preguntaOriginal)



permutation("abcd")