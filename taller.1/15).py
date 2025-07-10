#15
a = float(input("Ingrese el primer lado: "))
b = float(input("Ingrese el segundo lado: "))
c = float(input("Ingrese el tercer lado: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("triangulo equilatero")
    elif a == b or a == c or b == c:
        print("triangulo isosceles")
    else:
        print("Triangulo escaleno")
else:
    print("no es un triangulo valido")