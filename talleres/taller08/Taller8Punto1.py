"""
Taller 8
Estructura de datos y algoritmos
Sebastian Castaño 201610054014
Dennis Castrillon 201610035014

"""

def esUnNumero(c):
  try:
    float(c)
    return True
  except(TypeError,ValueError):
    return False

def notacionPolaca(s):
    pila = []
    for c in s:
        if esUnNumero(c):
            pila.append(int(c))
        else: #Es un operador
            numeroArriba = pila.pop()
            numeroAbajo =  pila.pop()
            resultado = 0
            if (c == "+"):
                resultado = numeroArriba + numeroAbajo
            if (c == "-"): #arriba - abajo? abajo - arriba?
                resultado = numeroAbajo - numeroArriba
            if (c == "*"): #arriba - abajo? abajo - arriba?
                resultado = numeroAbajo * numeroArriba
            if (c == "/"): #arriba - abajo? abajo - arriba?
                resultado = numeroAbajo / numeroArriba                
            pila.append(resultado)
    return pila.pop()

 
print(notacionPolaca("23+5*"))