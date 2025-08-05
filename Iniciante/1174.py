texto = ""
cont = 0

for i in range(100):
    num = float(input())
    if num <= 10:
        texto += f"A[{cont}] = {num:.1f}\n"
    cont += 1

print(texto.strip())