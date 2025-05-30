import csv

# Nome do arquivo CSV
arquivo_csv = "spotify-2023.csv"

# Abrindo o arquivo para leitura
with open(arquivo_csv, "r", encoding="latin-1") as arquivo:
    leitor = csv.reader(arquivo)
    
    # Lendo as cinco primeiras linhas
    for i, linha in enumerate(leitor):
        print(linha)
        if i == 4:  # Exibir apenas as cinco primeiras linhas
            break