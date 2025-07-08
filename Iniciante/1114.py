num = 0
saida = []
while num != 2002:
    num = int(input())
    if num != 2002:
        saida.append("Senha Invalida")
saida.append("Acesso Permitido")
for s in saida:
    print(s)