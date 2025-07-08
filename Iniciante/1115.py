num = [1,1]
saida =[]
while num[0] != 0 and num[1] != 0:
    num = list(map(int, input().split()))
    if num[0] != 0 and num[1] != 0:
        if num[0] > 0 and num[1] > 0:
            saida.append("primeiro")
        elif num[0] > 0 and num[1] < 0:
            saida.append("quarto")
        elif  num[0] < 0 and num[1] < 0:
            saida.append("terceiro")
        else:
            saida.append("segundo")

for s in saida:
    print(s)