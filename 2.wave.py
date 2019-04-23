import numpy as np
import matplotlib.pyplot as plt
f=int(input("enter the frequency"))
fs=int(input("enter the frequency"))
x=np.arange(-10,10,0.01)
a=np.sin((2*np.pi*f*x)/fs)
b=np.cos((2*np.pi*f*x)/fs)
plt.subplot(311)
plt.plot(x,a)
plt.title("sin")
plt.subplot(312)
plt.plot(x,b)
plt.title("cos")
c=a+b
plt.subplot(313)
plt.plot(x,c)
plt.show( )
