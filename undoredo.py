def show_lista(td_lista):
    print()
    print('Tarefas: ')
    print(td_lista)
    print()


def adiciona(td, td_lista):
    td_lista.append(td)


def retirar(td_lista, redo_lista):
    if not td_lista:
        print('Lista vazia!')
        return

    last_td = td_lista.pop()
    redo_lista.append(last_td)


def retornar(td_lista, redo_lista):
    if not redo_lista:
        print('Lista vazia!')
        return

    last_redo = redo_lista.pop()
    td_lista.append(last_redo)


if __name__ == '__main__':
    td_lista = []
    redo_lista = []

    while True:
        resp = input('Digite a tarefa que você deseja executar, após digite [listar, retirar, retornar]: ')

        if resp == 'listar':
            show_lista(td_lista)
            continue
        elif resp == 'retirar':
            retirar(td_lista, redo_lista)
            continue
        elif resp == 'retornar':
            retornar(td_lista, redo_lista)
            continue

        adiciona(resp, td_lista)

