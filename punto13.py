#13
# Menú repetitivo de operaciones básicas

while True:
    print("\n--- MENÚ ---")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a + b)

    elif opcion == "2":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a - b)

    elif opcion == "3":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a * b)

    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
