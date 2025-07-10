#11
nota = float(input("Ingrese la nota, recuerde que es entre 0.0 y 5.0: "))

if nota < 0 or nota > 5:
    print("nota fuera de rango")
elif nota >= 4.5:
    print("Excelente")
elif nota >= 4.0:
    print("Sobresaliente")
elif nota >= 3.0:
    print("aceptable")
elif nota >= 2.0:
    print("insuficiente")
else:
    print("deficiente")