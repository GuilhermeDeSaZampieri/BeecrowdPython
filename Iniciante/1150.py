x = int(input())
y = -2 ** 31
sum = 0
cont = 0
while x >= y:
    y = int(input())

while y > sum:
    sum += (x + cont)
    cont += 1

print(cont)