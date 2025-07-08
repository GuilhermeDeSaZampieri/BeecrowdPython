num = 0
count = 0
media = 0
saida = []

while num != 2:
    confirmar = 0
    num = float(input())
    if num >= 0 and num <= 10:
        media += num
        count += 1
    else:
        saida.append("nota invalida")

    if count == 2:
        saida.append(f"media = {media / 2:.2f}")
        media = 0
        while confirmar != 1 and confirmar !=2:
            saida.append("novo calculo (1-sim 2-nao)")
            confirmar = int(input())
            if confirmar == 2:
                num = 2
            else:
                count = 0

for s in saida:
    print(s)