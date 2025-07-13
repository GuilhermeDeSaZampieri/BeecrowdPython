x = 1
tex =[]
while x!=0:
    x = int(input())
    if x!= 0:
        texto = ("")
        for a in range(1,x+1):
            texto += f"{a} "
        tex.append(texto.strip())

for a in tex:
    print(a)