soma = 0

while True:
    numero = int(input("Digite um número (0 para parar): "))
    
    if numero == 0:
        break
    
    soma += numero

print("A soma de todos os números da sequência é:", soma)