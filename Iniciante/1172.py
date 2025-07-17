x = ""
for i in range(0,10):
    num = int(input())
    if num <= 0:
        x += f"X[{i}] = 1\n"
    else:
        x += f"X[{i}] = {num}\n"
print(x.strip())

