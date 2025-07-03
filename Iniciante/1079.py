x = int(input())
lista = []
result = []
for v in range(0,x):
    lista.append(list(map(float, input().split())))
    result.append((lista[v][0] * 2 + lista[v][1]*3 +  lista[v][2] * 5) / (2 +3+5))

for v in range(0,x):
    print(f"{result[v]:.1f}")