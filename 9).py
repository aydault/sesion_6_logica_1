#9


gastos = float(input("Ingrese el consumo mensual en kWh: "))


if gastos < 100:
    print("Estrato bajo")
elif 100 <= gastos <= 200:
    print("Estrato medio")
else:
    print("Estrato alto")    