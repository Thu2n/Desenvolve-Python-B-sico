#Crie uma função chamada mesclar_dicionarios que recebe dois dicionários como parâmetros e retorna um novo dicionário contendo a fusão dos dois.
#Se houver chaves comuns, o maior valor deve prevalecer.

def mesclar_dicionarios(dic1, dic2):
    resultado = dic1.copy()  # Cria uma cópia do primeiro dicionário
    for chave, valor in dic2.items():
        resultado[chave] = max(valor, resultado.get(chave, valor))
    return resultado

# Exemplo de uso
dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}
resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)