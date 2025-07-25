#11
# Suma hasta cero

suma = 0

print("Ingresa números para sumar. Escribe 0 para terminar.")

numero = int(input("Número: "))

while numero != 0:
    suma += numero
    numero = int(input("Número: "))

print("La suma total es:", suma)

