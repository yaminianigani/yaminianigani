import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
f=20
fs=9000
t=np.linspace(0,1,1000)
x=np.signal((2*np.pi*f*t)/fs)
p=np.random.rand(0,x.shape[0])
v=x+p
y=[]
for i in range(0,v.shape[0])
	y=np.append(y,np.sum(v[i:i+p]/p))
plt.subplot(411)
plt.plot(x)
plt.plot(412)
plt.plot(p)
plt.plot(413)
plt.plot(v)
plt.plot(414)
plt.plot(y)
plt.show( )
