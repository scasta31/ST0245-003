import time
import random
import matplotlib.pyplot as plt

def sum28(n):
    boolean=False
    suma=0 #Tn=C1=2
    for i in range(0,len(n)):
        if n[i]==2:
            suma=suma+n[i] #Tn=C2*n, C2=6
    if suma==8:
        boolean=True #Tn=C3=3
    return boolean #Tn=C4=1
#n=[1,2,13,2,1,2,2,2]
#print(sum28(n))

Tiempo = []
x=[]
for i in range(10000,1000000,45000):
    array = [random.randint(0, x) for x in range(i)]  
    start_time = time.time()
    sum28(array)
    Tiempo.append(time.time() - start_time)
    print(time.time() - start_time)
    x.append(i)

print(Tiempo)
plt.plot(x,Tiempo,'ro')
plt.ylabel('Tiempo')
plt.xlabel('Tamaño')