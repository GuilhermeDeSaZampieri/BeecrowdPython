quant = int(input())
saida =[]
result = 0
for q in range(0,quant):
    num = list(map(int, input().split()))
    if num[1] == 0:
        result = "divisao impossivel"
    else:
        result = num[0] / num[1]
    saida.append(result)

for s in saida:
    print(s)
