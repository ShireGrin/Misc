#!/usr/bin/python3

from math import sqrt
from statistics import stdev, mean
import numpy as np
import matplotlib.pyplot as plt
from lmfit import Model

# Distancias antes de caída libre, en m
d1  = [  0.2,   0.4,   0.6,   0.8]
dd1 = [0.001, 0.001, 0.001, 0.001]

corridas = [
    [1.27, 1.14, 1.37, 1.34, 1.46, 1.26, 1.19, 1.32, 1.34, 1.25], # 1
    [1.82, 1.81, 1.81, 1.88, 1.85, 1.82, 1.91, 1.94, 1.91, 1.91], # 2
    [2.44, 2.34, 2.31, 2.38, 2.50, 2.53, 2.41, 2.26, 2.46, 2.38], # 3
    [2.78, 2.78, 2.75, 2.95, 2.87, 2.73, 2.75, 2.75, 2.77, 2.83]  # 4
]

# Distancias luego de caer, en cm
d2 = [23.9, 24.2, 23.8, 23.7, 23.5, 23.8, 23.6, 23.8, 24.0, 23.7]

# Distancias luego de caer, en m
d2 = list(map(lambda x: x/100, d2)) # Conversión a metros

# Se obtiene la magnitud y la incerteza de la distancia en x luego de caer
# Se redondea hasta el tercer decimal debido a que la incerteza
# Solo tiene un dígito hasta el tercer decimal.
x = round(mean(d2), 3)
xerr = round(stdev(d2), 3)

# Listas que contendrán las magnitudes [medias] e incertezas [desviaciones]
# Para las 4 distancias antes de caer la esfera
t = list(map(lambda x: round(mean(x), 2), corridas))
dt = list(map(lambda x: round(stdev(x), 2), corridas))

print("Tiempos y longitudes en x [antes de caída]:")
for i in range(len(t)):
    print(f"Tiempo {i+1}: ({t[i]} \u00b1 {dt[i]}) s")
    print(f"Distancia {i+1}: ({d1[i]} \u00b1 {dd1[i]}) m\n")

print(f"Longitud Experimental x: ({x} \u00b1 {xerr}) m")


# Modelo de posición final que nos permitirá obtener a [como lo hace qtiplot]
def pos(x, a):
    return 0.5*a*(x**2)
# Guardamos el modelo cuadrático
cua = Model(pos)
# Realizamos el fit, para obtener a, con a que empieza en 4
res = cua.fit(d1, x=t, a=3)

# Guardamos los resultados del fit en 2 variables
# La magnitud y el error
a, da = round(res.params['a'].value, 3), round(res.params['a'].stderr, 3)

print(f"Aceleración en x: ({a} \u00b1 {da}) m/s^2")

# Velocidad final de x, con su error, al multiplicar el tiempo por la aceleración
# El tiempo será la media de la cuarta corrida
# El error la desviación, como se explicó antes
t4, dt4 = t[3], dt[3]
Vf, dVf  = round(t4*a, 2), round(a*t4*(dt4/t4 + da/a), 2)

print(f"Velocidad Final en x [para el tiempo 4]: ({Vf} \u00b1 {dVf}) m/s")

# Altura de la mesa al suelo
y = 98.1/100 # m
yerr = 0.001/100 # m

print(f"Altura de caída: ({y:.5f} \u00b1 {yerr:.5f}) m")

# Y con todo esto, y las ecuaciones escritas en el pizarrón por garrido
# Ya que tenemos la altura y,
# Podemos obtener la longitud en x [posición x de la esfera trás la caída] teóricamente
L = round(sqrt(2/9.8)*Vf*sqrt(y), 2)
Lerr = round(L*(dVf/Vf + yerr/(2*sqrt(y))), 2)

print(f"Longitud teórica x: ({L} \u00b1 {Lerr}) m")
