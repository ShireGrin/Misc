#!/usr/bin/python3

import sympy as s

# Se define una variable de tipo "dict"
# Estas variables pueden contener cualquier otro tipo de variable,
# La idea es que se definen dentro de ella, "llaves" y "valores"
    # Por ejemplo si defino el siguiente diccionario:
    # numeros = {
      # 'uno': 1
    # }
    # Observe que ahora el diccionario tiene una llave('uno'), con su respectivo valor (1)
    # Para obtener el valor 1, se deberá hacer lo siguiente:
    # numeros['uno']
    # Al realizarlo, el diccionario 'devolverá' el valor asociado con la cadena de caracteres 'uno'
# Se define el alfabeto proporcionado en el inciso, para obtenerse letras,
# O números, dependiendo el caso.
    # Por ejemplo para obtener la letra P, se debe hacer:
    # alfabeto['17']
    # Esto devolverá la letra 'P' para su manipulación.
alfabeto = {
    'A': 1,    '1':  'A',
    'B': 2,    '2':  'B',
    'C': 3,    '3':  'C',
    'D': 4,    '4':  'D',
    'E': 5,    '5':  'E',
    'F': 6,    '6':  'F',
    'G': 7,    '7':  'G',
    'H': 8,    '8':  'H',
    'I': 9,    '9':  'I',
    'J': 10,   '10': 'J',
    'K': 11,   '11': 'K',
    'L': 12,   '12': 'L',
    'M': 13,   '13': 'M',
    'N': 14,   '14': 'N',
    'Ñ': 15,   '15': 'Ñ',
    'O': 16,   '16': 'O',
    'P': 17,   '17': 'P',
    'Q': 18,   '18': 'Q',
    'R': 19,   '19': 'R',
    'S': 20,   '20': 'S',
    'T': 21,   '21': 'T',
    'U': 22,   '22': 'U',
    'V': 23,   '23': 'V',
    'X': 24,   '24': 'X',
    'Y': 25,   '25': 'Y',
    'Z': 26,   '26': 'Z',
    ' ': 27,   '27': ' ',
    '.': 0,    '0':  '.',
    '\"': 28, '28': '\"',
    'Á': 29,   '29': 'Á',
    'É': 30,   '30': 'É',
    'Í': 31,   '31': 'Í',
    'Ó': 40,   '40': 'Ó',
    'Ú': 32,   '32': 'Ú',
    ',': 33,   '33': ',',
}

##### Problema 1, 1.a #####

# La siguiente matriz contiene el mensaje encriptado
matrizMensajeEncriptado = s.Matrix([
    [ 105, 101, 73, 134,  66, 160, 156,  98, 109, 138, 98,  88, 137, 125, 129,  66, 146, 100,  92,  54, 138, 137,  75, 78],
    [ -18,   2, 31,  88, 119, 205,  36, -24,  24,   9, 94,  21,  80,  94, 140, -10,  44,  94,  82,  14,  78,  80, 107, 51],
    [  71,  45, 37,  53,   8,  15,  76,  76,  42,  70, 27,  35,  51,  40,  43,  49,  69,  15,  22,  19,  43,  51,  13, 30],
    [  -4, -67, -2,  34,  89,  44,   8,  39, -23, -13, 30, -69,   2,  -3,  79,  14,   2,  -3,   3, -12,  13,   2,  77,  7],
    [  84,   8, 10,  31,  11, -50,  81, 126,  42,  81,  1, -30,  14, -14,   8,  68,  59, -14, -17,  23,  48,  14,  23,  9]
])

# Esta es la matriz con la que se encriptó la matriz original
M = s.Matrix([
    [ 1, 0, 1,  3,  2],
    [-4, 1, 0,  5,  1],
    [ 2, 0, 1,  0,  0],
    [ 0, 2, 0,  2, -3],
    [ 5, 1, 0, -1, -2],
])
s.pprint(M)
print()

# La función inv(), devuelve la matriz inversa de M
# Se almacenará la matriz inversa de M en M_1
M_1 = M.inv()
s.pprint(M_1)
print()

# Para obtener la matriz original
# Multiplicamos la matriz inversa de M, por la matriz encriptada
# Se obtendrá entonces la matriz con la frase, pero aún falta convertirla a letras.
matrizMensajeDecodificado = M_1*matrizMensajeEncriptado
s.pprint(matrizMensajeDecodificado)
print()

# El atributo shape es una lista
# En cuyo índice 0 se contiene el número de filas
# Y en el índice 1 se contiene el número de columnas
# Almacenamos los valores en variables para fácil manipulación
filas = matrizMensajeDecodificado.shape[0]
columnas = matrizMensajeDecodificado.shape[1]

# El bucle externo, iterará desde 0, hasta el número de columnas de la matriz
for i in range(columnas):
    # El bucle interno, iterará desde 0, hasta el número de filas de la matriz
    for j in range(filas):

        # El siguiente comando obtendrá el valor numérico en la fila j, columna i
        # Luego, convertira ese valor numérico en una cadena de caracteres
        # Luego, en el "alfabeto" que definimos al inicio, se obtendrá la letra con ese "valor" numérico
            # Por ejemplo, sí la matriz, en la fila 1, columna 1, tuviera el número 17,
            # Se convierte a una cadena de caracteres, y se procede a buscar
            # en nuestro alfabeto, el valor, que tiene la cadena de caracteres "17"
            # Por como fué definido nuestro alfabeto, sabemos que 17 = P
            # Por lo que la letra retornada será P
            # (La conversión a cadena de caracteres debió hacerse por como funcionan los "dict" [diccionarios] en python)
        # Luego de obtener nuestra letra, la imprimimos a la consola
        # El argumento end='' (nada) es porque la función print() de python, siempre incluye al final un "newline"
        # (Si no se hiciera end='', las letras serían impresas linea por linea)
        print(alfabeto[str(matrizMensajeDecodificado[j, i])], end="")
print()
# Se obtiene así la frase encriptada originalmente:
# UN HOMBRE ES COMO UNA FRACCIÓN CUYO NUMERADOR CORRESPONDE A LO QUE ÉL ES, EN TANTO QUE EL DENOMINADOR ES LO QUE CREE SER

##### Problema 2, 1.a #####
# Se utilizó el mismo proceso que en el problema 1 para resolver este inciso.
# La frase que se obtiene es:
# CUANTO MAS GRANDE ES EL DENOMINADOR, MÁS PEQUEÑA ES LA FRACCIÓN.
matrizMensajeEncriptado = s.Matrix([
    [ 22, 169, 143,  93,  50, 114,  90,  84, 132, 192,  70,  98, 154, 153,  37,  79],
    [ 22,  16,  20,   1,  27,   5,   5,   9,  16,  13,  17,   5,   5,   1,   1,  40],
    [-34,  57,  35,  54, -40,  -3, -12,  51, -53,  52,  10,  71,  13,  60,  35,  46],
    [-26, -32, -40,  -3, -40, -39, -42,  -3, -81, -42, -14,   5, -47, -27,  10,  -5]
])

M = s.Matrix([
    [ 1,  0,  5,  1],
    [ 0,  1,  0,  0],
    [ 2,  0,  2, -3],
    [ 1,  0, -1, -2]
])

M_1 = M.inv()

matrizMensajeDecodificado = M_1*matrizMensajeEncriptado

filas = matrizMensajeDecodificado.shape[0]
columnas = matrizMensajeDecodificado.shape[1]
for i in range(0, columnas):
    for j in range(0, filas):
        print(alfabeto[str(matrizMensajeDecodificado[j, i])], end='')
print()



##### Problema 1.b #####

# Estos son los símbolos que usaremos para resolver el ejercicio
a, b, c, d = s.symbols("a b c d")

# Ésta es la matriz ya encriptada proporcionada en el ejercicio
matrizMensajeEncriptado = s.Matrix([
    [151,  63,  53,  61,   2, 140, 106,  77, 162, 145,  86,  94, 164, 118,  67,  95,  69,  90, 106],
    [212, 139, 187, 201, 141, 277, 137, 126, 262, 238, 178, 105, 221, 263, 156, 257, 163, 142, 336],
    [ 56,  86,  82,  78, 156,  56,  76,  -2, -35,  65,   9, -14, -20,  94, -19, 102,  40, -27,  74],
    [195, 176, 138, 144, 243, 197, 175,  77,  81, 200,  61,  29,  97, 247,  28, 194, 132,   1, 196]
])

# Esta es la matriz con la que se encriptó la matriz código original
M = s.Matrix([
    [ a,  0,  4, -1],
    [ b,  3,  2,  3],
    [ c, -1,  0,  5],
    [ 2, -2,  2,  7]
])

# La librería sympy es capáz de trabajar algebraícamente
# La función inv(), devuelve la matriz inversa de M
# En términos de a, b y c
M_1 = M.inv()

# El comando col() de la matriz, acepta un argumento numérico, n
# Que le indicará a la matriz que nos devuelva la columna numero n
# Luego se explicará porque nos servirá esta columna
columna_1_de_M_Encriptada = matrizMensajeEncriptado.col(0)
# [
#   [151],
#   [212],
#   [ 56],
#   [195],
# ]

# En el problema se nos indica que la primera palabra en el texto, es SI
# También se nos informa que la frase original, no contenía comillas
# Esto nos proporciona los primeros valores de la columna 1 de la matriz original
# También nos informa que SI es la primera "palabra" en la frase
# Es decir, que luego de la palabra SI, solo puede haber:
# Un espacio, una coma, ó un punto
# Sabemos que:
# S = 20
# I = 9
# También por la naturaleza gramática de una frase
# Dedujimos que no puede ser un punto, ya que no puede terminar luego de 2 letras.
# Nos queda la coma, y el espacio
# Que difícilmente sería una coma, ya que no tendría sentido
# Por "fuerza bruta", podríamos probar los 3 valores posibles de igual forma
# Pero decidimos suponer que el caracter luego de la palabra SI, es el espacio.
# Espacio = 27
# Y así, casi obtenemos la primera columna de la matriz original
# El cuarto valor, no será necesario saberlo, se explicará el ¿por qué?, luego.
columna_1_matriz_decodificada = s.Matrix([
    [20],
    [ 9],
    [27],
    [ d],
])

# Por la naturaleza de la multiplicación entre matrices,
# La primera fila multiplicada por la columna 1 encriptada, deberá sumar 20
# Esta ecuación, contiene a, b y c
# Podemos despejar para a, en términos de b y c
# La función dot() realiza el producto punto,
# Que es lo mismo que "multiplicar" la primera fila por la primera columna
ecuacion_1 = s.solve(s.simplify(M_1.row(0).dot(columna_1_de_M_Encriptada)) - 20, [a])

# La segunda fila de la inversa de M, multiplicada por la columna 1 encriptada,
# Debería ser igual a 9
# Tenemos otra ecuación que contiene a b y c
# Pero ya que tenemos a despejada de la ecuación anterior, podemos sustituír
# Para luego, obtener una ecuación que contiene b y c
# Se procede a despejar para b, en términos de c
ecuacion_2 = s.solve(s.simplify(M_1.row(1).dot(columna_1_de_M_Encriptada) - 9).subs(a, ecuacion_1[0]), [b])

# La tercera fila de la inversa de M, multiplicada por la columna 1 encriptada,
# Deberá sumar 27 (Siguiendo la suposición de que es un espacio)
# Se tiene otra ecuación en términos de a b y c
# Pero de las ecuaciones anteriores, tenemos a en términos de b y c
# Sustituímos primero a en le ecuación, dejándonos una ecuación con b y c
# Pero también tenemos b, de la ecuación anterior
# Podemos sustituír b, en términos de c, en la actual ecuación
# Dejándonos así una ecuación solo conteniendo c
# Se procede a despejar, y se tiene que c = -1
ecuacion_3 = s.solve(s.simplify(M_1.row(2).dot(columna_1_de_M_Encriptada) - 27).subs(a, ecuacion_1[0]).subs(b, ecuacion_2[0]), [c])

# Se almacena el valor de c en una variable para fácil manipulación
valor_numerico_c = ecuacion_3[0] # -1

# Luego se sustituye el valor de c, en la ecuación 2, que teníamos en términos de b y c
# Se procede a despejar para b, y se tiene que b = 4
# Se almacena su valor en una variable para fácil manipulación
valor_numerico_b = ecuacion_2[0].subs(c, valor_numerico_c) #  4

# Luego se sustituye el valor de c y b, en la ecuación 1, que teníamos en términos de a, b y c
# Se procede a despejar para a, y se tiene que a = 3
# Se almacena su valor en una variable para fácil manipulación
valor_numerico_a = ecuacion_1[0].subs(b, valor_numerico_b).subs(c, valor_numerico_c) #  3

# Ya que se tienen los valores de las tres variables:
# Se sustituyen por sus valores numéricos en la matriz M, usada para encriptar la frase
M[0, 0] = valor_numerico_a;
M[1, 0] = valor_numerico_b;
M[2, 0] = valor_numerico_c;

# Teniendo la matriz correcta, obtenemos su inversa
M_1 = M.inv()

# Teniendo la matriz inversa, y la frase encriptada
# Se procede a multiplicar la matriz inversa de M, por la frase encriptada
# Y así obtener la matriz que contiene la frase original.
matrizMensajeDecodificado = M_1*matrizMensajeEncriptado;

# Imprimimos a la consola la matriz desencriptada
# Se observan solo números enteros, entre 0 y 40
# Esto nos indica que vamos por buen camino,
# Ya que no se tienen valores negativos, o fraccionarios
# Solo se contienen los valores en nuestro "alfabeto"
s.pprint(matrizMensajeDecodificado)
print()

# Obtenemos el número de filas de la matriz
filas = matrizMensajeDecodificado.shape[0]
# Obtenemos el número de columnas de la matriz
columnas = matrizMensajeDecodificado.shape[1]

# El bucle externo, iterará desde 0, hasta el número de columnas de la matriz
for i in range(columnas):
    # El bucle interno, iterará desde 0, hasta el número de filas de la matriz
    for j in range(filas):

        # El siguiente comando obtendrá el valor numérico en la fila j, columna i
        # Luego, convertira ese valor numérico en una cadena de caracteres
        # Luego, en el "alfabeto" que definimos al inicio, se obtendrá la letra con ese "valor" numérico
            # Por ejemplo, sí la matriz, en la fila 1, columna 1, tuviera el número 17,
            # Se convierte a una cadena de caracteres, y se procede a buscar
            # en nuestro alfabeto, el valor, que tiene la cadena de caracteres "17"
            # Por como fué definido nuestro alfabeto, sabemos que 17 = P
            # Por lo que la letra retornada será P
            # (La conversión a cadena de caracteres debió hacerse por como funcionan los "dict" [diccionarios] en python)
        # Luego de obtener nuestra letra, la imprimimos a la consola
        # El argumento end='' (nada) es porque la función print() de python, siempre incluye al final un "newline"
        # (Si no se hiciera end='', las letras serían impresas linea por linea)
        print(alfabeto[str(matrizMensajeDecodificado[j, i])], end='')
print()
# De esta manera, al terminar el bucle externo, se habrá convertido e impreso toda la matriz numérica,
# A la frase original:
# SI PIENSA QUE PUEDE, USTED PUEDE, PERO SI PIENSA QUE NO PUEDE, "TIENE RAZÓN"
