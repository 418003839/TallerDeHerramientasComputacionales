# _*_ coding utf-8 _*_
Comprobar = True

while Comprobar:
        Calificacin =int(input("calificación: "))
        if Calificacin < 0:
                Comprobar = False
        
        if Calificacin>=6:
                print("Aprobado")
        else:
                
                print ("reprobado")

        
