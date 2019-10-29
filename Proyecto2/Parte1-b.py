#!/usr/bin/python3

# Módulo de graficación
import matplotlib.pyplot as plt

# Módulo con funciones matemáticas
import numpy as np

# La siguiente clase será una "gráfica"
# que nos permitirá graficar funciones polares.
class Grafica:
    ax = plt.subplot(111, projection='polar')
    ax.set_title("Gráficas de elipses con e = 0.5 y d variable", va='top')

    # Esta variable tendrá en cuenta cuántas veces hemos ploteado una función
    # Servirá para colocar el nombre del orbitas uno debajo del anterior
    # El uso es dentro de la función plotear, de esta clase
    conteo = 1

    # La función plot, recibirá una función polar f
    def plotear(self, f, nombre):
        # Dividir 2pi en intervalos de 0.01, y guardarlos en una lista
        theta = np.arange(0, 2*np.pi, 0.01)

        # Evaluará la función f en todos los valores en la lista theta
        # Y los almacenará en la lista r
        r = f(theta)
        
        # Ploteará todos los puntos en coordenadas polares (theta, r)
        self.ax.plot(theta, r)

        # Anotamos el nombre del orbitas en la esquina superior izquierda
        # Con una flecha apuntado hacia el vértice izquierdo de la elipse
        plt.annotate(
            nombre, xy=(np.pi, f(np.pi)), xycoords='data',
            # Aquí es donde se usa la variable conteo
            # xttext dirá en qué posición ponemos el nombre del orbitas
            # la coordenada x va de cero a uno, donde 0 es la izquierda
            # la coordenada y va de cero a uno, donde 0 es la parte de abajo de la gráfica
                    # x       # y                           # relativo a la figura
            xytext=(0.025, 1-self.conteo*0.08), textcoords='figure fraction', 
            arrowprops={
                #'width': 0.5,
                #'headwidth': 4,
                'arrowstyle': 'fancy',
                'fc': '0.6',
                'ec': 'none',
                'connectionstyle': 'angle3, angleA=0, angleB=-90'
            },
        )

        # Aumentar el conteo de ploteos
        self.conteo += 1

    # Mostrará la gráfica
    def mostrar(self):
        plt.show()

orbitas = {
    'd = 2': {
        'e': 0.5,
        'd': 2
    },
    'd = 4': {
        'e': 0.5,
        'd': 4

    },
    'd = 7': {
        'e': 0.5,
        'd': 7
    }
}

grafica = Grafica()

# Iterará por cada orbitas
for nombre in orbitas:
    # Objeto Planeta, para trabajar con él más fácil a lo largo del búcle
    orbita = orbitas[nombre]

    # Los siguientes print() informarán los datos obtenidos para cada orbitas
    print(f"La órbita tiene:")
    print(f"Excentricidad: {orbita['e']}")
    print(f"Directriz: {orbita['d']}")

    # Definimos la función polar de la órbita del exoorbitas y
    # se la pasamos a la gráfica para que plotee y grafique los puntos
    f = lambda theta: (orbita['e']*orbita['d'])/(1 + orbita['e']*np.cos(theta))
    grafica.plotear(f, nombre)

# Mostrar la gráfica en una ventana
grafica.mostrar()
