soma = 0
for _ in range(2) :
    entrada = input().split()
    cod = int(entrada[0])
    qtd = int(entrada[1])
    vlr = float(entrada[2])
    soma += qtd* vlr


print(f"VALOR A PAGAR: R$ {soma:.2f}")
