tri = list(map(float, input().split()))

if tri[0] + tri[1] > tri[2] and tri[0] + tri[2] > tri[1] and tri[2] + tri[1] > tri[0]:
    tam = sum(tri)
    print(f"Perimetro = {tam}")
else:
    tam = ((tri[0] + tri[1]) * tri[2]) / 2
    print(f"Area = {tam}")

