matriz  = []
tipo = input()

for i in range(144):
    matriz.append(float(input()))

soma = 0

for i in range(12):
    for p in range(12):
        if i < p:
            soma += matriz[i*12+p]

if tipo == "s":
    print(soma)
else:
    print(f"{(soma/66):.1f}")