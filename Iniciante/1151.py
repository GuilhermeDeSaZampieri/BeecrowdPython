x = int(input())
texto = ""
a = 0
b = 1

for i in range(0, x):
    texto += f"{a} "
    soma = a + b
    a = b
    b = soma

print(texto.strip())