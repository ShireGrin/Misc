#!/usr/bin/python3

from math import sqrt
from statistics import stdev, mean
import numpy as np
import matplotlib.pyplot as plt
from lmfit import Model

# m
d1  = [  0.2,   0.4,   0.6,   0.8]
dd1 = [0.001, 0.001, 0.001, 0.001]

corridas = [
    [1.27, 1.14, 1.37, 1.34, 1.46, 1.26, 1.19, 1.32, 1.34, 1.25],
    [1.82, 1.81, 1.81, 1.88, 1.85, 1.82, 1.91, 1.94, 1.91, 1.91],
    [2.44, 2.34, 2.31, 2.38, 2.50, 2.53, 2.41, 2.26, 2.46, 2.38],
    [2.78, 2.78, 2.75, 2.95, 2.87, 2.73, 2.75, 2.75, 2.77, 2.83]
]

# cm
d2 = [23.9, 24.2, 23.8, 23.7, 23.5, 23.8, 23.6, 23.8, 24.0, 23.7]
#m
d2 = list(map(lambda x: round(x/100, 3), d2)) # Conversión a metros
x = mean(d2)
xerr = round(stdev(d2), 3)
#print(f"{x} +- {xerr}")

# cm
dd2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
#m
dd2 = list(map(lambda x: x/100, dd2)) # Conversión a metros

# s
t  = []
dt = []
for tiempos in corridas:
    media = round(mean(tiempos), 2)
    t.append(media)

    desviacion = round(stdev(tiempos), 2)
    dt.append(desviacion)

print("Tiempos y longitudes en x [antes de caída]:")
for i in range(len(t)):
    print(f"Tiempo {i+1}: ({t[i]} \u00b1 {dt[i]}) s")
    print(f"Distancia {i+1}: ({d1[i]} \u00b1 {dd1[i]}) m\n")

print(f"Longitud Experimental x: ({x} \u00b1 {xerr}) m")

def pos(x, a):
    return 0.5*a*(x**2)
cua = Model(pos)
res = cua.fit(d1, x=t, a=4)

a  = round(res.params['a'].value, 3)
da = round(res.params['a'].stderr, 3)

print(f"Aceleración en x: ({a} \u00b1 {da}) m/s^2")

Vf  = round(t[3]*a, 2)
dVf = round(a*t[3]*(dt[3]/t[3] + da/a), 2)

print(f"Velocidad Final en x [para el tiempo 4]: ({Vf} \u00b1 {dVf}) m/s")

ty = round(x/Vf, 2)
tyerr = round((x/Vf)*(dVf/Vf + xerr/x), 2)

print(f"Tiempo de caída: ({ty:.2f} \u00b1 {tyerr}) s")

y = round((0.5*9.8)*(ty**2), 2)
yerr = round(0.5*9.8*(ty**2)*(tyerr/ty + tyerr/ty), 2)

print(f"Altura de caída: ({y} \u00b1 {yerr}) m")

L = round(sqrt(2/9.8)*Vf*sqrt(y), 2)
Lerr = round(L*(dVf/Vf + yerr/(2*sqrt(y))), 2)

print(f"Longitud teórica x: ({L} \u00b1 {Lerr}) m")

