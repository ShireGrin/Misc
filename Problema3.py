#!/usr/bin/python3

lineasArchivo = open('Problema3Input.txt', 'r').read()[:-1].split('\n')
noCasos = int(lineasArchivo[0])
lineasArchivo.pop(0)

# No. de combinaciones mínimas
comb = 0

# Contendrá los diferentes casos proporcionados
# Dentro de cada caso, se tendrá la dimensión
# Y una lista de listas, con los valores
casos = {}

for i in range(noCasos):
    dimension = int(lineasArchivo[0])*2
    lineasArchivo.pop(0)
    casos[str(i+1)] = {}
    casos[str(i+1)]['dimension'] = dimension
    casos[str(i+1)]['filas'] = []
    for j in range(dimension):
        casos[str(i+1)]['filas'].append(str(lineasArchivo[0]))
        lineasArchivo.pop(0)

for caso in casos:
    # Verificar si es posible ordenar
    matriz = casos[caso]
    for i in range(matriz['dimension']):
        # Contendrá la suma de los valores de cada fila/columna
        # Ya que cada fila/columna debe tener dimensión/2 "unos"
        # Sí la suma no es igual a dimensión/2
        # El caso es imposible
        suma = 0
        for j in range(matriz['dimension']):
            suma += int(matriz['filas'][i][j])
        if(not (suma == int(matriz['dimension']/2))):
            print("Caso #{}: Imposible".format(caso))
            imposible = True
            break
        else:
            imposible = False
    
    # Sí el caso es imposible, saltar al siguiente
    if(imposible):
        continue

    combinaciones = 0

    # Ordenar filas, de forma alterna
    for j in range(1, matriz['dimension']-1):
        anteriorFila = matriz['filas'][j-1]
        fila = matriz['filas'][j]
        siguientesFilas = matriz['filas'][j+1:]
        if(anteriorFila[0] == fila[0]):
            for k in range(j+1, j+1+len(siguientesFilas)):
                if(matriz['filas'][k][0] != fila[0]):
                    temp = matriz['filas'][k]
                    matriz['filas'][k] = fila
                    matriz['filas'][j] = temp
                    combinaciones += 1
                    break
        else:
            continue

    # Ordenar columnas, de forma alterna
    for j in range(1, matriz['dimension']-1):
        anteriorColumna = []
        for k in range(matriz['dimension']):
            anteriorColumna.append(matriz['filas'][k][j-1])

        columna = []
        for k in range(matriz['dimension']):
            columna.append(matriz['filas'][k][j])

        siguientesColumnas = []
        for k in range(j+1, matriz['dimension']):
            sigCol = []
            for l in range(matriz['dimension']):
                sigCol.append(matriz['filas'][l][k])
            siguientesColumnas.append(sigCol)

        if(anteriorColumna[0] == columna[0]):
            for k in range(len(siguientesColumnas)):
                if(columna[0] != siguientesColumnas[k][0]):
                    temp = ""
                    for l in range(matriz['dimension']):
                        temp += matriz['filas'][l][k+1]
                    for l in range(matriz['dimension']):
                        var = matriz['filas'][l][:j] + siguientesColumnas[k][l] + temp[l] 
                        matriz['filas'][l] = var
                    combinaciones += 1
    print("Caso #{}: {}".format(caso, combinaciones))
