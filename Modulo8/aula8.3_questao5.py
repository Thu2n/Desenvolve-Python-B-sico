#Você está responsável por analisar os resultados de uma votação. Cada voto é representado por um dicionário com o nome do candidato e a 
# quantidade de votos que recebeu em uma determinada sessão eleitoral. Escreva uma função chamada resultado_votacao que recebe uma lista de 
# dicionários de votos e retorna um dicionário onde as chaves são os nomes dos candidatos, e os valores são tuplas (total, percentual) com o 
# total de votos recebidos por cada candidato e o percentual em relação à soma total de votos em todos os candidatos.

def resultado_votacao(lista_votos):
    total_votos = {}
    
    # Somando os votos de cada candidato
    for sessao in lista_votos:
        for candidato, votos in sessao.items():
            total_votos[candidato] = total_votos.get(candidato, 0) + votos

    # Calculando o total geral de votos
    soma_total = sum(total_votos.values())

    # Criando o dicionário com totais e percentuais
    resultado = {candidato: (votos, round((votos / soma_total) * 100, 2)) for candidato, votos in total_votos.items()}
    
    return resultado

# Exemplo de uso
votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]

resultado = resultado_votacao(votos)
print(resultado)