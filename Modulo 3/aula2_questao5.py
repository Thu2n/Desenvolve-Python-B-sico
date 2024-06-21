genero = str (input("Escreva seu gênero:M para Masculino e F para Feminino: "))
idade = int (input("Escreva sua idade: "))
tempo = int (input("Digite quantos anos trabalhados: "))

if genero=="M" and idade >= 65: 
    print ("Pode aposentar: True")
elif genero=="F" and idade >= 60: 
    print ("Pode aposentar: True")
elif genero=="F" or genero=="M" and tempo >= 30: 
    print ("Pode aposentar: True")
elif genero=="F" or genero=="M" and idade >=60 and tempo >= 25: 
    print ("Pode aposentar: True")
else:
    print ("Pode aposentar: False")