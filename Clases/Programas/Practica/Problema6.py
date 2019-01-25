# -*- coding: utf-8 -*-
def fac(x,n):
    if n>0:
        x=fac(x,n-1)
        x=x*n
    else:
        x = 1, x= 2
        return x
num= input("Dame un num:")
resultado = fac(x,n)
#n * (n-1) * (n-2) * …* 2 * 1
