dist_metros = int(input(f"distancia em metros: "))
tempo_seg = int(input(f"Tempo em segundos: "))

velocidade = dist_metros / tempo_seg 
print(f"velocidade em e/s: {velocidade}")

dist_km = dist_metros / 1000
tempo_h = tempo_seg / 3600
vel_kmhora = dist_km / tempo_h

print(f"Velocidade em km/h: {vel_kmhora}")
