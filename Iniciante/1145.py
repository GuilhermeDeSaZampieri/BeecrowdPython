x = list(map(int, input().split()))
num = 1
for a in range(1, (x[1]//x[0])+1):
    texto = ""
    for b in range(0,x[0]):
        texto += f"{num++b} "
    print(f"{texto.strip()}")
    num+=x[0]
