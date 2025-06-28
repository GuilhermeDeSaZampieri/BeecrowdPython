temp = list(map(int, input().split()))

horai = temp[0] * 60 + temp[1]
horaf = temp[2] * 60 + temp[3]

horas = int(abs(horai - horaf) / 60)
minutos = abs((horai - horaf)) % 60

print(horas)
print(minutos)

if horai >= horaf:
    horas += 24

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")