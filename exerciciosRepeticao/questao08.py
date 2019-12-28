#anos em que zé será maior do que chico

chicoAlt = 1.50
chicoCresce = 0.02
zeAlt = 1.10
zeCresce = 0.03
ano = 0

while zeAlt <= chicoAlt:
 zeAlt += zeAlt * zeCresce
 chicoAlt += chicoAlt * chicoCresce
 ano += 1

print ("o zé será maior que o chico em", ano,"anos")
