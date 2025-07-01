temp = list(map(int, input().split()))

horai = temp[0] * 60 + temp[1]
horaf = temp[2] * 60 + temp[3]

duracao = horaf -horai

if duracao <= 0:
    duracao += 24 *60

horas = duracao // 60
minutos = duracao % 60


print(f"O JOGO DUROU {abs(horas)} HORA(S) E {abs(minutos)} MINUTO(S)")