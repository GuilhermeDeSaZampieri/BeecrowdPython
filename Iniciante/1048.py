sal = float(input())

aumento = {
    400.01: 0.15,
    800.01: 0.12,
    1200.01: 0.10,
    2000.01: 0.07,
    float('inf'): 0.04
}

newsal, reajuste, percentual = 0.0,0.0,0


for n in aumento:
    if sal < n:
        percentual = aumento[n]
        reajuste += (sal * percentual)
        newsal += sal + reajuste
        break
percentual *= 100

print(f"Novo salario: {newsal:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual:.0f} %")