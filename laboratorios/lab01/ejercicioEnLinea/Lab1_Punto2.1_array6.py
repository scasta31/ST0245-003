"""
Estructura de datos y algoritmos 1
Laboratorio 1 Punto 2.1
Ejercicios Recursión 1 CodingBat

Sebastian Castaño Orozco 201610054014
Dennis Castrillón Sepúlveda 201610035014

Given an array of ints, compute recursively if the array contains a 6.
"""
def array6(array,initialposition):
    return internalarray(array,initialposition,0)

def internalarray(array,initialposition,suma):
    if len(array)==0:
        return (suma)
    else:
        if array[len(array)-1]==6:
            suma=suma+1
        return internalarray(array[initialposition:len(array)-1],initialposition,suma)
    

"Test"                 
print("El vector "+str([1,4])+" tiene "+str(array6([1,4],0))+" seis.")
print("El vector "+str([1,4,6])+" tiene "+str(array6([1,4,6],0))+" seis.")
print("El vector "+str([6,0,6,6,6])+" tiene "+str(array6([6,0,6,6,6],0))+" seis.")
print("El vector "+str([6,-1,-4,-6,6])+" tiene "+str(array6([6,-1,-4,-6,6],0))+" seis.")