#O restaurante a quilo Bem-Bão cobra R$19,00 por cada quilo de refeição. Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e escreva o valor a pagar. Assuma que a balança já desconte o peso do prato.

#entrada de dados

pesoprato = float(input('digite o peso do prato use ponto ao inves de virgula ! '))

klderefeicao = 19.00

#processamento 

mult = klderefeicao * pesoprato

#saida

print(f'pagarei R${mult:.2f} por {pesoprato}Kg de comida ')







