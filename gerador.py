import random
import string

def gerar_senha(tamanho=12):
    caracters = string.ascii_letters + string.digits + string.punctuation 
    senha = ''.join(random.choice(caracters) for _ in range(tamanho))
    return senha
tamanho_desejado = int(input("Qual o tamanho da senha? "))
senha = gerar_senha(tamanho_desejado)
print(f"Senha gerada com sucesso:{senha}")

 # "   : ''

