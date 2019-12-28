#imprimir os valores digitados de maneira crescente (simples)

x = float(input("digite o primeiro valor: "))
y = float(input("digite o segundo valor: "))

if x > y:
   print(y, x)
elif y > x:
   print(x, y)
else:
   print("os valores nao podem ser iguais")

