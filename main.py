from helpers import lectura as rd
import algoritmos as alg
import test
import normalizacion as nm

# Primera Parte
datos = rd.leer_archivo("data/german_credit.csv")

datos_normalizados, min_max = nm.normalizacion_min_max(
    datos=datos,
    guardar=False)

datos_reales, datos_test = test.generar_test(
    porcentaje=0.1,
    datos=datos_normalizados,
    guardar=False)

print("Nuevo Registro".center(50, "-"))
alg.k_nuevo_registro(
    datos=datos_reales,
    min_max=min_max,
    k=1)

# Segunda Parte
conjunto = alg.generar_conjunto(
    datos_test=datos_test,
    datos_reales=datos_reales,
    k=3
)

print("Matriz de confusion".center(50, "-"))
vp, vn, fp, fn = alg.clases(conjunto)

print("Verdaderos Positivos (VP): ", vp)
print("Verdaderos Negativos (VN): ", vn)
print("Falsos Positivos (FP): ", fp)
print("Falsos Negativos (FN): ", fn)

exactitud = alg.exactitud(vp, vn, fp, fn)
print("Exactitud:", exactitud,"")

precision = alg.precision(vp, fp)
print("Precision:", precision)

sensibilidad = alg.sensibilidad(vp, fn)
print("Sensibilidad:", sensibilidad)

tnr = alg.razon_verdaderos_negativos(vn, fp)
print("TNR:", tnr)

fpr = alg.razon_falsos_positivos(fp, vn)
print("FPR:", fpr)
