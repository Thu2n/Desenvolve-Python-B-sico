#Você vai coletar de diferentes turmas de alunos seus interesses em atividades extra curriculares dentre futebol, vôlei, rugby, música, teatro, ações comunitárias. 
# Informe o conjunto de atividades comuns a todas a turmas. Pode preencher o iterável turmas com valores arbitrários.

# Lista de conjuntos contendo os interesses das turmas
turmas = [
    {'ações comunitárias', 'futebol', 'música', 'rugby'},
    {'ações comunitárias', 'música', 'rugby', 'teatro'},
    {'música', 'rugby', 'teatro', 'vôlei'},
    {'música', 'vôlei', 'rugby'},
    {'ações comunitárias', 'futebol', 'rugby', 'teatro', 'vôlei'},
    {'ações comunitárias', 'futebol', 'rugby'},
    {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
    {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
    {'ações comunitárias', 'rugby', 'vôlei'}
]

def atividades_comuns(turmas):
    # Utilizando a função de interseção para encontrar os elementos comuns em todas as turmas
    return set.intersection(*turmas)

# Obtendo o conjunto de atividades comuns
atividades_em_todas = atividades_comuns(turmas)

print(atividades_em_todas)