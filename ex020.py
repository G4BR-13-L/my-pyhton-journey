
#Esse algoritmo coloca os itens de uma lista em ordem aleatória

import random

lista = []
n = 0
while n<4:
    lista.append(str(input("Digite o nome do aluno [{}]: " .format(n))))
    n+=1
random.shuffle(lista)
print("A ordem de apresentação será : {}" .format(lista))