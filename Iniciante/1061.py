dia = list( input().split())
hms = list( input().split(" : "))
dia2 = list( input().split())
hms2 = list( input().split(" : "))

duracaoi = int(hms[0]) * 3600 + int(hms[1]) * 60 + int(hms[2])
duracaof = int(hms2[0]) * 3600 + int(hms2[1]) * 60 + int(hms2[2])

duracao = duracaof - duracaoi
dias = abs(int(dia[1])-int(dia2[1]))
minutos = (duracao % 3600) // 60

if duracao <= 0:
    duracao += 24*3600
    dias -= 1


horas =  duracao // 3600
segundos = duracao % 60

print(f"{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")