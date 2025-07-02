renda = float(input())

if renda <= 2000:
    print("Isento")
else:
    imposto = 0
    if renda > 2000: imposto += min(renda - 2000, 1000) * 0.08
    if renda > 3000: imposto += min(renda - 3000, 1500) * 0.18
    if renda > 4500: imposto += (renda - 4500) * 0.28
    print(f"R$ {imposto:.2f}")
