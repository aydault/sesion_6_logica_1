#8
nota_final = float(input("ingrese la nota final del estudiante: "))
asistencia = float(input("ingrese el porcentaje de asistencias del estudiante: "))

if nota_final >= 3.0 and asistencia >= 80:
    print("el estudiante aprueba")
else:
    print("el estudiante reprueba")