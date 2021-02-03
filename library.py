import math
import random
import time
import matplotlib.pyplot as plt

def randomwalk(iterations, steps):
    random.seed(None)
    dis = 0
    X = []
    Y = []
    sumdis = 0
    for j in range(0, iterations):
        X = []
        Y = []
        x = 0.0
        y = 0.0
        dis = 0.0
        X.append(x)
        Y.append(y)

        for i in range(0, steps):
            theta = 2 * math.pi * random.random()
            x += math.cos(theta)
            y += math.sin(theta)
            X.append(x)
            Y.append(y)
        X.append(X)
        Y.append(Y)
        dis = x ** 2 + y ** 2
        sumdis += dis
    rms = math.sqrt(sumdis / iterations)
    sumx = 0
    sumy = 0
    for i in range(iterations):
        sumx += X[i][- 1]
        sumy += Y[i][- 1]
    avgx = sumx / iterations
    avgy = sumy / iterations
    radialdis = math.sqrt(avgx ** 2 + avgy ** 2)

    return X, Y, rms, avgx, avgy, radialdis




def montecarlovolume(x1, x2, y1, y2, z1, z2, f, N, analytical):
    X = []
    Y = []
    Z = []
    volbox = (x2 - x1) * (y2 - y1) * (z2 - z1)
    volcurve = 0
    j= 0
    for i in range(N):
        x = random.uniform(x1, x2)
        y = random.uniform(y1, y2)
        z = random.uniform(z1, z2)
        if (f(x, y, z) <= 1):
            X.append(x)
            Y.append(y)
            Z.append(z)
            j += 1
    volcurve = (volbox/float(N)) * j
    fracerror = abs(volcurve - analytical)/analytical
    return X, Y, Z, fracerror,volcurve
