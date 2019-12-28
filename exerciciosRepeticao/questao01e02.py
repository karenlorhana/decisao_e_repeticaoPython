#fazer uma divisão com números digitados, sendo o segundo (denominador) diferente de 0


x = int(input("digite o primeiro valor: "))
y = int(input("digite o segundo valor: "))

while y == 0:
   print("valor invalido")
   y = int(input("o segundo valor não pode ser 0, informe outro valor"))

divisao = x/y
print(divisao)