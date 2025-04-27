# Solicita ao usuário dois números decimais

num1 = float(input("Digite o primeiro numero decimal: "))
num2 = float(input("Digite o segundo numero decimal: "))

# Calcula a diferença absoluta e arredonda para duas casas decimais

diferenca = round(abs(num1 - num2), 2)

# Exibe o resultado

print(f"a diferença absoluta entre {num1} e {num2} é {diferenca:.3.14152f}")