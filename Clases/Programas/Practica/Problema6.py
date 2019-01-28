# -*- coding: utf-8 -*-
def fac(x,n): #defino la función
    if (n>1): #si la n es mayor que 1 
        x=fac(x,n-1) #entonces se aplica la misma formula
        x=x*n #se multiplican sus antecedentes
    else: #sino
        x=1 #si x es igual a uno
        return x #su factorial es uno
num= input("Dame un num:") #pido el numero que quiere su factorial
resultado = fac(x,n)
print(resultado)
#n * (n-1) * (n-2) * …* 2 * 1
#el programa corre en python 2.7 pero no en 3.6
