import numpy as np
import matplotlib.pyplot as plt

N=1000
gamma=1
dt=0.1
N_p=1001
X1=[]
X10=[]
X30=[]
X100=[]
X1000=[]


x=np.zeros(1001)
y=np.zeros(1001)

for i in range(0,N-1,1):
    
    U1 = np.random.uniform(size=10000)
    U2 = np.random.uniform(size=10000)

    R = np.sqrt(-2 * np.log(U1))
    Theta = 2 * np.pi * U2

    A = R * np.cos(Theta)
    B = R * np.sin(Theta) 
   
    x[0] = 0
    y[0] = 0
    
    
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
        
    X1=np.append(X1, x[1])
    X10=np.append(X10, x[10])
    X30=np.append(X30, x[30])
    X100=np.append(X100, x[100])
    X1000=np.append(X1000, x[1000])
    
    
plt.hist(X1, bins=50, density=True)
plt.xlim([-30, 30])
plt.ylim([0, 1])
plt.xlabel("x")
plt.ylabel("P(x)")
plt.legend(['single element']) 
plt.hist(X10, bins=50, density=True)
plt.hist(X30, bins=50, density=True)
plt.hist(X100, bins=50, density=True)
plt.hist(X1000, bins=50, density=True)
plt.legend(['t=1', 't=10', 't=30', 't=100', 't=1000']) 
plt.show()
        
    