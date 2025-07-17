texto = ""
qtd = int(input())

for q in range(qtd):
    n = int(input())
    veri = 0
    for i in range(1,n+1):
        if n % i == 0:
            veri += 1
    if veri == 2:
        texto += f"{n} eh primo\n"
    else:
        texto += f"{n} nao eh primo\n"

print(texto.strip())