#Escreva uma função em Python chamada ordenar_tuplas que recebe uma lista de tuplas, cada uma contendo o nome de um aluno e sua respectiva 
# média, e retorna uma nova lista ordenada em ordem decrescente de médias.

def ordenar_tuplas(lista):
    return sorted(lista, key=lambda x: x[1], reverse=True)

# Exemplo de uso
alunos_notas = [('Alice', 8.5), ('Bob', 7.2), ('Charlie', 9.0), ('David', 8.8)]
resultado = ordenar_tuplas(alunos_notas)
print(resultado)