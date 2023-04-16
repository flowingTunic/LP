#Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%. Após o aumento, desconte 8% de impostos. Imprima o salário inicial, o salário com o aumento e o salário final.

#entrada de dados

salario_funcionario = float(input('digite o valor do seu salirio R$ '))

aumento = 0.15 * salario_funcionario

impostos = 0.08 * salario_funcionario

# processamento

soma_aumento = salario_funcionario + aumento

soma_final = soma_aumento - impostos 

# saida

print(f'seu salario R${salario_funcionario:.2f}: seu salario com o aumento {soma_aumento:.2f} e agora o valor final descontando os impostos {soma_final:.2f}')
