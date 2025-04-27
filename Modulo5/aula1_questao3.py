#Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.

import random

#Gera um numero aleatorio  entre 1 e 10

numero_aleatorio = random.randint(1, 10)

print("Tente adivinhar o numero entre 1 a 10.")

while True:
    #Solicitar o palpite do usuario

    Palpite = int(input("Digite seu Palpite: "))

    #Compara o palpite com o numero gerado

    if Palpite < numero_aleatorio:
        print("Muito baixo! Tente novamente.")
    elif Palpite > numero_aleatorio:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabens!Numero correto: {numero_aleatorio}")
        break #Interrompe a execução quando o usuario acerta