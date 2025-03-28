rm = int(input("Digite o RM do aluno: "))


num1 = (rm // 10) % 10
num2 = (num1 // 10) % 10
num3 = (num2 // 10) % 10
num4 = (num3 // 10) % 10
num5 = (num4 // 10) % 10
num6 = (num5 // 10) % 10

valorSoma = num1 + num2 + num3 +num4 + num5 + num6


print(valorSoma)