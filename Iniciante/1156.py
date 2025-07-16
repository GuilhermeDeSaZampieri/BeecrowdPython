res = 1
par = 2
impar = 0
for x in range(2, 41):
    if x % 2 != 0:
        impar = x
        res += (impar / par)
        par *= 2

print(f"{res:.2f}")