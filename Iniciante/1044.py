v = list(map(int, input().split()))

print("Sao Multiplos") if v[0] % v[1] == 0 or v[1] % v[0] == 0 else print("Nao sao Multiplos")