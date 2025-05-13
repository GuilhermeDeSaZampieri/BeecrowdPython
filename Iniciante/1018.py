dinheiro = int(input())
notas = [100,50,20,10,5,2,1]
contar = []
r = 0
print(dinheiro)
while(r < len(notas)):
    contar.append( dinheiro // notas[r])
    print(f"{contar[r]} nota(s) de R$ {notas[r]},00")
    dinheiro -= notas[r] * contar[r]
    r += 1


