#Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. 
# Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. Em seguida imprima:
#A lista elementos
#A soma dos valores da lista
#A média dos valores da lista

import random
#Construção da lista de valores aleatorios

lista1, lista2 = [], []
for i in range(20):
  lista1.append = (random.randint(0, 50))
  lista2.append = (random.randint(0, 50))

print(sorted(lista1))
print(sorted(lista1))

inters = []
  #Caminhar em uma lista e verificar a participação de cada elemento na segunda lista

for elemento in lista1:
    if elemento in lista2 and elemento not in inters:
      inters.append(elemento)

inters.sort()
for i in inters:
  print(f"{i}: ({lista1.count(i)}, {lista2.count(i)})")
