#25

nota = float(input("ingrese la nota (0 a 5): "))
letra = input("ingrese la letra (A a F): ").upper()

if nota < 0 or nota > 5:
    print("nota fuera de rango")
elif nota < 3:
    if letra == "D" or letra == "F":
        print("nota y letra son coherentes")
    else:
        print("nota y letra no coinciden, favor revisar")
else:
    if letra == "A" or letra == "B" or letra == "C":
        print("nota y letra son coherentes")
    else:
        print("nota y letra no coinciden, favor revisar")