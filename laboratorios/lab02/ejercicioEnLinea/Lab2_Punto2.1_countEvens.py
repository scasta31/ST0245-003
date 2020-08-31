import time
import random
import matplotlib.pyplot as plt

def contarPares(n):
    cont=0 #C1=1
    for i in range(0,len(n)):
        if n[i]%2==0:
            cont=cont+1 #Tn=C2*n, C2=6
    return cont #Tn=C3=1

#n=[31,4,5,6,8,7,10]
#print(contarPares(n))

Tiempo = []
x=[]
for i in range(10000,1000000,45000):
    array = [random.randint(0, x) for x in range(i)]  
    start_time = time.time()
    contarPares(array)
    Tiempo.append(time.time() - start_time)
    print(time.time() - start_time)
    x.append(i)

print(Tiempo)
plt.plot(x,Tiempo,'ro')
plt.ylabel('Tiempo')
plt.xlabel('Tamaño')
