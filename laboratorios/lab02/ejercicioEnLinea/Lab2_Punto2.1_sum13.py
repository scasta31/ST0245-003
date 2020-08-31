import time
import random
import matplotlib.pyplot as plt

def sum13(n):
    suma=0 #Tn=C1=1
    for i in range(0,len(n)):
        if n[i]!=13:
            suma=suma+n[i] #Tn=C2*n, C2=6
    return suma #Tn=C3=1
#n=[1,2,13,2,1]
#print(sum13(n))

Tiempo = []
x=[]
for i in range(10000,1000000,45000):
    array = [random.randint(0, x) for x in range(i)]  
    start_time = time.time()
    sum13(array)
    Tiempo.append(time.time() - start_time)
    print(time.time() - start_time)
    x.append(i)

print(Tiempo)
plt.plot(x,Tiempo,'ro')
plt.ylabel('Tiempo')
plt.xlabel('Tamaño')