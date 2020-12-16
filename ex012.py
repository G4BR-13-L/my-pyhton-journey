#esse algoritmo calcula o desconto de 5% sobre o valor de um produto

valor = float(input("Digite o preço do produto: "))
print("O produto que custa R${}, com o desconto de 5% passa a custar: {:.2f}" .format(valor, valor*0.95))