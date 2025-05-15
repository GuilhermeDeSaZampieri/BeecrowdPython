entrada = list(map(int, input().split()))
preco = [4.0, 4.5, 5.0, 2.0, 1.5]

print(f"Total: R$ {preco[(entrada[0]-1)] * entrada[1]:.2f}")

