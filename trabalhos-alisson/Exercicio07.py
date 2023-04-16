#Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados. Ex: Início A vale 3 e B vale 5 no final da execução A valerá 5 e B valerá 3.

#entra de dados

A = int(input('valor de A '))
B = int(input('valor de B '))

#processamento

variavel = A
A = B
B = variavel

#saida

print(f'o valor de A é {A} e o valor de B é {B}')