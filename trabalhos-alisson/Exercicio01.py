#A velocidade média de um veículo é dado pela expressão Vm= ∆S/∆t, onde: 
#∆S: variação de espaço (ponto de chegada – ponto de partida) em quilômetros
#∆t: variação de tempo (tempo final – tempo inicial) em horas
#Escreva um programa para calcular a velocidade média dada a variação espacial e a variação temporal.  

#entrada de dados 
print('para calcaular a velocidade média informe os valors a baixo ')
km = float(input('informe a quilometragem em km '))

temp = float(input('informe o tempo gasto em horas '))

#processamneto
velo_med = (km/temp)

#saida
print(f'a velocidade media vai ser de {velo_med}km/hs!')

