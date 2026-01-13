import pyautogui 
import pandas
import time

#Abrir o navegador 
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

#Escrever o caminho do site 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#Fazer login 
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3) 
pyautogui.click(x=446, y=375)
pyautogui.write("t.iferreira.dev@gmail,com")
pyautogui.press("tab")
pyautogui.write("12345678910")
pyautogui.press("enter")
time.sleep(4)

#Acessar o banco de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

#Cadastar produto

for linha in tabela.index:
    pyautogui.click(x=431, y=260)
    #insere o código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #insere a marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #insere o tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #insere a catergoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #insere  o preço
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    #insere o custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write()
    pyautogui.press("tab")
    #insere a observação se tiver
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)




