def somar(a,b):
    return a + b
def subtrair(a,b):
    return a - b
def dividir(a,b):
    if b != 0:
        return a / b
    else:
        return"Erro ao dividir por 0"
def multiplicar(a,b):
    return a * b

print("Escolha sua operaçao")
print("1 - soma ")
print("2 - subtraçao")
print("3 - divisao")
print("4 - multiplicar")

opcao = input("Digite a opção (1/2/3/4): ")

num1 = float(input("Digite seu primeiro numero"))
num2 = float(input("Digite seu segundo numero"))

if opcao == '1':
    print("Resultado:", somar(num1, num2))
elif opcao == '2':
    print("Resultado:", subtrair(num1, num2))
elif opcao == '3':
    print("Resultado:", dividir(num1, num2))

elif opcao == '4':
    print("Resultado:", multiplicar(num1, num2))
else:
    print("opçao invalida")










# Ctrl + Q




#: "