# Programa 5

Descargue el archivo german_credit.csv de la siguiente página Analysis of German Credit Data | STAT 508 (psu.edu) https://online.stat.psu.edu/stat508/resource/analysis/gcd
El conjunto de datos de crédito bancario contiene información sobre 1000 solicitantes de crédito bancario de Alemania. Esto incluye:

- el saldo de su cuenta
- el monto del crédito
- la edad
- la ocupación
- los registros de préstamos
- etc.

Mediante el uso de estos datos y haciendo uso de algoritmos de aprendizaje automático, podemos predecir si aprobar o no el préstamo de un solicitante nuevo de crédito. El problema se puede resolver utilizando el algoritmo KNN que clasificará la solicitud de préstamo del solicitante en dos clases:

- Aprobado (positivo)
- Desaprobado (negativo)

## Primera parte del programa

1. Revise los datos y realice limpieza si es necesario Realice la normalización de sus datos para atributos que salgan de un rango adecuado. Se sugiere que todos los datos se encuentren en un rango de [0,1]
2. Divida su conjunto de datos en un conjunto de prueba y un conjunto de entrenamiento (10%/90%). Programe el algoritmo de primeros vecinos en algún lenguaje de su preferencia para algún valor de k.
3. El usuario debe introducir un nuevo registro y el valor de k y el programa debe imprimir los k vecinos más cercanos (de entre los datos de entrenamiento) a ese nuevo registro y clasificarlo (aprobado o desaprobado)

## Segunda parte del programa

Ponga a prueba el algoritmo programado sobre el conjunto de datos de prueba (el 10% restante) mediante el cálculo de las tres métricas vistas en clase realizando los siguientes pasos:

1. Calcule una matriz de confusión realizando un conteo de verdaderos (positivos y negativos) y falsos (positivos y negativos) para distintos valores de k (los cuales debe elegir el usuario).
2. Si el usuario elige k=1 por ejemplo, el programa debe tomar el primer dato de prueba y calcular el vecino mas cercano con los datos de entrenamiento (predicción) y el primer dato de prueba también esta clasificado como “aprobado” (dato real), se tendrá un verdadero positivo.
3. Se toma después el segundo dato de prueba y se calcula el vecino mas cercano con los datos de entrenamiento; si el vecino más cercano de los datos de entrenamiento tiene “desaprobado” como atributo clase (predicción) y el segundo dato de prueba tiene “aprobado” como atributo clase (dato real), entonces se tendrá un falso negativo, y así sucesivamente con todos los datos de prueba.
4. Con la matriz de confusión obtenida (la cual se debe visualizar), calcular las medidas de exactitud, precisión y sensibilidad.
5. El programa debe decir si el método de vecinos mas cercanos es un algoritmo que ofrece o no ofrece un buen desempeño en las predicciones de la clase. Si el usuario elige k=3 por ejemplo, el programa debe tomar el primer dato de prueba y calcular los 3 vecinos (de los datos de entrenamiento) mas cercanos. **De esos tres vecinos, si por ejemplo los tres tienen el mismo atributo clase “aprobado” (predicción) y el primer dato tiene el atributo “desaprobado”, se tendrá un falso positivo. Si de los tres vecinos, dos de ellos tienen el mismo atributo “desaprobado” y 1 de ellos “aprobado” la predicción sería “desaprobado” y si el dato de prueba tiene como atributo clase “desaprobado”, se tendría un verdadero negativo.** Se toma después el segundo dato de prueba y se realiza el mismo procedimiento y así sucesivamente con todos los datos de prueba tal y como se hizo con k=1.
6. Se construye la matriz de confusión, se calculan las métricas, etc.

Fecha de revisión: Viernes 27 de octubre.
