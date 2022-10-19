import numpy as np
import matplotlib.pyplot as plt

N=1000
dt=0.1
T_t=100
N_p=int(T_t/dt)
X_inicial=[]
X_final=[]
Y_inicial=[]
Y_final=[]
D_list=[]
Gamma=[0.1,1,3,10,30,100,1000]
MSD_list=[]

x=np.zeros(N_p)
y=np.zeros(N_p)

for z in range(0,len(Gamma)):
    
    X_inicial=[]
    X_final=[]
    Y_inicial=[]
    Y_final=[]

    for i in range(0,N_p-1,1):

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

            x[i+1]=np.sqrt(2*Gamma[z]*dt)*A[i]+x[i]
            y[i+1]=np.sqrt(2*Gamma[z]*dt)*B[i]+y[i]

        X_final.append(x[99])
        Y_final.append(y[99])


    X_MSD= [e1 - e2 for e1, e2 in zip(X_final,X_inicial)]

    Y_MSD= [e1 - e2 for e1, e2 in zip(Y_final,Y_inicial)]

    r2=np.zeros(len(X_MSD))

    for i in range(0,len(X_MSD),1):

        r2[i]=X_MSD[i]**2+Y_MSD[i]**2
    
    P=sum(r2)
    
    MSD=1/N*P
    
    MSD_list.append(MSD)

    D=MSD/(4*T_t)
    D_list.append(D)



print(MSD_list)

plt.scatter(D_list,Gamma)
plt.yscale('log')
plt.xscale('log')
plt.xlabel("ln $\Gamma$")
plt.ylabel("ln D")
plt.plot(D_list,Gamma)


    
    