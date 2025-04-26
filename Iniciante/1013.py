entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

maior_ab = (a + b + abs(a - b)) // 2
maior = (maior_ab + c + abs(maior_ab - c)) // 2

print(f"{maior} eh o maior")
