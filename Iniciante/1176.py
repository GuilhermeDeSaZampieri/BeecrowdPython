texto = ""
num = int(input())

for i in range(num):
    find = int(input())
    a = 0
    b = 1
    for z in range(find):
        soma = a + b
        a = b
        b = soma
    texto += f"Fib({find}) = {a}\n"

print(texto.strip())