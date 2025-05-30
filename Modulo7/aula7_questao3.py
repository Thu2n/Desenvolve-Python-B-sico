#Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" e salve em seu computador com o nome "estomago.txt". Em seguida crie um script em Python que abra o 
# arquivo para leitura e imprima: 
#O texto das primeiras 25 linhas
#O número de linhas do arquivo
#A linha com maior número de caracteres
#O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring 
#"iria" se ela fizer parte de outras palavras).

import re

# Nome do arquivo
nome_arquivo = "estomago.txt"

# Lê todas as linhas do arquivo
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# Exibe as primeiras 25 linhas
print("Texto das primeiras 25 linhas:")
print("".join(linhas[:25]))

# Número total de linhas
num_linhas = len(linhas)
print(f"\nNúmero de linhas do arquivo: {num_linhas}")

# Encontrar a linha com maior número de caracteres
linha_maior = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres:\n{linha_maior.strip()}")

# Contar menções aos nomes "Nonato" e "Íria"
contagem_nonato = sum(len(re.findall(r'\b[nN]onato\b', linha)) for linha in linhas)
contagem_iria = sum(len(re.findall(r'\b[iI]ría\b', linha)) for linha in linhas)

print(f"\nNúmero de menções ao nome 'Nonato': {contagem_nonato}")
print(f"Número de menções ao nome 'Íria': {contagem_iria}")