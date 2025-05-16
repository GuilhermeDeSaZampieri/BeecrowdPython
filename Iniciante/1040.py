def mostrarTexto(media):
    if media >= 7.0:
        print(f"Media: {media:.1f}")
        print("Aluno aprovado.")
        return 1
    elif media < 5.0:
        print(f"Media: {media:.1f}")
        print("Aluno reprovado.")
        return 1
    else:
        print(f"Media: {media:.1f}")
        print("Aluno em exame.")
        return 0

notas = list(map(float, input().split()))
peso = [2, 3, 4, 1]
media = 0 

for cont in range(4):
    media += peso[cont] * notas[cont]

media = media / 10

if mostrarTexto(media) == 0:
    v = float(input())
    print(f"Nota do exame: {v:.1f}")
    media_final = (v + media) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")
