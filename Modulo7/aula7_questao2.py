#Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não
# alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".

import re

# Nome dos arquivos
arquivo_origem = "frase.txt"
arquivo_destino = "palavras.txt"

# Lê o conteúdo do arquivo de origem
with open(arquivo_origem, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Remove caracteres não alfabéticos e divide em palavras
palavras = re.findall(r'\b[A-Za-zÀ-ÖØ-öø-ÿ]+\b', conteudo)

# Salva as palavras no arquivo de destino, uma por linha
with open(arquivo_destino, "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(palavras))

# Imprime o conteúdo do arquivo palavras.txt
with open(arquivo_destino, "r", encoding="utf-8") as arquivo:
    print(arquivo.read())