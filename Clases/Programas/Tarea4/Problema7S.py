# _*_ coding utf-8 _*_
#Dados 10 datos indica el mayor, el menor y el promedio
#Ejemplo
#Calcula el mayor, menor y el promedio de los siguientes números
# 12, 43, 76, 90, 76, 89, 76, 45, 78, 55
list = [12, 43, 76, 90 ,76 , 89, 76, 45, 78, 55]
suma = 0
i = 0
for elemento in list:
    suma += elemento
    i += 1

promedio = suma / i
print (max(list))
print (min(list))
print(promedio)
