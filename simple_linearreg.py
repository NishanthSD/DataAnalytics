import numpy as np
from random import *
import matplotlib.pyplot as plt

def simple_linregressor(x,y):
    mx = np.mean(x)
    my = np.mean(y)

    Sxy = [(i - mx)*(j - my) for i,j in zip(x,y)]
    Sxx = [(i - mx)*(i - mx) for i in x]

    sxy = np.sum(Sxy)
    sxx = np.sum(Sxx)

    b1 = sxy/sxx
    b0 = my - b1*mx

    return [b0,b1]

if __name__ == "__main__":
    y = [i*4 + 3 + randint(-4,6)*random() for i in range(20)]
    x = [i for i in range(20)]

    b0,b1 = simple_linregressor(x,y)
    ynew = [b0 + i*b1 for i in x]
    plt.scatter(x,y,color = "g")
    plt.plot(x,ynew,color = "r")
    plt.show()