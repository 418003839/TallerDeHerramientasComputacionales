Clave = 'password'
i = 0
while i < 3:
    i +=1
    Contraseña=input("introduce tu contraseña: ")
    if Clave != Contraseña:
        print("Contraseña incorrecta")
    else:
        print ("Contraseña correcta")
        break
else:
    print("Se exceddió el número de intentos")
        
