L=[]
C = int(input("grados en celsius:"))
F = 1.8 * C + 32
L.append([F])
print(C, "grados celsius en farenheit son: ",F,"")
        

F = int(input("grados en farenheit:"))
C = (F - 32)/1.8
print(F, "grados celsius en farenheit son: ",C,"")


