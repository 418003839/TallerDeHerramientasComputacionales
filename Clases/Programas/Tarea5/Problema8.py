Clave = 'password'
i = 0
while i < 3:
    ClavesIncorrectas =[]
    i +=1
    Contraseña=input("introduce tu contraseña: ")
    if Clave != Contraseña:
        a= Contraseña
        print("Contraseña incorrecta")
        ClavesIncorrectas.extend ([a])
    else:
        print ("Contraseña correcta")
        a= Contraseña
        ClavesIncorrectas.extend ([a])
        break
else:
    print("Se exceddió el número de intentos")
print (ClavesIncorrectas)
