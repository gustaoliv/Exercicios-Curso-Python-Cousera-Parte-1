n = int(input("Digite o valor de n: "))
fat = 1



if n != 0:
    while n >= 1:
        fat *= n
        n -= 1

print(fat)