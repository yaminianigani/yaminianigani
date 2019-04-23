import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('wav')
print(fs,len(data),data)
t=np.arange(0,len(data)/fs,1.0/fs)
plt.subplot(211)
plt.plot(data)
plt.subplot(212)
plt.plot(t,data)
plt.show( )
wav.write('wav1',2*fs,data)
