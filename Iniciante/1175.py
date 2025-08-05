texto = ""
num = []

for i in range(20):
    num.append(int(input()))
num.reverse()

for b in range(20):
    texto += f"N[{b}] = {num[b]}\n"

print(texto.strip())