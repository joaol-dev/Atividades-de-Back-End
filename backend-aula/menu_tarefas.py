tarefas = []

while True:
    print("\n1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar situação")
    print("4 - Encerrar sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título da tarefa: ").strip()
        prioridade = input("Digite a prioridade (alta, média ou baixa): ").strip().lower()

        if titulo == "":
            print("O título da tarefa não pode estar vazio.")
        elif prioridade not in ["alta", "média", "baixa"]:
            print("Prioridade inválida. Escolha entre alta, média ou baixa.")
        else:
            tarefa = {
                "titulo": titulo,
                "prioridade": prioridade,
                "situacao": "pendente"
            }

            tarefas.append(tarefa)
            print("Tarefa cadastrada com sucesso.")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Não há tarefas cadastradas.")
        else:
            print("\nTarefas cadastradas:")

            for i, tarefa in enumerate(tarefas, start=1):
                print(
                    f"{i} - {tarefa['titulo']} | "
                    f"prioridade: {tarefa['prioridade']} | "
                    f"situação: {tarefa['situacao']}"
                )

    elif opcao == "3":
        numero = input("Digite o número da tarefa que será concluída: ")

        if numero.isdigit():
            numero = int(numero)
            indice = numero - 1

            if 0 <= indice < len(tarefas):
                tarefas[indice]["situacao"] = "concluída"
                print("Tarefa atualizada com sucesso.")
            else:
                print("Tarefa inexistente.")
        else:
            print("Número inválido. Digite apenas números.")

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha um número de 1 a 4.")