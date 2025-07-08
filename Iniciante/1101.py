pares = [1,1]
saida = []
while pares[0] > 0 and pares[1] > 0:
    par = list(map(int, input().split()))
    pares[0] = par[0]
    pares[1] = par[1]
    soma = 0
    if pares[0] > 0 and pares[1] > 0:
        for p in range(min(pares), max(pares)+1):
            soma+=p
            saida.append(f"{p} ")
        saida.append(f"Sum={soma}")

for s in saida:
    print(s, end='')
    if "Sum" in s:
        print("")