# passo a passo do projeto

# 1 abrir o sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar:pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.7

# pyautogui.click --> clicar com o mouse
# pyautogui.write --> escreva um texto
# pyautogui.press --> pressionar uma tecla do teclado
# pyautogui.hotkey --> apertar um conjunto de tecla ao mesmo tempo

# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no sistema da empresa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#aqui pode ser que ele demore alguns segundos para carregar o site / depende da sua conexão com a internet
time.sleep(3)

# 2 fazer login
pyautogui.click(x=705, y=459)
pyautogui.write("andreluizbcarvalho@gmail.com")

pyautogui.press("tab")
pyautogui.write("sua senha")

pyautogui.press("tab") #passou para o botao de login
pyautogui.press("enter")

time.sleep(3)

# 3 abrir/importar a base de dados de produtos para cadastrar
#import install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# 4 cadastrar um produto

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    # clicar no campo do codigo do produto
    pyautogui.click(x=678, y=325)
    # preencher o codigo
    pyautogui.write(codigo)
    # passar para o proximo campo
    pyautogui.press("tab")
    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim