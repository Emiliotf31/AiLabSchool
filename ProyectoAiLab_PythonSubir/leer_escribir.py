import csv

def escribir_csv(data, path="./ejemplo"):
    with open(path, "w") as file:
        escritor = csv.writer(file, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL)
        escritor.writerows(data)
    print("File stored with success")

def leer_csv(path="./ejemplo.csv"):
    arreglo = []
    with open(path) as archivo:
        lector = csv.reader(archivo, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL)
        for renglon in lector:
            if renglon != "":
                arreglo.append(renglon)
    return arreglo
