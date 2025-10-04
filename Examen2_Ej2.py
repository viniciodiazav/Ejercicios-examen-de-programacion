#Ejercicio 2

import random 

carpetas = ["carpeta 1", "carpeta 2", "carpeta 3", "carpeta 4", "carpeta 5", "carpeta 6"]

archivoSeleccionado = f"carpeta {random.randint(0,10)}"

archivoEncontrado = False
for carpeta in carpetas:
    if (carpeta == archivoSeleccionado):
        print("======== El archivo se encontro en la", carpeta, "========")
        archivoEncontrado = True
    else:
        print("El archivo no se encuentra en la", carpeta)

if (not archivoEncontrado):
    print("El archivo no se encontro en ninguna carpeta")
