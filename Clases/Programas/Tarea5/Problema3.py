# _*_ coding utf-8 _*_
L=[]
C = int(input("grados en celsius:"))
F = 1.8 * C + 32
A=F
print(C, "grados celsius en farenheit son: ",F,"")
        

F = int(input("grados en farenheit:"))
C = (F - 32)/1.8
B=C
L=([A,B])
print(F, "grados celsius en farenheit son: ",C,"")
print(L)
