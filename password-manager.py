from cryptography.fernet import Fernet

## Descomente as linhas abaixo para gerar uma nova key
# def write_key():
#    key = Fernet.generate_key()
#    with open("key.key", "wb") as key_file:
#       key_file.write(key)
    
# write_key()

def load_key():
   file = open("key.key", "rb")
   key = file.read()
   file.close()
   return key


key = load_key()
fer = Fernet(key)


## Descomentar a linha 28 para alterar a Senha Mestre
def write_token():
   typed_token = input("Digite uma nova Senha Mestre? ").encode()
   token = fer.encrypt(typed_token)
   with open("token.key", "wb") as key_file:
      key_file.write(token)
# write_token()

def load_token():
   file = open("token.key", "rb")
   token = file.read()
   file.close()
   return token


def view():
   with open('passwords.txt', 'r') as f:
      for line in f.readlines():
         data = line.rstrip()
         account, user, passw = data.split("|")
         print("Conta:",account, "| Usuário:", user, "| Senha:", fer.decrypt(passw.encode()).decode())


def add():
   accountName = input('Nome da Conta: ')
   userName = input('Nome de Usuário: ')
   password = input("Senha: ")
   
   with open('passwords.txt', 'a') as f:
      f.write(accountName + "|" + userName + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
   master_password = input("Qual é a sua Senha Mestre? ") ## Senha Mestre: 12345
   token = load_token()
   if master_password != fer.decrypt(token).decode():
      print('Senha Mestre inválida!')
      break
   
   mode = input("Deseja adicionar uma nova senha, visualizar as existentes, sair ou trocar a Senha Mestre (digite: add(adicionar), view(visualizar), q(sair) ou change(altera SM))? ").lower()
   if mode == "q":
      break
   
   if mode == "view":
      view()
   elif mode == "add":
      add()
   elif mode == "change":
      write_token()
   else:
      print("Modo inválido!")
      continue
     