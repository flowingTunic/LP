#Uma loja de roupas está fazendo uma liquidação e está oferecendo um desconto de 30% em todas as peças. Faça um programa em que o vendedor informe o valor da roupa e o programa retorna quanto ela custará durante a liquidação?
 
# entrada de dados

valordaroupa = float(input('digite o preço da roupa '))

desconto = 0.30 * valordaroupa

# processamento 

descontoroupa = valordaroupa - desconto

# saida

print(f"durante a liquidação o valor da roupa sera R$ {descontoroupa}")