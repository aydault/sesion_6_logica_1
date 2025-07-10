#6
velocidad = float(input("ingrese la velocida de su plan en Mbps: "))

if velocidad < 10: 
    print("muy lenta")
elif 10 <= velocidad <= 30: 
    print("aceptable")
elif 31 <= velocidad <= 100: 
    print ("buena")
else: 
    print("alta velocidad")