def lista_multiplo():
    i = 1
    while True:
        yield i
        i+= 1
    i = 0
    multiplos = []
    while i:
        if i % x == 0:
            multiplos.append(i)
            i=i+1
    return multiplos
