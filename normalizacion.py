from helpers.lectura import guardar_datos


def normalizacion_min_max(datos, guardar=False):
    columnas_normalizadas = []
    minimos_maximos = []
    for i in range(len(datos[0])):
        columna = [fila[i] for fila in datos]
        if set(columna) != {0, 1}:
            maximo = max(columna)
            minimo = min(columna)
            columna_normalizada = [
                (dato - minimo) / (maximo - minimo) for dato in columna]
        else:
            columna_normalizada = columna
        columnas_normalizadas.append(columna_normalizada)
        minimos_maximos.append((min(columna), max(columna)))

    datos_normalizados = [[fila[i] for fila in columnas_normalizadas]
                          for i in range(len(columnas_normalizadas[0]))]
    if guardar:
        guardar_datos(datos_normalizados, "normalizado")

    return datos_normalizados, minimos_maximos


# Si solo hay un dato
def normalizacion_min_max_individual(datos, min_max):
    datos_normalizados = []
    min_max.pop(0)
    for i in range(len(datos)):
        minimo = min_max[i][0]
        maximo = min_max[i][1]
        dato = datos[i]
        valor_normalizado = (dato - minimo) / (maximo - minimo)
        datos_normalizados.append(valor_normalizado)
    return datos_normalizados
