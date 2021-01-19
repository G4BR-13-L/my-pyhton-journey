
#Esse algoritimo calcula o valor do aluguel de um carro. Cada dia de aluguel equivale a 60 e cada quilometro rodado 0.15

dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos quilometros foram rodados? "))
print("o valor do aluguel é de: R${:.2f}" .format(dias*60+km*0.15))