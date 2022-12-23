##Esse exercício calcula a quantidade de tinta necessária para se pintar uma parede com base em sua área

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura*altura
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m²" .format(largura, altura, area))
print("Para pintar a parede você precisará de {} litros de tinta" .format(area/2))