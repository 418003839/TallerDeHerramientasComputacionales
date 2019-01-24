l = [1,2,6,8]
def f(l):
    a = 0
    b = 0

    for i in l:
        if i > 0:
            a += i
        else:
            a-= i
    return a + b

