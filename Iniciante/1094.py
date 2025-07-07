quant = int(input())
total = []
animal = {
    "C": [],
    "R": [],
    "S": []
}

for q in range(0,quant):
    total.append(input().split())
    animal[total[q][1]].append(int(total[q][0]))

todos = sum(animal["C"])+sum(animal["R"])+sum(animal["S"])

print(f"Total: {todos} cobaias\n"
      f"Total de coelhos: {sum(animal['C'])}\n"
      f"Total de ratos: {sum(animal['R'])}\n"
      f"Total de sapos: {sum(animal['S'])}\n"
      f"Percentual de coelhos: {(sum(animal['C'])/todos)*100:.2f} %\n"
      f"Percentual de ratos: {(sum(animal['R'])/todos)*100:.2f} %\n"
      f"Percentual de sapos: {(sum(animal['S'])/todos)*100:.2f} %")


