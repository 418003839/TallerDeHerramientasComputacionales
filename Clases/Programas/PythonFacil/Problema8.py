l =[3,5,8,9] #creo una lista
def g(l): #copio el codigo del libro
    a = 0

    for i in l:
        for j in l:
            if abs(i-j) >a:
                a = abs(i-j)
        return a
