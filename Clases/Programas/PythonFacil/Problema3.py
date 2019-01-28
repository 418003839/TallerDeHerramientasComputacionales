a=0 #defino una variable
n=int(input("Ingrese numero")) #pido el numero a evaluar

for i in range(1,n+1): #con for hago que pase por 1 y n+1
 if(n % i==0): # comparo su reciduo. Si es 0 entonces es dibisible
  a=a+1 #doy una asignacion para que verifique cuandos divisores tiene
  
if(a!=2): #a debe ser distinto de 2. porque si es 2, entonces se divide el solo y 1
    print("No es primo") #si tiene mas de 2 divisores no es primo
else: #sino
 print("Es primo") #si es primo
