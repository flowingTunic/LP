#A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de bolos a cada dia. Cada pãozinho custa R$ 0,12 e o pedaço de bolo custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e bolos (juntos), e quanto' deve guardar numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de bolos vendidos, e depois calcular quanto arrecadou naquele dia e quanto deve guardar na poupança.

#entrada de dados

quantidadepao = int(input('digite a quantidade de pães '))
quantidadebolopedaco = int(input('digite a quantidade de bolos '))

valorpao = 0.12
valorbolopedaco = 1.50
guardacontapoupanca = 0.10
#processamento

arrecadoupao = quantidadepao * valorpao
arrecadoubolo = quantidadebolopedaco * valorbolopedaco

arecadoutotal = arrecadoupao + arrecadoubolo

poupanca = arecadoutotal * guardacontapoupanca

#saida

print(f'arecadação de pães R${arrecadoupao} arecadação de bolos R${arrecadoubolo} vendidos,arrecadação total do dia {arecadoutotal} quanto deve guardar na poupança {poupanca} ')


