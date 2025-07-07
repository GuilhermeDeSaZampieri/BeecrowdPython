x = 0
while x <= 2:
    print(f"I={x} J={1+x}\n"
          f"I={x} J={2+x}\n"
          f"I={x} J={3+x}")
    x = round(x+0.2,1)
    if x == 1.0 or x ==2.0:
        x= int(x)

