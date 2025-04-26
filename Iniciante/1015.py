import math

entrada = input().split()
x1 = float(entrada[0])
y1 = float(entrada[1])
entrada2 = input().split()
x2 = float(entrada2[0])
y2 = float(entrada2[1])

soma = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2) )

print(f"{soma:.4f}")