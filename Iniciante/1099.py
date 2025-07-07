quest = int(input())
soma = []
for t  in range(0, quest):
    valores = list(map(int, input().split()))
    resu = 0
    for z in range(min(valores)+1, max(valores)):
        if z%2 != 0:
            resu +=z
    soma.append(resu)

for s in soma:
    print(s)


