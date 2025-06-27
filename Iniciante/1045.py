tri = list(map(float, input().split()))
newTri = sorted(tri, reverse=True)

if newTri[0] >= newTri[1] + newTri[2]:
    print("NAO FORMA TRIANGULO")
else:
    newTri = [elemento ** 2 for elemento in newTri]
    if newTri[0] == newTri[1] + newTri[2]:
        print("TRIANGULO RETANGULO")
    if newTri[0] > newTri[1] + newTri[2]:
        print("TRIANGULO OBTUSANGULO")
    if newTri[0] < newTri[1] + newTri[2]:
        print("TRIANGULO ACUTANGULO")
    if newTri[0] == newTri[1] == newTri[2]:
        print("TRIANGULO EQUILATERO")
    if newTri[0] == newTri[1] and newTri[2] != newTri[0] or newTri[2] == newTri[0] and newTri[1] != newTri[2] or newTri[2] == newTri[1] and newTri[2] != newTri[0]:
        print("TRIANGULO ISOSCELES")

