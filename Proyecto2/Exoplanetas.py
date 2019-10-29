#!/usr/bin/python3

# Módulo de graficación
import matplotlib.pyplot as plt

# Módulo con funciones matemáticas
import numpy as np

# La siguiente clase será una "gráfica"
# que nos permitirá graficar funciones polares.
class Grafica:
    ax = plt.subplot(111, projection='polar')
    ax.set_title("Órbitas de exoplanetas en nuestro Sistema Solar", va='top')

    # Esta variable tendrá en cuenta cuántas veces hemos ploteado una función
    # Servirá para colocar el nombre del planeta uno debajo del anterior
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

        # Anotamos el nombre del planeta en la esquina superior izquierda
        # Con una flecha apuntado hacia el vértice izquierdo de la elipse
        plt.annotate(
            nombre.capitalize(), xy=(np.pi, f(np.pi)), xycoords='data',
            # Aquí es donde se usa la variable conteo
            # xttext dirá en qué posición ponemos el nombre del planeta
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

exoplanetas = {
    # Nombre del planeta
    'ceres': {
        # Excentricidad
        'e': 0.076,
        # Longitud de semieje mayor
        'a': 2.769,
        'theta': np.pi/4,
        'tGrafico': '\u03c0/4'
    },
    'plutón': {
        'e': 0.244,
        'a': 39.264,
        'theta': np.pi/3,
        'tGrafico': '\u03c0/3'
    },
    'haumea': {
        'e': 0.1888,
        'a': 43.335,
        'theta': 2*np.pi/3,
        'tGrafico': '2\u03c0/3'
    },
    'makemake':{
        'e': 0.159,
        'a': 45.791,
        'theta': 5*np.pi/4,
        'tGrafico': '5\u03c0/4'
    },
    'eris': {
        'e': 0.4417,
        'a': 67.67,
        'theta': 7*np.pi/6,
        'tGrafico': '7\u03c0/6'
    }
}
grafica = Grafica()

# Iterará por cada planeta
for nombre in exoplanetas:
    # Objeto Planeta, para trabajar con él más fácil a lo largo del búcle
    planeta = exoplanetas[nombre]

    # El perihelio del planeta estará dado por a*(1 - e)
    planeta['perihelio'] = planeta['a']*(1-planeta['e'])

    # El afelio del planeta estará dado por a*(1 + e)
    planeta['afelio'] = planeta['a']*(1+planeta['e'])

    # Ya que el perihelio es la longitud desde el foco, hasta un vértice
    # Y el afelio es la longitud desde el foco hasta el vértice contrario,
    # La suma entre el perihelio y el afelio debería ser
    # La longitud del eje mayor de la órbita del exoplaneta
    planeta['ejemayor'] = planeta['perihelio'] + planeta['afelio']

    # Para poder obtener la función polar que define la órbita del exoplaneta, necesitamos
    # el valor de su directríz, y determinar si ésta es positiva o negativa.
    # Para todos los exoplanetas, se observa que el perihelio es siempre menor que el afelio
    # (La elipse abre hacia la izquierda)
    # Dicho de otra manera, la longitud del perihelio, es lo mismo
    # que la función polar, evaluada en cero radianes.
    # Y ya que la elipse abre hacia la izquierda, sabemos que la función
    # trigonométrica será cos(theta), positivo
    # Sí la elipse "abre" hacia la izquierda, la directríz estará a la derecha del perihelio
    # Despejamos la ecuación de las cónicas en polares, para d (directriz)
    # Y sustituímos valores para e, r y theta, donde:
    # e nos la dan en el documento del proyecto para cada exoplaneta
    # theta será igual a cero radianes
    # r será la longitud del perihelio
    planeta['d'] = (planeta['perihelio'])*(1 + planeta['e']*np.cos(0))/(planeta['e'])
    # Directriz de la cónica

    # El inciso j nos pide obtener la distancia del exoplaneta al foco (sol)
    # para determinado angulo theta.
    # Es decir, la función polar de la órbita evaluada en theta.
    # Distancia al foco (sol) obtenida por la función de la cónica evaluada en theta
    planeta['distAlSol'] = (planeta['e']*planeta['d'])/(1 + planeta['e']*np.cos(planeta['theta']))

    # Los siguientes print() informarán los datos obtenidos para cada planeta
    print(f"El planeta {nombre.capitalize()} tiene:")
    print(f"Excentricidad: {planeta['e']}")
    print(f"Directriz: {planeta['d']}")
    print(f"Perihelio: {planeta['perihelio']}")
    print(f"Afelio: {planeta['afelio']}")

    # Inciso j
    print(f"Una distancia al sol de: {planeta['distAlSol']} ua")
    print(f"cuando el angulo \u03b8 es = {planeta['tGrafico']}")
    print(f"Y ecuación de su órbita: r = ({planeta['e']}*{planeta['d']})/(1 + {planeta['e']}*cos(\u03b8))\n")

    # Definimos la función polar de la órbita del exoplaneta y
    # se la pasamos a la gráfica para que plotee y grafique los puntos
    f = lambda theta: (planeta['e']*planeta['d'])/(1 + planeta['e']*np.cos(theta))
    grafica.plotear(f, nombre)

# Mostrar la gráfica en una ventana
grafica.mostrar()
