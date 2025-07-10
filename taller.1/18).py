#18

print("MENÚ DE OPERACIONES")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Seleccione una opción (1-4): "))
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

match opcion:
    case 1:
        resultado = num1 + num2
        print("Resultado:", resultado)
    case 2:
        resultado = num1 - num2
        print("Resultado:", resultado)
    case 3:
        resultado = num1 * num2
        print("Resultado:", resultado)
    case 4:
        if num2 == 0:
            print("No se puede dividir por cero")
        else:
            resultado = num1 / num2
            print("Resultado:", resultado)
    case _:
        print("Opción no válida")
