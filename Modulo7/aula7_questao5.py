#A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula". É a extensão utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou Google Sheets. Nesse exercício vamos criar uma planilha com dados sobre livros que você já leu ou gostaria de ler. Siga as instruções.
#Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir as seguintes informações: título, autor, ano de publicação e número de páginas.
#No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.
#Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha com uma quebra de linha.
#A partir da segunda linha escreva as informações de cada livro que você levantou, separando cada informação por uma vírgula (sem espaço em branco). Lembre de finalizar cada linha com uma quebra de linha.
#Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha. Como você já tem conta no Google, sugiro abrir com o Google Sheets.

import csv

# Lista de livros com título, autor, ano de publicação e número de páginas
livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Casmurro", "Machado de Assis", 1899, 304],
    ["A Revolução dos Bichos", "George Orwell", 1945, 152],
    ["Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881, 212],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 264],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1178],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 480]
]

# Criando e escrevendo no arquivo CSV
with open("meus_livros.csv", "w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    
    # Escrevendo os títulos da planilha
    escritor.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    
    # Escrevendo os dados dos livros
    escritor.writerows(livros)

print("Arquivo 'meus_livros.csv' criado com sucesso!")