def listaMul(x): #defino una funcion
    i = 1 #una variable
    while True: #hago lo que esta en el libro
        if i % x == 0: #si el reciduo de i y x es cero, entonces son multiplios
            yield i #hago lo del libro
            i +=1 #pido que se vaya acumulando la suma 
#al correr el codigo me sale <generator object listaMul at 0x7f572faa7308>. no sé que es 
