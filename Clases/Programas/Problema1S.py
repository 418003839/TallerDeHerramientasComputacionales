# _*_ coding utf-8 _*_
#Encontrar el mínimo común divisor de dos número 15, 20
MCD = False
x = int(input("x"))
y = int(input("y"))

if x >0 and y > 0 and x !=y:
    i = x

    while not MCD and i >1:
        if x % i == 0 and y % i ==0:
            print("MCD es",i)
            MCD = True

        else:
            i -=1

