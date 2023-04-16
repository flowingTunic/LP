#Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina informe quanto será o valor arrecadado.

#entrada de dados
print('informe o a quantidade de camisetas vendidas ')

camisa_P = int(input('total de camisas tamanho P vendidas '))
camisa_M = int(input('total de camisas tamanho M vendidas '))
camisa_G = int(input('total de camisas tamanho G vendidas '))

cp = 10
cm = 12
cg = 15

#processamento

total_P = camisa_P * cp

total_M = camisa_M * cm

total_G = camisa_G * cg

total_final = total_P + total_M + total_G

camiseta_total = camisa_P + camisa_M + camisa_G

#saida

print(f'foram vendidas {camisa_P} camisetas P arecadação R${total_P:.2f}:foram vendidas {camisa_M} camisetas M arecadação R${total_M:.2f}:foram vendidas {camisa_G} camisetas G arecadação R${total_G:.2f}:foram vendidas {camiseta_total} camisetas no total que arecadou em R${total_final:.2f} ')
