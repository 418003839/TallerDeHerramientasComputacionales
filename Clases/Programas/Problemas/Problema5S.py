# _*_ coding utf-8 _*_
#Calcular la suma desde i=1 hasta n de i
#Calcule la suma de 1+2...+100
def sumar(n):
    return (n* (n+1))/2
n = int(input("Numero de naturales a sumar"))
suma = sumar (n)
print ("resultado: ", suma)

