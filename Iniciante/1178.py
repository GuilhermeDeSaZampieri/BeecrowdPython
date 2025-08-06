texto = ""
t = float(input())

for q in range(100):
    texto += f"N[{q}] = {t:.4f}\n"
    t /= 2

print(texto.strip())