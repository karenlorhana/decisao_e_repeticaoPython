#verificar se um valor é maior que o outro

valor1 = float(input("digite o primeiro valor: "))
valor2 = float(input("digite o segundo valor: "))

if(valor1 > valor2):
   print("o primeiro valor (", valor1, ") é maior que o segundo valor (", valor2, ")")
elif(valor2 > valor1):
    print("o segundo valor (", valor2, ") é maior que o primeiro valor (", valor1, ")")
else:
   print("digite valores diferentes")