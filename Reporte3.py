#!/usr/bin/python3

from statistics import stdev
from math import sqrt
from numpy import sin,pi

tensiones = [0.8, 1.5, 2.0, 2.8, 3.4, 4.0] # N
dt = stdev(tensiones) # desviación estándar

posiciones = [0.06, 0.11, 0.16, 0.21, 0.26, 0.31] # m
dx = stdev(posiciones) # desviación estándar

M = 0.0325 # kg
dM = 0.0001 # kg


m = 0.500 # kg
dm = 0.0001 # kg

L = 0.48 # m
dL = 0.001 # m

theta = 57*pi/180 # rad
dtheta = 1*pi/180 # rad

g = 9.8 # m/s^2

xArb = 0.36 # x arbitraria, en m
dxArb = dx # desviación estándar de las primeras 6 medidas de x, en m

# Tensión Teórica
Tteo = round(
        (M*g*xArb)/(L*sin(theta)) + (m*g)/(2*sin(theta)) # 3.206115849024259
, 1) # Se redondea para que tenga 1 decimal, ya que el error tiene dígitos hasta esta cantidad de decimales
dTteo = round(
        Tteo*(dM/M + dm/m + dL/L + dtheta/theta + dxArb/xArb) # 0.9065017945999381
, 1) # Se redondea para que tenga 1 decimal, ya que el error tiene dígitos hasta esta cantidad de decimales

print(f"Tensión teórica: ({Tteo} \u00b1 {dTteo}) N")



# Tensión Empírica, con K obtenido en qtiplot
K  = 13.026896828469
dK = 1.1927719981614

Temp = round(
        K*xArb # 4.68968285824884
, 0) # Se redondea para que tenga cero decimales ya que el error tiene dígitos desde las unidades
dTemp = round(
        Temp*(dK/K + dxArb/xArb) # 1.647952537962681
, 0) # Se redondea para que tenga cero decimales ya que el error tiene dígitos desde las unidades
print(f"Tensión empírica: ({Temp} \u00b1 {dTemp}) N")



# Tensión Experimental
Texp  = 4.4 # N
dTexp = 0.1 # N
print(f"Tensión experimental: ({Texp} \u00b1 {dTexp}) N")
