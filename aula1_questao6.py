
N=int(input("Digite o numero de experimentos realizados: "))

S =int(input("Deste valor digitado.Digite o numero de experimentos realizados com sapos: "))
R =int(input("Deste valor digitado.Digite o numero de experimentos realizados com ratos: "))
C =int(input("Deste valor digitado.Digite o numero de experimentos realizados com coelhos: "))

if N > 0:
    percentual_S = (S/ N) * 100
    percentual_R = (R/ N) * 100
    percentual_C = (C/ N) * 100

print(f"Percentual de sapos: {percentual_S:.2f}%")
print(int"Percentual de sapos: {S:}%")

print(f"Percentual de ratos: {percentual_R:.2f}%")
print(int"Percentual de ratos: {R:}%")

print(f"Percentual de coelhos: {percentual_C:.2f}%")
print(int"Percentual de coelhos: {C:}%")

