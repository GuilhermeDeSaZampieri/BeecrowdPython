import math

a = input().split()
b = float(a[0])
c = float(a[1])
h = float(a[2])
print(f"TRIANGULO: {b*h/2:.3f}\n"
      f"CIRCULO: {math.pow(h,2) * 3.14159:.3f}\n"
      f"TRAPEZIO: {((b+c)*h)/2:.3f}\n"
      f"QUADRADO: {math.pow(c,2):.3f}\n"
      f"RETANGULO: {b*c:.3f}")