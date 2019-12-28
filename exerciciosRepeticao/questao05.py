#quantos anos a taxa de crescimento populacional de um país ultrapassará a outra

paisA = int(input("informe a população do país A: "))
paisB = int(input("informe a população do país B: "))
taxaA = float(input("informe a taxa de crescimento do país A: "))
taxaB = float(input("informe a taxa de crescimento do país B: "))
ano = 0

taxaA = taxaA / 100
taxaB = taxaB / 100

while paisA <= paisB:
    paisA += paisA * taxaA
    paisB += paisB * taxaB
ano += 1

print ( "o país A ultrapassa ou iguala o país B em ", ano," anos")