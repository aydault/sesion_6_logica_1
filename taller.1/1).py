#1

numero = int(input("ingresa un numero entero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("es multiplo de 3 y 5")
elif numero % 5 == 0:
    print("es multiplo solo de 3")
elif numero % 5 == 0:
    print("es multiplo solo de 5")
else:
    print("no es multiplo de 3 y de 5")