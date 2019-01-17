# _*_ coding utf-8 _*_
#Calcule el termino numero 20 de la suceción de fibonacci
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 #Para cácular el valor n de la sucecion de fibonacci basta correr el codigo y suplir la n por el valor que deseemos
#Ejemplo fibonacci(19) = 4181
