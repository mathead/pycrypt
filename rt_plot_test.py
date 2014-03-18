import time
import numpy as np
import matplotlib.pyplot as plt
import math

fig=plt.figure()
plt.axis([0,100,-1,1])

i=0
x=list()
y=list()

plt.ion()
plt.show()

while i <1000:
    temp_y=math.sin(i/10.0)
    x.append(i)
    y.append(temp_y)
    plt.scatter(i,temp_y)
    i+=1
    plt.draw()