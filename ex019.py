
#O seguinte algoritmo sorteia um aluno de uma lista

from random import choice

lista = []
n = 0
while n<10:
    lista.append(str(input("Digite o nome do aluno [{}]: " .format(n))))
    n+=1
print("A pessoa escolhida foi: {} " .format(choice(lista)))