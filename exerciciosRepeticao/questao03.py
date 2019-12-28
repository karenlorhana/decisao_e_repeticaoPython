#estruturade repetição onde o valor informado não pode ser menor que 0 ou maior que 10

nota = float(input("informe uma nota: "))

while nota < 0 or nota > 10 :
   print("valor invalido")
   nota = float(input("informe outra nota: "))
print(nota)