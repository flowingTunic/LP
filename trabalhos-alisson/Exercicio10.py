#Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.

#entrada de dados

nome= str(input('nome do vendedor '))
slfx= float(input('digite seu salario '))
tve= float(input('digite o total de vendas efetuadas '))

#processamento

slf = tve * 0.15
sf= slfx + slf

#saida


print(f'o salario do(a) {nome} fixo é no valor de R$ {slfx:.2f} mas já que ele(a) teve um total de vendas no valor de R$ {tve:.2f} seu salario final será de R$ {sf:.2f}')