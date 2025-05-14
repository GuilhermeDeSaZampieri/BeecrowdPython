dinheiro = float(input())
notas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]
contar = []
r = 0
valor = round(dinheiro * 100)

print("NOTAS:")
while r < 6:
    nota_valor = round(notas[r] * 100)
    contar.append(valor // nota_valor)
    print(f"{int(contar[r])} nota(s) de R$ {notas[r]:.2f}")
    valor %= nota_valor
    r += 1

print("MOEDAS:")
while r < 12:
    moeda_valor = round(notas[r] * 100)
    contar.append(valor // moeda_valor)
    print(f"{int(contar[r])} moeda(s) de R$ {notas[r]:.2f}")
    valor %= moeda_valor
    r += 1
