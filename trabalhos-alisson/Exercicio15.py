#Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de saída:
#Ex: Tibúrcio, você já viveu 6935 dias.

#entrada de dados

nome = str(input('digite o seu nome '))
idade = int(input('digite sua idade '))
um_ano = 365

#processamento 

mult = idade * um_ano

#saida

print(f'{nome}, você já viveu {mult} dias ')