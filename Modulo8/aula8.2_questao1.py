#Escreva uma função calcula_area_perimetro que recebe apenas um parâmetro dimensoes e calcula a área e o perímetro a partir das dimensões dadas.

#dimensoes é uma tupla (largura, comprimento) com as dimensões de um terreno retangular
#Sua função deve calcular e retornar as seguintes operações

#area=largura x comprimento
#perimetro = 2 x (largura + comprimento)

def calcula_area_perimetro(dimensoes):
    largura, comprimento = dimensoes
    area = largura * comprimento
    perimetro = 2 * (largura + comprimento)
    return area, perimetro

# Exemplo de uso
largura = 5
comprimento = 7
retorno = calcula_area_perimetro((largura, comprimento))

print(retorno, type(retorno))