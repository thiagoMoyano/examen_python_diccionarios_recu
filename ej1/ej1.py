notas = {
    "Gomez": [],
    "Rodriguez": [],
    "Lopez": [],
    "Fernandez": [],
    "Martinez": []
}

while True:
    print("\n--- SISTEMA DE MANEJO DE NOTAS ---\1. Ver todas las notas \n 2. Ver notas por alumno \n 3. Cargar notas \n 4. Promedio de un alumno\n 5. Salir")

    opcion = input("elija una opcion (1-5): ")
    
    if opcion == "1":
        print("\n--- Todas las notas ---")
        for alumno, lista_notas in notas.items():
            if len(lista_notas) == 0:
                print(f"Alumno: {alumno} - Notas Sin cargar bob")
            else:
                print(f"Alumno {alumno}  Notas: {lista_notas}")
                
    elif opcion == "2":
        print("\n--- Ver notas por esclavo / alumno ---")
        apellido = input("Ingrese el apellido del alumno: ")
        if apellido in notas:
            if len(notas[apellido]) == 0:
                print(f"el alumno {apellido} anu no tiene notas cargadas")
            else:
                print(f"notas de {apellido}: {notas[apellido]}")
        else:
            print("El alumno no se encuentra en el sistema")
            
    elif opcion == "3":
        print("\n--- Cargar notas ---")
        if apellido in notas:
            notas[apellido] = []
            print(f"Cargando 5 notas para el alumno {apellido}:")
            for i in range(1, 6):
                while True:
                    try:
                        nota = float(input(f"Ingrese la nota {i}: "))
                        if 0 <= nota <= 10:
                            notas[apellido].append(nota)
                            break
                        else:
                            print("Por favor ingrse una nota entre 0 y 10")
                    except ValueError:
                        print("Error")
            print(f"Notas cargadas con exito para {apellido}")
        else:
            print("El alumno no se encuentra en el sistema")
            
    elif opcion == "4":
        print("\n--- promedio alumno ---")
        apellido = input("ingrese el apellido del aulmno: ")
        if apellido in notas:
            if len(notas[apellido]) == 0:
                print(f"el alumno {apellido} no tiene notas cargadas para calcular el promedio")
            else:
                promedio = sum(notas[apellido]) / len(notas[apellido])
                print(f"el promedio del alumno {apellido} es: {promedio:}")
        else:
            print("el alumno no se encuentra en el sistema")
            
    elif opcion == "5":
        print("Saliendo")
        break
        
    else:
        print("Error por fa elija un unmero entero 1 al 5")