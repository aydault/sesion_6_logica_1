#14
# Uso de break y continue

numero = 1

while True:
    if numero % 3 == 0:
        numero += 1
        continue  # Salta los múltiplos de 3

    print(numero)

    if numero == 20:
        break  # Se detiene al llegar a 20

    numero += 1

