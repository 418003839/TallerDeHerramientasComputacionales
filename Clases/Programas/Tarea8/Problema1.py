
lista1=[]
for i in range(5):
    valor=int(input("Ingrese un dato:"))
    lista1.append(valor)
print(lista1)
lista2=[]

for i in range(5):
    valor=int(input("Ingrese un dato:"))
    lista2.append(valor)
print(lista2)


if lista1==lista2:
    print("Las listas son iguales")
else:
    print("Las listas no son iguales")
