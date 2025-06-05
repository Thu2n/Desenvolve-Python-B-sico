#Escreva uma função em Python chamada contagem_caracteres que recebe uma string como parâmetro e retorna um dicionário onde as chaves são os 
# caracteres presentes na string e os valores são a contagem de cada caractere.

from collections import Counter

def contagem_caracteres(string):
    return dict(Counter(string))

# Exemplo de uso
frase = "python programming"
resultado = contagem_caracteres(frase)
print(resultado)