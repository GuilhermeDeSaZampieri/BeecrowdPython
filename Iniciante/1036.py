import math

v = list(map(float, input().split()))
if v[0] == 0:
    print("Impossivel calcular")
else:
    delta = math.pow(v[1],2) - (4* v[2]*v[0])
    if delta < 0:
        print("Impossivel calcular")
    else:
        r1 = (-v[1] + math.sqrt(delta)) / (v[0] * 2)
        r2 = (-v[1] - math.sqrt(delta)) / (v[0] * 2)
        print(f"R1 = {r1:.5f}")
        print(f"R2 = {r2:.5f}")

