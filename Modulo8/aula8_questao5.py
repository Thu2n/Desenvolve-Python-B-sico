#Panagramas são frases que contém todas as letras do alfabeto pelo menos uma vez. Crie uma função checa_panagrama que recebe uma string e retorna True caso seja 
# um panagrama ou Falsecaso contrário. Use seu conhecimento de sets para solucionar essa questão.

#Ex:

#Entrada: "The quick brown fox jumps over the lazy dog" 
#Saída: É um panagrama
#Entrada: "Python é uma linguagem de programação" 
#aída: Não é um panagrama

import string

def checa_panagrama(frase):
    # Converter a frase para minúsculas e remover espaços
    frase = frase.lower()
    
    # Criar um conjunto com todas as letras do alfabeto
    alfabeto = set(string.ascii_lowercase)
    
    # Criar um conjunto com as letras presentes na frase
    letras_presentes = set(frase)
    
    # Verificar se todas as letras do alfabeto estão na frase
    return alfabeto.issubset(letras_presentes)

# Exemplos de uso
entrada1 = "The quick brown fox jumps over the lazy dog"
entrada2 = "Python é uma linguagem de programação"

print("É um panagrama" if checa_panagrama(entrada1) else "Não é um panagrama")
print("É um panagrama" if checa_panagrama(entrada2) else "Não é um panagrama")