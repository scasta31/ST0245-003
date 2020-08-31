import time
import random
import matplotlib.pyplot as plt

def lucky13(n):
    comp=True #Tn=C1=1
    for i in range(0,len(n)):  
        comp=comp and n[i]!=13 and n[i]!=1 #Tn=C2*n, C2=7
    return comp #Tn=C3=1
#n=[1,2,4]
#print(lucky13(n))


Tiempo = []
x=[]
for i in range(10000,1000000,45000):
    array = [random.randint(0, x) for x in range(i)]  
    start_time = time.time()
    lucky13(array)
    Tiempo.append(time.time() - start_time)
    print(time.time() - start_time)
    x.append(i)

print(Tiempo)
plt.plot(x,Tiempo,'ro')
plt.ylabel('Tiempo')
plt.xlabel('Tamaño')


