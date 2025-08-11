import PySimpleGUI as sg

sg.theme("DarkBlue14")

layout = [
    [sg.Text("Número 1:"), sg.Input(key="num1")],
    [sg.Text("Número 2:"), sg.Input(key="num2")],
    [sg.Text("Operação:"), sg.Combo(["+", "-", "*", "/"], key="op")],
    [sg.Button("Calcular"), sg.Button("Sair")],
    [sg.Text("Resultado:", size=(20, 1), key="resultado")]
]

janela = sg.Window("Calculadora", layout)

while True:
    evento, valores = janela.read()
    if evento in (sg.WINDOW_CLOSED, "Sair"):
        break

    if evento == "Calcular":
        try:
            num1 = float(valores["num1"])
            num2 = float(valores["num2"])
            op = valores["op"]

            if op == "+":
                res = num1 + num2
            elif op == "-":
                res = num1 - num2
            elif op == "*":
                res = num1 * num2
            elif op == "/":
                res = num1 / num2 if num2 != 0 else "Erro: divisão por zero"
            else:
                res = "Selecione uma operação"

            janela["resultado"].update(f"Resultado: {res}")
        except ValueError:
            janela["resultado"].update("Erro: insira números válidos")
