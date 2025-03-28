gols_a = int(input("Gols do time A: "))
gols_b = int(input("Gols do time b: "))

if gols_a > gols_b: 
    print (f"TIme A ganhou: {gols_a} X {gols_b}")
elif gols_a < gols_b: 
    print(f"Time B ganhou: {gols_a} X {gols_b}")
else: 
    print(f"Os dois times empataram {gols_a} X {gols_b}")
