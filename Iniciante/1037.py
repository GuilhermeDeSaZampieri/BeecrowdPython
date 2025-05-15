intervalo = [0, 25, 50, 75, 100]
recebe = float(input())
if recebe >= intervalo[0] and  recebe <= intervalo[1]:
    print(f"Intervalo [{intervalo[0]},{intervalo[1]}]")
elif recebe > intervalo[1] and  recebe <= intervalo[2]:
    print(f"Intervalo ({intervalo[1]},{intervalo[2]}]")
elif recebe > intervalo[2] and  recebe <= intervalo[3]:
    print(f"Intervalo ({intervalo[2]},{intervalo[3]}]")
elif recebe > intervalo[3] and  recebe <= intervalo[4]:
    print(f"Intervalo ({intervalo[3]},{intervalo[4]}]")
else:
    print("Fora de intervalo")