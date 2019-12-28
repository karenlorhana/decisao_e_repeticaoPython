#cadastro de usuário (simples)

user = str(input("digite o seu nome de usuário: "))
senha = str(input("digite sua senha: "))

while user == senha:
   print("o seu nome de usuário não pode ser igual a senha")
   user = str(input("digite outro nome de usuário: "))
   senha = str(input("digite outra senha: "))
print("usuário ", user, " foi cadastrado com sucesso!")
