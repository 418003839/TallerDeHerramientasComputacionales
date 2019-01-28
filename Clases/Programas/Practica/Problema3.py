def SDeC(numeros): #defino una funcipon
    suma=0 #una suma
    for numero in numeros: #recorro numero en numeros
        suma+=numeros**3 # y defino la suma de los cuadrados
    return suma #pido que regrese la suma
print(SDeC(3))
