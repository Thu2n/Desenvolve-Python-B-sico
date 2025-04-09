N = int(input("Digite o numero de pessoas que serão inseridas as idades: "))
cont = 0
media = 0
idade = 0
while cont <= N:
      idade = int(input("Digite a primeira idade: "))
      soma += idade
      cont+= 1

      media = (soma/N)

      print("A media das idades he: {media}")