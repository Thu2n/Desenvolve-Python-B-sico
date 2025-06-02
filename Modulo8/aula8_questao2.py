#Desenvolva uma função em Python chamada tem_elementos_comuns() que recebe duas listas como parâmetros e retorna True se houver algum elemento comum entre as 
#duas listas, e False caso contrário. Utilize sets para resolver essa tarefa.

def tem_elementos_comuns(lista1, lista2):
    # Converter as listas em conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    # Verificar se há interseção entre os conjuntos
    return bool(conjunto1 & conjunto2)  # O operador "&" retorna a interseção entre dois conjuntos

# Exemplos de uso
print(tem_elementos_comuns([1, 2, 3], [3, 4, 5]))  # True
print(tem_elementos_comuns(["a", "b", "c"], ["d", "e", "f"]))  # False