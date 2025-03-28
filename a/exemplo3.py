num_a = int(input("Digite um numero: "))
op = input("Digite o operador (+-*/): ")
num_b = int(input("digite outro numero: "))

if op == '+': 
    resultado = num_a + num_b 
elif op == '-': 
    resultado = num_a - num_b
elif op == '*':
    resultado = num_a * num_b
elif op == '/': 
    resultado = num_a / num_b

else op :
    print("OPERADOR INVALIDO")
    resultado = None

print(f"O resultado da conta {num_a} {op} {num_b} é {resultado}")

