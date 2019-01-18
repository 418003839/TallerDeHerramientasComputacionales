# _*_ coding utf-8 _*_

def euc(num1, num2):
    if num2 == 0:
        return num1
    return euc(num2, num1 % num2)

num1 = int(input("Anota el número menor"))
num2 = int(input("Anota el número mayot"))

print("El MCD es:", euc(num1, num2))
