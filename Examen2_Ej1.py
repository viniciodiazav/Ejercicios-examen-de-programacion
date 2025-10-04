#Ejercicio 1

total_compra = 0
while True:
    print("""
====== Menu ======
1. Cafe americano - $5
2. Cappuccino - $7
3. Latte - $6
4. Mocha - $8
0. Finalizar compra""")
    opcion = input("Ingrese el numero de la opcion que desee: ")
    if (opcion == "0"):
        print("Gracias por comprar :)")
        print("Total de la compra: $", total_compra)
        break
    match opcion:
        case "1":
            print("Agregando cafe americano")
            total_compra += 5
            print("Total actualizado: $", total_compra)
            continuar = input("Desea agregar mas productos? (S/n): ")
            if (continuar.lower() == "n"):
                print("Gracias por comprar :)")
                print("Total de la compra: $", total_compra)
                break
        case "2":
            print("Agregando cappuccino")
            total_compra += 7
            print("Total actualizado: $", total_compra)
            continuar = input("Desea agregar mas productos? (S/n): ")
            if (continuar.lower() == "n"):
                print("Gracias por comprar :)")
                print("Total de la compra: $", total_compra)
                break
        case "3":
            print("Agregando latte")
            total_compra += 6
            print("Total actualizado: $", total_compra)
            continuar = input("Desea agregar mas productos? (S/n): ")
            if (continuar.lower() == "n"):
                print("Gracias por comprar :)")
                print("Total de la compra: $", total_compra)
                break
        case "4":
            print("Agregando mocha")
            total_compra += 8
            print("Total actualizado: $", total_compra)
            continuar = input("Desea agregar mas productos? (S/n): ")
            if (continuar.lower() == "n"):
                print("Gracias por comprar :)")
                print("Total de la compra: $", total_compra)
                break
        case _:
            print("\nRespuesta invalida, intentelo de nuevo...")