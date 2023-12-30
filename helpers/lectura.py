import pandas as pd


def leer_archivo(path):
    data = pd.read_csv(path)
    return data.values.tolist()


def guardar_datos(datos, tipo):
    with open(f"data/german_credit_{tipo}.csv", "w") as f:
        for fila in datos:
            for i in range(len(fila)):
                if i == len(fila) - 1:
                    f.write(str(fila[i]))
                else:
                    f.write(str(fila[i]) + ",")
            f.write("\n")
