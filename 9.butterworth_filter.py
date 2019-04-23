import numpy as np
from matplotlib import pyplot as plt
dp=0.8
ds=0.2
wp=2*np.pi*4000
ws=2*np.pi*5000
def butterworth(dp,ds,wp,ws):
    a=(1.0/(dp**2))-1
    b=(1.0/(ds**2))-1
    N=int(np.ceil(0.5*np.log10(a/b)/np.log10(wp/ws)))
    wc=wp/(a**(1.0/(2.0*N)))
    return N,wc
Nb,wc=butterworth(dp,ds,wp,ws)
print(Nb,wp,wc,ws)
W=2*np.pi*np.asarray(range(10000),'float32')
Hb=[]
for w in range(10000):
    mag=1.0/np.sqrt(1+((2*np.pi*w/wc)**(2.0*Nb)))
    Hb=np.append(Hb,mag)
print(Hb.shape)

a1=plt.subplot(211)
a1.plot(Hb)
#a1.plot(20*np.log10(Hb))
#a1.plot(np.log10(W),20*np.log10(Hb))
plt.ylabel('magitude/gain')
plt.title('Butterworth Analog Filter')
