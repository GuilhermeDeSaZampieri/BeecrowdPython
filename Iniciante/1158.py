n = int(input())
texto = ""
for x in range(n):
    num = list(map(int, input().split()))
    impar = 0
    for i in range(num[1]):
        if num[0] % 2 == 0:
            num[0] += 1
        impar += num[0]
        num[0] += 2
    texto += f"{impar}\n"

print(texto.strip())