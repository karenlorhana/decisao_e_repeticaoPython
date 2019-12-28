#calcular média aluno dizendo sua média

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

media = (nota1 + nota2)/2

if(media >= 6):
   print("o aluno foi aprovado com a média ", media)
else:
   print("o aluno foi reprovado com a média ", media)
