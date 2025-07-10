#7
valor_compra = float(input("ingrese el valor total de la compra: "))
if valor_compra < 100.000:
    print("sin descuento")
elif 100000 <= valor_compra <= 200000: 
    print("aplica un 5% de descuento") 
else:
    print("aplica un 10% de descuento")