dias = int(input())
datas = [365, 30, 1]
contarAnoMesDia = 0
anoMesDia = ["ano(s)", "mes(es)","dia(s)"]
contador = 0
while contador < len(datas):
    contarAnoMesDia =  dias // datas[contador]
    dias -= contarAnoMesDia * datas[contador]
    print(f"{contarAnoMesDia} {anoMesDia[contador]}")
    contador += 1