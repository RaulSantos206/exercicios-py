valor_vista = float(input("Valor a vista do IPTU: "))
parcela = float(input("parcela: "))
valor_real = parcela *10 

desconto = valor_real - valor_vista
desc_perc = desconto / valor_vista

print(f"O desconto concedido é {desc_perc:.2f}%")
