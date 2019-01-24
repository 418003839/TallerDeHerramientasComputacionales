def MultiplosDe(x):
    i = 0
    multiplos = []
    while i:
        if i % x == 0:
            multiplos.append(i)
            i=i+1
    return multiplos
DameLax = input("Dame la x")
multiplos = MultiplosDe(DameLax)
print ("Sus multiplos son"), multiplos
