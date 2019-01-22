# _*_ coding utf-8 _*_
def fibo(n):
    f=[]
    a,b = 0,1
    i=0
    while i < n:
        print(a, b)
        a, b = b, a+b
        f.extend([a, b])
        i +=1
    print f
    return(b)
fibo(10)
print 
