#Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente.
# Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del.
# Você deve imprimir a lista antes e depois da deleção.

import random

# Gerar lista com 20 elementos aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

# Função para encontrar o intervalo com mais números negativos
def encontrar_maior_intervalo_negativo(lista):
    maior_inicio, maior_fim = 0, 0
    inicio_atual = None

    for i in range(len(lista)):
        if lista[i] < 0:
            if inicio_atual is None:
                inicio_atual = i
        else:
            if inicio_atual is not None:
                if i - inicio_atual > maior_fim - maior_inicio:
                    maior_inicio, maior_fim = inicio_atual, i
                inicio_atual = None

    # Caso a lista termine com um intervalo negativo
    if inicio_atual is not None and len(lista) - inicio_atual > maior_fim - maior_inicio:
        maior_inicio, maior_fim = inicio_atual, len(lista)

    return maior_inicio, maior_fim

# Encontrar e remover o maior intervalo de negativos
inicio, fim = encontrar_maior_intervalo_negativo(lista)

print("Lista original:", lista)
del lista[inicio:fim]
print("Lista após a deleção:", lista)