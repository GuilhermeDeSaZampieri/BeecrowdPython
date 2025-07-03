x = int(input())
frases =[]

for v in range(0,x):
    i = int(input())
    frase = ""
    if i % 2 == 0:
        frase += "EVEN"
    else:
        frase += "ODD"

    if i > 0:
        frase  += " POSITIVE"
    elif i <0:
        frase  +=" NEGATIVE"
    else:
        frase  = "NULL"
    frases.append(frase)

for v in range(0,x):
    print(frases[v])