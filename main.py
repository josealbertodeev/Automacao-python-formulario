import pyautogui  # biblioteca para automação de mouse e teclado
import time  # biblioteca para controlar tempo (pausas, delays)

pyautogui.PAUSE = 1  # pausa de 1 segundo entre cada ação

# COMANDOS BÁSICOS DO PYAUTOGUI
# pyautogui.press() -> apertar 1 tecla
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.hotkey("ctrl", "c") -> apertar uma combinação de teclas

# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site (hashtagtreinamentos.com/curso-python)
pyautogui.write("hashtagtreinamentos.com/curso-python")
pyautogui.press("enter")
time.sleep(5)  # esperar 5 segundos para a página carregar

# preencher o formulários
pyautogui.click(x=466, y=568)
pyautogui.write("Alberto")
pyautogui.press("tab")

pyautogui.write("thetrooper_lord@hotmail.com")
pyautogui.press("tab")

pyautogui.write("950354574")
pyautogui.press("tab")

# enviar o formulário
pyautogui.press("enter")

print("Formulário enviado com sucesso!")