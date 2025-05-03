tarefas = []
def mostrar_menu():
    print("\n--- To-Do List ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso.")
    
    elif escolha == "2":
        print("\nSuas tarefas:")
        if not tarefas:
            print("Nennhuma tarefa encontrada.")
        else:
            for i,tarefa in enumerate(tarefa, start=1):
                print(f"{i}. {tarefa}")
    elif escolha == "3":
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefa, start=1):
            print(f"{i}. {tarefa}")
        try:
            num = int(input("Digite o numero da tarefa a remover: "))
            if 1 <= num <= len(tarefas):
                removida = tarefas.pop(num - 1)
                print(f"Tarefa '{removida} removida.")
            else:
                print("Numero Invalido")
        except ValueError:
            print("Digite um numero VALIDO")
    elif escolha == "4":
        print("Saindo. . . .Ate mais!")
        break
    else:
        print("Opçao invalida.Tente novamente.")
            





# " 