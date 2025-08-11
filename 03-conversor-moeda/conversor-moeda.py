import PySimpleGUI as sg

sg.theme("DarkBlue14")

taxa_dolar = 5.10
taxa_euro = 5.60

layout = [
    [sg.Text("Valor em R$: "), sg.Input(key="reais")],
    [sg.Button("Converter"), sg.Button("Sair")],
    [sg.Text("", size=(30, 1), key="resultado_dolar")],
    [sg.Text("", size=(30, 1), key="resultado_euro")]
]

janela = sg.Window("Conversor de Moeda", layout)

while True:
    evento, valores = janela.read()
    if evento in (sg.WINDOW_CLOSED, "Sair"):
        break

    if evento == "Converter":
        try:
            reais = float(valores["reais"])
            janela["resultado_dolar"].update(f"US$: {reais / taxa_dolar:.2f}")
            janela["resultado_euro"].update(f"€: {reais / taxa_euro:.2f}")
        except ValueError:
            janela["resultado_dolar"].update("Erro: valor inválido")
            janela["resultado_euro"].update("")
