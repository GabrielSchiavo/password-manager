from cryptography.fernet import Fernet

# def write_key():
#    key = Fernet.generate_key()
#    with open("key.key", "wb") as key_file:
#       key_file.write(key)
#     
# write_key()

def load_key():
   file = open("key.key", "rb")
   key = file.read()
   file.close()
   return key

# master_password = input("Qual é a sua senha mestre? ")
key = load_key() # + master_password.encode()
fer = Fernet(key)

def view():
   with open('passwords.txt', 'r') as f:
      for line in f.readlines():
         data = line.rstrip()
         user, passw = data.split("|")
         print("Usuário:", user, "| Senha:", fer.decrypt(passw.encode()).decode())


def add():
   name = input('Nome da Conta: ')
   password = input("Senha: ")
   
   with open('passwords.txt', 'a') as f:
      f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
   mode = input("Deseja adicionar uma nova senha ou visualizar as existentes (digite: view ou add) ou presione q para sair? ").lower()
   if mode == "q":
      break
   
   if mode == "view":
      view()
   elif mode == "add":
      add()
   else:
      print("Modo inválido.")
      continue
     