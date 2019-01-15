def vAbsoluto(x):
    if x>=0:
        return(x)
    else:
        return(-x)

def raiz(x):
    h=x
    b=1.0
    e=0.0001
    while vAbsoluto(b-h)>e:
        h = (b+h)/2
        b = x/h
    return(b)

def raiz1(x):
    h=x
    b=1.0
    e=0.0001 #Marca el error que deseamos
    i=0 #Cuenta el numero de veces que se ejecuta el ciclo 
    while vAbsoluto(b-h)>e:
        h = (b+h)/2
        b = x/h
        i=i+1 #Le decimos que cuenta una vez mas la veces que 
    print "El ciclo que se repitio %d veces"% (i)    
    return(b)
    
print  raiz1(1)
print raiz1(4)
print  raiz1(9)
print  raiz1(9.1)
print  raiz1(1000000)




