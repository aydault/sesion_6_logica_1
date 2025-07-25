#15
# Búsqueda con while-else

lista = [4, 8, 15, 16, 23, 42]
numero_a_buscar = int(input("Ingresa un número para buscar: "))

i = 0
while i < len(lista):
    if lista[i] == numero_a_buscar:
        print(f"Número encontrado en el índice {i}")
        break
    i += 1
else:
    print("Número no encontrado")
