texto = ""
qtd = int(input())

for q in range(qtd):
    n = int(input())
    veri = 0
    for i in range(1,n):
        if n % i == 0:
            veri += i
    if veri == n:
        texto += f"{n} eh perfeito\n"
    else:
        texto += f"{n} nao eh perfeito\n"

print(texto.strip())