#5
# Promedio de lista

numeros = [12, 7, 22, 5, 14, 9]
suma = 0
contador = 0

for numero in numeros:
    suma += numero
    contador += 1

promedio = suma / contador

print("La lista es:", numeros)
print("El promedio es:", promedio)
