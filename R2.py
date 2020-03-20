#!/usr/bin/python3

from statistics import mean, stdev
from math import sqrt, pi

## Tiempos para n vueltas

t0 = 0

# tiempo para 1 vuelta
listat1 = [0.77, 0.86, 0.64, 0.77, 0.48]
t1 = mean(listat1)
dt1 = stdev(listat1)

# tiempo para 2 vueltas...
listat2 = [0.99, 0.96, 0.93, 0.99, 0.99]
t2 = mean(listat2)
dt2 = stdev(listat2)

# tiempo para 3 vueltas...
listat3 = [1.18, 1.27, 1.42, 1.27, 1.31]
t3 = mean(listat3)
dt3 = stdev(listat3)

# tiempo para 4 vueltas...
listat4 = [1.56, 1.64, 1.71, 1.77, 1.52]
t4 = mean(listat4)
dt4 = stdev(listat4)

# tiempo para 5 vueltas...
listat5 = [1.89, 1.84, 1.80, 1.74, 1.89]
t5 = mean(listat5)
dt5 = stdev(listat5)

# tiempo para 6 vueltas...
listat6 = [1.92, 1.89, 1.80, 1.93, 2.01]
t6 = mean(listat6)
dt6 = stdev(listat6)

# Tiempos:
tiempos = [t1, t2, t3, t4, t5, t6]
dtiempos = [dt1, dt2, dt3, dt4, dt5, dt6]

for t, dt in zip(tiempos, dtiempos):
    print(f"({round(t, 2)} \u00b1 {round(dt, 2)}) s")
print()

theta0 = 0
theta1 = 2*pi
theta2 = 4*pi
theta3 = 6*pi
theta4 = 8*pi
theta5 = 10*pi
theta6 = 12*pi

w1 = (theta2 - theta0)/(t2 - t0)
w2 = (theta3 - theta1)/(t3 - t1)
w3 = (theta4 - theta2)/(t4 - t2)
w4 = (theta5 - theta3)/(t5 - t3)
w5 = (theta6 - theta4)/(t6 - t4)

velAngulares = [w1, w2, w3, w4, w5]

for i in range(1, 6):
    print(f"w{i}: {velAngulares[i-1]} rad/s^2")
print()

alpha = 22
dalpha = 2
print(f"alpha: ({alpha} \u00b1 {dalpha}) rad/s^2")
print()

w6 = alpha*t6
dw6 = w6*(dalpha/alpha + dt6/t6)
print(f"w6: ({w6} \u00b1 {dw6}) rad/s")
print()

# altura de la mesa a debajo de la tabla
h = 2 # cm
dh = 0.1

# masa de la esfera
m = 40.0 # g
dm = 0.1 # g

# gravedad
g = 980 # cm/s^2

# diámetro esfera
d = 2.2 # cm
dd = 0.005 # cm

r = d/2 # cm
dr = dd/2 # cm

Vcm = w6*r
dVcm = Vcm*(dw6/w6 + dr/r)
print(f"Vcm: ({Vcm} \u00b1 {dVcm}) cm/s")
print()

Iexp = ((2*g*h)/(Vcm**2) - 1)*m*(r**2)
dIexp = Iexp*((2*dVcm)/Vcm + dm/m + (2*dr)/r)
print(f"Iexp: ({Iexp} \u00b1 {dIexp}) g*cm^2")
print()

Iteo = (2/5)*m*(r**2)
dIteo = Iteo*(dm/m + (2*dr)/r)
print(f"Iteo: ({Iteo} \u00b1 {dIteo}) g*cm^2")
print()
