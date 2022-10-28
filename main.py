import win32com.client as comclt
import time

wsh= comclt.Dispatch("WScript.Shell")
contagem = 1
wsh.AppActivate("Tibia") # ativar janela do jogo
while True:
    print(f'Enviando comando {contagem}')
    time.sleep(10)
    wsh.SendKeys("0") # hotkey para comer
    time.sleep(2)
    wsh.SendKeys("9") # hotkey para runa
    time.sleep(5)
    contagem = contagem+1
    