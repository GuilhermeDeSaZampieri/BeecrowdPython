textoPar = ""
cont = [0,0]
textoImpar = ""
texto =""

for q in range(15):
    t = int(input())
    if t % 2 == 0:
        textoPar += f"par[{cont[0]}] = {t}\n"
        cont[0] += 1
        if cont[0] == 5:
            texto += textoPar
            textoPar = ""
            cont[0] = 0
    else:
        textoImpar += f"impar[{cont[1]}] = {t}\n"
        cont[1] += 1
        if cont[1] == 5:
            texto += textoImpar
            textoImpar = ""
            cont[1] = 0

texto += textoImpar
texto += textoPar
print(texto.strip())











