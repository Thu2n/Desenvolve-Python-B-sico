n = int(input("Digite um numero inteiro: "))

maior=0

while n > 0:
    x=int(input("Digite outro numero inteiro: "))
    if x > maior:
        maior = x
    n = n-1
else:
    n = n-1
print("maior")
