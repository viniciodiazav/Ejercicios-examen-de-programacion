#Ejercicio 2

import random 

carpetas = ["carpeta 1", "carpeta 2", "carpeta 3", "carpeta 4", "carpeta 5", "carpeta 6"]

archivoABuscar = f"carpeta {random.randint(1,10)}"

archivoEncontrado = False
for carpeta in carpetas:
    if (archivoABuscar == carpeta):
        print("El archivo se encuentra en la", carpeta)
        archivoEncontrado = True
        break
    else:
        print("El archivo no se encuentra en la", carpeta)

if (archivoEncontrado == False):
    print("\nEl archivo no se encotnro en ninguna carpeta")