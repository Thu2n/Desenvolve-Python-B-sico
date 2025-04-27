#Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação apresentada a seguir:

from datetime import datetime

# Obtém a data e hora atuais
agora = datetime.now()

# Formata a saída para "DD/MM/AAAA HH:MM:SS"
data_hora_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

# Exibe o resultado
print(f"Data e hora atual: {data_hora_formatada}")