# _*_ coding utf-8 _*_
#Convertir de grados Celsius a grados Fahrenheit y viceversa
#Calcule a cuantos gradros F equivalen 18 grados C
#Calcule a cuantos gradros C equivalen 12 grados F
C = int(input("grados en celsius:"))
F = 1.8 * C + 32
print(C, "grados celsius en farenheit son: ",F,"")
        

F = int(input("grados en farenheit:"))
C = (F - 32)/1.8
print(F, "grados celsius en farenheit son: ",C,"")

