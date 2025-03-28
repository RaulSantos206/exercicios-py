SalarioAnterior = float(input("Digite o salario anterior: "))
SalarioAtual = float(input("Digite o salario atual: "))

percentualAumento = ((SalarioAtual - SalarioAnterior) / SalarioAnterior) * 100

print("o aumento foi de: ", percentualAumento, "%")
print("agora voce ganha", SalarioAtual - SalarioAnterior, " a mais" )

