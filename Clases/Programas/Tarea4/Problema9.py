Comprobar = True

while Comprobar:
    
    n = int(input("ingrese un número natural: "))
    if n > 0:
         
         Comprobar = False
         
         i= 2
         
         while i < n:
             creciente = 2
         
             esPrimo = True
         
             while esPrimo and creciente < i:
                 
                 if i % creciente == 0:
                     esPrimo = False
         
                 else:
                      creciente += 1

             if esPrimo:
         
                print(i, "es primo")
         
             i += 1

    else:
        print("El numero no es correcto")
                
