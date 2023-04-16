#A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra

# entrada de dados

quantidade_lanches = int(input('informe a quantidade de lanches '))

fatia_queijo = 2 * 0.050
fatia_presunto = 0.050
fatia_hamburguer = 0.100

# processamento

compra_queijo = quantidade_lanches * fatia_queijo
compra_presunto = quantidade_lanches * fatia_presunto
compra_hamburguer = quantidade_lanches * fatia_hamburguer
# saida

print(f'você precisara comprar {compra_queijo}Kg de queijo {compra_presunto}Kg de presunto e  {compra_hamburguer}Kg de carne ')

