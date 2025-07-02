dia = list( input().split())
hms = list( input().split(" : "))
dia2 = list( input().split())
hms2 = list( input().split(" : "))

duracaoi = int(hms[0]) * 60 + int(hms[1])
duracaof = int(hms2[0]) * 60 + int(hms[1])

duracao = duracaoi - duracaof

if duracao <= 0:
    duracao += 24*60

horas =  duracao // 60
minutos = duracao % 60
segundos = abs(int(hms[2]) - int(hms2[2]))

print(f"{abs(int(dia[1])-int(dia2[1]))} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")