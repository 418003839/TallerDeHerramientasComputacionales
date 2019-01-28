
lista1=[] #Creo una lista vacia 
for i in range(5): #Recorro esta lista y le digo que solo llegue a 5
    valor=int(input("Ingrese un dato:")) #pido los valores de las litas
    lista1.append(valor) #agrego los valores a la lista
print(lista1) #imprimo la lista
#procdimiento analogo al caso anterior
lista2=[] 

for i in range(5):
    valor=int(input("Ingrese un dato:"))
    lista2.append(valor)
print(lista2)


if lista1==lista2: #Comparo las dos litas creadas
    print("Las listas son iguales") #si son iguales se imprime esto
else: #sino 
    print("Las listas no son iguales") #esto
