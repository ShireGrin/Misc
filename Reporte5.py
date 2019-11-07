#!/usr/bin/python3

from statistics import stdev, mean
import numpy as np

# Parte 1
m1 = 45.2/1000 # kg
m2 = 30.1/1000 # kg
dm = 0.1e-3 # kg

theta = np.pi/6 # 30°

mus = (m2 - m1*np.sin(theta))/(m1*np.cos(theta))
dmus = (mus)*((dm)/(m1) + (dm)/(m2))

print(f"Coeficiente de fricción estático: ({round(mus, 3)} \u00b1 {round(dmus, 3)})")


# Parte 2

m1 = 45.2/1000 # kg
m2 = 37.5/1000 # kg
dm = 0.1e-3 # kg

g = 9.8 # m/s^2

alturas = [
    0.885,
    0.883,
    0.884,
    0.883,
    0.882,
    0.885,
    0.881
]
h = mean(alturas)
dh = 1e-3 # m

print(f"Altura: ({round(h, 3)} \u00b1 {round(dh, 3)}) m")

tiempos = [
    2.25,
    2.06,
    2.01,
    2.28,
    2.12,
    2.38,
    2.21,
]
t = mean(tiempos)
dt = stdev(tiempos)

print(f"Tiempo: ({round(t, 1)} {round(dt, 1)}) s")

a = 2*h/(t**2)
da = a*((dh)/(h) + (2*dt)/(t))

print(f"Aceleración: ({round(a, 2)} \u00b1 {round(da, 2)}) m/s^2")

muk = ((m2)*(g) - (m1)*(g)*np.sin(theta) - (a)*(m1 + m2))/(m1*g*np.cos(theta))
dmuk = muk*((dm)/(m1) + (dm)/(m2) + (da)/(a))

print(f"Coeficiente de fricción cinético: ({round(muk, 2)} \u00b1 {round(dmuk, 2)})")
