x = list(map(int, input().split()))
sum = x[0]
for a in x:
    if a>0:
        for b in range(1,a+1):
            sum += (b -1)
print(f"{sum}")