import numpy as np
import matplotlib.pyplot as plt

N=1000
gamma=1
dt=0.1
T_t=10
N_p=int(T_t/dt)
X_inicial=[]
X_final=[]
Y_inicial=[]
Y_final=[]

x=np.zeros(100)
y=np.zeros(100)

for i in range(0,N-1,1):
    
    U1 = np.random.uniform(size=10000)
    U2 = np.random.uniform(size=10000)

    R = np.sqrt(-2 * np.log(U1))
    Theta = 2 * np.pi * U2

    A = R * np.cos(Theta)
    B = R * np.sin(Theta)
    
    x[0] = np.random.uniform(-50,50)
    y[0] = np.random.uniform(-50,50)
    
    X_inicial.append(x[0])
    Y_inicial.append(y[0])
    
    
    for i in range(0,N_p-1,1):
        
        x[i+1]=np.sqrt(2*gamma*dt)*A[i]+x[i]
        y[i+1]=np.sqrt(2*gamma*dt)*B[i]+y[i]
        
        if x[i+1]>50:
            x[i+1]=x[i+1]-100
            
        if x[i+1]<-50:
            x[i+1]=x[i+1]+100
            
        if y[i+1]>50:
            y[i+1]=y[i+1]-100
            
        if y[i+1]<-50:
            y[i+1]=y[i+1]+100
    
            
    X_final.append(x[99])
    Y_final.append(y[99])
            
    
        
plt.xlim([-50, 50])
plt.ylim([-50, 50])
plt.xlabel("x")
plt.ylabel("y")
plt.plot(X_inicial,Y_inicial, 'o', color="blue", markersize=5)
plt.show()

plt.xlim([-50, 50])
plt.ylim([-50, 50])
plt.xlabel("x")
plt.ylabel("y")
plt.plot(X_final,Y_final, 'ro', markersize=5)
plt.show()


    
    
    

