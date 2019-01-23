def fib(n):
    if n>2:
        return fib(n-1) + fib(n-2)
    else:
        return 1

def suma(n):
    if n>1:
        return n + suma(n-1)
    else:
        return(1)


def printr(L):
    if L:
        print L[0],
        printr(L[1:])
    else:
        None

def printr1(L):
    T=25
    if len(L)>1:
        print L[0],
        printr(L[1:])
    else:
        print(L[0])

def f1():
    return 2*x

T=[25,1,4,1,4]
fib(1)
fib(2)
fib(5)
fib(10)
print([2,1,2,1,2])
print([4,1,4,1,4,1,4])
print T
