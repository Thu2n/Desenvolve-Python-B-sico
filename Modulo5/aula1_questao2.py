#Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao usuário o valor de n
#Biblioteca random: Função randint()
#Biblioteca math:  Função sqrt()

import random
import math

# Solicita ao usuário a quantidade de números a serem gerados
n = int(input("Digite a quantidade de números inteiros aleatórios: "))

# Gera n números inteiros aleatórios entre 0 e 100
numeros = [random.randint(0, 100) for _ in range(n)]

# Calcula a soma dos números gerados
soma = sum(numeros)

# Calcula a raiz quadrada da soma
raiz_quadrada = math.sqrt(soma)

# Exibe os resultados
print(f"Números gerados: {numeros}")
print(f"Soma dos números: {soma}")
print(f"Raiz quadrada da soma: {raiz_quadrada:.2f}")
