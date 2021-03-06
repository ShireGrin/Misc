#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

# La siguiente función, recibe 3 argumentos obligatorios, y uno opcional
# f será la función que se integrará
# a será el límite inferior
# b será el límite superior
# N por defecto será 40, pero se puede cambiar para dividir el área bajo la curva en N divisiones, como se desee.
def trap(f, a, b, N=40):
    dx = (b-a)/N
    x = np.linspace(a, b, N+1)
    y = f(x)
    x1 = np.linspace(a, b, 200)
    y1 = f(x1)
    plt.plot(x1, y1,color=(1, 0, 0, 1))
    plt.plot(x, y)
    plt.xlim([a, b]); plt.ylim([y1[-1], y1[0]])
    for i in range(0, len(x)-1):
        plt.fill_between([x[i],x[i+1]],[y[i],y[i+1]], edgecolor=(1, 1, 1, 1), facecolor=(245./255, 188./255, 35./255, 1))
    y_izquierda = y[1:]
    y_derecha = y[:-1]
    SumaTrapezoidal = (dx/2)*np.sum(y_izquierda + y_derecha)
    plt.suptitle("Suma Trapezoidal: {}".format(str(SumaTrapezoidal)))
    plt.show()
    return SumaTrapezoidal

# La siguiente función, recibe 3 argumentos obligatorios, y uno opcional
# f será la función que se integrará
# a será el límite inferior
# b será el límite superior
# N por defecto será 18, pero se puede cambiar para dividir el área bajo la curva en N divisiones, como se desee.
def simps(f, a, b, N=18):
    if(N % 2 == 1):
        raise ValueError("N debe ser un entero par.")
    dx = (b - a)/N
    x = np.linspace(a, b, N+1)
    y = f(x)
    x1 = np.linspace(a, b, 1000)
    y1 = f(x1)
    plt.plot(x1, y1, color=(0, 0, 1, 1))
    plt.xlim([a, b]); plt.ylim([y1[0], y1[-1]+2.5*dx])
    for i in range(0, len(x)-1):
        plt.fill_between([x[i],x[i+1]],[y[i],y[i+1]], edgecolor=(1, 1, 1, 1), facecolor=(245./255, 188./255, 35./255, 1))
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    plt.suptitle("Sumatoria con regla de Simpson: {}".format(str(S)))
    plt.show()
    return S

# Se llama a la función, con la función que se pide en el proyecto, de cero a pi.
simps(lambda x : (np.sin(x))/(1+x), 0, np.pi)

# Se llama a la función, con la función que se pide en el proyecto, de cero a uno.
trap(lambda x : 1/(x**2+x+1), 0, 1)
