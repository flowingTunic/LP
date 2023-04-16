#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem 
#do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a 
#percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo 
#que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

#preço carro ao consumidor + custo de fabrica com a % do distribuidor 28% e + inpostos 45% 

#custo consumidor = custo de fabrica -> custo do distribuidor + inposto

#custo distribuidor = 0.28 custo fabrica

#inposto = 0.45 custo fabrica

#entrada de dados

cdf = float(input('digite o valor do carro '))
cdd = 0.28 * cdf
imposto = 0.45 * cdf

#processamento

cdc = cdf + cdd +imposto

#saida

print(f'o valor da carro ao consumidor sera de {cdc:.2f} ')

