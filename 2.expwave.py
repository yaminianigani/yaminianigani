import numpy as v
import matplotlib.pyplot as plt
n=v.arange(-10,10,0.1)
A=v.exp(n)
plt.plot(n,A)
plt.title("exponencial wave")
plt.xlabel("------->time")
plt.ylabel("----------->amplitude")
plt.show( )