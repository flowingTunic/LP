#Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.

#entrada de dados

precocustoproduto = float(input('custo do produto '))
acrecimoporcentual = float(input('digite o valor da porcentagem '))

#processamento

valorsomaproduto = precocustoproduto * acrecimoporcentual
valorfinalproduto = precocustoproduto + valorsomaproduto
#saida 

print(f'o valor do produto para venda é de R$ {valorfinalproduto:.2f}')
