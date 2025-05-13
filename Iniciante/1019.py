tempo = int(input())
formato = [3600,60,1]
contador = 0
a = 0
while contador < len(formato):
    a =  tempo // formato[contador]
    tempo -= a*formato[contador]
    print(f"{a}", end=":" if contador < 2 else "\n")
    contador+=1