import time
import random
import matplotlib.pyplot as plt

def bigDiff(n):
    maxi=n[0]
    mini=n[0] #Tn=C1=2
    if len(n)==0:
        maxi=0
        mini=0 #Tn=C2=5
    else:
        for i in range(0,len(n)):
            if maxi<n[i]:
                maxi=n[i]
            if mini>n[i]:
                mini=n[i]# Tn=C3*n, C3=8
    return maxi-mini #Tn=C4=2
#n=[10,11,5,6]
#print(bigDiff(n))


Tiempo = []
x=[]
for i in range(10000,1000000,45000):
    array = [random.randint(0, x) for x in range(i)]  
    start_time = time.time()
    bigDiff(array)
    Tiempo.append(time.time() - start_time)
    print(time.time() - start_time)
    x.append(i)

print(Tiempo)
plt.plot(x,Tiempo,'ro')
plt.ylabel('Tiempo')
plt.xlabel('Tamaño')
