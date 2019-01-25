L = [] #Creo una lista vacia
suma = 0 #defino una suma desde 0
def sumacuadrados(numeros): #creo la funcion
    num= (int(input("Dame los numeros: ")))#pido los numeros
    L.append(num) #hago que esos numeros se agreguen a la lista
    for num in L: #recorro la lista
        suma += num**2 #asigno a la suma la suma mas uno del numero al cuadrado
print(suma) # pido que regrese ese numeros
# PERO NO COPILAAAAAAAA
