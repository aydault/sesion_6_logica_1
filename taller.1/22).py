#22

print("Seleccione el tipo de evento:")
print("1. Cine ($20.000)")
print("2. Teatro ($35.000)")
print("3. Concierto ($50.000)")

opcion = int(input("Ingrese una opción (1-3): "))
cantidad = int(input("Ingrese la cantidad de entradas: "))


if opcion == 1:
    precio = 20000
elif opcion == 2:
    precio = 35000
elif opcion == 3:
    precio = 50000
else:
    print("Opción no válida")
    exit()

total = precio * cantidad

if total > 100000:
    descuento = total * 0.10
    total -= descuento


print(f"Total a pagar: ${total:,.0f}")
