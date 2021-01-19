


#Esse algoritmo calcula o tamanho da hipotenusa
from math import hypot
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

print("cateto oposto: {}\ncateto adjacente: {}\nHipotenusa: {}" .format(cateto_oposto,cateto_adjacente, hypot(cateto_adjacente,cateto_oposto)))
