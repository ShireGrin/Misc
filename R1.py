#!/usr/bin/python3

from statistics import mean, stdev
from math import sqrt

# tiempos en s
t1 = [2.83, 2.70, 2.73, 2.68, 2.77] # Lista de datos para la corrida de 1 vuelta, osea 2pi radianes
t1barra = mean(t1) # Media aritmética de la lista t1
dt1 = stdev(t1) # Error (desviación estándar) para la lista t1

t2 = [4.83, 4.18, 3.96, 4.11, 4.14]
t2barra = mean(t2)
dt2 = stdev(t2)

t3 = [5.83, 5.26, 5.52, 5.59, 5.71]
t3barra = mean(t3)
dt3 = stdev(t3)

t4 = [6.83, 6.27, 6.30, 6.62, 6.95]
t4barra = mean(t4)
dt4 = stdev(t4)

t5 = [7.83, 7.49, 7.92, 8.15, 8.30]
t5barra = mean(t5)
dt5 = stdev(t5)

tiempos  = [t1barra, t2barra, t3barra, t4barra, t5barra] # lista que contiene todos los tiempos promedios
dtiempos = [dt1, dt2, dt3, dt4, dt5] # lista con los errores de los tiempos promedios

# El búcle informará las medias de los tiempos con su error para su respectiva cantidad de vueltas
for i in range(5):
    print(f"({round(tiempos[i], 2)} \u00B1 {round(dtiempos[i], 2)}) s para {i + 1} vuelta/s del disco.")
print()

# Al hacer el fit polinomial en qtiplot, se obtiene la aceleración angular con su error
alpha = 0.17
dalpha = 0.01

# Tiempo en recorrer la altura h
t  = [6.06, 6.03, 5.82, 6.72, 6.09] # Lista de las 5 corridas
tbarra = mean(t) # Media áritmética
dt = stdev(t) # Error (desviación estándar)

print(f"Tiempo promedio que tarda la masa antes de llegar a la mesa: ({round(tbarra, 2)} \u00B1 {round(dt, 2)}) s")

h  = 64.0 # Altura que recorre la masa hasta llegar a la mesa, en cm
dh = 0.1 # Error de la altura

a = (2*h)/(tbarra**2) # Aceleración Lineal en cm/s
da = a*((dh)/(h) + (2*dt)/(tbarra)) # Error de la Aceleración Lineal con ecuación proporcionada en clase

print(f"Aceleración Lineal: ({round(a, 2)} \u00b1 {round(da, 2)}) m/s^2")

R1 = a/alpha # Radio obtenido por medio de la aceleración lineal dividida la aceleración angular
dR1 = R1*(da/a + dalpha/alpha) # Error del radio

print(f"R1: ({round(R1, 2)} \u00b1 {round(dR1, 2)}) cm")

R2 = 3.8 # Radio del disco, en cm
dR2 = 0.003 # Error del radio del disco, medido con el vernier

print(f"R2: ({3.8} \u00b1 {0.003}) cm")
