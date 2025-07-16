n = int(input())
texto = ""
for x in range(1,n+1):
   if n % x == 0:
       texto += f"{x}\n"
print(texto.strip())