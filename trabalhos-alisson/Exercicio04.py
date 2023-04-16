#Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida 
#a distância total percorrida pelo automóvel e o total de combustível gasto

#entrada de dados

dtp = int(input('digite a distancia percorida em km '))

tcg = float(input('digite o total de conbistivel gasoto em litros '))

#processamento

md = dtp / tcg

#saida 

print(f'a media do veiculo é {md:.2f} ')