import json
from pathlib import Path

ARQUIVO = Path("tarefas.json")


def carregar_tarefas():
    if not ARQUIVO.exists():
        return []

    try:
        return json.loads(ARQUIVO.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def salvar_tarefas(tarefas):
    ARQUIVO.write_text(
        json.dumps(tarefas, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def listar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n===== TAREFAS =====")

    for tarefa in tarefas:
        status = "X" if tarefa["concluida"] else " "
        print(f'{tarefa["id"]}. [{status}] {tarefa["titulo"]}')


def adicionar_tarefa(tarefas):
    titulo = input("\nDigite a tarefa: ").strip()

    if not titulo:
        print("A tarefa não pode ficar vazia.")
        return

    novo_id = max(
        (tarefa["id"] for tarefa in tarefas),
        default=0
    ) + 1

    nova_tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "concluida": False
    }

    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)

    print("Tarefa adicionada com sucesso!")


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    if not tarefas:
        return

    try:
        tarefa_id = int(
            input("\nDigite o ID da tarefa que deseja concluir: ")
        )
    except ValueError:
        print("Digite apenas um número.")
        return

    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:

            if tarefa["concluida"]:
                print("Essa tarefa já está concluída.")
                return

            tarefa["concluida"] = True
            salvar_tarefas(tarefas)

            print("Tarefa concluída com sucesso!")
            return

    print("Tarefa não encontrada.")


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)

    if not tarefas:
        return

    try:
        tarefa_id = int(
            input("\nDigite o ID da tarefa que deseja remover: ")
        )
    except ValueError:
        print("Digite apenas um número.")
        return

    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefas.remove(tarefa)
            salvar_tarefas(tarefas)

            print("Tarefa removida com sucesso!")
            return

    print("Tarefa não encontrada.")


def menu():
    tarefas = carregar_tarefas()

    while True:
        print("""
=========================
      LISTA DE TAREFAS
=========================

1 - Listar tarefas
2 - Adicionar tarefa
3 - Concluir tarefa
4 - Remover tarefa
0 - Sair
""")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_tarefas(tarefas)

        elif opcao == "2":
            adicionar_tarefa(tarefas)

        elif opcao == "3":
            concluir_tarefa(tarefas)

        elif opcao == "4":
            remover_tarefa(tarefas)

        elif opcao == "0":
            print("\nPrograma encerrado. Até mais!")
            break

        else:
            print("\nOpção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    menu()