#Escreva um script que peça o nome e a idade de todos na fila de uma balada. Crie uma lista de tuplas com os pares (nome, idade) de cada um.
#Em seguida crie e imprima duas tuplas apenas com os nomes, uma com os menores de idade que não poderão entrar, e uma com os maiores de idade 
# (idade >= 18).

def coletar_dados():
    fila = []
    while True:
        nome = input("Digite o nome (ou 'sair' para finalizar): ")
        if nome.lower() == 'sair':
            break
        idade = int(input(f"Digite a idade de {nome}: "))
        fila.append((nome, idade))
    return fila

def separar_por_idade(fila):
    menores = tuple(nome for nome, idade in fila if idade < 18)
    maiores = tuple(nome for nome, idade in fila if idade >= 18)
    return menores, maiores

# Coletando dados
fila_balada = coletar_dados()

# Separando grupos
menores_idade, maiores_idade = separar_por_idade(fila_balada)

print("\nMenores de idade (não poderão entrar):", menores_idade)
print("Maiores de idade (entrada permitida):", maiores_idade)