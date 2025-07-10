#2)

temperatura = float(input("ingresa la temperatura del paciente en celsius: "))

if temperatura < 36: 
    print("el paciente presenta hipotermia.")
elif 36 <= temperatura <= 37.5:
    print("temperatura normal.")
else:
    print("tiene fiebre")
