import library as rands
import matplotlib.pyplot as plt
import math
figure, axes = plt.subplots(nrows=3, ncols=2)#define no. of rows and collumns
RMS = []
Nroot = []
l = 100# no. of iterations
N = 250# start from N=250
i=1
while (i<=5):
    print("************************************************************************************************************")
    print(" For Steps = "+str(N)+" and Number of walks = 5  ")
    print("************************************************************************************************************")
    X, Y, rms, avgx, avgy, radialdis = rands.randomwalk(l, N)

    print("The root mean square distance = ", rms)
    print("Average displacement in the x direction = ", avgx)
    print("Average displacement in the y direction = ", avgy)
    print("The Radial distance R = ", radialdis)

    RMS.append(rms)
    Nroot.append(math.sqrt(N))
    k=u=0
    if (i<3) : 
        u=0
        k=i-1
    elif(i==3 or i==4) : 
        u=1
        k=i-3
    else :
        u=2
        k=0
    for j in range(5):
        axes[u,k].set_xlabel('X')
        axes[u,k].set_ylabel('Y')
        axes[u,k].grid(True)
        axes[u,k].set_title("No. of steps = "+ str(N))
        axes[u,k].plot(X[j],Y[j])
    N +=250
    i+=1
plt.figure()
plt.title("RMS distance vs root of N plot for different number of steps starting from 250 ")
plt.ylabel('RMS distance')
plt.xlabel('squareroot of N')
plt.plot(Nroot, RMS)

plt.grid(True)
plt.show()
'''************************************************************************************************************
 For Steps = 250 and Number of walks = 5  
************************************************************************************************************
The root mean square distance =  15.629352039696183
Average displacement in the x direction =  2.880434476082775  
Average displacement in the y direction =  -1.2758385256133062
The Radial distance R =  3.1503439041548127
************************************************************************************************************
 For Steps = 500 and Number of walks = 5  
************************************************************************************************************
The root mean square distance =  22.76072031959625
Average displacement in the x direction =  0.7067189887553609
Average displacement in the y direction =  2.151122020124929
The Radial distance R =  2.2642388731169145
************************************************************************************************************
 For Steps = 750 and Number of walks = 5  
************************************************************************************************************
The root mean square distance =  26.504581980149055
Average displacement in the x direction =  1.2664351771738056
Average displacement in the y direction =  -0.349450693936544
The Radial distance R =  1.3137632379831536
************************************************************************************************************
 For Steps = 1000 and Number of walks = 5
************************************************************************************************************
The root mean square distance =  32.50692594653746
Average displacement in the x direction =  4.3253278465174425
Average displacement in the y direction =  -1.743836441343079
The Radial distance R =  4.663628041987837
************************************************************************************************************
 For Steps = 1250 and Number of walks = 5  
************************************************************************************************************
The root mean square distance =  33.981880998320044
Average displacement in the x direction =  -0.4284515473756484
Average displacement in the y direction =  1.4508808279631595
The Radial distance R =  1.5128205132796326'''
