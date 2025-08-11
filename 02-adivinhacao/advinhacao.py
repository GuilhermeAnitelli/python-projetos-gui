import PySimpleGUI as sg
import random

sg.theme("DarkBlue14")

numero_secreto = random.randint(1, 100)
tentativas = 0

layout = [
    [sg.Text("Digite um número de 1 a 100:")],
    [sg.Input(key="palpite")],
    [sg.Button("Enviar"), sg.Button("Sair")],
    [sg.Text("", size=(30, 1), key="mensagem")]
]

janela = sg.Window("Jogo da Adivinhação", layout)

while True:
    evento, valores = janela.read()
    if evento in (sg.WINDOW_CLOSED, "Sair"):
        break

    if evento == "Enviar":
        try:
            tentativa = int(valores["palpite"])
            tentativas += 1

            if tentativa == numero_secreto:
                janela["mensagem"].update(f"Parabéns! Acertou em {tentativas} tentativas!")
            elif tentativa < numero_secreto:
                janela["mensagem"].update("O número é MAIOR!")
            else:
                janela["mensagem"].update("O número é MENOR!")
        except ValueError:
            janela["mensagem"].update("Digite um número válido!")
