#12
# Validación de contraseña

CONTRASEÑA_CORRECTA = "python123"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    entrada = input("Introduce la contraseña: ")
    
    if entrada == CONTRASEÑA_CORRECTA:
        print("¡Acceso concedido!")
        break
    else:
        intentos += 1
        print("Contraseña incorrecta. Intentos restantes:", max_intentos - intentos)

if intentos == max_intentos:
    print("Usuario bloqueado")
