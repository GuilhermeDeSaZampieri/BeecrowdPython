x = []
for v in range(0,100):
    x.append(int(input()))

print(f"{max(x)}\n{x.index(max(x)) + 1}")
