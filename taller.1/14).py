#14
nota = float(input("ingrese la nota de desempeño del colaborador (entre 0.0 y 5.0): "))
proyectos = int(input("Ingrese la cantidad de proyectos finalizados"))

if nota >= 4.5 and proyectos >= 3:
    print("Empleado destacado")
elif nota >= 4.5 or proyectos >= 3:
    print("Empleado competente")
else:
    print("Empleado en formacion.")
