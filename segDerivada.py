#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 13:23:35 2021

@author: dr.guillermo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 10:52:09 2021

@author: dr.guillermo
"""

# segunda Derivada numérica 
import numpy as np
import matplotlib.pyplot as plt

#definimos la función 
def f(x):
    return(3*x**3 + 2*x**2 + 5*x + 1)

# definimos el número de datos
N=101
#N=101
#definimos el intervalo
a=-2
b=2

#definimos el vector x que va de a-->b con N elementos
x = np.linspace(a,b,N)

# calculamos el intervalo delta x o h 
dx=(b-a)/(N-1) # n-1, ya que si tenemos 5 datos tenemos 4 subintervalos

#evaluamos los datos
y=f(x)

#graficamos
plt.plot(x,y,'g-')
plt.title('Cúbica')
plt.show()
# al derivar uan función cúbica debemos obtener una parabóla

# Inicializamos ydoble p (2a derivada) con tanto ceros como x 
ypp=np.zeros_like(x)

# ciclo iterativo
# con 3 terminos
for i in range(N):
    if i==0:  # es el primer dato va derivada hacia adelante
        ypp[i]=(y[i+2]-2*y[i+1]+y[i])/dx**2
    elif i==N-1: # es el ultimo dato, derivada hacia atras
        ypp[i]=(y[i]-2*y[i-1]+y[i-2])/dx**2
    else: # para los demás datos es derivada central
        ypp[i]=(y[i+1]-2*y[i]+y[i-1])/dx**2
        
# opcional obtenemos primera derivada exacta para comparar los resultados      
def fp(x):
    return(9*x**2 + 4*x + 5)

# opcional obtenemos segunda derivada exacta para comparar los resultados
# debe ser una recta      
def fpp(x):
    return(18*x + 4)
#gráficamos ambas 
plt.plot(x,fpp(x),'g-') # rayas verdes analitica
plt.plot(x,ypp,'bo')    # puntos azules aproximada
plt.show()
