texto = ""
num = int(input())

for i in range(10):
    texto += f"N[{i}] = {num}\n"
    num *= 2

print(texto.strip())
