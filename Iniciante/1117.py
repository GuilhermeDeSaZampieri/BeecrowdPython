nota = -1
saida = []
result = 0
count = 0
while count != 2:
    nota = float(input())
    if nota < 0 or nota > 10:
        saida.append("nota invalida")
    else:
        result += nota
        count +=1
result /= 2
saida.append(f"media = {result:.2f}")
for s in saida:
    print(s)