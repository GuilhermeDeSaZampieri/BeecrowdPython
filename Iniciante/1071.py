x = sorted([int(input()), int(input())])
soma = 0

for v in range(x[0]+1,x[1]):
    if v % 2 != 0:
        soma += v
print(soma)
