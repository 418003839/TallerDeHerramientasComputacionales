# _*_ coding utf-8 _*_
def sumar(n):
    return (n* (n+1))/2
n = int(input("Numero de naturales a sumar"))
L = []
suma = sumar (n)
L.extend([suma])
print(L)

    

