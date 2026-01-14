goles = {}
lesionados = [ "Rocha", "Batres", "Cupillar" ]

while True:
    print("\n--- MENU DE GOLES ---")
    print("1. Ingresar goles")
    print("2. Consultar jugador")
    print("3. Informe del equipo")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":  
        jugador = input("Ingrese el nombre del jugador: ")
        if jugador in lesionados:
            print(f"El jugador {jugador} está lesionado.")
        else:
            try:
                cgoles = int(input("Ingrese la cantidad de goles anotados: "))
                if cgoles < 0:
                    print("La cantidad no puede ser negativa.")
                else:
                    goles[jugador] = goles.get(jugador, 0) + cgoles
                    print(f"Goles actualizados para {jugador}.")
            except ValueError:
                print("Ingrese un número válido.")
    elif opcion == "2":
        jugador = input("Ingrese el nombre del jugador: ")
        print(f"{jugador} tiene {goles.get(jugador, 0)} goles.")
    elif opcion == "3":
        print(f"Total equipo: {sum(goles.values())}")
        for j, g in goles.items():
            print(f"{j}: {g} goles")
    elif opcion == "4":
        break
