matriz  = []
soma = 0
linha = int(input())
tipo = input()

for i in range(144):
    matriz.append(float(input()))

for i in range(12):
    soma += matriz[(i+(12*linha))]

if tipo == "s":
    print(soma)
else:
    print(f"{(soma/12):.1f}")



