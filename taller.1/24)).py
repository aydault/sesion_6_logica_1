#24
tipo = input("Ingrese el tipo de actividad (dependiente, independiente, empresario): ").lower()


ingreso = float(input("Ingrese el ingreso mensual: "))


if ingreso <= 0:
    print("El ingreso debe ser un valor positivo")
    exit()

if tipo == "dependiente":
    retencion = ingreso * 0.10
elif tipo == "independiente":
    retencion = ingreso * 0.15
elif tipo == "empresario":
    retencion = ingreso * 0.20
else:
    print("Tipo de actividad no válido")
    exit()

print(f"Valor del impuesto: ${retencion:,.0f}")
