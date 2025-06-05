#Escreva uma função em Python chamada comprimir_tuplas que recebe uma lista de tuplas, cada uma contendo uma palavra e um número, 
# e retorna uma nova lista de tuplas onde palavras idênticas são agrupadas e seus números são somados.

from collections import defaultdict

def comprimir_tuplas(lista):
    dicionario = defaultdict(int)
    for palavra, numero in lista:
        dicionario[palavra] += numero
    return list(dicionario.items())

# Exemplo de uso
tuplas_originais = [('maçã', 3), ('banana', 2), ('maçã', 5), ('laranja', 1), ('banana', 3)]
resultado = comprimir_tuplas(tuplas_originais)
print(resultado)