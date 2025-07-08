saida = []
num = [0,1]
while num[0] != num[1]:
    num = list(map(int, input().split()))
    if num[0] != num[1]:
        if num[0] < num[1]:
            result = "Crescente"
        else:
            result = "Decrescente"
        saida.append(result)

for s in saida:
    print(s)