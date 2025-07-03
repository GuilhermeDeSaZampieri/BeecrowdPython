x = int(input())
cont =[0,0]

for v in range(0,x):
    i = int(input())
    if i >= 10 and i <= 20:
        cont[0] += 1
    else:
        cont[1] +=1

print(f"{cont[0]} in\n{cont[1]} out")
