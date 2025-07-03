cont = 0
media = 0

for v in range(0,6):
    i = float(input())
    if i >= 0:
        cont +=1
        media += i

print(f"{cont} valores positivos\n{(media/cont):.1f}")