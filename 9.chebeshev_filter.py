import numpy as np
from matplotlib import pyplot as plt
dp=0.8
ds=0.2
wp=2*np.pi*4000
ws=2*np.pi*5000
def chebyshev(dp,ds,wp,ws):
    a=(1.0/(dp**2))-1
    b=(1.0/(ds**2))-1
    eps=np.sqrt(a)
    N=int(np.ceil(np.arccosh(np.sqrt(b/a))/np.arccosh(ws/wp)))
    return N,eps
Nc,eps=chebyshev(dp,ds,wp,ws)
print(Nc,eps)
Hc=[]
for w in range(10000):
  if(2*np.pi*w<wp):
    mag=1.0/np.sqrt(1+(eps*(np.cos(Nc*np.arccos(2*np.pi*w/wp))))**2)
    Hc=np.append(Hc,mag)
  else:
    mag1=1.0/np.sqrt(1+(eps*(np.cosh(Nc*np.arccosh(2*np.pi*w/wp))))**2)
    Hc=np.append(Hc,mag1)

print(Hc.shape)
a2=plt.subplot(212,sharex=a1)
a2.plot(Hc)
#a2.plot(20*np.log10(Hc))
#a2.plot(np.log10(W),20*np.log10(Hc))
plt.ylabel('magitude/gain')
plt.xlabel('frequency in Hz')
plt.title('Chebyshev Analog Filter')
plt.show()
