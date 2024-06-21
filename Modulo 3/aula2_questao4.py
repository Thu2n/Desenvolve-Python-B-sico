classe = str (input("Digite qual classe seu personagem pertence (guerreiro,mago,arqueiro): "))
forca = int (input("Digite os pontos de forca (de 1 a 20): "))
magia = int (input("Digite os pontos de magia (de 1 a 20): "))

if classe=="guerreiro" or classe=="mago" or classe=="arqueiro" and forca >= 1 and forca <= 20 and magia >= 1 and magia <= 20:
    print ("Pontos de atributo consistentes com a classe escolhida: True")
else:
    print ("Pontos de atributo consistentes com a classe escolhida: False")