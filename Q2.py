import matplotlib.pyplot as plt
import library as lib
n = []
V = []
error = []
anavol = 12.56637#Analytical volume
a=1#dimensions of the ellipsoid
b=1.5
c=2
def elip(x,y,z):#equation of the ellipsoid
    return ((x**2)/(a**2))+((y**2)/(b**2))+((z**2)/(c**2))
N = 45000
i = 0
while i < N:
    i +=100
    X1, Y1, Z1, err, vol  = lib.montecarlovolume(-a,a,-b,b,-c,c,elip,i, anavol)
    n.append(i)
    V.append(vol)
    error.append(err)
print("**************************************************************************************************************")
print("The volume of the ellipsoid obtained from montecarlo method is",vol,"and the fractional error in the estimation is ",err)
print("**************************************************************************************************************")

plt.figure()
plt.plot(n, V)
plt.axhline(12.56637, color='r')

plt.text(30000, 12.6, "Analytical value = 12.56637", size=16,
         va="baseline", ha="left", multialignment="left")
plt.title("Estimated volume of an ellipsoid vs number of points")
plt.xlabel("Number of points")
plt.ylabel("Volume of ellipsoid")

plt.figure()
plt.plot(n,error)

plt.title("Fractional error as a function of number of points")
plt.xlabel("No. of points")
plt.ylabel("Fractional Error")
plt.show()


X, Y, Z, f, V = lib.montecarlovolume(-a,a,-b,b,-c,c,elip,10000, anavol)
fig = plt.figure (figsize = (16, 9)) 
ax = plt.axes (projection = "3d") 
ax.scatter3D (X, Y, Z, color = "green") 
plt.title ("3D scatter plot of ellipsoid for N=10,000") 
plt.show ()

'''
**************************************************************************************************************
The volume of the ellipsoid obtained from montecarlo method is 12.585066666666668 and the fractional error in the estimation is  0.0014878335324098213
**************************************************************************************************************'''