xy = [int(input()), int(input())]
soma= 0

for i in range(min(xy), max(xy)+1):
    if i % 13 != 0:
       soma += i
print(soma)