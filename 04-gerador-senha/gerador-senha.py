import PySimpleGUI as sg
import random
import string

sg.theme("DarkBlue14")

layout = [
    [sg.Text("Tamanho da senha:"), sg.Input(key="tamanho", size=(5, 1))],
    [sg.Checkbox("Letras", default=True, key="letras")],
    [sg.Checkbox("Números", default=True, key="numeros")],
    [sg.Checkbox("Símbolos", default=True, key="simbolos")],
    [sg.Button("Gerar"), sg.Button("Sair")],
    [sg.Text("", size=(30, 1), key="senha")]
]

janela = sg.Window("Gerador de Senhas", layout)

while True:
    evento, valores = janela.read()
    if evento in (sg.WINDOW_CLOSED, "Sair"):
        break

    if evento == "Gerar":
        try:
            tamanho = int(valores["tamanho"])
            caracteres = ""

            if valores["letras"]:
                caracteres += string.ascii_letters
            if valores["numeros"]:
                caracteres += string.digits
            if valores["simbolos"]:
                caracteres += string.punctuation

            if not caracteres:
                janela["senha"].update("Selecione pelo menos 1 opção!")
            else:
                senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
                janela["senha"].update(senha)
        except ValueError:
            janela["senha"].update("Digite um número válido!")
