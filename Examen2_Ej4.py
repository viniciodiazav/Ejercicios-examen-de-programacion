#Ejercicio 4

peliculasDisponibles = [
    {"titulo": "Cars 2", "director": "John Lasseter y Brad Lewis", "año": 2011, "duracion": 106},
    {"titulo": "El Mago de Oz", "director": "Victor Fleming", "año": 1939, "duracion": 102},
    {"titulo": "Flow", "director": "Gints Zilbalodis", "año": 2024, "duracion": 84},
    {"titulo": "El Rey Leon", "director": "Roger Allers y Rob Minkoff", "año": 1994, "duracion": 86},
    {"titulo": "Wall-E", "director": "Andrew Stanton", "año": 2008, "duracion": 103}
]

peliculasAlquiladas = []

while True:
    print("""
====== Menu ======
1. Ver peliculas disponibles
2. Alquilar pelicula
3. Ver peliculas alquiladas
4. Devolver pelicula alquilada
0. salir""")
    opcion = input("Ingrese la opcion que desee: ")
    if (opcion == "0"):
        print("Gracias por alquilar peliculas :)")
        break
    match opcion:
        case "1":
            print("\n====== Peliculas disponibles ======")
            print("Peliculas disponibles:", len(peliculasDisponibles))
            contador = 1
            for peliculaDisponible in peliculasDisponibles:
                print(f"{contador}.", peliculaDisponible)
                contador += 1
        case "2":
            print("\n====== Alquilar pelicula ======")
            if (len(peliculasDisponibles) > 0):
                contador = 1
                for peliculaDisponible in peliculasDisponibles:
                    print(f"{contador}.", peliculaDisponible["titulo"])
                    contador += 1
                nombrePelicula = input("Ingrese el titulo de la pelicula que desee: ").lower()
                peliculaEncontrada = False
                for peliculaDisponible in peliculasDisponibles:
                    if (nombrePelicula == peliculaDisponible["titulo"].lower()):
                        peliculasAlquiladas.append(peliculaDisponible)
                        peliculasDisponibles.remove(peliculaDisponible)
                        peliculaEncontrada = True
                if (peliculaEncontrada == False):
                    print("No se encontro la pelicula con el nombre", nombrePelicula)
            else:
                print("Ya no hay peliculas disponibles")
        case "3":
            print("\n====== Peliculas alquiladas ======")
            print("Peliculas alquiladas:", len(peliculasAlquiladas))
            contador = 1
            for peliculaAlquilada in peliculasAlquiladas:
                print(f"{contador}.", peliculaAlquilada)
                contador += 1
        case "4":
            if (len(peliculasAlquiladas) > 0):
                print("\n====== Devolver pelicula alqiulada ======")
                contador = 1
                for peliculaAlquilada in peliculasAlquiladas:
                    print(f"{contador}.", peliculaAlquilada)
                    contador += 1
                nombrePelicula = input("Ingrese el titulo de la pelicula que desee: ").lower()
                peliculaEncontrada = False
                for peliculaAlquilada in peliculasAlquiladas:
                    if (nombrePelicula == peliculaAlquilada["titulo"].lower()):
                        peliculasDisponibles.append(peliculaDisponible)
                        peliculasAlquiladas.remove(peliculaDisponible)
                        peliculaEncontrada = True
                if (peliculaEncontrada == False):
                    print("No se encontro la pelicula con el nombre", nombrePelicula)
            else:
                print("Todavia no alquila ninguna pelicula")