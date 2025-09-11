import numpy as np
import matplotlib.pyplot as plt
fs=1000
t=np.arange(0,1,1/fs)
s1=np.sin(2*np.pi*5*t)
s2=np.sin(2*np.pi*5*(t-0.1))
plt.plot(t,s1) #original
plt.plot(t,s2) #shifted
plt.show()
