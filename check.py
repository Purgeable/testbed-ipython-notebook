# -*- coding: utf-8 -*-
#%matplotlib inline
#In [2]:
    
#import numpy as np
#from quantecon import LinearStateSpace
#
#
#phi_0, phi_1, phi_2 = 1.1, 0.8, -0.8
#
#A = [[1,     0,     0],
#     [phi_0, phi_1, phi_2],
#     [0,     1,     0]]
#C = np.zeros((3, 1))
#G = [0, 1, 0]

#ar = LinearStateSpace(A, C, G, mu_0=np.ones(3))
#x, y = ar.simulate(ts_length=50)


#φ0 = 1.1, φ1 = 0.8, φ2 = −0.8, y0 = y−1 = 1
#yt+1 = φ0 + φ1yt + φ2yt−1



import numpy as np

N = 1000
y = [1] * N

def noise():
    return np.random.normal(loc=0.0, scale=1.0, size=1)     

for t in range(0,N-1):
    y[t+1] = 0.8 * y[t] - 0.8 * y[t-1] + noise()

#%matplotlib inline  
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8, 4.6))
ax.plot(y, 'b-', lw=2, alpha=0.7)
ax.grid()
ax.set_xlabel('time')
ax.set_ylabel(r'$y_t$', fontsize=16)
plt.show()