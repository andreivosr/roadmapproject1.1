import argparse
import os
import json
from datetime import datetime

ARQUIVO = "tasks.json"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=2)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="comando")

#ADD TASK
add = subparsers.add_parser("add")
add.add_argument('texto', type=str)

#UPDATE TASK
update = subparsers.add_parser('update')
update.add_argument('id', type=int)
update.add_argument('description', type=str)

#REMOVE TASK
remove = subparsers.add_parser('remove')
remove.add_argument('id', type=int)

args = parser.parse_args()

if args.comando == "add":
    tarefas = carregar_tarefas()

    novo_id = 1

    if tarefas:
        novo_id = max(t["id"] for t in tarefas) + 1

    agora = datetime.now().isoformat()

    nova_tarefa = {
        "id": novo_id,
        "description": args.texto,
        "status": "todo",
        "createdAt": agora,
        "updatedAt": agora
    }

    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)

    print(f"tarefa adicionada com sucesso (ID: {novo_id})")


elif args.comando == "update":
    tarefas = carregar_tarefas()
    id_update = args.id
    task_update = next((obj for obj in tarefas if obj.get("id") == id_update), None)

    if task_update is None:
        print(f"Tarefa com ID {id_update} não encontrada")
    else:
        task_update["description"] = args.description
        salvar_tarefas(task_update)

        print(f"Tarefa atualizada com sucesso (ID: {id_update})")

elif args.comando == "remove":
    tarefas = carregar_tarefas()
    id_remove = args.id
    task_remove = next((objr for objr in tarefas if objr.get("id") == id_remove), None)

    if task_remove is None:
        print(f"Tarefa com ID {id_remove} não encontrada")

    else:
        tarefas.remove(task_remove)
        salvar_tarefas(tarefas)

        print(f"Tarefa deletada com sucesso (ID: {id_remove})")






