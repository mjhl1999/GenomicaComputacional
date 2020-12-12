import sys

fasta = sys.argv[1]

entrada = open("/home/hp-spectre/GenomicaComputacional/Lambda/data/" +
        str(fasta), "r")

def longitudes(entrada):
    longitudes = list()
    caracteres = 0

    for linea in entrada:
        if not linea.startswith('>'):
            caracteres = get_long(linea)
            longitudes.append(caracteres)
    return longitudes

def promedio(lista_longitudes):
    promedio = sum(lista_longitudes) / len(lista_longitudes)
    return promedio

def get_long(cadena):
    n = 0
    for c in cadena:
        n = n + 1
    return n

longitudes = promedio(longitudes(entrada))

print("Promedio de la longitud de las secuencias: " + str(longitudes))
