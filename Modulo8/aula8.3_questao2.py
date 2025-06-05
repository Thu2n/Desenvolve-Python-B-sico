#Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" e salve em seu computador com o nome "estomago.txt".
#https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt
#Escreva um script python que abre o arquivo de texto e cria um dicionário contando a quantidade de vezes que cada palavra aparece no texto.
#Em seguida ordene o dicionário de forma decrescente pelos valores. Dessa maneira ele irá apresentar as palavras mais frequentes no início.
#Apresente na tela o dicionário ordenado

from collections import Counter
import re

def contar_palavras(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read().lower()
        palavras = re.findall(r"\b\w+\b", texto)  # Remove pontuação e separa palavras
        contagem = Counter(palavras)
    return dict(sorted(contagem.items(), key=lambda x: x[1], reverse=True))

# Nome do arquivo salvo
nome_arquivo = "estomago.txt"

# Executando a contagem
resultado = contar_palavras(nome_arquivo)

# Exibindo as palavras mais frequentes
for palavra, quantidade in list(resultado.items())[:20]:  # Exibir apenas as 20 mais frequentes
    print(f"{palavra}: {quantidade}")