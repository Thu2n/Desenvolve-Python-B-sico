#Vamos fazer o jogo da forca! Antes de programar: 
#Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua escolha (separadas por quebras de linha, "\n"). Essas serão as opções de palavra do jogo.
#Crie um arquivo chamado "gabarito_enforcado.txt" com o conteúdo apresentado ao final dessa questão.
#Escreva um programa em Python para executar o jogo, de acordo com as definições:
#Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
#Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
#No início exiba o número de letras na palavra como underscores;
#Permita que o jogador insira letras para adivinhar a palavra;
#Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
#Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;
#Limite o número de tentativas para 6 (as partes do enforcado).

import random

# Lendo palavras do arquivo "gabarito_forca.txt"
with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
    palavras = [linha.strip() for linha in arquivo.readlines()]

# Escolhendo aleatoriamente uma palavra
palavra = random.choice(palavras).lower()
palavra_oculta = ["_" for _ in palavra]

# Lendo os estágios do enforcado do arquivo "gabarito_enforcado.txt"
with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
    enforcado_estagios = arquivo.read().split("\n\n")

# Função para imprimir o estado do enforcado
def imprime_enforcado(erros):
    print(enforcado_estagios[erros])

# Variáveis de controle
tentativas = 6
erros = 0
letras_usadas = set()

# Loop principal do jogo
while erros < tentativas and "_" in palavra_oculta:
    print("\nPalavra: " + " ".join(palavra_oculta))
    letra = input("Digite uma letra: ").lower()

    if letra in letras_usadas:
        print("Você já usou essa letra. Tente outra.")
        continue

    letras_usadas.add(letra)

    if letra in palavra:
        for i, char in enumerate(palavra):
            if char == letra:
                palavra_oculta[i] = letra
    else:
        erros += 1
        imprime_enforcado(erros)

# Exibição do resultado
if "_" not in palavra_oculta:
    print("\nParabéns! Você acertou a palavra:", palavra)
else:
    print("\nFim de jogo! A palavra correta era:", palavra)