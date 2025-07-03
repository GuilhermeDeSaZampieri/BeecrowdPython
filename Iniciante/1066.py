cont = [0,0,0,0]
for v in range(0, 5):
    i = int(input())
    if i % 2 == 0:
        cont[0] += 1
    else:
        cont[1] +=1

    if i > 0:
        cont[2] +=1
    if i< 0:
        cont[3] +=1

print(f"{cont[0]} valor(es) par(es)\n"
      f"{cont[1]} valor(es) impar(es)\n"
      f"{cont[2]} valor(es) positivo(s)\n"
      f"{cont[3]} valor(es) negativo(s)")