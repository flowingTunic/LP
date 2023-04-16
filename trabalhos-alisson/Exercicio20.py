#Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. Faça um programa para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais. Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. Não havendo moeda de um tipo, a quantidade respectiva é zero.

# entrada de dados
# pg = pergunta

moeda1centavopg = int(input('quantas moedas de 0,01 centavos você tem ? '))
moeda5centavopg = int(input('quantas moedas de 0,05 centavos você tem ? '))
moeda10centavopg = int(input('quantas moedas de 0,10 centavos você tem ? '))
moeda25centavopg = int(input('quantas moedas de 0,25 centavos você tem ? '))
moeda50centavopg = int(input('quantas moedas de 0,50 centavos você tem ? '))
moeda1realpg = int(input('quantas moedas de 1 real você tem ? '))

moeda1centavo = 0.01
moeda5centavo = 0.05
moeda10centavo = 0.10
moeda25centavo = 0.25
moeda50centavo = 0.50
moeda1real = 1

# processamento

total = moeda1centavopg * moeda1centavo + moeda5centavopg * moeda5centavo + moeda10centavopg * moeda10centavo + moeda25centavopg * moeda25centavo + moeda50centavopg * moeda50centavo + moeda1realpg * moeda1real

# saida

print(f'o valor total economizado, em reais é R${total}')