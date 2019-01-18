# _*_ coding utf-8 _*_


lista = []
DiezDatos  = int(input("DiezDatos: "))
mayor = 0
menor = 0
suma = 10
i= 1

while (DiezDatos > 0):
    numero = (input("Numero #" + str(i) + ": "))
    lista.append(numero)
    i = i + 1
    DiezDatos = DiezDatos - 1

promedio = suma / i 
mayor = (max(lista))
menor = (min(lista))

print ("Mayor: ", mayor)
print ("Menor: ", menor)
print (promedio)

