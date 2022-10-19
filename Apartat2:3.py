import numpy as np
import matplotlib.pyplot as plt


#apartat 1


U1 = np.random.uniform(size=10000)
U2 = np.random.uniform(size=10000)

R = np.sqrt(-2 * np.log(U1))
Theta = 2 * np.pi * U2

A = R * np.cos(Theta)
B = R * np.sin(Theta)


plt.hist(A, bins=50, density=True)
plt.xlabel("x")
plt.ylabel("P(x)")
plt.show()
plt.hist(A, bins=50, density=True, log=True)
plt.xlabel("x")
plt.ylabel("ln(P(x)")
plt.show()

mean=np.mean(A)
var=np.var(A)
print(mean)
print(var)


#apartat 2

gamma=1
dt=0.1
T_t=10
N_p=int(T_t/dt)

x=np.zeros(100)
y=np.zeros(100)

for i in range(0,N_p-1,1):
    
    x[i+1]=np.sqrt(2*gamma*dt)*A[i]+x[i]
    y[i+1]=np.sqrt(2*gamma*dt)*B[i]+y[i]
    
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)
       
         
    

    
    


    