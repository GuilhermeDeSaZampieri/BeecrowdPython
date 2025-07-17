n = 1
texto = ""
while n != 0:
    n = int(input())
    if n == 0:
        break
    par = 0
    for i in range(5):
        if n % 2 != 0:
            n += 1
        par += n
        n += 2
    texto += f"{par}\n"

print(texto.strip())