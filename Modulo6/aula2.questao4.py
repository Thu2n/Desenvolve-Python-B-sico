#Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores.
#Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista,
#adicionando ao final os elementos remanescentes da maior lista.

def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    tamanho_minimo = min(len(lista1), len(lista2))

    # Intercalar os elementos até o final da menor lista
    for i in range(tamanho_minimo):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])

    # Adicionar os elementos restantes da lista maior
    lista_intercalada.extend(lista1[tamanho_minimo:])
    lista_intercalada.extend(lista2[tamanho_minimo:])

    return lista_intercalada

# Receber as listas do usuário
lista1 = list(map(int, input("Digite os números da primeira lista separados por espaço: ").split()))
lista2 = list(map(int, input("Digite os números da segunda lista separados por espaço: ").split()))

# Criar a lista intercalada
lista_intercalada = intercalar_listas(lista1, lista2)

# Imprimir o resultado
print("\nLista 1:", lista1)
print("Lista 2:", lista2)
print("Lista Intercalada:", lista_intercalada)