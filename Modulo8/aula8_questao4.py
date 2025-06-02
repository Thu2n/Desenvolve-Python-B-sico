#Considere duas listas que são duplicatas uma da outra, exceto por um elemento, exemplo:

#A = [1, 4, 5, 7, 9]
#B = [4, 5, 7, 9]
#Encontre e apresente o elemento diferente, informando também qual das listas está desfalcada. Para o exemplo acima, a saída esperada é

#O elemento 1 está faltando na segunda lista

def elemento_faltando(lista1, lista2):
    # Converter listas em conjuntos e calcular a diferença
    diferenca = set(lista1) - set(lista2)
    
    if diferenca:
        elemento = diferenca.pop()
        print(f"O elemento {elemento} está faltando na segunda lista.")
    else:
        print("As listas são idênticas ou a primeira lista está desfalcada.")

# Exemplo de uso
A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]

elemento_faltando(A, B)