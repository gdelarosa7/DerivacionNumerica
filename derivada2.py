#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 11:47:37 2021

@author: dr.guillermo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 10:52:09 2021

@author: dr.guillermo
"""

# Derivación
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return(3*x**3 + 2*x**2 + 5*x + 1)
N=100
a=-2
b=2

x = np.linspace(a,b,N)
dx=(b-a)/(N-1)

y=f(x)

#plt.plot(x,y,'g-')
#plt.show()

yp=np.zeros_like(x)

for i in range(N):
    if i==0:
        yp[i]=(y[i+1]-y[i])/dx
    elif i==N-1:
        yp[i]=(y[i]-y[i-1])/dx
    else:
        yp[i]=(y[i+1]-y[i-1])/(2*dx)
        
def fp(x):
    return(9*x**2 + 4*x + 5)

plt.plot(x,fp(x),'g-')
plt.plot(x,yp,'bo')
plt.show()

#observe como en azul en las orillas se pierde
# entones se resuleve tomando más datos 