matriz  = []
soma = 0
linha = int(input())
tipo = input()

for i in range(144):
    matriz.append(float(input()))

for i in range(12):
    soma += matriz[linha]
    linha+=12

if tipo == "s":
    print(soma)
else:
    print(f"{(soma/12):.1f}")


