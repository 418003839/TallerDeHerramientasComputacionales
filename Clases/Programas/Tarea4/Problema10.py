# _*_ coding utf-8 _*_
Comprobar = True

while Comprobar:
        Calificación =int(input("calificación: "))
        if Calificación < 0:
                Comprobar = False
        
        if Calificación>=6:
                print("Aprobado")
        else:
                
                print ("reprobado")

        
