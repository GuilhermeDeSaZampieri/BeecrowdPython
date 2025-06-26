receber = list(map(int, input().split()))
crescente = sorted(receber)

def imprimir (lista):
    for r in lista:
        print(r)

imprimir(crescente)
print("")
imprimir(receber)




# crescente = []
# maior = 0
# for r in receber:
#     if(r >= maior):
#         maior = r
#         crescente.append(r)
#     else:
#         crescente.insert(0,r)
#
# print(crescente)
#
