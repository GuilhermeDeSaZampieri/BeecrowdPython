num = 0
saida = []
partida = [0, 0, 0, 0]
while num != 2:
    gols = list(map(int, input().split()))
    partida[0] +=1
    if gols[0] == gols[1]:
        partida[3] +=1
    elif gols[0] > gols[1]:
        partida[1] +=1
    else:
        partida[2] +=1
    saida.append("Novo grenal (1-sim 2-nao)")
    num = int(input())

saida.append(f"{partida[0]} grenais")
saida.append(f"Inter:{partida[1]}")
saida.append(f"Gremio:{partida[2]}")
saida.append(f"Empates:{partida[3]}")

if partida[1] > partida[2]:
    saida.append("Inter venceu mais")
elif partida[2] > partida[1]:
    saida.append("Gremio venceu mais")
else:
    saida.append("Nao houve vencedor")

for s in saida:
    print(s)
