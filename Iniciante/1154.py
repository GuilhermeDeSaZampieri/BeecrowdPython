x = 0
c = -1
res = 0
while x >= 0:
    res += x
    c += 1
    x = int(input())

print(f"{(res / c):.2f}")