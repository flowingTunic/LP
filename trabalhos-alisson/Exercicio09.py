#Um motorista deseja colocar no tanque do seu carro X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.

#entrada de dados

litrosdegas = float(input('preço do litros de gasolina '))
precogas = 5.69

#processamento

pg = litrosdegas / precogas

#saida

print(f'você consegui colocar {pg:.2f} litros no tanque ')