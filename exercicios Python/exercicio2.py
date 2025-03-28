PrecoProduto = int(input("Digite o preço do produto: "))
desconto = 0

if PrecoProduto <= 100:
    desconto = PrecoProduto * 0.10  # 10% de desconto
elif PrecoProduto <= 150:
    desconto = PrecoProduto * 0.15  # 15% de desconto
else:
    desconto = PrecoProduto * 0.20  # 20% de desconto

print("Você tem o desconto de: R$", desconto)