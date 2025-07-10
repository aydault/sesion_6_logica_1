#10

numero = int(input("Ingresa un numero para verificar: "))

if (numero >= 100 and numero <= 999) or (numero <= -100 and numero >= -999):
    print("El numero tiene exactamente 3 cifras")
else:
    print("El numero no cumple con el requisito.")
