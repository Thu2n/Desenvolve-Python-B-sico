#Dada uma string, imprima todas as vogais que aparecem na string, bem como todos os índices onde elas ocorrem. Para isso, use a função enumerate.

frase = "O rato roeu a roupa da Alice"
vogais = "AEIOUaeiou"

for indice, caractere in enumerate(frase):
    if caractere in vogais:
        print(f"Vogal '{caractere}' encontrada no índice {indice}")