#cálculo para verificar se a pessoa poderá votar ou não

nasc = int(input("digite seu ano de nascimento: "))
anoatual = int(input("digite o ano atual em que você está: "))

calc = anoatual - nasc

if(calc>=16):
   print("você poderá votar!")
else:
   print("você não poderá votar pois não atingiu a idade necessária!")