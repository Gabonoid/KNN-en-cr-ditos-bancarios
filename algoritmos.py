import math
import normalizacion as nm


def distancia_euclidiana(propuesto, datos):
    distancias = []

    for fila in datos:
        is_aprobado = fila[0]
        fila_resto = fila[1:]
        distancia = math.sqrt(
            sum((dato-var_propuesto)**2 for dato,
                var_propuesto in zip(fila_resto, propuesto))
        )
        distancias.append((is_aprobado, distancia))

    distancias = sorted(distancias, key=lambda x: x[1])

    return distancias


def generar_conjunto(datos_reales, datos_test, k=1):
    finales_test = [dato.pop(0) for dato in datos_test]
    finales_reales = []

    for dato in datos_test:
        distancias = distancia_euclidiana(
            propuesto=dato,
            datos=datos_reales
        )

        final_test = {
            'desaprobado': 0,
            'aprobado': 0
        }

        for i in range(k):
            vecino = distancias[i]
            if vecino[0] == 1:
                final_test['aprobado'] += 1
            else:
                final_test['desaprobado'] += 1

        atributo_maximo = max(final_test, key=lambda i: final_test[i])
        finales_reales.append(1 if atributo_maximo == 'aprobado' else 0)

    return [[i, j]for i, j in zip(finales_test, finales_reales)]


def matriz_confusion(reales, predicciones):
    matriz = []
    for real, prediccion in zip(reales, predicciones):
        matriz.append([real, prediccion])
    return matriz


def clases(matriz_confusion):
    vp = 0
    vn = 0
    fp = 0
    fn = 0
    for linea in matriz_confusion:
        if linea[0] == 1 and linea[1] == 1:
            vp += 1
        elif linea[0] == 1 and linea[1] == 0:
            fn += 1
        elif linea[0] == 0 and linea[1] == 1:
            fp += 1
        elif linea[0] == 0 and linea[1] == 0:
            vn += 1
    return vp, vn, fp, fn


def exactitud(vp, vn, fp, fn):
    return (vp + vn) / (vp + vn + fp + fn)


def sensibilidad(vp, fn):
    return vp / (vp + fn)


def precision(vp, fp):
    return vp / (vp + fp)


def razon_verdaderos_negativos(vn, fp):
    return vn / (vn + fp)


def razon_falsos_positivos(fp, vn):
    return fp / (fp + vn)


def razon_falsos_negativos(fn, vp):
    return fn / (fn + vp)


def k_nuevo_registro(datos, k, min_max):
    datos_propuestos = [2,36,2,5,2384,1,2,4,3,1,1,4,33,3,1,1,2,1,1,1]
    ''' datos_propuestos = []
    temas = ["Saldo de la cuenta (1-4): ",
             "Duración del crédito: ",
             "Estado de pago del crédito anterior (0-4): ",
             "Objetivo (0-10): ",
             "Monto de crédito: ",
             "Valor Ahorro/Acciones (1-5): ",
             "Duración del empleo actual (1-5): ",
             "Porcentaje de cuotas (1-4): ",
             "Sexo y estado civil (1-4): ",
             "Garantes (1-3): ",
             "Duración en Dirección actual (1-4): ",
             "Activo disponible más valioso (1-4): ",
             "Edad: ",
             "Créditos concurrentes (1-3): ",
             "Tipo de apartamento (1-3): ",
             "No de Créditos en este Banco (1-4): ",
             "Ocupación (1-4): ",
             "Número de dependientes (1-2): ",
             "Teléfono (1-2): ",
             "Trabajador extranjero (1-2): "]

    for tema in temas:
        datos_propuestos.append(int(input(tema))) '''

    dato_normalizado = nm.normalizacion_min_max_individual(
        datos=datos_propuestos,
        min_max=min_max)

    distancias = distancia_euclidiana(
        propuesto=dato_normalizado,
        datos=datos)
    
    final_test = {
            'desaprobado': 0,
            'aprobado': 0,
        }

    for i in range(k):
        vecino = distancias[i]
        is_aprobado = "es aprobado" if vecino[0] == 1 else "es desaprobado"
        
        if vecino[0] == 1:
            final_test['aprobado'] += 1
        else:
            final_test['desaprobado'] += 1
        
        print(
            f'El vecino {i+1} con una distancia de {vecino[1]} el cual "{is_aprobado}" el credito')
    
    atributo_maximo = max(final_test, key=lambda i: final_test[i])
    
    print(f'El credito propuesto es "{atributo_maximo}"')
    
