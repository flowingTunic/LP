#A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.

#entrada de dados 

valordecompra = float(input('digite o valor da compra '))

#processamento

valordaprestacao = valordecompra / 5

#saida

print(f'o valor das prestações é de R$ {valordaprestacao:.2f} reais')
