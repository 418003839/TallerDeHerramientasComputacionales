numeros = [2,8]
def euc(numeros):
    if numeros[1] == 0:
        return numeros[0]
    return euc([numeros[0], numeros[0] % numeros[1]])


print("El MCD es:", euc(numeros))
