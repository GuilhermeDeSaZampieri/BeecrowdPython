x = int(input())

for v in range(1,x+1):
    if v % 2 == 0:
        print(f"{v}^2 = {pow(v,2)}")