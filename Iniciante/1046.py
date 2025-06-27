temp = list(map(int, input().split()))

duracao =  24-(temp[0]-temp[1]) if temp[0] >= temp[1] else(temp[1]) -  (temp[0])

print(f"O JOGO DUROU {duracao} HORA(S)")