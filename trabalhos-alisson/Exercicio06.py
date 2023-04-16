#Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).

#entrada de dados
aluno = str(input('digite seu nome '))
prova1= float(input('digite o valor da prova 1 ')) 
prova2= float(input('digite o valor da prava 2 ')) 
prova3= float(input('digite o valor da prova 3 ')) 

#processamento

media = prova1 + prova2 + prova3 
media / 3

#saida

print(f'a media do {aluno} é de {media}')