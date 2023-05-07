from Manejador_Viajeros import lista

def menu(listaV):
    viaj=listaV.numViajero()
    if viaj:
        while True:
            print("Bienvenido al menú de opciones")
            print("1. Consultar Cantidad de Millas.")
            print("2. Acumular Millas.")
            print("3. Canjear Millas.")
            print("4. Salir")
            
            opcion = input("Ingrese una opción: ")
            
            if opcion == "1":
                print("Ha elegido la opción: Consultar Cantidad de Millas")
                print(f"Cantidad de Millas: {viaj.getMillas()}")
            elif opcion == "2":
                print("Ha elegido la opción: Acumular Millas")
                millas=int(input("Ingresar Millas recorridas: "))
                print(f"Millas acumuladas: {viaj.acumularMillas(millas)}")
            elif opcion == "3":
                print("Ha elegido la opción: Canjear Millas")
                canjear=int(input("Ingresar Millas a canjear: "))
                print(f"Millas Acumuladas restantes: {viaj.canjearMillas(canjear)}")
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
    else:
        print("El numero de viajero ingreaso no existe")
                
if __name__=="__main__":
    listaV=lista()
    listaV.test()
    #menu(listaV)
    listaV.sumaMillas()
    listaV.restaMillas()
    listaV.compararMillas()

    