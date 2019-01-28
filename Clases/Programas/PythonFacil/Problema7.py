l = [1,2,6,8] #creo una lista
def f(l): #copio el codigo del libro
    a = 0
    b = 0

    for i in l:
        if i > 0:
            a += i
        else:
            a-= i
    return a + b

