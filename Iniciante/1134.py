x = 0
contador = {
    1:0,
    2:0,
    3:0
}
while x != 4:
    x = int(input())
    if x == 1 or x == 2 or x ==3:
        contador[x] += 1

print(f"MUITO OBRIGADO\nAlcool: {contador[1]}\nGasolina: {contador[2]}\nDiesel: {contador[3]}")


