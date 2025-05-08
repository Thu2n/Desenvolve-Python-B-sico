#Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50.
# Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
#Ambas as listas
#A lista intersecção ordenada
#A quantidade de vezes que cada elemento aparece em cada lista
#Atenção, a lista de intersecções não pode ter duplicatas. 

import random

# Gerar duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Criar uma lista de interseção sem duplicatas
interseccao = sorted(set(lista1) & set(lista2))

# Contar a frequência de cada número em ambas as listas
contagem_lista1 = {num: lista1.count(num) for num in lista1}
contagem_lista2 = {num: lista2.count(num) for num in lista2}

# Imprimir os resultados
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista de Interseção Ordenada:", interseccao)
print("\nFrequência de cada elemento em Lista 1:")
for num, freq in contagem_lista1.items():
    print(f"{num}: {freq} vezes")

print("\nFrequência de cada elemento em Lista 2:")
for num, freq in contagem_lista2.items():
    print(f"{num}: {freq} vezes")
