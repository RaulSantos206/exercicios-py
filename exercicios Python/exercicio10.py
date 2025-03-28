"""Usain Bolt é o recordista mundial dos 100 metros rasos com o tempo de 9,58 segundos.
Escreva um algoritmo que calcula a velocidade média em m/s e em km/h de um corredor,
seu algoritmo recebe como dados de entrada a distância em metros e o tempo em segundos """

tempo = float(input("Digite o tempo: "))
distPercorrido = float(input("Digite a distancaia percorrido: "))
##valorDoUsuario = int(input("Digite um valor de 0 a 99: "))

velocidadeMedia = (distPercorrido / tempo)

print(velocidadeMedia)