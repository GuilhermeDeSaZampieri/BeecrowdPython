par = []
impar = []
for q in range(15):
    t = int(input())
    if t % 2 == 0:
        par.append(t)
    else:
        impar.append(t)
texto = ""
tapar = len(par)
taimpar = len(impar)
cont = 0

for i in range(15):
    if tapar > taimpar:
        texto += f"par[{cont}] = {par[cont]}\n"
        cont += 1
        if cont == 5:
            cont = 0
            tapar -= 5
    else:
        texto += f"impar[{cont}] = {impar[cont]}\n"
        cont += 1
        if cont == 5:
            cont = 0
            taimpar -= 5

print(texto.strip())