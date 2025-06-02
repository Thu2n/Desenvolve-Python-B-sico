#Dada uma string qualquer, use seu conhecimento de sets para apresentar os caracteres únicos que aparecem na string, ordenados alfabeticamente e sem duplicatas. 
#Preste atenção em duplicatas de maiúsculas e minúsculas.

frase = "O rato roeu a roupa do Robson"

# Converter para minúsculas e criar um conjunto com os caracteres únicos
caracteres_unicos = sorted(set(frase.lower()))

# Remover espaços para apresentar apenas os caracteres relevantes
caracteres_unicos = [c for c in caracteres_unicos if c != " "]

print(caracteres_unicos)