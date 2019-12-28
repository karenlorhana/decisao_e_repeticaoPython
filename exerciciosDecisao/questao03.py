#calcular o preço da quantidde de maçãs

# < 12 = 1,30
# >= 12 = 1,00

x = int(input("digite a quantidade de maçãs que deseja comprar: "))

if(x>=12):
   mi = x * 1.00
   print("o valor total das maçãs é: ", mi)
elif(x<12):
   m = x * 1.30
   print("o valor total das maçãs é: ", m)
