#Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. 
# Em seguida imprima na ordem estabelecida:
#A lista ordenada, sem modificar a lista original
#A lista original
#O índice do maior valor da lista
#O índice do menor valor da lista

import random

#Construção da lista de valores aleatorios

aleatorios = []
for i in range(20):
  valor = random.randint(-100, 100)
  aleatorios.append(valor)

  ###aleatorios.sort() modifica a lista original
  print(sorted(aleatorios))
  print(aleatorios)
  print("O maior valor está no indice: ",
        aleatorios.index(max(aleatorios)))
  
  print("O menor valor está no indice: ",
        aleatorios.index(min(aleatorios)))