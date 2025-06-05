#Desenvolva uma função em Python chamada filtrar_dicionario que recebe um dicionário e uma lista de chaves como parâmetros e retorna um novo 
# dicionário contendo apenas as chaves que estão presentes na lista.

def filtrar_dicionario(dicionario, chaves):
    return {chave: dicionario[chave] for chave in chaves if chave in dicionario}

# Exemplo de uso
dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']
resultado = filtrar_dicionario(dados, chaves_filtradas)
print(resultado)