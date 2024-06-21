idade = int (input("Digite sua idade: "))
jogou = str (input("Já jogou ao menos 3 jogos de tabuleiro? Digite True para Sim e False para Não: "))
vencido = int (input("Destes 3 jogos ganhou quantas vezes? "))

if idade >= 16 and idade <= 18 and jogou != True and vencido != 0:
    print ("Apto para ingressar no clube de jogos de tabuleiro: True")
else:
    print ("Apto para ingressar no clube de jogos de tabuleiro: False")