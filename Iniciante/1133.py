x = [int(input()), int(input())]

for a in range(min(x)+1, max(x)):
    if a % 5 == 2 or a % 5 == 3:
        print(a)