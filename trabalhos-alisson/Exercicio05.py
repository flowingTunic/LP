#Faça um algoritmo que receba dois números e ao final mostre a soma, subtração, 
#multiplicação e a divisão dos números lidos.

#entra de dados 

n1 = int(input('digite um numero inteiro '))

n2 = int(input('digite outro numero inteiro '))

#processamento

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

#saida

print(f'o resultado da soma é {soma}')
print(f'o resultado da subritação é {sub}') 
print(f'o resultada da multiplicação {mult}')
print(f'o resultado da divizão é {div}')