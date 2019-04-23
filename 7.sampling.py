import numpy as np
import matplotlib.pyplot as plt
f=int(input("f:"))
fs=int(input("fs:"))
f=f*1.0
fs=fs*1.0
print (f/fs)
t=np.linspace(0,0.01,100)
n=np.linspace(0,12,12)
y=np.sin(2*np.pi*f*t)
plt.plot(t,y)
plt.show();
k=np.sin(2*np.pi*(f/fs)*n)
plt.stem(n,k)
plt.show();
