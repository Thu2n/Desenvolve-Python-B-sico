#Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores), 
# os armazena em uma lista e, usando fatiamento de listas, imprima:
#A lista original
#Os 3 primeiros elementos
#Os 2 últimos elementos
#A lista invertida (do fim para o começo)
#Os elementos de índice par (0, 2, 4 … )
#Os elementos de índice ímpar (1, 3, 5, … )

# Solicitar do usuário uma lista de pelo menos 4 números inteiros
while True:
    numeros = list(map(int, input("Digite pelo menos 4 números inteiros separados por espaço: ").split()))
    if len(numeros) >= 4:
        break
    print("Por favor, insira pelo menos 4 números.")

# Exibir a lista original
print("\nLista original:", numeros)

# Exibir os 3 primeiros elementos
print("Os 3 primeiros elementos:", numeros[:3])

# Exibir os 2 últimos elementos
print("Os 2 últimos elementos:", numeros[-2:])

# Exibir a lista invertida
print("Lista invertida:", numeros[::-1])

# Exibir os elementos de índice par
print("Elementos de índice par:", numeros[::2])

# Exibir os elementos de índice ímpar
print("Elementos de índice ímpar:", numeros[1::2])