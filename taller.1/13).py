#13

year = int(input("ingrese un año: "))

if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print("Es bisiesto")
else:
    print("no es bisiesto")

