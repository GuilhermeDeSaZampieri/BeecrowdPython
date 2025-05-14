v = list(map(int, input().split()))
if v[1] > v[2] and v[3]  > v[0] and (v[2]+v[3]) > (v[0]+v[1]) and v[2] > -1 and v[3] > -1 and (v[0] % 2) == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
