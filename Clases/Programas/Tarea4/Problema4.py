# _*_ coding utf-8 _*_
def fibo(n):
    a,b = 0,1
    i=0
    while i < n:
        print(a, b)
        a, b = b, a+b
        i +=1
fibo(10)
print 
