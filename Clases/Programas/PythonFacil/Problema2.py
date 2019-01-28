lista1=[] #creo una lista
def sumalmatriz(SC, SF): #defino una funcion con dos argumentos suma columnas, suma filas
    for i in range(5): #Recorro la lista y la limito a 5 datos
        valor=int(input("Ingrese un dato:")) #pido los datos
        lista1.append(valor) #agrego los datos a la lista
       if len(SC) == 1: #si la longitud de la lista es uno, aquí me marca error
            return SC[0] #su suma es eĺ mismo
       else: #si es mayor a uno
            return SC[0] + sumamatriz(SC[1:]) #su suma es el acumulado desde el indice uno
#analogamente lo hago con las filas
if len(SF) == 1: 
            return SF[0]
       else:
            return SF[0] + sumamatriz(SF[1:])
    

print(sumamatriz([lista1)) #pido que la funcion se apliqe a la lista 


