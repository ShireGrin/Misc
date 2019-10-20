#!/usr/bin/python3

from numpy import pi

          # 33   +   # 30 = 63
carnes = [201908274, 201901458]
#carnes = [201908274, 201907774, 201904061]

# Diámetro
d = 0

# Búcle para obtener la suma de los dígitos de todos los carnés
# Para cada carné en la lista carnes...
for carne in carnes:
    # Se convierte el carné a una cadena de caracteres
    # Luego se convierte la cadena de caracteres a una lista
    # que contiene los dígitos del carné
    digitos = list(str(carne))
    
    # Para cada dígito en el carné...
    for digito in digitos:
        # Sumarlo a la variable d
        d += int(digito)

print(d)

# Funciones en términos del diámetro para obtener:
# A: Altura(d) de una esfera
# S: AreaSuperficial(d) de una esfera
# V: Volumen(D) de una esfera
A = lambda d: d
S = lambda d: 4*pi*(d/2)**2
V = lambda d: 4/3*pi*((d/2)**3)

# Variables que van a almacenar el resultado final de las series
Altura = 0
Area = 0
Volumen = 0

# Aunque se le pida al búcle que se repita 1000 veces,
# habrá una iteración en la que el resultado se mantenga constante.
# Y se detendrá el búcle. Se obtendrá ese número de iteración.
# Al final de cada iteración, la variable d se multiplicará por un factor
# de 0.75, que equivale al 75% del anterior diámetro
for i in range(1000):
    if(Altura == (Altura + A(d))):
        print(f"Para la iteración {i}, los valores ya no cambian.")
        print(f"Altura: {Altura + A(d)}, aproxima a {round(Altura)}")
        print(f"Área: {Area + S(d)}, aproxima a {round(Area)}"),
        print(f"Volumen: {Volumen + V(d)}, aproxima a {round(Volumen)}")
        break
    Altura += A(d)
    Area += S(d)
    Volumen += V(d)
    d = 0.75*d
