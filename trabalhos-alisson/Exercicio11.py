#Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a. m.

#entrada de dados

vd = float(input('digite o valor do deposito '))
rd = 0.0070

#processamento

total = vd * rd

#saida

print(f'graças ao rendimento mensal da sua poupança o valor R$ {vd} rendeu R$ {total:.2f} reais ')