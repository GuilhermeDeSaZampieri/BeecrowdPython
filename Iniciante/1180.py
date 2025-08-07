num = int(input())
lista = list(map(int, input().split()))
menor = min(lista)
posi = lista.index(menor)

print(f"Menor valor: {menor}\nPosicao: {posi}")