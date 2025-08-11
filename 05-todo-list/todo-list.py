import PySimpleGUI as sg

def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as f:
            return [linha.strip() for linha in f]
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open("tarefas.txt", "w") as f:
        for tarefa in tarefas:
            f.write(tarefa + "\n")

sg.theme("DarkBlue14")

tarefas = carregar_tarefas()

layout = [
    [sg.Text("Tarefas:"), sg.Listbox(values=tarefas, size=(30, 10), key="lista", enable_events=True)],
    [sg.Input(key="nova_tarefa"), sg.Button("Adicionar"), sg.Button("Remover")],
    [sg.Button("Sair")]
]

janela = sg.Window("To-Do List", layout)

while True:
    evento, valores = janela.read()
    if evento in (sg.WINDOW_CLOSED, "Sair"):
        break

    if evento == "Adicionar":
        nova = valores["nova_tarefa"].strip()
        if nova:
            tarefas.append(nova)
            salvar_tarefas(tarefas)
            janela["lista"].update(tarefas)

    elif evento == "Remover":
        if valores["lista"]:
            tarefa_selecionada = valores["lista"][0]
            tarefas.remove(tarefa_selecionada)
            salvar_tarefas(tarefas)
            janela["lista"].update(tarefas)

janela.close()
