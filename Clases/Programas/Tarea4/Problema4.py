# _*_ coding utf-8 _*_
def fibo(n):
    a,b = 0,1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()
fibo(79999)