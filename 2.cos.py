import numpy as v
import matplotlib.pyplot as plt
n=v.arange(-10,10,0.1)
A=v.cos(n)
plt.plot(n,A)
plt.title("cos wave")
plt.xlabel("------->time")
plt.ylabel("----------->amplitude")
plt.show( )