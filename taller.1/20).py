#20
tipo = input("Ingrese el tipo de vehículo (carro, moto, bicicleta): ").lower()
horas = float(input("Ingrese el número de horas: "))

if tipo == "carro":
    tarifa = 5000
elif tipo == "moto":
    tarifa = 2000
elif tipo == "bicicleta":
    tarifa = 500
else:
    print("Tipo de vehículo no válido")
    exit()

total = tarifa * horas
print(f"Total a pagar: ${total:,.0f}")