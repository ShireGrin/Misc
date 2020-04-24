#!/usr/bin/python3

from numpy import pi

dia_hilo = 0.25/1000.0 # en m
l_hilo = 110/100.0 # en m

area_transversal = pi*dia_hilo**2/4 # en m^2
g = 9.8 # m/s^2



longitudes_iniciales = [0.865 , 0.865 , 0.865 , 0.865 , 0.865 , 0.865 , 0.865 ] # m
longitudes_finales   = [0.910 , 0.930 , 0.950 , 0.980 , 1.000 , 1.010 , 1.025 ] # m
masas                = [0.1793, 0.3293, 0.4803, 0.6083, 0.8063, 1.0063, 1.2030] # kg


delta_longitudes = [] # m
for i in range(7): # Número de longitudes
    lfinal = longitudes_finales[i]     # Obtenemos la iésima longitud final
    linicial = longitudes_iniciales[i] # Obtenemos la iésima longitud inicial

    delta_l = round(lfinal - linicial, 5) # Obtenemos la diferencia entre las longitudes
    delta_longitudes.append(delta_l) # Agregamos la diferencia a la lista de diferencias


tensiones = [] # N
for i in range(7):
    masa = masas[i] # Obtenemos la iésima masa
    tension = round(masa*g, 5) # Multiplicamos por la gravedad para obtener la fuerza o tensión afectando al hilo, en Newtons
    tensiones.append(tension)
delta_tensiones = 7*[0.0001*9.8] # Una lista con 7 elementos iguales a 0.0001*9.8, igual a delta de la masa, por gravedad


esfuerzos = [] # kg/(s^2*m)
for i in range(7):
    fuerza = tensiones[i] # Se obtiene la iésima fuerza
    esfuerzo = round(fuerza/area_transversal, 5) # Dividimos la fuerza por el área transversal para obtener el esfuerzo
    esfuerzos.append(esfuerzo) # Guardamos el esfuerzo en la lista
delta_esfuerzos = []
for i in range(7):
    esfuerzo = esfuerzos[i]
    delta_tension = delta_tensiones[i]
    tension = tensiones[i]
    delta_esfuerzo = esfuerzo*(delta_tension/tension)
    delta_esfuerzos.append(delta_esfuerzo)


deformaciones = [] # Adimensional
for i in range(7):
    delta_l = delta_longitudes[i] # Obtenemos el iésimo delta
    longitud_inicial = longitudes_iniciales[i] # Obtenemos la iésima longitud inicial (constante, todas son 0.865 m)
    deformacion = round(delta_l/longitud_inicial, 5) # Se calcula la deformación
    deformaciones.append(deformacion) # Se agrega la deformación a la lista
delta_deformaciones = []
for i in range(7):
    deformacion = deformaciones[i]
    longitud_inicial = longitudes_iniciales[i]
    longitud_final = longitudes_finales[i]
    delta_longitud_inicial = 0.001
    delta_deformacion = deformacion*((0.001+0.001)/(longitud_final - longitud_inicial) + (delta_longitud_inicial)/(longitud_inicial))
    delta_deformaciones.append(delta_deformacion)


print(f"No.            Tensión                            Esfuerzo                                     Deformación")
for i in range(7):
    tension = tensiones[i]
    dtension = delta_tensiones[i]
    esfuerzo = esfuerzos[i]
    desfuerzo = delta_esfuerzos[i]
    deformacion = deformaciones[i]
    ddeformacion = delta_deformaciones[i]
    print(f"{i+1}    {tension} +- {dtension}            {esfuerzo} +- {desfuerzo}           {deformacion} +- {ddeformacion}")


################################################
# Al ejecutarse el programa, tenemos los resultados:
# No.            Tensión                            Esfuerzo                                     Deformación
# 1              1.75714 +- 0.00098                  35796162.13818 +- 19964.39606145009         0.05202 +- 0.002372138728323697
# 2              3.22714 +- 0.00098                  65742756.23035 +- 19964.39606144853         0.07514 +- 0.002398867052023119
# 3              4.70694 +- 0.00098                  95888994.28313 +- 19964.39606144701         0.09827 +- 0.002425842230533833
# 4              5.96134 +- 0.00098                 121443421.24178 +- 19964.39606144666         0.13295 +- 0.002465873335008796
# 5              7.90174 +- 0.00098                 160972925.44345 +- 19964.39606144735         0.15607 +- 0.002492575893812887
# 6              9.86174 +- 0.00098                 200901717.56634 +- 19964.39606144689         0.16763 +- 0.002505929838548933
# 7              11.7894 +- 0.00098                 240171684.61921 +- 19964.39606144722         0.18497 +- 0.002525963150289018
# Nota: Los resultados serán redondeados al colocarlos en sus respectivas tablas

# a1 = 1.1082031162523e+09 6.6385023231843e+07 # módulo de Young experimental obtenido en qtiplot
# a1 = 1.11e9 0.07e9 # módulo de Young experimental obtenido en qtiplot redondeado
################################################
