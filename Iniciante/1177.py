texto = ""
num = int(input())
t = 0

for q in range(1000):
    texto += f"N[{q}] = {t}\n"
    t += 1
    if t == num:
        t = 0

print(texto.strip())