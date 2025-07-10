#3)
# Solicitar datos al usuario
edad = int(input("Ingresa tu edad: "))
estatura = float(input("Ingresa tu estatura en metros: "))

if edad >= 12 and estatura >= 1.40:
    print("puedes subir")
else:
    print("no puedes subir")